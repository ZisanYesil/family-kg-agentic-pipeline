#!/usr/bin/env python3
"""Relation-guided deterministic SPARQL QA over the frozen dataset graphs."""

from __future__ import annotations

import argparse
from pathlib import Path

import run_sparql_generic as generic
from phase2_qa.common import aggregate, atomic_json, parse_ids, score_answer


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dataset", type=Path, required=True)
    parser.add_argument("--ids", type=parse_ids, required=True)
    parser.add_argument("--ontology", type=Path, default=Path("ontology/ontology.ttl"))
    parser.add_argument("--graph-stage", choices=("extracted", "reasoned"), required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args(argv)
    dataset = args.dataset.resolve()
    ontology_index = generic.load_ontology_word_index(args.ontology.resolve())
    manifest = {int(row["example_id"]): row for row in generic.read_manifest_rows(dataset)}
    results = []
    for example_id in args.ids:
        if example_id not in manifest:
            raise ValueError(f"ID {example_id} is absent from the dataset manifest")
        scored = generic.score_example(
            dataset / str(example_id), manifest[example_id], ontology_index, args.graph_stage
        )
        score = score_answer(scored.get("predicted_answer"), scored["gold_answer"])
        results.append({
            "id": example_id,
            "status": "completed",
            "method": "relation_guided_symbolic_qa",
            "query_guidance": {
                "question_type": manifest[example_id]["type"],
                "relations": [value.strip() for value in manifest[example_id]["relations"].split("|")],
            },
            "graph_stage": args.graph_stage,
            **scored,
            **score,
        })
    payload = {
        "experiment": "relation_guided_symbolic_qa",
        "valid_for_direct_baseline_comparison": True,
        "query_guidance_source": "manifest.csv type and relations",
        "graph_stage": args.graph_stage,
        "query_execution": {
            "uses_llm": False,
            "llm_calls": 0,
            "llm_tokens": 0,
            "graph_construction_cost_included": False,
            "scope_note": (
                "Zero LLM usage applies only to QA over an already constructed graph; "
                "upstream extraction and SHACL feedback may use LLM calls."
            ),
        },
        "summary": aggregate(results),
        "results": results,
    }
    atomic_json(args.output, payload)
    print(payload["summary"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
