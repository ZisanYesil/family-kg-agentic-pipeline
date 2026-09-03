#!/usr/bin/env python3
"""Compare paired QA result files on an identical example cohort."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from phase2_qa.common import atomic_json, score_answer


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--baseline", type=Path, required=True)
    parser.add_argument("--system", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--allow-oracle", action="store_true")
    args = parser.parse_args(argv)
    baseline = json.loads(args.baseline.read_text(encoding="utf-8"))
    system = json.loads(args.system.read_text(encoding="utf-8"))
    if not args.allow_oracle and system.get("valid_for_direct_baseline_comparison") is False:
        raise SystemExit("Refusing primary comparison against an oracle-assisted symbolic result")
    left = {row["id"]: row for row in baseline["results"] if row.get("status") == "completed"}
    right = {row["id"]: row for row in system["results"] if row.get("status") == "completed"}
    if left.keys() != right.keys():
        raise SystemExit("Completed result cohorts differ; paired comparison would be invalid")
    rows = []
    for example_id in sorted(left):
        a, b = left[example_id], right[example_id]
        a_score = score_answer(a.get("predicted_answer"), a.get("gold_answer"))
        b_score = score_answer(b.get("predicted_answer"), b.get("gold_answer"))
        rows.append({
            "id": example_id,
            "baseline_strict_exact": bool(a_score["strict_exact_match"]),
            "system_strict_exact": bool(b_score["strict_exact_match"]),
            "baseline_exact": bool(a_score["exact_match"]),
            "system_exact": bool(b_score["exact_match"]),
            "baseline_token_f1": float(a_score["token_f1"]),
            "system_token_f1": float(b_score["token_f1"]),
            "delta_token_f1": float(b_score["token_f1"]) - float(a_score["token_f1"]),
        })
    n = len(rows)
    payload = {
        "examples": n,
        "baseline_experiment": baseline.get("experiment"),
        "system_experiment": system.get("experiment"),
        "baseline_strict_exact_match": sum(row["baseline_strict_exact"] for row in rows) / n if n else 0,
        "system_strict_exact_match": sum(row["system_strict_exact"] for row in rows) / n if n else 0,
        "baseline_exact_match": sum(row["baseline_exact"] for row in rows) / n if n else 0,
        "system_exact_match": sum(row["system_exact"] for row in rows) / n if n else 0,
        "baseline_mean_token_f1": sum(row["baseline_token_f1"] for row in rows) / n if n else 0,
        "system_mean_token_f1": sum(row["system_token_f1"] for row in rows) / n if n else 0,
        "discordant_pairs": {
            "baseline_only_correct": sum(row["baseline_exact"] and not row["system_exact"] for row in rows),
            "system_only_correct": sum(row["system_exact"] and not row["baseline_exact"] for row in rows),
            "both_correct": sum(row["baseline_exact"] and row["system_exact"] for row in rows),
            "neither_correct": sum(not row["baseline_exact"] and not row["system_exact"] for row in rows),
        },
        "results": rows,
    }
    atomic_json(args.output, payload)
    print(json.dumps({key: value for key, value in payload.items() if key != "results"}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
