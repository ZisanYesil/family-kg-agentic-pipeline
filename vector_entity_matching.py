#!/usr/bin/env python3
"""Resolve entities in extracted 2Wiki graphs against ground-truth graphs.

The matcher combines alias-aware sentence embeddings, lexical similarity,
ontology-aware graph context, class compatibility, and globally optimal
Hungarian assignment. It supports one graph pair or index-matched directories.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import unicodedata
from collections import Counter, defaultdict
from difflib import SequenceMatcher
from pathlib import Path
from typing import Any
from urllib.parse import unquote, urlsplit

from rdflib import Graph, Literal, Namespace, OWL, RDF, RDFS, URIRef
from rdflib.namespace import SKOS

from evaluation_scope import path_is_graph_evaluation_excluded


SCRIPT_DIR = Path(__file__).resolve().parent
EX = Namespace("http://example.org/2wiki-ontology#")
WIKIDATA_ENTITY = "http://www.wikidata.org/entity/"
DEFAULT_MODEL = "paraphrase-multilingual-MiniLM-L12-v2"
DEFAULT_THRESHOLD = 0.55
DEFAULT_MARGIN = 0.05
DEFAULT_NAME_WEIGHT = 0.50
DEFAULT_STRING_WEIGHT = 0.25
DEFAULT_CONTEXT_WEIGHT = 0.25
DEFAULT_MIN_LEXICAL_ACCEPTANCE = 0.70
INFEASIBLE_COST = 1e6
LABEL_PREDICATES = {RDFS.label, SKOS.prefLabel, SKOS.altLabel}


def numeric_index(path: Path) -> int | None:
    match = re.search(r"(\d+)$", path.stem)
    return int(match.group(1)) if match else None


def local_name(value: str) -> str:
    split = urlsplit(value)
    if split.fragment:
        return split.fragment
    return split.path.rsplit("/", 1)[-1] if "/" in split.path else split.path


def semantic_form(value: str) -> str:
    text = unquote(value).replace("_", " ")
    text = re.sub(r"(?<=[a-z0-9])(?=[A-Z])", " ", text)
    text = unicodedata.normalize("NFKC", text)
    return re.sub(r"\s+", " ", text).strip()


def canonical_name_key(value: str) -> str:
    """Return a conservative cross-script key for exact-name anchoring.

    Diacritics and apostrophe variants are presentation differences in 2Wiki names, and
    ground-truth URI slugging often turns an apostrophe into an underscore (Ja'far ->
    Ja_far). Removing separators lets those forms meet. The anchor remains safe because
    unique_name_anchors requires the key to occur exactly once on both sides and checks
    ontology type compatibility.
    """
    text = unquote(value).replace("_", " ")
    text = unicodedata.normalize("NFKD", text).casefold()
    text = text.translate(str.maketrans("", "", "'’‘ʻʼʿʾ`´"))
    text = "".join(char for char in text if not unicodedata.combining(char))
    return "".join(char for char in text if char.isalnum())


def qid_from_uri(uri: URIRef | str | None) -> str | None:
    if uri is None:
        return None
    value = str(uri)
    if not value.startswith(WIKIDATA_ENTITY):
        return None
    qid = value[len(WIKIDATA_ENTITY):]
    return qid if re.fullmatch(r"Q\d+", qid) else None


def load_alias_index(path: Path) -> dict[str, dict[str, list[str]]]:
    """Load the project's JSONL alias file (despite its .json extension)."""
    index = {}
    with path.open(encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, 1):
            if not line.strip():
                continue
            try:
                row = json.loads(line)
            except json.JSONDecodeError as exc:
                raise ValueError(f"Invalid alias JSON on line {line_number}: {exc}") from exc
            qid = row.get("Q_id")
            if not isinstance(qid, str) or not re.fullmatch(r"Q\d+", qid):
                raise ValueError(f"Invalid Q_id on alias line {line_number}: {qid!r}")
            index[qid] = {
                "aliases": [str(v) for v in row.get("aliases", []) if str(v).strip()],
                "demonyms": [str(v) for v in row.get("demonyms", []) if str(v).strip()],
                "types": [str(v) for v in row.get("types", []) if str(v).strip()],
            }
    return index


def load_ontology(path: Path):
    graph = Graph().parse(path, format="turtle")
    classes = set(graph.subjects(RDF.type, OWL.Class))
    object_properties = set(graph.subjects(RDF.type, OWL.ObjectProperty))
    datatype_properties = set(graph.subjects(RDF.type, OWL.DatatypeProperty))
    parents = defaultdict(set)
    for child, parent in graph.subject_objects(RDFS.subClassOf):
        if child in classes and parent in classes:
            parents[child].add(parent)
    labels = {
        prop: str(graph.value(prop, RDFS.label) or semantic_form(local_name(str(prop))))
        for prop in object_properties | datatype_properties
    }
    # domain/range per property, used by usage_inferred_types() below to give
    # ground-truth entities a type even though ground-truth .ttl files never
    # carry explicit rdf:type triples (see build_dataset.py).
    domain_of, range_of = {}, {}
    for prop in object_properties | datatype_properties:
        domain_value = graph.value(prop, RDFS.domain)
        if domain_value in classes:
            domain_of[prop] = domain_value
        range_value = graph.value(prop, RDFS.range)
        if range_value in classes:  # datatype-property ranges (xsd:*, rdfs:Literal) aren't classes; skip
            range_of[prop] = range_value
    return graph, classes, object_properties, datatype_properties, parents, labels, domain_of, range_of


def ancestor_closure(cls: URIRef, parents: dict[URIRef, set[URIRef]]) -> set[URIRef]:
    closure = {cls}
    frontier = [cls]
    while frontier:
        current = frontier.pop()
        for parent in parents.get(current, ()):
            if parent not in closure:
                closure.add(parent)
                frontier.append(parent)
    return closure


def usage_inferred_types(
    entity: URIRef,
    graph: Graph,
    object_properties: set[URIRef],
    domain_of: dict[URIRef, URIRef],
    range_of: dict[URIRef, URIRef],
) -> set[URIRef]:
    """Types implied by how `entity` is actually used as subject/object of
    property triples in `graph`, via each property's declared rdfs:domain /
    rdfs:range -- e.g. an entity used as the subject of ex:hasBirthDate is
    implied to be an ex:Person, since that's hasBirthDate's declared domain.

    This exists because ground-truth .ttl files (build_dataset.py's output)
    never contain rdf:type triples -- only the relation triples themselves.
    Without this fallback, entity_types() returns an empty set for every
    single ground-truth entity, and types_compatible() treats an empty type
    set as "no constraint" -- so the matcher's class-compatibility gate
    (advertised in matching_config as "class_compatibility": "hard") never
    actually rejects anything: a Place-typed extraction can be assigned to a
    ground-truth Person purely because the ground truth carries no type to
    disagree with. Inferring a type from property usage is the same
    reasoning a person would use reading the same triples.
    """
    types = set()
    for _, predicate, _ in graph.triples((entity, None, None)):
        cls = domain_of.get(predicate)
        if cls is not None:
            types.add(cls)
    for _, predicate, _ in graph.triples((None, None, entity)):
        if predicate in object_properties:
            cls = range_of.get(predicate)
            if cls is not None:
                types.add(cls)
    return types


def entity_types(
    entity: URIRef,
    graph: Graph,
    classes: set[URIRef],
    object_properties: set[URIRef] | None = None,
    domain_of: dict[URIRef, URIRef] | None = None,
    range_of: dict[URIRef, URIRef] | None = None,
) -> set[URIRef]:
    asserted = {value for value in graph.objects(entity, RDF.type) if value in classes}
    if asserted:
        # An explicit rdf:type is the extraction's own claim about this
        # entity (or, in principle, an asserted ground-truth type) -- trust
        # it rather than overriding/diluting it with usage-inferred types.
        return asserted
    if object_properties is not None and domain_of is not None:
        return usage_inferred_types(entity, graph, object_properties, domain_of, range_of or {})
    return asserted


def most_specific_types(
    entity: URIRef,
    graph: Graph,
    classes: set[URIRef],
    parents: dict[URIRef, set[URIRef]],
    object_properties: set[URIRef] | None = None,
    domain_of: dict[URIRef, URIRef] | None = None,
    range_of: dict[URIRef, URIRef] | None = None,
) -> set[URIRef]:
    types = entity_types(entity, graph, classes, object_properties, domain_of, range_of)
    return {
        cls
        for cls in types
        if not any(cls != other and cls in ancestor_closure(other, parents) for other in types)
    }


def types_compatible(
    left: set[URIRef], right: set[URIRef], parents: dict[URIRef, set[URIRef]]
) -> bool:
    if not left or not right:
        return True
    return any(
        a in ancestor_closure(b, parents) or b in ancestor_closure(a, parents)
        for a in left
        for b in right
    )


def collect_entities(
    graph: Graph,
    classes: set[URIRef],
    object_properties: set[URIRef],
    datatype_properties: set[URIRef],
) -> list[URIRef]:
    entities = {
        subject
        for subject, _, cls in graph.triples((None, RDF.type, None))
        if isinstance(subject, URIRef) and cls in classes
    }
    for subject, predicate, obj in graph:
        if predicate in object_properties | datatype_properties and isinstance(subject, URIRef):
            entities.add(subject)
        if predicate in object_properties and isinstance(obj, URIRef):
            entities.add(obj)
    return sorted(entities, key=str)


def collect_name_variants(
    entity: URIRef,
    graph: Graph,
    aliases: dict[str, dict[str, list[str]]],
) -> list[dict[str, str]]:
    variants = []
    seen = set()

    def add(value: object, source: str):
        text = semantic_form(str(value))
        key = text.casefold()
        if text and key not in seen:
            seen.add(key)
            variants.append({"text": text, "source": source})

    qid = qid_from_uri(entity)
    alias_row = aliases.get(qid or "", {})
    for value in alias_row.get("aliases", []):
        add(value, "id_aliases:alias")
    for value in alias_row.get("demonyms", []):
        add(value, "id_aliases:demonym")
    for predicate in LABEL_PREDICATES:
        for value in graph.objects(entity, predicate):
            add(value, local_name(str(predicate)))
    for predicate, value in graph.predicate_objects(entity):
        if local_name(str(predicate)) in {"alsoKnownAs", "knownAs", "hasDemonym"}:
            add(value, local_name(str(predicate)))
    if not qid:
        add(local_name(str(entity)), "uri")
    if not variants:
        add(qid or local_name(str(entity)), "uri")
    return variants


def preferred_name(entity: URIRef, graph: Graph, aliases) -> str:
    return collect_name_variants(entity, graph, aliases)[0]["text"]


def build_context_string(
    entity: URIRef,
    graph: Graph,
    aliases,
    property_labels: dict[URIRef, str],
    object_properties: set[URIRef],
    datatype_properties: set[URIRef],
) -> str:
    parts = [preferred_name(entity, graph, aliases) + "."]
    facts = set()
    for _, predicate, obj in graph.triples((entity, None, None)):
        if predicate in object_properties and isinstance(obj, URIRef):
            facts.add(f"{property_labels[predicate]}: {preferred_name(obj, graph, aliases)}.")
        elif predicate in datatype_properties and isinstance(obj, Literal):
            facts.add(f"{property_labels[predicate]}: {obj}.")
    for subject, predicate, _ in graph.triples((None, None, entity)):
        if predicate in object_properties and isinstance(subject, URIRef):
            facts.add(
                f"inverse {property_labels[predicate]}: "
                f"{preferred_name(subject, graph, aliases)}."
            )
    return " ".join(parts + sorted(facts, key=str.casefold))


class EmbeddingBackend:
    model_name = "custom"

    def encode(self, texts: list[str]):
        raise NotImplementedError


class SentenceTransformerBackend(EmbeddingBackend):
    def __init__(self, model_name=DEFAULT_MODEL, allow_download=False):
        self.model_name = model_name
        old_hf = os.environ.get("HF_HUB_OFFLINE")
        old_transformers = os.environ.get("TRANSFORMERS_OFFLINE")
        if not allow_download:
            os.environ["HF_HUB_OFFLINE"] = "1"
            os.environ["TRANSFORMERS_OFFLINE"] = "1"
        try:
            from sentence_transformers import SentenceTransformer

            self.model = SentenceTransformer(model_name)
            self.cache = {}
        except ModuleNotFoundError as exc:
            raise RuntimeError(
                "sentence-transformers is required; install requirements.txt"
            ) from exc
        except (OSError, ValueError) as exc:
            if not allow_download:
                raise RuntimeError(
                    f"Embedding model is not cached: {model_name}; use --allow-model-download"
                ) from exc
            raise
        finally:
            if old_hf is None:
                os.environ.pop("HF_HUB_OFFLINE", None)
            else:
                os.environ["HF_HUB_OFFLINE"] = old_hf
            if old_transformers is None:
                os.environ.pop("TRANSFORMERS_OFFLINE", None)
            else:
                os.environ["TRANSFORMERS_OFFLINE"] = old_transformers

    def encode(self, texts: list[str]):
        np, _ = require_numeric_stack()
        missing = list(dict.fromkeys(text for text in texts if text not in self.cache))
        if missing:
            vectors = self.model.encode(
                missing, convert_to_numpy=True, normalize_embeddings=True
            )
            self.cache.update(zip(missing, vectors))
        if not texts:
            dimension = self.model.get_sentence_embedding_dimension()
            return np.zeros((0, dimension), dtype=np.float32)
        return np.asarray([self.cache[text] for text in texts], dtype=np.float32)


def require_numeric_stack():
    try:
        import numpy as np
        from scipy.optimize import linear_sum_assignment
    except ModuleNotFoundError as exc:
        raise RuntimeError("numpy and scipy are required; install requirements.txt") from exc
    return np, linear_sum_assignment


def cosine_similarity_matrix(left, right):
    np, _ = require_numeric_stack()
    if left.shape[0] == 0 or right.shape[0] == 0:
        return np.zeros((left.shape[0], right.shape[0]), dtype=np.float32)
    result = np.asarray(left, dtype=np.float64) @ np.asarray(right, dtype=np.float64).T
    if not np.isfinite(result).all():
        raise ValueError("Embedding backend returned non-finite values")
    return np.clip(result, -1.0, 1.0).astype(np.float32)


def string_similarity(left: str, right: str) -> float:
    a, b = left.casefold(), right.casefold()
    sequence = SequenceMatcher(None, a, b).ratio()
    a_tokens, b_tokens = set(re.findall(r"\w+", a)), set(re.findall(r"\w+", b))
    union = a_tokens | b_tokens
    jaccard = len(a_tokens & b_tokens) / len(union) if union else 0.0
    containment = (
        len(a_tokens & b_tokens) / min(len(a_tokens), len(b_tokens))
        if a_tokens and b_tokens
        else 0.0
    )
    return 0.45 * sequence + 0.25 * jaccard + 0.30 * containment


def alias_aware_scores(left_variants, right_variants, embedder, name_weight, string_weight):
    np, _ = require_numeric_stack()
    left_flat = [v for variants in left_variants for v in variants]
    right_flat = [v for variants in right_variants for v in variants]
    embeddings = embedder.encode([v["text"] for v in left_flat + right_flat])
    left_offsets, right_offsets, offset = [], [], 0
    for variants in left_variants:
        left_offsets.append((offset, offset + len(variants)))
        offset += len(variants)
    for variants in right_variants:
        right_offsets.append((offset, offset + len(variants)))
        offset += len(variants)
    name_scores = np.zeros((len(left_variants), len(right_variants)), dtype=np.float32)
    lexical_scores = np.zeros_like(name_scores)
    best_pairs = [[None for _ in right_variants] for _ in left_variants]
    for i, (ls, le) in enumerate(left_offsets):
        for j, (rs, re_) in enumerate(right_offsets):
            emb = cosine_similarity_matrix(embeddings[ls:le], embeddings[rs:re_])
            lex = np.asarray(
                [
                    [string_similarity(a["text"], b["text"]) for b in right_variants[j]]
                    for a in left_variants[i]
                ],
                dtype=np.float32,
            )
            row, col = np.unravel_index(int(np.argmax(name_weight * emb + string_weight * lex)), emb.shape)
            name_scores[i, j], lexical_scores[i, j] = emb[row, col], lex[row, col]
            best_pairs[i][j] = {
                "extracted_text": left_variants[i][row]["text"],
                "extracted_source": left_variants[i][row]["source"],
                "ground_truth_text": right_variants[j][col]["text"],
                "ground_truth_source": right_variants[j][col]["source"],
            }
    return name_scores, lexical_scores, best_pairs


def unique_name_anchors(left_entities, right_entities, left_variants, right_variants, compatible):
    left_names, right_names = defaultdict(set), defaultdict(set)
    for entity, variants in zip(left_entities, left_variants):
        for variant in variants:
            key = canonical_name_key(variant["text"])
            if key:
                left_names[key].add(entity)
    for entity, variants in zip(right_entities, right_variants):
        for variant in variants:
            key = canonical_name_key(variant["text"])
            if key:
                right_names[key].add(entity)
    provisional = {}
    for name in left_names.keys() & right_names.keys():
        if len(left_names[name]) == len(right_names[name]) == 1:
            left, right = next(iter(left_names[name])), next(iter(right_names[name]))
            if compatible(left, right):
                provisional[left] = right
    target_counts = Counter(provisional.values())
    return {
        left: right
        for left, right in provisional.items()
        if target_counts[right] == 1
    }


def relation_profile(entity, graph, object_properties):
    profile = defaultdict(set)
    for _, predicate, obj in graph.triples((entity, None, None)):
        if predicate in object_properties and isinstance(obj, URIRef):
            profile[obj].add((str(predicate), "out"))
    for subject, predicate, _ in graph.triples((None, None, entity)):
        if predicate in object_properties and isinstance(subject, URIRef):
            profile[subject].add((str(predicate), "in"))
    return profile


def anchored_context_scores(
    left_entities, right_entities, left_graph, right_graph, object_properties, anchors, fallback
):
    np, _ = require_numeric_stack()
    scores = np.array(fallback, copy=True)
    left_profiles = {e: relation_profile(e, left_graph, object_properties) for e in left_entities}
    right_profiles = {e: relation_profile(e, right_graph, object_properties) for e in right_entities}
    for i, left in enumerate(left_entities):
        for j, right in enumerate(right_entities):
            a, b = set(), set()
            for left_anchor, right_anchor in anchors.items():
                anchor = str(right_anchor)
                a.update((relation, direction, anchor) for relation, direction in left_profiles[left].get(left_anchor, ()))
                b.update((relation, direction, anchor) for relation, direction in right_profiles[right].get(right_anchor, ()))
            if a or b:
                scores[i, j] = 0.5 * fallback[i, j] + 0.5 * (len(a & b) / len(a | b))
    return scores


def hungarian_match(scores, compatible_matrix, threshold):
    np, linear_sum_assignment = require_numeric_stack()
    rows, candidates = scores.shape
    cost = np.full((rows, candidates + rows), INFEASIBLE_COST, dtype=np.float64)
    for i in range(rows):
        for j in range(candidates):
            if compatible_matrix[i, j]:
                cost[i, j] = 1.0 - float(scores[i, j])
        cost[i, candidates + i] = 1.0 - threshold
    row_indices, columns = linear_sum_assignment(cost)
    return {
        int(i): (int(j) if j < candidates and scores[i, j] >= threshold else None)
        for i, j in zip(row_indices, columns)
    }


def canonicalize_graph(source, mapping, destination):
    graph = Graph()
    for prefix, namespace in source.namespaces():
        graph.bind(prefix, namespace)
    for subject, predicate, obj in source:
        if predicate == OWL.sameAs:
            continue
        graph.add((mapping.get(subject, subject), predicate, mapping.get(obj, obj)))
    destination.parent.mkdir(parents=True, exist_ok=True)
    graph.serialize(destination, format="turtle")


def write_same_as(mapping, destination):
    graph = Graph()
    graph.bind("owl", OWL)
    for extracted, ground_truth in mapping.items():
        graph.add((extracted, OWL.sameAs, ground_truth))
    destination.parent.mkdir(parents=True, exist_ok=True)
    graph.serialize(destination, format="turtle")


def write_matched_subgraph(source, all_entities, kept_entities, destination, renaming=None):
    """Write the full graph, canonicalizing only accepted entity URIs.

    ``all_entities`` and ``kept_entities`` are retained in the signature for
    compatibility with existing callers.  Unmatched entities are deliberately
    left unchanged instead of being filtered out.
    """
    renaming = renaming or {}
    graph = Graph()
    for prefix, namespace in source.namespaces():
        graph.bind(prefix, namespace)
    graph.bind("owl", OWL)
    for subject, predicate, obj in source:
        if predicate == OWL.sameAs:
            continue
        canonical_subject = renaming.get(subject, subject)
        canonical_object = renaming.get(obj, obj)
        if predicate == OWL.sameAs and canonical_subject == canonical_object:
            continue
        graph.add((canonical_subject, predicate, canonical_object))
    destination.parent.mkdir(parents=True, exist_ok=True)
    graph.serialize(destination, format="turtle")


def write_markdown_report(payload, destination):
    summary = payload["summary"]
    lines = [
        f"# Entity matching report: {destination.parent.parent.name}",
        "",
        f"- Extracted entities: {summary['extracted_entities']}",
        f"- Ground-truth entities: {summary['ground_truth_entities']}",
        f"- Accepted matches: {summary['matched']}",
        f"- Review: {summary['review']}",
        f"- Unmatched extracted entities: {summary['unmatched']}",
        f"- Unmatched ground-truth entities: {summary['unmatched_ground_truth']}",
        "",
        "| Decision | Extracted entity | Ground-truth entity | Score | Margin |",
        "|---|---|---|---:|---:|",
    ]
    for row in payload["entities"]:
        score = "" if row["final_score"] is None else f"{row['final_score']:.4f}"
        margin = "" if row["margin"] is None else f"{row['margin']:.4f}"
        lines.append(
            f"| {row['decision']} | `{row['extracted_uri']}` | "
            f"`{row['ground_truth_uri'] or ''}` | {score} | {margin} |"
        )
    if payload["unmatched_ground_truth_entities"]:
        lines.extend(["", "## Unmatched ground-truth entities", ""])
        lines.extend(f"- `{uri}`" for uri in payload["unmatched_ground_truth_entities"])
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_json(path, payload):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")


def match_graph_pair(
    extracted_path: Path,
    ground_truth_path: Path,
    ontology_data,
    aliases,
    embedder,
    threshold,
    margin_threshold,
    weights,
    dump_matrix=False,
):
    np, _ = require_numeric_stack()
    _, classes, object_properties, datatype_properties, parents, property_labels, domain_of, range_of = ontology_data
    extracted_graph = Graph().parse(extracted_path, format="turtle")
    ground_graph = Graph().parse(ground_truth_path, format="turtle")
    left = collect_entities(extracted_graph, classes, object_properties, datatype_properties)
    right = collect_entities(ground_graph, classes, object_properties, datatype_properties)
    if not right:
        raise ValueError(f"No project entities found in ground-truth graph: {ground_truth_path}")

    # A valid extraction may be empty. Keep it in the evaluation cohort instead
    # of aborting the whole batch: it has no candidate pairs and every
    # ground-truth entity is unmatched. Downstream inference/triple matching can
    # then score the example as an ordinary zero-recall case.
    if not left:
        unmatched_ground = [str(entity) for entity in right]
        payload = {
            "mode": "2wiki_graph_pair",
            "extracted_graph": str(extracted_path),
            "ground_truth_graph": str(ground_truth_path),
            "matching_config": {
                "embedding_model": getattr(embedder, "model_name", type(embedder).__name__),
                "threshold": threshold,
                "margin": margin_threshold,
                "name_weight": weights[0],
                "string_weight": weights[1],
                "context_weight": weights[2],
                "class_compatibility": "hard",
                "automatic_acceptance": "combined-score assignment above confidence margin",
            },
            "exact_name_anchors": {},
            "summary": {
                "extracted_entities": 0,
                "ground_truth_entities": len(right),
                "matched": 0,
                "review": 0,
                "unmatched": 0,
                "unmatched_ground_truth": len(right),
            },
            "entities": [],
            "unmatched_ground_truth_entities": unmatched_ground,
        }
        if dump_matrix:
            payload["debug_similarity_matrix"] = {
                "extracted": [],
                "ground_truth": unmatched_ground,
                "compatible": [],
                "name_embedding": [],
                "string": [],
                "context": [],
                "graph": [],
                "combined": [],
            }
        return payload, {}, extracted_graph

    left_types = [
        most_specific_types(e, extracted_graph, classes, parents, object_properties, domain_of, range_of)
        for e in left
    ]
    right_types = [
        most_specific_types(e, ground_graph, classes, parents, object_properties, domain_of, range_of)
        for e in right
    ]
    compatible = np.asarray(
        [[types_compatible(a, b, parents) for b in right_types] for a in left_types], dtype=bool
    )
    identity_pairs = set()
    for i, extracted_entity in enumerate(left):
        for j, ground_entity in enumerate(right):
            extracted_qid = qid_from_uri(extracted_entity)
            same_qid = extracted_qid is not None and extracted_qid == qid_from_uri(ground_entity)
            asserted_same_as = (extracted_entity, OWL.sameAs, ground_entity) in extracted_graph
            if asserted_same_as or same_qid:
                identity_pairs.add((i, j))
                compatible[i, j] = True
    left_variants = [collect_name_variants(e, extracted_graph, aliases) for e in left]
    right_variants = [collect_name_variants(e, ground_graph, aliases) for e in right]
    name_scores, lexical_scores, best_pairs = alias_aware_scores(
        left_variants, right_variants, embedder, weights[0], weights[1]
    )
    left_context = [
        build_context_string(e, extracted_graph, aliases, property_labels, object_properties, datatype_properties)
        for e in left
    ]
    right_context = [
        build_context_string(e, ground_graph, aliases, property_labels, object_properties, datatype_properties)
        for e in right
    ]
    context_embeddings = embedder.encode(left_context + right_context)
    context_scores = cosine_similarity_matrix(context_embeddings[: len(left)], context_embeddings[len(left):])
    anchors = unique_name_anchors(
        left, right, left_variants, right_variants,
        lambda a, b: compatible[left.index(a), right.index(b)],
    )
    identity_anchors = {left[i]: right[j] for i, j in identity_pairs}
    reserved_targets = set(identity_anchors.values())
    anchors = {
        source: target
        for source, target in anchors.items()
        if source in identity_anchors or target not in reserved_targets
    }
    anchors.update(identity_anchors)
    graph_scores = anchored_context_scores(
        left, right, extracted_graph, ground_graph, object_properties, anchors, context_scores
    )
    combined = weights[0] * name_scores + weights[1] * lexical_scores + weights[2] * graph_scores
    # A normalized name that is unique on both sides and type-compatible is stronger
    # evidence than a small embedding-margin fluctuation. Give these anchors the same
    # assignment priority as explicit identity evidence; ambiguous keys never enter
    # ``anchors`` and therefore remain governed by the normal threshold/margin rules.
    for source, target in anchors.items():
        combined[left.index(source), right.index(target)] = 1.0
    # Explicit owl:sameAs and identical QIDs outrank class disagreement.
    for i, j in identity_pairs:
        combined[i, j] = 1.0
    assignment = hungarian_match(combined, compatible, threshold)

    rows, accepted = [], {}
    for i, entity in enumerate(left):
        assigned = assignment.get(i)
        alternatives = [
            float(combined[i, j]) for j in range(len(right)) if j != assigned and compatible[i, j]
        ]
        score = float(combined[i, assigned]) if assigned is not None else None
        best_alternative = max(alternatives) if alternatives else None
        margin = score - best_alternative if score is not None and best_alternative is not None else score
        is_independent_anchor = (
            assigned is not None
            and (
                anchors.get(entity) == right[assigned]
                or (i, assigned) in identity_pairs
            )
        )
        lexical_score = (
            float(lexical_scores[i, assigned]) if assigned is not None else None
        )
        # Accept the assigned candidate when the global assignment clears the configured
        # confidence margin. This preserves the original matcher behaviour, in which the
        # combined name, lexical, and graph-context score determines acceptance.
        independently_supported = is_independent_anchor or (
            lexical_score is not None
            and lexical_score >= DEFAULT_MIN_LEXICAL_ACCEPTANCE
        )
        decision = (
            "unmatched"
            if assigned is None
            else "matched"
            if margin is not None
            and margin >= margin_threshold
            else "review"
        )
        if decision == "matched":
            accepted[entity] = right[assigned]
        rows.append({
            "extracted_uri": str(entity),
            "extracted_types": sorted(local_name(str(v)) for v in left_types[i]),
            "extracted_name_variants": left_variants[i],
            "context": left_context[i],
            "decision": decision,
            "matched": decision == "matched",
            "ground_truth_uri": str(right[assigned]) if assigned is not None else None,
            "ground_truth_types": sorted(local_name(str(v)) for v in right_types[assigned]) if assigned is not None else None,
            "ground_truth_name_variants": right_variants[assigned] if assigned is not None else None,
            "best_name_pair": best_pairs[i][assigned] if assigned is not None else None,
            "final_score": score,
            "name_embedding_score": float(name_scores[i, assigned]) if assigned is not None else None,
            "string_score": lexical_score,
            "independent_identity_support": independently_supported,
            "context_score": float(context_scores[i, assigned]) if assigned is not None else None,
            "graph_score": float(graph_scores[i, assigned]) if assigned is not None else None,
            "margin": margin,
        })
    rows.sort(key=lambda r: ({"matched": 0, "review": 1, "unmatched": 2}[r["decision"]], -(r["final_score"] or 0), r["extracted_uri"]))
    unmatched_ground = sorted(str(entity) for entity in set(right) - set(accepted.values()))
    payload = {
        "mode": "2wiki_graph_pair",
        "extracted_graph": str(extracted_path),
        "ground_truth_graph": str(ground_truth_path),
        "matching_config": {
            "embedding_model": getattr(embedder, "model_name", type(embedder).__name__),
            "threshold": threshold,
            "margin": margin_threshold,
            "name_weight": weights[0],
            "string_weight": weights[1],
            "context_weight": weights[2],
            "class_compatibility": "hard",
            "automatic_acceptance": "combined-score assignment above confidence margin",
        },
        "exact_name_anchors": {str(a): str(b) for a, b in anchors.items()},
        "summary": {
            "extracted_entities": len(left),
            "ground_truth_entities": len(right),
            "matched": sum(r["decision"] == "matched" for r in rows),
            "review": sum(r["decision"] == "review" for r in rows),
            "unmatched": sum(r["decision"] == "unmatched" for r in rows),
            "unmatched_ground_truth": len(unmatched_ground),
        },
        "entities": rows,
        "unmatched_ground_truth_entities": unmatched_ground,
    }
    if dump_matrix:
        payload["debug_similarity_matrix"] = {
            "extracted": [str(v) for v in left],
            "ground_truth": [str(v) for v in right],
            "compatible": compatible.tolist(),
            "name_embedding": name_scores.tolist(),
            "string": lexical_scores.tolist(),
            "context": context_scores.tolist(),
            "graph": graph_scores.tolist(),
            "combined": combined.tolist(),
        }
    return payload, accepted, extracted_graph


def build_parser():
    parser = argparse.ArgumentParser(description="Ontology-aware 2Wiki vector entity matching")
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--extracted-graph", type=Path)
    mode.add_argument("--extracted-dir", type=Path)
    parser.add_argument("--ground-truth-graph", type=Path)
    parser.add_argument("--ground-truth-dir", type=Path, default=SCRIPT_DIR / "pilot")
    parser.add_argument("--ontology", type=Path, default=SCRIPT_DIR / "ontology" / "ontology.ttl")
    parser.add_argument("--aliases", type=Path, default=SCRIPT_DIR / "data" / "id_aliases.json")
    parser.add_argument("--output", type=Path)
    parser.add_argument("--summary-output", type=Path)
    parser.add_argument(
        "--output-dir",
        type=Path,
        help="Optional flat batch output; default writes to each example's entity_matching/ directory",
    )
    parser.add_argument("--output-ttl", type=Path, help="Optional canonicalized graph (direct mode)")
    parser.add_argument("--same-as-output", type=Path, help="Optional owl:sameAs graph (direct mode)")
    parser.add_argument(
        "--write-canonicalized",
        action="store_true",
        help="Write canonicalized_N.ttl files in batch mode",
    )
    parser.add_argument(
        "--write-matched-graphs",
        action="store_true",
        help="Write full extracted and ground-truth graphs, canonicalizing accepted matches",
    )
    parser.add_argument("--embedding-model", default=DEFAULT_MODEL)
    parser.add_argument("--allow-model-download", action="store_true")
    parser.add_argument("--threshold", type=float, default=DEFAULT_THRESHOLD)
    parser.add_argument("--margin", type=float, default=DEFAULT_MARGIN)
    parser.add_argument("--name-weight", type=float, default=DEFAULT_NAME_WEIGHT)
    parser.add_argument("--string-weight", type=float, default=DEFAULT_STRING_WEIGHT)
    parser.add_argument("--context-weight", type=float, default=DEFAULT_CONTEXT_WEIGHT)
    parser.add_argument("--dump-similarity-matrix", action="store_true")
    return parser


def validate_args(args):
    for path in (args.ontology, args.aliases):
        if not path.is_file():
            raise FileNotFoundError(path)
    if not -1 <= args.threshold <= 1:
        raise ValueError("--threshold must be between -1 and 1")
    if not 0 <= args.margin <= 2:
        raise ValueError("--margin must be between 0 and 2")
    weights = (args.name_weight, args.string_weight, args.context_weight)
    if any(v < 0 or v > 1 for v in weights) or abs(sum(weights) - 1) > 1e-9:
        raise ValueError("matching weights must each be in [0,1] and sum to 1")
    if args.extracted_graph:
        if not args.extracted_graph.is_file():
            raise FileNotFoundError(args.extracted_graph)
        if not args.ground_truth_graph or not args.ground_truth_graph.is_file():
            raise ValueError("direct mode requires an existing --ground-truth-graph")
    elif args.summary_output is None:
        raise ValueError("batch mode requires --summary-output")
    elif not args.extracted_dir.is_dir() or not args.ground_truth_dir.is_dir():
        raise ValueError("batch mode requires existing extracted and ground-truth directories")
    return weights


def indexed_files(directory: Path, prefix: str | None = None) -> dict[int, Path]:
    result = {}
    for path in sorted(directory.rglob("*.ttl")):
        if path_is_graph_evaluation_excluded(path):
            continue
        if prefix is not None:
            if not re.fullmatch(rf"{re.escape(prefix)}\d+\.ttl", path.name):
                continue
        index = numeric_index(path)
        if index is not None:
            if index in result:
                raise ValueError(f"Duplicate graph index {index} in {directory}")
            result[index] = path
    return result


def main(argv=None):
    args = build_parser().parse_args(argv)
    try:
        weights = validate_args(args)
        ontology_data = load_ontology(args.ontology)
        aliases = load_alias_index(args.aliases)
        embedder = SentenceTransformerBackend(args.embedding_model, args.allow_model_download)
        common = dict(
            ontology_data=ontology_data,
            aliases=aliases,
            embedder=embedder,
            threshold=args.threshold,
            margin_threshold=args.margin,
            weights=weights,
            dump_matrix=args.dump_similarity_matrix,
        )
        if args.extracted_graph:
            payload, mapping, source = match_graph_pair(
                args.extracted_graph, args.ground_truth_graph, **common
            )
            output = args.output or Path("vector_entity_match.json")
            write_json(output, payload)
            if args.output_ttl:
                canonicalize_graph(source, mapping, args.output_ttl)
            if args.same_as_output:
                write_same_as(mapping, args.same_as_output)
            print(json.dumps(payload["summary"], ensure_ascii=False))
            print(f"Wrote {output}")
            return 0

        extracted = indexed_files(args.extracted_dir, "extracted_")
        ground = indexed_files(args.ground_truth_dir, "ground_truth_")
        missing = sorted(extracted.keys() - ground.keys())
        if missing:
            raise ValueError(f"Missing ground-truth indices: {missing[:20]}")
        if not extracted:
            raise ValueError(f"No indexed .ttl files found in {args.extracted_dir}")
        summaries, totals = [], Counter()
        for index in sorted(extracted):
            payload, mapping, source = match_graph_pair(extracted[index], ground[index], **common)
            if args.output_dir:
                destination = args.output_dir
            else:
                parent = extracted[index].parent
                example_directory = parent.parent if parent.name == "originals" else parent
                destination = example_directory / "entity_matching"
            artifacts = destination / "artifacts"
            write_json(artifacts / f"match_{index}.json", payload)
            write_markdown_report(payload, destination / f"report_{index}.md")
            write_same_as(mapping, artifacts / f"same_as_{index}.ttl")
            if args.write_matched_graphs:
                ground_source = Graph().parse(ground[index], format="turtle")
                _, classes, object_properties, datatype_properties, _, _, _, _ = ontology_data
                extracted_entities = collect_entities(source, classes, object_properties, datatype_properties)
                ground_entities = collect_entities(ground_source, classes, object_properties, datatype_properties)
                write_matched_subgraph(
                    source,
                    extracted_entities,
                    mapping.keys(),
                    destination / f"matched_extracted_{index}.ttl",
                    renaming=mapping,
                )
                write_matched_subgraph(
                    ground_source,
                    ground_entities,
                    mapping.values(),
                    destination / f"matched_ground_truth_{index}.ttl",
                )
            if args.write_canonicalized:
                canonicalize_graph(
                    source, mapping, destination / f"canonicalized_{index}.ttl"
                )
            summaries.append({"index": index, **payload["summary"]})
            totals.update(payload["summary"])
        summary = {"mode": "2wiki_batch", "files": len(summaries), "totals": dict(totals), "graphs": summaries}
        summary_path = args.summary_output
        write_json(summary_path, summary)
        print(json.dumps(summary["totals"], ensure_ascii=False))
        print(f"Wrote {args.output_dir or 'per-example entity_matching/ directories'}")
        return 0
    except (OSError, ValueError, RuntimeError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
