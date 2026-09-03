#!/usr/bin/env python3
"""Apply SHACL-guided feedback to frozen extraction graphs without re-extraction."""

from __future__ import annotations

import argparse
import json
import os
import tempfile
from dataclasses import asdict
from pathlib import Path

from dotenv import load_dotenv
from rdflib import Graph

from agents.kg_builder_agent import kg_builder_agent_with_diagnostics
from ontology.schema_loader import load_ontology_schema
from run_agent_pipeline import repair_graph_with_feedback
from utils.rdf import serialize_turtle_graph


ROOT = Path(__file__).resolve().parent


def parse_ids(value: str) -> list[int]:
    result: set[int] = set()
    for part in value.split(","):
        part = part.strip()
        if "-" in part:
            start, end = map(int, part.split("-", 1))
            if start < 1 or end < start:
                raise argparse.ArgumentTypeError(f"Invalid range: {part}")
            result.update(range(start, end + 1))
        elif part:
            result.add(int(part))
    if not result or min(result) < 1:
        raise argparse.ArgumentTypeError("IDs must be positive")
    return sorted(result)


def atomic_write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary_name = None
    try:
        with tempfile.NamedTemporaryFile(
            "w", encoding="utf-8", dir=path.parent, prefix=f".{path.name}.", delete=False
        ) as handle:
            handle.write(content)
            handle.flush()
            os.fsync(handle.fileno())
            temporary_name = handle.name
        os.replace(temporary_name, path)
    finally:
        if temporary_name and os.path.exists(temporary_name):
            os.unlink(temporary_name)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input-dir", required=True, type=Path)
    parser.add_argument("--ids", required=True, type=parse_ids)
    parser.add_argument("--ontology", type=Path, default=ROOT / "ontology" / "ontology.ttl")
    parser.add_argument("--max-repair-iterations", type=int, default=3)
    parser.add_argument("--summary-output", type=Path)
    args = parser.parse_args(argv)
    if args.max_repair_iterations < 1:
        parser.error("--max-repair-iterations must be positive")

    load_dotenv(ROOT / ".env")
    dataset = args.input_dir.resolve()
    schema = load_ontology_schema(str(args.ontology.resolve()))
    results = []
    for index in args.ids:
        example = dataset / str(index)
        resolved = example / "entity_resolved" / f"extracted_resolved_{index}.ttl"
        resolved_mapping = example / "entity_resolved" / "artifacts" / f"mapping_resolved_{index}.json"
        original = resolved if resolved.is_file() else example / "originals" / f"extracted_{index}.ttl"
        mapping_path = resolved_mapping if resolved_mapping.is_file() else example / "originals" / "artifacts" / f"mapping_{index}.json"
        if not original.is_file() or not mapping_path.is_file():
            row = {"id": index, "status": "failed", "error": "missing original or mapping artifact"}
            results.append(row)
            print(f"id={index} status=failed", flush=True)
            continue

        mapping = json.loads(mapping_path.read_text(encoding="utf-8"))
        built = kg_builder_agent_with_diagnostics(mapping, schema)
        graph = Graph().parse(original, format="turtle")
        source_text = (example / f"text_{index}.txt").read_text(encoding="utf-8")
        final_graph, validation, audit = repair_graph_with_feedback(
            graph,
            schema,
            mapping,
            built,
            source_text,
            max_iterations=args.max_repair_iterations,
        )
        initially_conforming = audit["initial_validation"]["conforms"]
        if initially_conforming:
            row = {
                "id": index,
                "status": "not_needed",
                "initially_conforming": True,
                "final_conforms": True,
                "inference_source": str(original),
                "entity_resolution_source": resolved.is_file(),
            }
        else:
            output = example / "after_shacl"
            graph_path = output / f"extracted_shacl_{index}.ttl"
            audit_path = output / "artifacts" / f"repair_{index}.json"
            audit["dangling_references"] = [asdict(item) for item in built.dangling_references]
            atomic_write(graph_path, serialize_turtle_graph(final_graph))
            atomic_write(audit_path, json.dumps(audit, ensure_ascii=False, indent=2) + "\n")
            row = {
                "id": index,
                "status": audit["status"],
                "initially_conforming": False,
                "final_conforms": validation.conforms,
                "iterations": len(audit["iterations"]),
                "inference_source": str(graph_path),
                "audit": str(audit_path),
                "entity_resolution_source": resolved.is_file(),
            }
        results.append(row)
        print(f"id={index} status={row['status']}", flush=True)

    summary = {
        "examples": len(results),
        "not_needed": sum(row["status"] == "not_needed" for row in results),
        "repaired": sum(row["status"] == "repaired" for row in results),
        "unresolved": sum(row["status"] in {"unresolved", "plateau", "max_iterations", "feedback_error"} for row in results),
        "failed": sum(row["status"] == "failed" for row in results),
        "results": results,
    }
    summary_path = args.summary_output or dataset / "shacl_summary.json"
    atomic_write(summary_path.resolve(), json.dumps(summary, ensure_ascii=False, indent=2) + "\n")
    print(
        f"not_needed={summary['not_needed']} repaired={summary['repaired']} "
        f"unresolved={summary['unresolved']} failed={summary['failed']}"
    )
    return 1 if summary["failed"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
