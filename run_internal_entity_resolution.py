#!/usr/bin/env python3
"""Resolve duplicate extracted entities without consulting evaluation ground truth."""

from __future__ import annotations

import argparse
import json
from collections import defaultdict
from pathlib import Path

from rdflib import Graph, URIRef

from agents.kg_builder_agent import DEFAULT_ENTITY_NAMESPACE
from run_inference_pipeline import atomic_write, parse_ids


def duplicate_groups(link_payload: dict) -> list[dict]:
    """Return only identity groups supported by one shared external QID."""
    by_qid: dict[str, set[str]] = defaultdict(set)
    for row in link_payload.get("entities", []):
        qid = row.get("qid")
        if row.get("decision") == "matched" and qid:
            by_qid[str(qid)].add(str(row["entity_id"]))
        conflict_qid = row.get("conflicting_qid")
        if row.get("method") == "duplicate_qid_conflict" and conflict_qid:
            by_qid[str(conflict_qid)].update(map(str, row.get("conflicting_entity_ids", [])))
    return [
        {"qid": qid, "entity_ids": sorted(entity_ids), "evidence": "shared_unique_wikidata_qid"}
        for qid, entity_ids in sorted(by_qid.items()) if len(entity_ids) > 1
    ]


def _safe_groups(mapping: dict, groups: list[dict]) -> tuple[list[dict], list[dict]]:
    entities = {str(row["id"]): row for row in mapping.get("entities", [])}
    accepted, rejected = [], []
    for group in groups:
        rows = [entities[value] for value in group["entity_ids"] if value in entities]
        types = {str(row.get("type")) for row in rows if row.get("type")}
        attribute_values: dict[str, set[str]] = defaultdict(set)
        for row in rows:
            for key, value in (row.get("attributes") or {}).items():
                if value is not None:
                    attribute_values[str(key)].add(json.dumps(value, sort_keys=True, ensure_ascii=False))
        conflicts = sorted(key for key, values in attribute_values.items() if len(values) > 1)
        if len(rows) != len(group["entity_ids"]) or len(types) > 1 or conflicts:
            rejected.append({
                **group,
                "decision": "review",
                "reason": "missing_entity_or_type_or_attribute_conflict",
                "types": sorted(types),
                "conflicting_attributes": conflicts,
            })
            continue
        accepted.append({**group, "decision": "merged", "canonical_id": group["entity_ids"][0]})
    return accepted, rejected


def resolve_mapping(mapping: dict, accepted: list[dict]) -> tuple[dict, dict[str, str]]:
    renaming = {
        entity_id: group["canonical_id"]
        for group in accepted for entity_id in group["entity_ids"]
    }
    merged_entities: dict[str, dict] = {}
    for source in mapping.get("entities", []):
        source_id = str(source["id"])
        canonical = renaming.get(source_id, source_id)
        if canonical not in merged_entities:
            merged_entities[canonical] = {**source, "id": canonical}
            merged_entities[canonical]["aliases"] = list(source.get("aliases") or [])
            merged_entities[canonical]["attributes"] = dict(source.get("attributes") or {})
            continue
        target = merged_entities[canonical]
        labels = [target.get("label"), source.get("label"), *(target.get("aliases") or []), *(source.get("aliases") or [])]
        target["aliases"] = sorted({str(value) for value in labels if value and value != target.get("label")})
        target["attributes"].update(source.get("attributes") or {})

    relations = []
    seen = set()
    for relation in mapping.get("relations", []):
        row = dict(relation)
        row["subject"] = renaming.get(str(row["subject"]), str(row["subject"]))
        row["object"] = renaming.get(str(row["object"]), str(row["object"]))
        key = (row["subject"], row["predicate"], row["object"])
        if key not in seen:
            relations.append(row)
            seen.add(key)
    resolved = dict(mapping)
    resolved["entities"] = list(merged_entities.values())
    resolved["relations"] = relations
    return resolved, renaming


def resolve_graph(graph: Graph, renaming: dict[str, str]) -> Graph:
    namespace = DEFAULT_ENTITY_NAMESPACE
    uri_mapping = {
        URIRef(namespace + source): URIRef(namespace + target)
        for source, target in renaming.items() if source != target
    }
    resolved = Graph()
    for prefix, value in graph.namespaces():
        resolved.bind(prefix, value)
    for subject, predicate, obj in graph:
        resolved.add((uri_mapping.get(subject, subject), predicate, uri_mapping.get(obj, obj)))
    return resolved


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input-dir", type=Path, required=True)
    parser.add_argument("--ids", type=parse_ids, required=True)
    parser.add_argument("--summary-output", type=Path)
    args = parser.parse_args(argv)
    dataset = args.input_dir.resolve()
    rows = []
    for index in args.ids:
        example = dataset / str(index)
        source = example / "originals" / f"extracted_{index}.ttl"
        mapping_path = example / "originals" / "artifacts" / f"mapping_{index}.json"
        links_path = example / "originals" / "artifacts" / f"entity_links_{index}.json"
        missing = [str(path) for path in (source, mapping_path, links_path) if not path.is_file()]
        if missing:
            rows.append({"id": index, "status": "failed", "error": f"Missing inputs: {missing}"})
            continue
        mapping = json.loads(mapping_path.read_text(encoding="utf-8"))
        links = json.loads(links_path.read_text(encoding="utf-8"))
        candidates = duplicate_groups(links)
        accepted, review = _safe_groups(mapping, candidates)
        resolved_mapping, renaming = resolve_mapping(mapping, accepted)
        resolved_graph = resolve_graph(Graph().parse(source, format="turtle"), renaming)
        output = example / "entity_resolved"
        graph_path = output / f"extracted_resolved_{index}.ttl"
        resolved_mapping_path = output / "artifacts" / f"mapping_resolved_{index}.json"
        report_path = output / "artifacts" / f"resolution_{index}.json"
        atomic_write(graph_path, resolved_graph.serialize(format="turtle"))
        atomic_write(resolved_mapping_path, json.dumps(resolved_mapping, ensure_ascii=False, indent=2) + "\n")
        report = {
            "id": index,
            "uses_ground_truth": False,
            "policy": "Merge only entities supported by one shared unique Wikidata QID, compatible types, and nonconflicting attributes.",
            "candidate_groups": candidates,
            "accepted_merges": accepted,
            "review_groups": review,
            "source_triples": len(Graph().parse(source, format="turtle")),
            "resolved_triples": len(resolved_graph),
        }
        atomic_write(report_path, json.dumps(report, ensure_ascii=False, indent=2) + "\n")
        rows.append({"id": index, "status": "completed", "merges": len(accepted), "reviews": len(review)})
    summary = {
        "examples": len(rows),
        "completed": sum(row["status"] == "completed" for row in rows),
        "failed": sum(row["status"] == "failed" for row in rows),
        "examples_with_merges": sum(row.get("merges", 0) > 0 for row in rows),
        "accepted_merges": sum(row.get("merges", 0) for row in rows),
        "review_groups": sum(row.get("reviews", 0) for row in rows),
        "results": rows,
    }
    destination = args.summary_output or dataset / "internal_entity_resolution_summary.json"
    atomic_write(destination.resolve(), json.dumps(summary, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({key: value for key, value in summary.items() if key != "results"}, indent=2))
    return 1 if summary["failed"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
