#!/usr/bin/env python3
"""Freeze an oversized extracted candidate pool into an auditable final cohort.

Selection never reads triple-matching metrics. Candidate order comes exclusively
from build_dataset.py's manifest. Empty or RDF-unrepresentable extractions may be
replaced from the reserve pool; validation/model mistakes remain in the cohort.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import shutil
import tempfile
from collections import Counter
from pathlib import Path


ALLOWED_PIPELINE_STATUSES = {"completed", "review", "skipped", "unscoreable_extraction"}
BLOCKING_PIPELINE_STATUSES = {"failed"}


def read_candidate_manifest(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    required = {"example_id", "original_id", "type", "relations", "candidate_role"}
    if not rows or not required.issubset(rows[0]):
        raise ValueError(f"Candidate manifest lacks required columns: {sorted(required)}")
    ids = [int(row["example_id"]) for row in rows]
    if len(ids) != len(set(ids)):
        raise ValueError("Candidate manifest contains duplicate example IDs")
    return rows


def read_pipeline_manifest(path: Path) -> dict[int, dict]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, list):
        raise ValueError("Pipeline manifest must be a JSON list")
    indexed = {}
    for row in payload:
        if not isinstance(row, dict) or not isinstance(row.get("id"), int):
            raise ValueError("Every pipeline-manifest entry must contain an integer id")
        if row["id"] in indexed:
            raise ValueError(f"Duplicate pipeline result for ID {row['id']}")
        indexed[row["id"]] = row
    return indexed


def quality_for(candidate_id: int, pipeline_row: dict, pipeline_root: Path) -> dict | None:
    embedded = pipeline_row.get("extraction_quality")
    if isinstance(embedded, dict):
        return embedded
    matches = list(
        (pipeline_root / str(candidate_id)).rglob(f"extraction_quality_{candidate_id}.json")
    )
    if len(matches) > 1:
        raise ValueError(f"Multiple extraction-quality artifacts for ID {candidate_id}")
    return json.loads(matches[0].read_text(encoding="utf-8")) if matches else None


def classify_candidate(candidate_id: int, pipeline_row: dict, pipeline_root: Path) -> dict:
    status = str(pipeline_row.get("status", ""))
    if status in BLOCKING_PIPELINE_STATUSES:
        return {
            "candidate_id": candidate_id,
            "decision": "blocked",
            "reason": "pipeline_execution_failed",
            "detail": pipeline_row.get("error"),
        }
    if status not in ALLOWED_PIPELINE_STATUSES:
        return {
            "candidate_id": candidate_id,
            "decision": "blocked",
            "reason": "missing_or_unknown_pipeline_status",
            "detail": status or None,
        }
    quality = quality_for(candidate_id, pipeline_row, pipeline_root)
    if quality is None:
        return {
            "candidate_id": candidate_id,
            "decision": "blocked",
            "reason": "missing_extraction_quality_assessment",
        }
    metrics = quality.get("metrics") if isinstance(quality.get("metrics"), dict) else {}
    raw_facts = int(metrics.get("raw_semantic_facts") or 0)
    mapped_facts = metrics.get("mapped_semantic_facts")
    eligible = bool(quality.get("eligible_for_graph_evaluation"))
    if status == "unscoreable_extraction" or raw_facts == 0:
        return {
            "candidate_id": candidate_id,
            "decision": "exclude",
            "reason": "empty_extracted_graph",
            "quality": quality,
        }
    if mapped_facts is not None and int(mapped_facts) == 0:
        return {
            "candidate_id": candidate_id,
            "decision": "exclude",
            "reason": "no_rdf_representable_semantic_fact",
            "quality": quality,
        }
    if not eligible:
        return {
            "candidate_id": candidate_id,
            "decision": "blocked",
            "reason": "unrecognized_unscoreable_condition",
            "quality": quality,
        }
    return {
        "candidate_id": candidate_id,
        "decision": "eligible",
        "reason": "nonempty_scoreable_extraction",
        "pipeline_status": status,
        "quality_warning_codes": [
            item.get("code")
            for item in quality.get("issues", [])
            if isinstance(item, dict) and item.get("severity") == "warning"
        ],
    }


def select_cohort(
    candidate_rows: list[dict[str, str]],
    pipeline_rows: dict[int, dict],
    pipeline_root: Path,
    target: int,
) -> tuple[list[tuple[dict[str, str], dict]], list[dict]]:
    decisions = []
    eligible = []
    for row in candidate_rows:
        candidate_id = int(row["example_id"])
        pipeline_row = pipeline_rows.get(candidate_id)
        if pipeline_row is None:
            decision = {
                "candidate_id": candidate_id,
                "decision": "blocked",
                "reason": "candidate_not_processed",
            }
        else:
            decision = classify_candidate(candidate_id, pipeline_row, pipeline_root)
        decisions.append(decision)
        if decision["decision"] == "eligible":
            eligible.append((row, decision))

    blocked = [item for item in decisions if item["decision"] == "blocked"]
    if blocked:
        examples = ", ".join(f"{item['candidate_id']}:{item['reason']}" for item in blocked[:10])
        raise RuntimeError(
            f"Finalization blocked by {len(blocked)} unresolved pipeline result(s): {examples}. "
            "Retry or repair them; they cannot be silently replaced."
        )
    if len(eligible) < target:
        raise RuntimeError(
            f"Only {len(eligible)} eligible non-empty candidates remain for target {target}; "
            "extract additional reserve candidates."
        )
    selected = eligible[:target]
    selected_ids = {int(row["example_id"]) for row, _ in selected}
    for decision in decisions:
        if decision["decision"] == "eligible":
            decision["decision"] = "selected" if decision["candidate_id"] in selected_ids else "unused_reserve"
    return selected, decisions


def renamed_basename(name: str, old_id: int, new_id: int) -> str:
    name = name.replace(f"example{old_id}", f"example{new_id}")
    return re.sub(rf"(?<=_){old_id}(?=(?:\.|_))", str(new_id), name)


def rename_example_artifacts(directory: Path, old_id: int, new_id: int) -> None:
    paths = sorted(directory.rglob("*"), key=lambda path: len(path.parts), reverse=True)
    for path in paths:
        renamed = renamed_basename(path.name, old_id, new_id)
        if renamed != path.name:
            destination = path.with_name(renamed)
            if destination.exists():
                raise FileExistsError(f"Renaming collision: {destination}")
            path.rename(destination)


def copy_selected_example(
    source_root: Path,
    pipeline_root: Path,
    destination: Path,
    old_id: int,
    new_id: int,
) -> None:
    source = source_root / str(old_id)
    pipeline = pipeline_root / str(old_id)
    if not source.is_dir():
        raise FileNotFoundError(f"Missing candidate source directory: {source}")
    shutil.copytree(source, destination)
    if pipeline.resolve() != source.resolve():
        if not pipeline.is_dir():
            raise FileNotFoundError(f"Missing pipeline output directory: {pipeline}")
        shutil.copytree(pipeline, destination, dirs_exist_ok=True)
    # The final cohort freezes the pre-SHACL extraction baseline. Experimental
    # repair/inference outputs from candidate trials must not leak into it.
    for path in destination.rglob("repair_*.json"):
        path.unlink()
    for path in destination.rglob("extracted_initial_*.ttl"):
        path.unlink()
    shutil.rmtree(destination / "inference", ignore_errors=True)
    rename_example_artifacts(destination, old_id, new_id)


def file_checksum(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def tree_checksum(root: Path) -> str:
    digest = hashlib.sha256()
    for path in sorted(
        item for item in root.rglob("*")
        if item.is_file() and item.name != "finalization_report.json"
    ):
        digest.update(str(path.relative_to(root)).encode("utf-8"))
        digest.update(b"\0")
        digest.update(path.read_bytes())
        digest.update(b"\0")
    return digest.hexdigest()


def write_final_manifest(path: Path, selected: list[tuple[dict[str, str], dict]]) -> None:
    source_fields = list(selected[0][0])
    fields = ["example_id", "candidate_example_id", *[f for f in source_fields if f != "example_id"]]
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for final_id, (row, _) in enumerate(selected, start=1):
            writer.writerow({
                "example_id": final_id,
                "candidate_example_id": row["example_id"],
                **{key: value for key, value in row.items() if key != "example_id"},
            })


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--candidate-dir", type=Path, required=True)
    parser.add_argument("--pipeline-dir", type=Path, required=True)
    parser.add_argument("--pipeline-manifest", type=Path, default=None)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--target", type=int, default=1000)
    parser.add_argument("--dry-run", action="store_true")
    return parser


def main(argv=None) -> int:
    args = build_parser().parse_args(argv)
    if args.target <= 0:
        raise SystemExit("--target must be positive")
    candidate_root = args.candidate_dir.resolve()
    pipeline_root = args.pipeline_dir.resolve()
    pipeline_manifest = (
        args.pipeline_manifest.resolve()
        if args.pipeline_manifest
        else pipeline_root / "manifest.json"
    )
    candidate_rows = read_candidate_manifest(candidate_root / "manifest.csv")
    pipeline_rows = read_pipeline_manifest(pipeline_manifest)
    selected, decisions = select_cohort(
        candidate_rows, pipeline_rows, pipeline_root, args.target
    )
    counts = Counter(item["decision"] for item in decisions)
    print(" ".join(f"{key}={value}" for key, value in sorted(counts.items())))
    if args.dry_run:
        return 0

    output = args.output_dir.resolve()
    if output.exists():
        raise FileExistsError(f"Refusing to overwrite existing output directory: {output}")
    output.parent.mkdir(parents=True, exist_ok=True)
    temporary = Path(tempfile.mkdtemp(prefix=f".{output.name}.", dir=output.parent))
    try:
        for final_id, (row, _) in enumerate(selected, start=1):
            copy_selected_example(
                candidate_root,
                pipeline_root,
                temporary / str(final_id),
                int(row["example_id"]),
                final_id,
            )
        write_final_manifest(temporary / "manifest.csv", selected)
        report = {
            "selection_policy": (
                "Manifest-order promotion; no triple scores are read. Empty or RDF-"
                "unrepresentable extractions are excluded; warning/review model errors remain."
            ),
            "target": args.target,
            "candidate_examples": len(candidate_rows),
            "decision_counts": dict(sorted(counts.items())),
            "selected_mapping": [
                {
                    "final_id": final_id,
                    "candidate_id": int(row["example_id"]),
                    "original_id": row["original_id"],
                    "baseline_graph": f"{final_id}/originals/extracted_{final_id}.ttl",
                    "baseline_graph_sha256": file_checksum(
                        temporary / str(final_id) / "originals" / f"extracted_{final_id}.ttl"
                    ),
                }
                for final_id, (row, _) in enumerate(selected, start=1)
            ],
            "decisions": decisions,
        }
        (temporary / "finalization_report.json").write_text(
            json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
        )
        report["dataset_sha256"] = tree_checksum(temporary)
        (temporary / "finalization_report.json").write_text(
            json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
        )
        temporary.rename(output)
    except Exception:
        shutil.rmtree(temporary, ignore_errors=True)
        raise
    print(f"Finalized {args.target} examples at {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
