import json
from pathlib import Path

from phase2_qa import common
from phase2_qa import compare_qa
from phase2_qa.run_symbolic_sparql_qa import validate_select_query
from phase2_qa.verify_symbolic_repeatability import canonical_result, result_fingerprint
from run_sparql_generic import extract_anchor_entities


def test_answer_normalization_handles_articles_accents_and_punctuation():
    assert common.normalize_answer("The Małgorzata Braunek!") == "małgorzata braunek"


def test_token_f1_gives_partial_credit_without_substring_matching():
    assert common.token_f1("Jane Director", "Jane Smith Director") == 0.8


def test_answer_scoring_accepts_boolean_and_date_precision_equivalence():
    assert common.score_answer("false", "no")["exact_match"] is True
    assert common.score_answer("false", "no")["strict_exact_match"] is False
    assert common.score_answer("1983-03-07", "1983")["exact_match"] is True
    assert common.score_answer("1983-03-07", "1983")["strict_exact_match"] is False
    assert common.score_answer("1983-03-07", "1983")["token_f1"] == 1.0


def test_strict_exact_match_uses_only_normalized_equality():
    assert common.score_answer("The France!", "France")["strict_exact_match"] is True
    assert common.score_answer("Germany", "German")["strict_exact_match"] is False
    assert common.score_answer("acute leukemia", "leukemia")["strict_exact_match"] is False


def test_anchor_fallback_handles_qualified_name_variation_conservatively():
    titles = ["Eleanor of Vermandois", "Eleanor of Aquitaine", "John"]
    assert extract_anchor_entities(
        "Who is the aunt of Eleanor, Countess of Vermandois?", titles
    ) == ["Eleanor of Vermandois"]
    assert extract_anchor_entities("Who is Johnny's aunt?", titles) == []


def test_compare_refuses_oracle_as_primary_system(tmp_path: Path):
    baseline = tmp_path / "baseline.json"
    system = tmp_path / "system.json"
    output = tmp_path / "comparison.json"
    baseline.write_text(json.dumps({"results": []}), encoding="utf-8")
    system.write_text(
        json.dumps({"valid_for_direct_baseline_comparison": False, "results": []}),
        encoding="utf-8",
    )
    try:
        compare_qa.main([
            "--baseline", str(baseline), "--system", str(system), "--output", str(output)
        ])
    except SystemExit as exc:
        assert "oracle-assisted" in str(exc)
    else:
        raise AssertionError("Oracle comparison should have been rejected")


def test_symbolic_query_must_be_read_only_select_with_answer_binding():
    query = validate_select_query(
        "PREFIX ex: <http://example.org/>\nSELECT ?answer WHERE { ?s ex:p ?answer }"
    )
    assert query.startswith("PREFIX")
    assert validate_select_query("ASK { ?s ?p ?o }").startswith("ASK")

    for invalid in (
        "CONSTRUCT { ?s ?p ?o } WHERE { ?s ?p ?o }",
        "SELECT ?value WHERE { ?s ?p ?value }",
        "SELECT ?answer WHERE { SERVICE <https://example.org> { ?s ?p ?answer } }",
    ):
        try:
            validate_select_query(invalid)
        except ValueError:
            pass
        else:
            raise AssertionError(f"Unsafe or invalid query was accepted: {invalid}")


def test_aggregate_counts_empty_symbolic_answers_as_unanswered():
    summary = common.aggregate([
        {"status": "completed", "predicted_answer": "Alice", "strict_exact_match": True, "exact_match": True, "token_f1": 1.0},
        {"status": "completed", "predicted_answer": "", "strict_exact_match": False, "exact_match": False, "token_f1": 0.0},
    ])
    assert summary["answered"] == 1
    assert summary["unanswered"] == 1
    assert summary["answer_rate"] == 0.5


def test_repeatability_fingerprint_is_order_independent():
    first = [
        {"example_id": "2", "predicted_answer": "Bob", "note": "hasParent"},
        {"example_id": "1", "predicted_answer": "Alice", "note": "hasSpouse"},
    ]
    assert result_fingerprint(first) == result_fingerprint(list(reversed(first)))


def test_repeatability_fingerprint_detects_answer_or_trace_changes():
    original = [{"example_id": "1", "predicted_answer": "Alice", "note": "hasSpouse"}]
    changed_answer = [{"example_id": "1", "predicted_answer": "Bob", "note": "hasSpouse"}]
    changed_trace = [{"example_id": "1", "predicted_answer": "Alice", "note": "hasParent"}]
    assert result_fingerprint(original) != result_fingerprint(changed_answer)
    assert result_fingerprint(original) != result_fingerprint(changed_trace)
    assert canonical_result(original[0]) == {
        "id": 1,
        "predicted_answer": "Alice",
        "retrieval_trace": "hasSpouse",
    }
