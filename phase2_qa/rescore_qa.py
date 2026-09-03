#!/usr/bin/env python3
"""Recompute QA metrics from saved predictions without rerunning a system."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from phase2_qa.common import aggregate, atomic_json, score_answer


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args(argv)
    payload = json.loads(args.input.read_text(encoding="utf-8"))
    for row in payload.get("results", []):
        if row.get("status") == "completed":
            row.update(score_answer(row.get("predicted_answer"), row.get("gold_answer")))
    payload["summary"] = aggregate(payload.get("results", []))
    atomic_json(args.output or args.input, payload)
    print(json.dumps(payload["summary"], indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
