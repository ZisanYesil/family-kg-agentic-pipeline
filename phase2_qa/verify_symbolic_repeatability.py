#!/usr/bin/env python3
"""Verify repeatable symbolic-QA answers and retrieval traces on fixed inputs."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import run_sparql_generic as generic
from phase2_qa.common import atomic_json, parse_ids


def _sha256_bytes(content: bytes) -> str:
    return hashlib.sha256(content).hexdigest()


def _sha256_file(path: Path) -> str:
    return _sha256_bytes(path.read_bytes())


def canonical_result(row: dict) -> dict:
    """Retain only query outputs whose repeatability is under test."""
    return {
        "id": int(row["example_id"]),
        "predicted_answer": row.get("predicted_answer"),
        "retrieval_trace": row.get("note"),
    }


def result_fingerprint(results: list[dict]) -> str:
    canonical = sorted((canonical_result(row) for row in results), key=lambda row: row["id"])
    encoded = json.dumps(
        canonical, ensure_ascii=False, sort_keys=True, separators=(",", ":")
    ).encode("utf-8")
    return _sha256_bytes(encoded)


def input_fingerprint(
    dataset: Path,
    ontology: Path,
    ids: list[int],
    graph_stage: str,
) -> tuple[str, dict]:
    files = [ontology, dataset / "manifest.csv"]
    for example_id in ids:
        example = dataset / str(example_id)
        files.append(example / f"example{example_id}_question.txt")
        if graph_stage == "reasoned":
            files.append(example / "inference" / f"extracted_reasoned_{example_id}.ttl")
        else:
            files.append(example / "originals" / f"extracted_{example_id}.ttl")
    missing = [str(path) for path in files if not path.is_file()]
    if missing:
        raise FileNotFoundError(f"Repeatability inputs are missing: {missing}")
    file_hashes = {str(path.resolve()): _sha256_file(path) for path in files}
    encoded = json.dumps(file_hashes, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return _sha256_bytes(encoded), file_hashes


def execute_once(
    dataset: Path,
    ids: list[int],
    graph_stage: str,
    ontology_index,
    manifest: dict[int, dict],
) -> list[dict]:
    results = []
    for example_id in ids:
        if example_id not in manifest:
            raise ValueError(f"ID {example_id} is absent from the dataset manifest")
        results.append(
            generic.score_example(
                dataset / str(example_id),
                manifest[example_id],
                ontology_index,
                graph_stage,
            )
        )
    return results


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dataset", type=Path, required=True)
    parser.add_argument("--ids", type=parse_ids, required=True)
    parser.add_argument("--ontology", type=Path, default=Path("ontology/ontology.ttl"))
    parser.add_argument("--graph-stage", choices=("extracted", "reasoned"), required=True)
    parser.add_argument("--runs", type=int, default=3)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args(argv)
    if args.runs < 2:
        parser.error("--runs must be at least 2")

    dataset = args.dataset.resolve()
    ontology = args.ontology.resolve()
    ontology_index = generic.load_ontology_word_index(ontology)
    manifest = {int(row["example_id"]): row for row in generic.read_manifest_rows(dataset)}
    inputs_digest, file_hashes = input_fingerprint(
        dataset, ontology, args.ids, args.graph_stage
    )

    runs = []
    reference = None
    mismatches = []
    for run_number in range(1, args.runs + 1):
        results = execute_once(
            dataset, args.ids, args.graph_stage, ontology_index, manifest
        )
        canonical = sorted(
            (canonical_result(row) for row in results), key=lambda row: row["id"]
        )
        fingerprint = result_fingerprint(results)
        if reference is None:
            reference = canonical
        else:
            if len(reference) != len(canonical):
                mismatches.append({
                    "run": run_number,
                    "id": None,
                    "expected_result_count": len(reference),
                    "observed_result_count": len(canonical),
                })
            for expected, observed in zip(reference, canonical):
                if expected != observed:
                    mismatches.append({
                        "run": run_number,
                        "id": expected["id"],
                        "expected": expected,
                        "observed": observed,
                    })
        runs.append({"run": run_number, "result_fingerprint": fingerprint})

    repeatable = not mismatches and len({run["result_fingerprint"] for run in runs}) == 1
    payload = {
        "experiment": "symbolic_qa_repeatability_verification",
        "claim_scope": (
            "Repeatability applies to QA over fixed graph, ontology, manifest, and "
            "question inputs; it does not apply to upstream LLM graph construction."
        ),
        "graph_stage": args.graph_stage,
        "examples": len(args.ids),
        "runs": args.runs,
        "input_fingerprint": inputs_digest,
        "input_file_hashes": file_hashes,
        "run_results": runs,
        "repeatable": repeatable,
        "mismatch_count": len(mismatches),
        "mismatches": mismatches,
    }
    atomic_json(args.output, payload)
    print(json.dumps({key: value for key, value in payload.items() if key not in {"input_file_hashes", "mismatches"}}, indent=2))
    return 0 if repeatable else 1


if __name__ == "__main__":
    raise SystemExit(main())
