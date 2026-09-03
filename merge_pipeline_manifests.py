#!/usr/bin/env python3
"""Merge ordered batch manifests; later files replace earlier rows by example ID."""

from __future__ import annotations

import argparse
import json
import os
import tempfile
from pathlib import Path


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("manifests", nargs="+", type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--expected-count", type=int)
    args = parser.parse_args(argv)

    indexed: dict[int, dict] = {}
    provenance: dict[int, str] = {}
    for path in args.manifests:
        payload = json.loads(path.read_text(encoding="utf-8"))
        if not isinstance(payload, list):
            raise ValueError(f"Manifest must contain a JSON list: {path}")
        for row in payload:
            if not isinstance(row, dict) or not isinstance(row.get("id"), int):
                raise ValueError(f"Invalid row in {path}")
            indexed[row["id"]] = row
            provenance[row["id"]] = str(path)

    ids = sorted(indexed)
    if args.expected_count is not None:
        expected = set(range(1, args.expected_count + 1))
        missing = sorted(expected - set(ids))
        unexpected = sorted(set(ids) - expected)
        if missing or unexpected:
            raise RuntimeError(
                f"Manifest coverage mismatch: missing={missing[:20]}, "
                f"unexpected={unexpected[:20]}"
            )

    output = args.output.resolve()
    output.parent.mkdir(parents=True, exist_ok=True)
    temporary_name = None
    try:
        with tempfile.NamedTemporaryFile(
            mode="w",
            encoding="utf-8",
            dir=output.parent,
            prefix=f".{output.name}.",
            delete=False,
        ) as handle:
            json.dump([indexed[item] for item in ids], handle, ensure_ascii=False, indent=2)
            handle.write("\n")
            handle.flush()
            os.fsync(handle.fileno())
            temporary_name = handle.name
        os.replace(temporary_name, output)
    finally:
        if temporary_name and os.path.exists(temporary_name):
            os.unlink(temporary_name)

    print(
        f"merged={len(ids)} overrides={sum(1 for item in ids if provenance[item] != str(args.manifests[0]))} "
        f"output={output}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
