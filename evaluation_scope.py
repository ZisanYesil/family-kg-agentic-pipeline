"""Shared graph-evaluation scope controls."""

from __future__ import annotations

import json
from pathlib import Path


EXCLUSION_FILE = "graph_evaluation_exclusion.json"


def graph_evaluation_exclusion(example_directory: Path) -> dict | None:
    marker = example_directory / EXCLUSION_FILE
    if not marker.is_file():
        return None
    payload = json.loads(marker.read_text(encoding="utf-8"))
    if not isinstance(payload, dict) or not isinstance(payload.get("reason"), str):
        raise ValueError(f"Invalid graph evaluation exclusion: {marker}")
    return payload


def is_graph_evaluation_excluded(example_directory: Path) -> bool:
    return graph_evaluation_exclusion(example_directory) is not None


def example_directory_for(path: Path) -> Path | None:
    for candidate in (path, *path.parents):
        if candidate.name.isdigit():
            return candidate
    return None


def path_is_graph_evaluation_excluded(path: Path) -> bool:
    example = example_directory_for(path)
    return bool(example and is_graph_evaluation_excluded(example))
