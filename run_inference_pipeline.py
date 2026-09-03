#!/usr/bin/env python3
"""Run HermiT on construction graphs before evaluation-time entity alignment."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
import tempfile
from pathlib import Path

from evaluation_scope import graph_evaluation_exclusion


ROOT = Path(__file__).resolve().parent


def parse_ids(value: str) -> list[int]:
    result = set()
    for part in value.split(","):
        part = part.strip()
        if "-" in part:
            start, end = map(int, part.split("-", 1))
            if start < 0 or end < start:
                raise argparse.ArgumentTypeError(f"Invalid range: {part}")
            result.update(range(start, end + 1))
        elif part:
            result.add(int(part))
    if not result or min(result) < 0:
        raise argparse.ArgumentTypeError("IDs must be non-negative")
    return sorted(result)


def atomic_write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = None
    try:
        with tempfile.NamedTemporaryFile("w", encoding="utf-8", dir=path.parent, delete=False) as handle:
            handle.write(content)
            temporary = Path(handle.name)
        temporary.replace(path)
    finally:
        if temporary and temporary.exists():
            temporary.unlink()


def run_one(source: Path, output_dir: Path, index: int, side: str, ontology: Path) -> dict:
    artifacts = output_dir / "artifacts"
    artifacts.mkdir(parents=True, exist_ok=True)
    materialized = output_dir / f"{side}_reasoned_{index}.ttl"
    inferred = artifacts / f"{side}_inferred_only_{index}.ttl"
    log = artifacts / f"{side}_reasoner_{index}.log"
    command = [
        sys.executable,
        str(ROOT / "reasoner-inference" / "reasoner_kg_hermit.py"),
        str(source),
        "--tbox", str(ontology),
        "--summary-only",
        "--output-ttl", str(materialized),
        "--inferred-output-ttl", str(inferred),
    ]
    completed = subprocess.run(command, text=True, capture_output=True, check=False)
    atomic_write(log, completed.stdout + completed.stderr)
    return {
        "side": side,
        "source": str(source),
        "status": "completed" if completed.returncode == 0 else "failed",
        "return_code": completed.returncode,
        "materialized_graph": str(materialized) if completed.returncode == 0 else None,
        "inferred_only_graph": str(inferred) if completed.returncode == 0 else None,
        "log": str(log),
    }


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input-dir", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--ids", type=parse_ids, required=True)
    parser.add_argument("--ontology", type=Path, default=ROOT / "ontology" / "ontology.ttl")
    parser.add_argument("--summary-output", type=Path, default=None)
    parser.add_argument(
        "--include-excluded",
        action="store_true",
        help="Process examples marked as excluded from graph evaluation.",
    )
    args = parser.parse_args(argv)
    results = []
    for index in args.ids:
        example = args.input_dir.resolve() / str(index)
        exclusion = graph_evaluation_exclusion(example)
        if exclusion and not args.include_excluded:
            results.append({"id": index, "status": "excluded", "reason": exclusion["reason"]})
            print(f"id={index} status=excluded", flush=True)
            continue
        output = args.output_dir.resolve() / str(index) / "inference"
        shacl_graph = example / "after_shacl" / f"extracted_shacl_{index}.ttl"
        resolved_graph = example / "entity_resolved" / f"extracted_resolved_{index}.ttl"
        original_graph = example / "originals" / f"extracted_{index}.ttl"
        sources = {
            "extracted": shacl_graph if shacl_graph.is_file() else (
                resolved_graph if resolved_graph.is_file() else original_graph
            ),
            "ground_truth": example / f"ground_truth_{index}.ttl",
        }
        missing = [str(path) for path in sources.values() if not path.is_file()]
        if missing:
            row = {"id": index, "status": "failed", "error": f"Missing inputs: {missing}"}
        else:
            runs = [run_one(path, output, index, side, args.ontology.resolve()) for side, path in sources.items()]
            row = {
                "id": index,
                "status": "completed" if all(run["status"] == "completed" for run in runs) else "failed",
                "extracted_stage": (
                    "after_shacl" if shacl_graph.is_file() else
                    ("entity_resolved" if resolved_graph.is_file() else "original_unchanged")
                ),
                "runs": runs,
            }
        results.append(row)
        atomic_write(output / "artifacts" / f"inference_report_{index}.json", json.dumps(row, ensure_ascii=False, indent=2) + "\n")
        print(f"id={index} status={row['status']}", flush=True)
    summary = {
        "examples": len(results),
        "completed": sum(row["status"] == "completed" for row in results),
        "failed": sum(row["status"] == "failed" for row in results),
        "excluded": sum(row["status"] == "excluded" for row in results),
        "results": results,
    }
    summary_output = args.summary_output.resolve() if args.summary_output else args.output_dir.resolve() / "inference_summary.json"
    atomic_write(summary_output, json.dumps(summary, ensure_ascii=False, indent=2) + "\n")
    print(f"completed={summary['completed']} failed={summary['failed']}")
    return 1 if summary["failed"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
