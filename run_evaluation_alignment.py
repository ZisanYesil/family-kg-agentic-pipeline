#!/usr/bin/env python3
"""Derive one entity mapping from originals and apply it to both evaluation conditions."""

from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path

from rdflib import Graph

from run_inference_pipeline import atomic_write, parse_ids
from vector_entity_matching import (
    DEFAULT_CONTEXT_WEIGHT,
    DEFAULT_MARGIN,
    DEFAULT_MODEL,
    DEFAULT_NAME_WEIGHT,
    DEFAULT_STRING_WEIGHT,
    DEFAULT_THRESHOLD,
    SentenceTransformerBackend,
    canonicalize_graph,
    load_alias_index,
    load_ontology,
    match_graph_pair,
    write_same_as,
)


ROOT = Path(__file__).resolve().parent


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input-dir", required=True, type=Path)
    parser.add_argument("--ids", required=True, type=parse_ids)
    parser.add_argument("--ontology", type=Path, default=ROOT / "ontology" / "ontology.ttl")
    parser.add_argument("--aliases", type=Path, default=ROOT / "data" / "id_aliases.json")
    parser.add_argument("--embedding-model", default=DEFAULT_MODEL)
    parser.add_argument("--threshold", type=float, default=DEFAULT_THRESHOLD)
    parser.add_argument("--margin", type=float, default=DEFAULT_MARGIN)
    parser.add_argument("--summary-output", type=Path)
    args = parser.parse_args(argv)

    dataset = args.input_dir.resolve()
    ontology_data = load_ontology(args.ontology.resolve())
    aliases = load_alias_index(args.aliases.resolve())
    embedder = SentenceTransformerBackend(args.embedding_model, allow_download=False)
    common = {
        "ontology_data": ontology_data,
        "aliases": aliases,
        "embedder": embedder,
        "threshold": args.threshold,
        "margin_threshold": args.margin,
        "weights": (DEFAULT_NAME_WEIGHT, DEFAULT_STRING_WEIGHT, DEFAULT_CONTEXT_WEIGHT),
    }
    rows = []
    totals: Counter[str] = Counter()
    for index in args.ids:
        example = dataset / str(index)
        original_extracted = example / "originals" / f"extracted_{index}.ttl"
        original_ground = example / f"ground_truth_{index}.ttl"
        final_extracted = example / "inference" / f"extracted_reasoned_{index}.ttl"
        final_ground = example / "inference" / f"ground_truth_reasoned_{index}.ttl"
        missing = [
            str(path)
            for path in (original_extracted, original_ground, final_extracted, final_ground)
            if not path.is_file()
        ]
        if missing:
            rows.append({"id": index, "status": "failed", "error": f"Missing inputs: {missing}"})
            print(f"id={index} status=failed", flush=True)
            continue

        payload, mapping, _source = match_graph_pair(
            original_extracted, original_ground, **common
        )
        output = example / "evaluation" / "entity_alignment"
        artifacts = output / "artifacts"
        atomic_write(
            artifacts / f"mapping_{index}.json",
            json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        )
        write_same_as(mapping, artifacts / f"same_as_{index}.ttl")
        canonicalize_graph(
            Graph().parse(original_extracted, format="turtle"),
            mapping,
            output / f"baseline_extracted_aligned_{index}.ttl",
        )
        canonicalize_graph(
            Graph().parse(original_ground, format="turtle"),
            mapping,
            output / f"baseline_ground_truth_aligned_{index}.ttl",
        )
        canonicalize_graph(
            Graph().parse(final_extracted, format="turtle"),
            mapping,
            output / f"final_extracted_aligned_{index}.ttl",
        )
        canonicalize_graph(
            Graph().parse(final_ground, format="turtle"),
            mapping,
            output / f"final_ground_truth_aligned_{index}.ttl",
        )
        summary = payload["summary"]
        totals.update(summary)
        rows.append({"id": index, "status": "completed", **summary})
        print(f"id={index} status=completed matched={summary['matched']}", flush=True)

    summary = {
        "policy": (
            "One automatic mapping is derived from the frozen original graph pair and "
            "applied unchanged to baseline and final evaluation graphs. Review and "
            "unmatched entities remain unaligned."
        ),
        "examples": len(rows),
        "completed": sum(row["status"] == "completed" for row in rows),
        "failed": sum(row["status"] == "failed" for row in rows),
        "totals": dict(totals),
        "results": rows,
    }
    summary_path = args.summary_output or dataset / "evaluation" / "entity_alignment_summary.json"
    atomic_write(summary_path.resolve(), json.dumps(summary, ensure_ascii=False, indent=2) + "\n")
    print(f"completed={summary['completed']} failed={summary['failed']}")
    return 1 if summary["failed"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
