#!/usr/bin/env python3
"""Question-only SPARQL QA over the final SHACL-and-inference graph."""

from __future__ import annotations

import argparse
import json
import re
import time
from pathlib import Path

import openai
from dotenv import load_dotenv
from rdflib import Graph, Literal, RDF, RDFS, URIRef
from rdflib.namespace import OWL
from tenacity import retry, retry_if_exception_type, stop_after_attempt, wait_exponential

from core.llm_config import completion_parameters, create_client, load_llm_settings
from phase2_qa.common import aggregate, atomic_json, example_fields, parse_ids, score_answer


ROOT = Path(__file__).resolve().parents[1]
PROMPT_VERSION = "question_to_sparql_v1"
ONTOLOGY_NAMESPACE = "http://example.org/2wiki-ontology#"
FORBIDDEN_SPARQL = re.compile(
    r"\b(?:INSERT|DELETE|LOAD|CLEAR|CREATE|DROP|COPY|MOVE|ADD|SERVICE)\b",
    re.IGNORECASE,
)
SYSTEM_PROMPT = """Generate one read-only SPARQL query that answers the supplied
question from the RDF graph. Use only the supplied ontology vocabulary and entity labels.
Never use outside knowledge. The query must bind the final answer to a variable named
?answer. It may use property paths, inverse paths, FILTER, ordering, aggregation, and date
arithmetic when required. Resolve each entity using the exact predicate shown in the
entity_label_index: rdfs:label for label and skos:altLabel for aliases. Use an ASK query for
yes/no questions; use SELECT ?answer for every other question. Return JSON only with fields
sparql and explanation. The
explanation must be one short sentence and must not claim that the query succeeded."""
RESPONSE_FORMAT = {
    "type": "json_schema",
    "json_schema": {
        "name": "symbolic_sparql_plan",
        "strict": True,
        "schema": {
            "type": "object",
            "additionalProperties": False,
            "required": ["sparql", "explanation"],
            "properties": {
                "sparql": {"type": "string"},
                "explanation": {"type": "string"},
            },
        },
    },
}


def ontology_reference(path: Path) -> list[dict[str, object]]:
    graph = Graph().parse(path, format="turtle")
    properties = set(graph.subjects(RDF.type, OWL.ObjectProperty)) | set(
        graph.subjects(RDF.type, OWL.DatatypeProperty)
    )
    rows = []
    for prop in sorted(properties, key=str):
        rows.append(
            {
                "iri": str(prop),
                "label": str(graph.value(prop, RDFS.label) or ""),
                "comment": str(graph.value(prop, RDFS.comment) or ""),
                "domain": [str(value) for value in graph.objects(prop, RDFS.domain)],
                "range": [str(value) for value in graph.objects(prop, RDFS.range)],
                "inverse": [str(value) for value in graph.objects(prop, OWL.inverseOf)],
                "parent": [str(value) for value in graph.objects(prop, RDFS.subPropertyOf)],
            }
        )
    return rows


def graph_inputs(dataset: Path, example_id: int) -> tuple[Path, Path]:
    example = dataset / str(example_id)
    final_graph = example / "inference" / f"extracted_reasoned_{example_id}.ttl"
    metadata = example / "originals" / f"extracted_{example_id}.ttl"
    missing = [str(path) for path in (final_graph, metadata) if not path.is_file()]
    if missing:
        raise FileNotFoundError(f"Example {example_id} lacks symbolic QA inputs: {missing}")
    return final_graph, metadata


def load_query_graph(final_graph: Path, metadata: Path) -> Graph:
    graph = Graph().parse(final_graph, format="turtle")
    metadata_graph = Graph().parse(metadata, format="turtle")
    for subject, predicate, obj in metadata_graph:
        if predicate in {RDFS.label, URIRef("http://www.w3.org/2004/02/skos/core#altLabel")}:
            graph.add((subject, predicate, obj))
    return graph


def entity_label_index(graph: Graph) -> list[dict[str, object]]:
    alt = URIRef("http://www.w3.org/2004/02/skos/core#altLabel")
    resources = set(graph.subjects(RDFS.label, None)) | set(graph.subjects(alt, None))
    return [
        {
            "label": str(graph.value(resource, RDFS.label) or ""),
            "aliases": sorted(str(value) for value in graph.objects(resource, alt)),
        }
        for resource in sorted(resources, key=str)
    ]


def validate_select_query(query: str) -> str:
    cleaned = query.strip()
    without_prefixes = re.sub(
        r"(?im)^\s*PREFIX\s+[^\n]+$", "", cleaned
    ).lstrip()
    query_type = re.match(r"(?is)^(SELECT|ASK)\b", without_prefixes)
    if query_type is None:
        raise ValueError("Symbolic planner must return a SPARQL SELECT or ASK query")
    if FORBIDDEN_SPARQL.search(cleaned):
        raise ValueError("SPARQL query contains a forbidden operation")
    if query_type.group(1).upper() == "SELECT" and not re.search(r"(?i)\?answer\b", cleaned):
        raise ValueError("SPARQL query must bind ?answer")
    return cleaned


@retry(
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=0.2, min=0.2, max=2),
    retry=retry_if_exception_type(
        (openai.APIConnectionError, openai.APITimeoutError, openai.RateLimitError)
    ),
    reraise=True,
)
def completion(client, settings, payload):
    return client.chat.completions.create(
        model=settings.model,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": json.dumps(payload, ensure_ascii=False)},
        ],
        **completion_parameters(settings, RESPONSE_FORMAT),
    )


def display_value(graph: Graph, value) -> str:
    if isinstance(value, Literal):
        return str(value)
    if isinstance(value, URIRef):
        label = graph.value(value, RDFS.label)
        return str(label) if label is not None else str(value).rsplit("/", 1)[-1].rsplit("#", 1)[-1]
    return str(value)


def rendered_binding(graph: Graph, row) -> dict[str, str]:
    return {
        str(variable): display_value(graph, value)
        for variable, value in row.asdict().items()
        if value is not None
    }


def supporting_triples(graph: Graph, answer_terms: list) -> list[dict[str, str]]:
    triples = set()
    for answer in answer_terms:
        resources = {answer} if isinstance(answer, URIRef) else set()
        if isinstance(answer, Literal):
            triples.update(graph.triples((None, None, answer)))
            resources.update(graph.subjects(RDFS.label, answer))
            resources.update(
                graph.subjects(URIRef("http://www.w3.org/2004/02/skos/core#altLabel"), answer)
            )
        for resource in resources:
            triples.update(graph.triples((resource, None, None)))
            triples.update(graph.triples((None, None, resource)))
    rows = []
    for subject, predicate, obj in sorted(triples, key=lambda triple: tuple(map(str, triple))):
        if not str(predicate).startswith(ONTOLOGY_NAMESPACE):
            continue
        rows.append(
            {
                "subject": str(subject),
                "predicate": str(predicate),
                "object": obj.n3() if isinstance(obj, Literal) else str(obj),
            }
        )
    return rows


def _triple_set(rows: list[dict[str, str]]) -> set[tuple[str, str, str]]:
    return {(row["subject"], row["predicate"], row["object"]) for row in rows}


def dependency_flags(dataset: Path, example_id: int, support: list[dict[str, str]]) -> dict[str, bool]:
    example = dataset / str(example_id)
    support_set = _triple_set(support)
    inferred_path = example / "inference" / "artifacts" / f"extracted_inferred_only_{example_id}.ttl"
    inferred_rows = []
    if inferred_path.is_file():
        inferred = Graph().parse(inferred_path, format="turtle")
        inferred_rows = [
            {"subject": str(s), "predicate": str(p), "object": o.n3() if isinstance(o, Literal) else str(o)}
            for s, p, o in inferred
        ]
    original_path = example / "originals" / f"extracted_{example_id}.ttl"
    repaired_path = example / "after_shacl" / f"extracted_shacl_{example_id}.ttl"
    repair_rows = []
    if repaired_path.is_file():
        original = Graph().parse(original_path, format="turtle")
        repaired = Graph().parse(repaired_path, format="turtle")
        repair_rows = [
            {"subject": str(s), "predicate": str(p), "object": o.n3() if isinstance(o, Literal) else str(o)}
            for s, p, o in set(repaired) - set(original)
        ]
    return {
        "support_uses_inferred_triple": bool(support_set & _triple_set(inferred_rows)),
        "support_uses_shacl_repair": bool(support_set & _triple_set(repair_rows)),
    }


def run_one(client, settings, dataset: Path, example_id: int, ontology: list[dict]) -> dict:
    fields = example_fields(dataset, example_id)
    final_path, metadata_path = graph_inputs(dataset, example_id)
    graph = load_query_graph(final_path, metadata_path)
    payload = {
        "question": fields["question"],
        "ontology_properties": ontology,
        "entity_label_index": entity_label_index(graph),
    }
    started = time.monotonic()
    planning_attempts = []
    for attempt in range(1, 4):
        response = completion(client, settings, payload)
        plan = json.loads(response.choices[0].message.content)
        try:
            query = validate_select_query(plan["sparql"])
            query_started = time.monotonic()
            executed = graph.query(query)
            break
        except Exception as exc:
            planning_attempts.append(
                {"attempt": attempt, "sparql": plan.get("sparql"), "error": str(exc)}
            )
            if attempt == 3:
                raise
            payload = {
                **payload,
                "previous_invalid_query": plan.get("sparql"),
                "query_error": str(exc),
                "repair_instruction": "Return a corrected complete SPARQL query.",
            }
    is_ask = getattr(executed, "type", "") == "ASK"
    variables = [] if is_ask else [str(variable) for variable in executed.vars]
    query_result = [] if is_ask else list(executed)
    query_seconds = time.monotonic() - query_started
    elapsed = time.monotonic() - started
    if is_ask:
        answer_terms = [Literal(bool(executed.askAnswer))]
    else:
        answer_index = variables.index("answer")
        answer_terms = [row[answer_index] for row in query_result if len(row) > answer_index]
    answers = [display_value(graph, value) for value in answer_terms]
    predicted = answers[0] if answers else ""
    support = supporting_triples(graph, answer_terms)
    usage = getattr(response, "usage", None)
    return {
        "id": example_id,
        "status": "completed",
        "execution_status": "answered" if answers else "empty_result",
        "method": "question_only_symbolic_sparql_qa",
        "prompt_version": PROMPT_VERSION,
        "question": fields["question"],
        "gold_answer": fields["answer"],
        "predicted_answer": predicted,
        **score_answer(predicted, fields["answer"]),
        "sparql": query,
        "planner_explanation": plan["explanation"],
        "planning_attempts": planning_attempts,
        "bindings": (
            [{"answer": "true" if bool(executed.askAnswer) else "false"}]
            if is_ask
            else [rendered_binding(graph, row) for row in query_result]
        ),
        "supporting_triples": support,
        **dependency_flags(dataset, example_id, support),
        "elapsed_seconds": elapsed,
        "query_seconds": query_seconds,
        "usage": {
            key: getattr(usage, key, None)
            for key in ("prompt_tokens", "completion_tokens", "total_tokens")
        } if usage else None,
    }


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dataset", type=Path, required=True)
    parser.add_argument("--ids", type=parse_ids, required=True)
    parser.add_argument("--ontology", type=Path, default=ROOT / "ontology" / "ontology.ttl")
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--overwrite", action="store_true")
    args = parser.parse_args(argv)
    load_dotenv(ROOT / ".env")
    settings = load_llm_settings()
    client = create_client(settings)
    ontology = ontology_reference(args.ontology.resolve())
    existing = []
    if args.output.exists() and not args.overwrite:
        existing = json.loads(args.output.read_text(encoding="utf-8")).get("results", [])
    by_id = {row["id"]: row for row in existing}
    for example_id in args.ids:
        if example_id in by_id and by_id[example_id].get("status") == "completed":
            continue
        try:
            row = run_one(client, settings, args.dataset.resolve(), example_id, ontology)
        except Exception as exc:
            row = {
                "id": example_id,
                "status": "failed",
                "method": "question_only_symbolic_sparql_qa",
                "error": str(exc),
            }
        by_id[example_id] = row
        results = [by_id[key] for key in sorted(by_id)]
        atomic_json(
            args.output,
            {
                "experiment": "question_only_symbolic_sparql_qa",
                "valid_for_direct_baseline_comparison": True,
                "model": settings.model,
                "provider": settings.provider,
                "prompt_version": PROMPT_VERSION,
                "graph_stage": "shacl_plus_inference",
                "summary": aggregate(results),
                "results": results,
            },
        )
        print(f"id={example_id} status={row['status']}", flush=True)
    return 1 if any(row.get("status") == "failed" for row in by_id.values()) else 0


if __name__ == "__main__":
    raise SystemExit(main())
