#!/usr/bin/env python3
"""Run question-focused extraction -> mapping -> RDF -> SHACL safely."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
import tempfile
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

from dotenv import load_dotenv
from rdflib import Graph

from agents.extraction_agent import extraction_agent, prune_resolution_metadata, validate_extraction_result
from agents.feedback_agent import FeedbackAgentError, feedback_agent
from agents.kg_builder_agent import KGBuilderResult, kg_builder_agent_with_diagnostics
from agents.ontology_mapping_agent import UnmappedRelation, ontology_mapping_agent_with_diagnostics
from agents.validation_agent import validation_agent
from feedback.apply_edits import ApplyEditsError, apply_feedback_plan
from ontology.schema_loader import OntologySchema, load_ontology_schema
from utils.rdf import clone_graph, serialize_turtle_graph
from wikidata_entity_linking import (
    accepted_links,
    add_same_as_links,
    build_candidate_index,
    link_entities,
)


ROOT = Path(__file__).resolve().parent
_TEXT_PATTERN = re.compile(r"^text_(\d+)\.txt$")
VALIDATION_CONTRACT_VERSION = 2
EXTRACTION_QUALITY_CONTRACT_VERSION = 1
DEFAULT_REPAIR_ITERATIONS = 3


@dataclass(frozen=True)
class ExtractionQualityIssue:
    code: str
    severity: str
    message: str


def _mention_key(value: object) -> str:
    return "".join(character for character in str(value).casefold() if character.isalnum())


def assess_extraction_quality(
    extraction: dict[str, Any],
    mapping: dict[str, Any] | None,
    *,
    question: str,
    source_text: str,
) -> dict[str, Any]:
    """Classify post-extraction usability without judging factual correctness.

    Errors identify outputs that cannot be scored as graphs. Warnings expose likely
    model errors (for example hallucinated labels or missing question anchors) but do
    not make the example ineligible: those failures belong in the measured result.
    """
    issues: list[ExtractionQualityIssue] = []

    def issue(code: str, severity: str, message: str) -> None:
        issues.append(ExtractionQualityIssue(code, severity, message))

    entities = extraction.get("entities") if isinstance(extraction.get("entities"), list) else []
    relations = extraction.get("relations") if isinstance(extraction.get("relations"), list) else []
    fact_attributes = [
        (str(entity.get("id", "")), str(name))
        for entity in entities
        if isinstance(entity, dict)
        for name, value in (entity.get("attributes") or {}).items()
        if value is not None
    ]
    raw_fact_count = len(relations) + len(fact_attributes)
    if not entities:
        issue("no_entities", "error", "Extraction contains no entities.")
    if raw_fact_count == 0:
        issue("no_semantic_facts", "error", "Extraction contains neither relations nor populated attributes.")

    active_ids = {entity_id for entity_id, _ in fact_attributes}
    active_ids.update(
        str(relation.get(endpoint, ""))
        for relation in relations
        if isinstance(relation, dict)
        for endpoint in ("subject", "object")
    )
    question_key = _mention_key(question)
    source_key = _mention_key(source_text)
    active_entities = [
        entity for entity in entities
        if isinstance(entity, dict) and str(entity.get("id", "")) in active_ids
    ]
    question_anchors = []
    ungrounded_entities = []
    for entity in active_entities:
        names = [entity.get("label", ""), *(entity.get("aliases") or [])]
        keys = [key for name in names if (key := _mention_key(name))]
        if any(key in question_key for key in keys):
            question_anchors.append(str(entity.get("id", "")))
        if keys and not any(key in source_key for key in keys):
            ungrounded_entities.append(str(entity.get("id", "")))
    if raw_fact_count and not question_anchors:
        issue("no_question_anchor", "warning", "No fact-bearing extracted entity label or alias occurs in the question.")
    if ungrounded_entities:
        issue(
            "entities_not_source_grounded",
            "warning",
            "Fact-bearing entity labels/aliases not found in source text: " + ", ".join(sorted(ungrounded_entities)),
        )

    mapped_relations = []
    unmapped_count = 0
    if mapping is not None:
        mapped_relations = mapping.get("relations") if isinstance(mapping.get("relations"), list) else []
        unmapped = mapping.get("unmapped_relations")
        unmapped_count = len(unmapped) if isinstance(unmapped, list) else 0
        mapped_fact_count = len(mapped_relations) + len(fact_attributes)
        if raw_fact_count and mapped_fact_count == 0:
            issue("no_mapped_semantic_facts", "error", "No extracted semantic fact can be represented in the RDF graph.")
        elif unmapped_count:
            issue("unmapped_relations", "warning", f"{unmapped_count} extracted relation(s) could not be mapped.")
    else:
        mapped_fact_count = None

    status = "unscoreable" if any(item.severity == "error" for item in issues) else "scoreable"
    return {
        "contract_version": EXTRACTION_QUALITY_CONTRACT_VERSION,
        "status": status,
        "eligible_for_graph_evaluation": status == "scoreable",
        "policy": "Only structural unscoreability excludes a candidate; warning-level model errors remain measurable.",
        "metrics": {
            "entities": len(entities),
            "active_entities": len(active_entities),
            "raw_semantic_facts": raw_fact_count,
            "mapped_semantic_facts": mapped_fact_count,
            "mapped_relations": len(mapped_relations),
            "unmapped_relations": unmapped_count,
            "question_anchor_entities": len(question_anchors),
            "ungrounded_active_entities": len(ungrounded_entities),
        },
        "question_anchor_entity_ids": sorted(question_anchors),
        "ungrounded_active_entity_ids": sorted(ungrounded_entities),
        "issues": [asdict(item) for item in issues],
    }


def _numeric_index(path: Path) -> int:
    match = _TEXT_PATTERN.match(path.name)
    if not match:
        raise ValueError(f"Input filename must match text_N.txt: {path}")
    return int(match.group(1))


def _input_files(path: Path) -> list[Path]:
    candidates = [path] if path.is_file() else list(path.rglob("text_*.txt")) if path.is_dir() else []
    if not candidates:
        raise FileNotFoundError(f"No text_N.txt input files found at: {path}")
    indexed: dict[int, Path] = {}
    for candidate in candidates:
        index = _numeric_index(candidate)
        if index in indexed:
            raise ValueError(f"Duplicate text id {index}: {indexed[index]} and {candidate}")
        indexed[index] = candidate
    return [indexed[index] for index in sorted(indexed)]


def _parse_ids(value: str) -> set[int]:
    result: set[int] = set()
    for part in value.split(","):
        part = part.strip()
        if not part:
            continue
        if "-" in part:
            start_text, end_text = part.split("-", 1)
            start, end = int(start_text), int(end_text)
            if start < 0 or end < start:
                raise argparse.ArgumentTypeError(f"Invalid id range: {part}")
            result.update(range(start, end + 1))
        else:
            index = int(part)
            if index < 0:
                raise argparse.ArgumentTypeError("Ids must be non-negative")
            result.add(index)
    if not result:
        raise argparse.ArgumentTypeError("At least one id is required")
    return result


def _select_files(
    files: list[Path],
    *,
    ids: set[int] | None,
    start: int | None,
    end: int | None,
    limit: int | None,
) -> list[Path]:
    selected = []
    for path in files:
        index = _numeric_index(path)
        if ids is not None and index not in ids:
            continue
        if start is not None and index < start:
            continue
        if end is not None and index > end:
            continue
        selected.append(path)
    if limit is not None:
        if limit <= 0:
            raise ValueError("--limit must be positive")
        selected = selected[:limit]
    if ids is not None:
        missing = sorted(ids - {_numeric_index(path) for path in selected})
        if missing:
            raise ValueError(f"Requested text ids were not found: {missing}")
    if not selected:
        raise ValueError("No input files matched the requested selection")
    return selected


def _question_for(input_path: Path) -> str | None:
    """Read the question from that example's own folder, e.g.
    pilot/274/274_question.txt next to pilot/274/text_274.txt -- instead of a
    shared train.json array."""
    match = next(input_path.parent.glob("*_question.txt"), None)
    if match is None:
        return None
    text = match.read_text(encoding="utf-8").strip()
    return text or None

def _extraction_digest(extraction: dict[str, Any]) -> str:
    canonical = json.dumps(
        extraction, ensure_ascii=False, sort_keys=True, separators=(",", ":")
    ).encode("utf-8")
    return hashlib.sha256(canonical).hexdigest()


def _mapping_matches_extraction(mapping: dict[str, Any], extraction: dict[str, Any]) -> bool:
    return mapping.get("_source_extraction_sha256") == _extraction_digest(extraction)


def _atomic_write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary_name = None
    try:
        with tempfile.NamedTemporaryFile(
            mode="w", encoding="utf-8", dir=path.parent, prefix=f".{path.name}.", delete=False
        ) as handle:
            handle.write(content)
            handle.flush()
            os.fsync(handle.fileno())
            temporary_name = handle.name
        os.replace(temporary_name, path)
    finally:
        if temporary_name and os.path.exists(temporary_name):
            os.unlink(temporary_name)


def _write_json(path: Path, payload: Any) -> None:
    _atomic_write_text(path, json.dumps(payload, ensure_ascii=False, indent=2) + "\n")


def _read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def _artifact_paths(input_path: Path, output_root: Path | None) -> dict[str, Path]:
    index = _numeric_index(input_path)
    if output_root is None:
        example_directory = input_path.parent.parent if input_path.parent.name == "originals" else input_path.parent
        directory = input_path.parent
    else:
        example_directory = output_root / str(index)
        directory = example_directory / "originals"
    artifacts_directory = directory / "artifacts"
    inference_directory = example_directory / "inference"
    return {
        "extraction": artifacts_directory / f"extraction_{index}.json",
        "extraction_quality": artifacts_directory / f"extraction_quality_{index}.json",
        "mapping": artifacts_directory / f"mapping_{index}.json",
        "entity_links": artifacts_directory / f"entity_links_{index}.json",
        "same_as": artifacts_directory / f"same_as_{index}.ttl",
        "turtle": directory / f"extracted_{index}.ttl",
        "initial_turtle": artifacts_directory / f"extracted_initial_{index}.ttl",
        "shacl_json": artifacts_directory / f"shacl_{index}.json",
        "repair_json": artifacts_directory / f"repair_{index}.json",
        "reasoned": inference_directory / f"reasoned_{index}.ttl",
        "reasoner_log": inference_directory / "artifacts" / f"reasoner_{index}.log",
    }


def _unmapped_relations(mapping_payload: dict[str, Any]) -> tuple[UnmappedRelation, ...]:
    """Rehydrate cached mapping diagnostics for the canonical validator."""
    return tuple(
        UnmappedRelation(
            subject=str(item["subject"]),
            object=str(item["object"]),
            relation_phrase=str(item["relation_phrase"]),
            reason=str(item["reason"]),
        )
        for item in mapping_payload.get("unmapped_relations", [])
    )


def _validate_graph(
    turtle: str,
    schema: OntologySchema,
    mapping_payload: dict[str, Any],
    built: KGBuilderResult,
) -> dict[str, Any]:
    """Validate through the same canonical entry point as the asynchronous API."""
    result = validation_agent(
        Graph().parse(data=turtle, format="turtle"),
        schema,
        unmapped_relations=_unmapped_relations(mapping_payload),
        dangling_references=built.dangling_references,
        entities=mapping_payload["entities"],
    )
    return {
        "validation_contract_version": VALIDATION_CONTRACT_VERSION,
        "conforms": result.conforms,
        "fingerprint": result.fingerprint,
        "violations": [violation.as_dict() for violation in result.violations],
    }


def _validation_result(
    graph: Graph,
    schema: OntologySchema,
    mapping_payload: dict[str, Any],
    built: KGBuilderResult,
):
    return validation_agent(
        graph,
        schema,
        unmapped_relations=_unmapped_relations(mapping_payload),
        dangling_references=built.dangling_references,
        entities=mapping_payload["entities"],
    )


def _validation_payload(result) -> dict[str, Any]:
    return {
        "validation_contract_version": VALIDATION_CONTRACT_VERSION,
        "conforms": result.conforms,
        "fingerprint": result.fingerprint,
        "violations": [violation.as_dict() for violation in result.violations],
    }


def repair_graph_with_feedback(
    graph: Graph,
    schema: OntologySchema,
    mapping_payload: dict[str, Any],
    built: KGBuilderResult,
    source_text: str,
    *,
    max_iterations: int = DEFAULT_REPAIR_ITERATIONS,
) -> tuple[Graph, Any, dict[str, Any]]:
    """Validate and repair a graph with bounded, source-grounded LLM feedback.

    Each proposed edit is checked by ``apply_feedback_plan`` before it can affect the
    graph. Validation is rerun after every accepted plan. Identical reports, empty
    plans, feedback failures, and the iteration limit stop the loop without presenting
    an unrepaired graph as conforming.
    """
    if max_iterations < 1:
        raise ValueError("max_iterations must be positive")

    working = clone_graph(graph)
    initial = _validation_result(working, schema, mapping_payload, built)
    current = initial
    audit: dict[str, Any] = {
        "enabled": True,
        "max_iterations": max_iterations,
        "initial_validation": _validation_payload(initial),
        "iterations": [],
        "status": "not_needed" if initial.conforms else "running",
    }
    if initial.conforms:
        audit["final_validation"] = _validation_payload(initial)
        return working, initial, audit

    previous_fingerprint: str | None = None
    for iteration in range(1, max_iterations + 1):
        if current.fingerprint == previous_fingerprint:
            audit["status"] = "plateau"
            break

        before_count = len(working)
        entry: dict[str, Any] = {
            "iteration": iteration,
            "validation_before": _validation_payload(current),
            "triples_before": before_count,
        }
        try:
            plan = feedback_agent(
                clone_graph(working), current.violations, schema, source_text
            )
            applied = apply_feedback_plan(
                working,
                plan,
                violations=current.violations,
                schema=schema,
                source_text=source_text,
            )
        except (FeedbackAgentError, ApplyEditsError) as exc:
            entry.update(
                {
                    "outcome": "feedback_error",
                    "error": str(exc),
                    "triples_after": before_count,
                }
            )
            audit["iterations"].append(entry)
            audit["status"] = "feedback_error"
            break

        entry.update(
            {
                "feedback_reasoning": plan.reasoning,
                "repairs": [repair.model_dump(mode="json") for repair in plan.repairs],
                "edit_log": [asdict(item) for item in applied.edit_log],
                "unresolved_violation_fingerprints": list(
                    applied.unresolved_violation_fingerprints
                ),
                "triples_after": len(applied.graph),
            }
        )
        previous_fingerprint = current.fingerprint
        working = applied.graph
        current = _validation_result(working, schema, mapping_payload, built)
        entry["validation_after"] = _validation_payload(current)
        entry["outcome"] = "conforms" if current.conforms else "revalidate"
        audit["iterations"].append(entry)

        if current.conforms:
            audit["status"] = "repaired"
            break
        if not applied.edit_log:
            audit["status"] = "unresolved"
            break
    else:
        audit["status"] = "max_iterations"

    audit["final_validation"] = _validation_payload(current)
    return working, current, audit


def extraction_has_usable_facts(payload: dict[str, Any]) -> bool:
    """Return true when an extraction can produce at least one semantic fact."""
    entities = payload.get("entities")
    if not isinstance(entities, list) or not entities:
        return False
    relations = payload.get("relations")
    if isinstance(relations, list) and relations:
        return True
    return any(
        value is not None
        for entity in entities
        if isinstance(entity, dict)
        for value in (entity.get("attributes") or {}).values()
    )


def process_file(
    input_path: Path,
    ontology_path: Path,
    schema: OntologySchema,
    *,
    question: str | None,
    output_root: Path | None,
    overwrite: bool,
    run_reasoner: bool,
    entity_linker=None,
    rebuild_downstream: bool = False,
    repair_shacl: bool = False,
    max_repair_iterations: int = DEFAULT_REPAIR_ITERATIONS,
) -> dict[str, Any]:
    index = _numeric_index(input_path)
    paths = _artifact_paths(input_path, output_root)
    required = [
        paths["extraction"], paths["extraction_quality"], paths["mapping"],
        paths["turtle"], paths["shacl_json"],
    ]
    if repair_shacl:
        required.extend((paths["initial_turtle"], paths["repair_json"]))
    if entity_linker is not None:
        required.extend((paths["entity_links"], paths["same_as"]))
    if not overwrite and not rebuild_downstream and all(path.exists() for path in required):
        cached_extraction = prune_resolution_metadata(
            validate_extraction_result(_read_json(paths["extraction"]), schema), question
        )
        cached_mapping = _read_json(paths["mapping"])
        cached_validation = _read_json(paths["shacl_json"])
        if (
            _mapping_matches_extraction(cached_mapping, cached_extraction)
            and cached_validation.get("validation_contract_version")
            == VALIDATION_CONTRACT_VERSION
        ):
            if not extraction_has_usable_facts(cached_extraction):
                quality = _read_json(paths["extraction_quality"])
                return {
                    "id": index,
                    "input": str(input_path),
                    "status": "unscoreable_extraction",
                    "entities": len(cached_extraction.get("entities", [])),
                    "relations": len(cached_extraction.get("relations", [])),
                    "reason": "cached extraction contains no usable relation graph",
                    "extraction_quality": quality,
                }
            link_summary = (
                _read_json(paths["entity_links"]).get("summary", {})
                if entity_linker is not None
                else {"matched": 0, "review": 0, "unmatched": 0}
            )
            cached_quality = _read_json(paths["extraction_quality"])
            return {
                "id": index,
                "input": str(input_path),
                "status": "skipped",
                "reason": "validated stage outputs already exist",
                "unmapped_relations": len(cached_mapping.get("unmapped_relations", [])),
                "shacl_conforms": bool(cached_validation.get("conforms")),
                "entity_links": link_summary,
                "extraction_quality": cached_quality,
            }

    if not question:
        raise ValueError(f"No question found for text id {index}; refusing distractor-wide extraction")
    source_text = input_path.read_text(encoding="utf-8")

    if paths["extraction"].exists() and not overwrite:
        extracted = prune_resolution_metadata(
            validate_extraction_result(_read_json(paths["extraction"]), schema), question
        )
        # Persist normalization so its digest correctly invalidates stale downstream
        # mapping artifacts and future resumes observe the same extraction.
        _write_json(paths["extraction"], extracted)
    else:
        extracted = extraction_agent(source_text, schema, question=question)
        _write_json(paths["extraction"], extracted)

    # Datatype-only questions can be answered by an entity attribute without an object
    # edge (for example, publication-date questions). Reject only a payload with no
    # entity or no semantic fact at all.
    if not extraction_has_usable_facts(extracted):
        quality = assess_extraction_quality(
            extracted, None, question=question, source_text=source_text
        )
        _write_json(paths["extraction_quality"], quality)
        return {
            "id": index,
            "input": str(input_path),
            "status": "unscoreable_extraction",
            "entities": len(extracted["entities"]),
            "relations": len(extracted["relations"]),
            "reason": "question-focused extraction produced no usable relation graph",
            "extraction_quality": quality,
        }

    mapping_payload = _read_json(paths["mapping"]) if paths["mapping"].exists() and not overwrite else None
    if mapping_payload is None or not _mapping_matches_extraction(mapping_payload, extracted):
        mapped = ontology_mapping_agent_with_diagnostics(extracted, schema)
        mapping_payload = {
            "_source_extraction_sha256": _extraction_digest(extracted),
            "entities": mapped.entities,
            "relations": mapped.relations,
            "unmapped_relations": [asdict(item) for item in mapped.unmapped_relations],
        }
        _write_json(paths["mapping"], mapping_payload)

    extraction_quality = assess_extraction_quality(
        extracted, mapping_payload, question=question, source_text=source_text
    )
    _write_json(paths["extraction_quality"], extraction_quality)
    built = kg_builder_agent_with_diagnostics(mapping_payload, schema)
    turtle_graph = built.turtle_graph
    repair_summary = {"enabled": False, "status": "not_requested", "iterations": []}
    if repair_shacl:
        initial_graph = Graph().parse(data=turtle_graph, format="turtle")
        _atomic_write_text(paths["initial_turtle"], serialize_turtle_graph(initial_graph))
        repaired_graph, validation_result, repair_summary = repair_graph_with_feedback(
            initial_graph,
            schema,
            mapping_payload,
            built,
            source_text,
            max_iterations=max_repair_iterations,
        )
        turtle_graph = serialize_turtle_graph(repaired_graph)
        _write_json(paths["repair_json"], repair_summary)

    link_summary = {"matched": 0, "review": 0, "unmatched": 0}
    if entity_linker is not None:
        link_payload = link_entities(mapping_payload["entities"], entity_linker)
        turtle_graph, same_as_turtle = add_same_as_links(
            turtle_graph,
            accepted_links(link_payload),
            # QIDs are linking metadata, not evidence assertions. Preserve the
            # dedicated artifact without exposing owl:sameAs to the reasoner.
            include_in_graph=False,
        )
        _write_json(paths["entity_links"], link_payload)
        _atomic_write_text(paths["same_as"], same_as_turtle)
        link_summary = link_payload["summary"]
    if entity_linker is not None or overwrite or not paths["turtle"].exists():
        _atomic_write_text(paths["turtle"], turtle_graph)
    else:
        Graph().parse(paths["turtle"], format="turtle")

    if repair_shacl:
        validation = _validation_payload(validation_result)
        validation["repair"] = {
            "status": repair_summary["status"],
            "iterations": len(repair_summary["iterations"]),
            "artifact": str(paths["repair_json"]),
        }
    else:
        validation = _validate_graph(turtle_graph, schema, mapping_payload, built)
    validation["dangling_references"] = [asdict(item) for item in built.dangling_references]
    _write_json(paths["shacl_json"], validation)

    initial_unmapped_count = len(mapping_payload.get("unmapped_relations", []))
    initial_dangling_count = len(built.dangling_references)
    unmapped_count = sum(
        item.get("kind") == "unmapped_relation" for item in validation["violations"]
    )
    dangling_count = sum(
        item.get("kind") == "dangling_reference" for item in validation["violations"]
    )
    unresolved_links = link_summary.get("review", 0) + link_summary.get("unmatched", 0)
    entity_link_status = (
        "unmatched"
        if link_summary.get("unmatched", 0)
        else "review"
        if link_summary.get("review", 0)
        else "matched"
    )
    review_reasons = []
    if not validation["conforms"]:
        review_reasons.append("graph_validation")
    if unresolved_links:
        review_reasons.append("entity_linking")
    clean = (
        validation["conforms"]
        and unmapped_count == 0
        and dangling_count == 0
        and unresolved_links == 0
    )
    reasoner_status = "not_requested"
    if run_reasoner and clean:
        completed = subprocess.run(
            [
                sys.executable,
                str(ROOT / "reasoner-inference" / "reasoner_kg_hermit.py"),
                str(paths["turtle"]),
                "--tbox",
                str(ontology_path),
                "--summary-only",
                "--output-ttl",
                str(paths["reasoned"]),
            ],
            check=False,
            text=True,
            capture_output=True,
        )
        reasoner_status = "completed" if completed.returncode == 0 else "failed"
        _atomic_write_text(paths["reasoner_log"], completed.stdout + completed.stderr)
        clean = clean and completed.returncode == 0

    return {
        "id": index,
        "input": str(input_path),
        # Preserve the validation-stage status contract. Cohort promotion uses
        # extraction_quality.eligible_for_graph_evaluation independently.
        "status": "completed" if clean else "review",
        "entities": len(mapping_payload["entities"]),
        "relations": len(mapping_payload["relations"]),
        "unmapped_relations": unmapped_count,
        "dangling_references": dangling_count,
        "initial_unmapped_relations": initial_unmapped_count,
        "initial_dangling_references": initial_dangling_count,
        "shacl_conforms": validation["conforms"],
        "validation_conforms": validation["conforms"],
        "validation_status": "conforming" if validation["conforms"] else "nonconforming",
        "shacl_repair": {
            "enabled": repair_shacl,
            "status": repair_summary["status"],
            "iterations": len(repair_summary["iterations"]),
        },
        "reasoner": reasoner_status,
        "entity_links": link_summary,
        "entity_link_status": entity_link_status,
        "review_reasons": review_reasons,
        "extraction_quality": extraction_quality,
        "extracted_ttl": str(paths["turtle"]),
    }


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="A text_N.txt file or directory")
    parser.add_argument("--ids", type=_parse_ids, help="IDs such as 0-19 or 0,2,4-7")
    parser.add_argument("--start", type=int)
    parser.add_argument("--end", type=int)
    parser.add_argument("--limit", type=int)
    parser.add_argument(
        "--output-dir",
        type=Path,
        required=True,
        help="Directory where generated pipeline artifacts will be written",
    )
    parser.add_argument("--ontology", type=Path, default=ROOT / "ontology" / "ontology.ttl")
    parser.add_argument("--manifest", type=Path, default=None)
    parser.add_argument("--overwrite", action="store_true")
    parser.add_argument(
        "--rebuild-downstream",
        action="store_true",
        help="Reuse extraction/mapping JSON and rebuild KG, linking and validation outputs",
    )
    parser.add_argument("--reasoner", action="store_true")
    parser.add_argument(
        "--shacl-repair",
        action="store_true",
        help="Revalidate nonconforming graphs through the source-grounded LLM feedback loop",
    )
    parser.add_argument(
        "--max-repair-iterations",
        type=int,
        default=DEFAULT_REPAIR_ITERATIONS,
        help=f"Maximum feedback attempts per graph (default: {DEFAULT_REPAIR_ITERATIONS})",
    )
    parser.add_argument(
        "--no-entity-linking",
        action="store_true",
        help="Disable ground-truth-free linking through the local Wikidata alias index",
    )
    parser.add_argument("--aliases", type=Path, default=ROOT / "data" / "id_aliases.json")
    parser.add_argument("--stop-on-error", action="store_true")
    parser.add_argument("--stop-on-review", action="store_true")
    parser.add_argument("--dry-run", action="store_true", help="Validate selection without API calls")
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    if not args.no_entity_linking and args.aliases is None:
        parser.error("--aliases is required unless --no-entity-linking is used")
    load_dotenv(ROOT / ".env")
    if args.start is not None and args.start < 0:
        raise SystemExit("--start must be non-negative")
    if args.end is not None and args.end < 0:
        raise SystemExit("--end must be non-negative")
    if args.start is not None and args.end is not None and args.end < args.start:
        raise SystemExit("--end must be greater than or equal to --start")
    if args.max_repair_iterations < 1:
        raise SystemExit("--max-repair-iterations must be positive")

    files = _select_files(
        _input_files(args.input.resolve()),
        ids=args.ids,
        start=args.start,
        end=args.end,
        limit=args.limit,
    )
    ontology_path = args.ontology.resolve()
    schema = load_ontology_schema(str(ontology_path))
    entity_linker = None if args.no_entity_linking else build_candidate_index(args.aliases.resolve())
    output_root = args.output_dir.resolve() if args.output_dir else None
    manifest_path = args.manifest.resolve() if args.manifest else output_root / "manifest.json"
    if args.dry_run:
        preview = [
            {
                "id": _numeric_index(path),
                "input": str(path),
                "question_present": bool(_question_for(path)),
                "extracted_ttl": str(_artifact_paths(path, output_root)["turtle"]),
            }
            for path in files
        ]
        missing_questions = [item["id"] for item in preview if not item["question_present"]]
        print(json.dumps(preview, ensure_ascii=False, indent=2))
        return 1 if missing_questions else 0
    results: list[dict[str, Any]] = []

    for input_path in files:
        index = _numeric_index(input_path)
        try:
            result = process_file(
                input_path,
                ontology_path,
                schema,
                question=_question_for(input_path),
                output_root=output_root,
                overwrite=args.overwrite,
                run_reasoner=args.reasoner,
                entity_linker=entity_linker,
                rebuild_downstream=args.rebuild_downstream,
                repair_shacl=args.shacl_repair,
                max_repair_iterations=args.max_repair_iterations,
            )
        except Exception as exc:
            result = {"id": index, "input": str(input_path), "status": "failed", "error": str(exc)}
            results.append(result)
            _write_json(manifest_path, results)
            if args.stop_on_error:
                print(json.dumps(result, ensure_ascii=False), file=sys.stderr)
                return 2
            continue
        results.append(result)
        _write_json(manifest_path, results)
        if args.stop_on_review and result["status"] == "review":
            print(json.dumps(result, ensure_ascii=False), file=sys.stderr)
            return 3

    counts = {
        status: sum(item["status"] == status for item in results)
        for status in ("completed", "review", "unscoreable_extraction", "failed", "skipped")
    }
    print(" ".join(f"{key}={value}" for key, value in counts.items()))
    return 1 if counts["failed"] or counts["review"] or counts["unscoreable_extraction"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
