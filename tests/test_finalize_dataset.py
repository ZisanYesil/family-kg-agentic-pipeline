from pathlib import Path

import pytest

import finalize_dataset


def quality(raw=1, mapped=1, eligible=True, warnings=None):
    return {
        "eligible_for_graph_evaluation": eligible,
        "metrics": {
            "raw_semantic_facts": raw,
            "mapped_semantic_facts": mapped,
        },
        "issues": warnings or [],
    }


def candidate(candidate_id):
    return {
        "example_id": str(candidate_id),
        "original_id": f"original-{candidate_id}",
        "type": "compositional",
        "relations": "father",
        "candidate_role": "primary" if candidate_id <= 2 else "reserve",
    }


def test_selection_replaces_only_unscoreable_candidate_in_manifest_order(tmp_path: Path):
    rows = [candidate(1), candidate(2), candidate(3)]
    pipeline = {
        1: {"id": 1, "status": "completed", "extraction_quality": quality()},
        2: {
            "id": 2,
            "status": "unscoreable_extraction",
            "extraction_quality": quality(raw=0, mapped=None, eligible=False),
        },
        3: {
            "id": 3,
            "status": "review",
            "extraction_quality": quality(
                warnings=[{
                    "code": "entities_not_source_grounded",
                    "severity": "warning",
                }]
            ),
            # A deliberately poor score must have no bearing on promotion.
            "f1": 0.0,
        },
    }
    selected, decisions = finalize_dataset.select_cohort(rows, pipeline, tmp_path, 2)
    assert [int(row["example_id"]) for row, _ in selected] == [1, 3]
    assert {item["candidate_id"]: item["decision"] for item in decisions} == {
        1: "selected",
        2: "exclude",
        3: "selected",
    }


def test_pipeline_failure_blocks_instead_of_silently_using_reserve(tmp_path: Path):
    rows = [candidate(1), candidate(2)]
    pipeline = {
        1: {"id": 1, "status": "failed", "error": "temporary API outage"},
        2: {"id": 2, "status": "completed", "extraction_quality": quality()},
    }
    with pytest.raises(RuntimeError, match="cannot be silently replaced"):
        finalize_dataset.select_cohort(rows, pipeline, tmp_path, 1)


def test_artifact_names_are_renumbered_only_at_id_tokens():
    assert finalize_dataset.renamed_basename("example27_question.txt", 27, 4) == "example4_question.txt"
    assert finalize_dataset.renamed_basename("extraction_quality_27.json", 27, 4) == "extraction_quality_4.json"
    assert finalize_dataset.renamed_basename("year_1927_notes.txt", 27, 4) == "year_1927_notes.txt"
