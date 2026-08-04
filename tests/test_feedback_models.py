from __future__ import annotations

import json

import pytest
from pydantic import ValidationError

from feedback.models import (
    AddTriple,
    FeedbackPlan,
    IriObject,
    LiteralObject,
    RemoveTriple,
    ReplaceLiteral,
    ViolationRepair,
    build_feedback_response_format,
)


FINGERPRINT_A = "a" * 64
FINGERPRINT_B = "b" * 64
XSD_INTEGER = "http://www.w3.org/2001/XMLSchema#integer"


def _iri(value: str) -> dict[str, object]:
    return {"kind": "iri", "value": value}


def _literal(
    value: str,
    *,
    datatype: str | None = None,
    language: str | None = None,
) -> dict[str, object]:
    return {
        "kind": "literal",
        "value": value,
        "datatype": datatype,
        "language": language,
    }


def test_feedback_plan_accepts_all_supported_edit_operations() -> None:
    plan = FeedbackPlan.model_validate(
        {
            "reasoning": "Apply only source-supported repairs.",
            "repairs": [
                {
                    "violation_fingerprint": FINGERPRINT_A,
                    "reasoning": "Repair the affected facts.",
                    "operations": [
                        {
                            "operation": "add_triple",
                            "subject": "urn:person:alex",
                            "predicate": "urn:family:hasFather",
                            "object": _iri("urn:person:john"),
                        },
                        {
                            "operation": "remove_triple",
                            "subject": "urn:person:alex",
                            "predicate": "urn:family:hasBirthYear",
                            "object": _literal(
                                "recent",
                                datatype=None,
                                language=None,
                            ),
                        },
                        {
                            "operation": "replace_literal",
                            "subject": "urn:person:alex",
                            "predicate": "urn:family:hasBirthYear",
                            "old_literal": _literal(
                                "recent",
                                datatype=None,
                                language=None,
                            ),
                            "new_literal": _literal(
                                "1950",
                                datatype=XSD_INTEGER,
                                language=None,
                            ),
                        },
                    ],
                }
            ],
        }
    )

    operations = plan.repairs[0].operations
    assert isinstance(operations[0], AddTriple)
    assert isinstance(operations[1], RemoveTriple)
    assert isinstance(operations[2], ReplaceLiteral)
    assert isinstance(operations[0].object, IriObject)
    assert isinstance(operations[1].object, LiteralObject)


def test_empty_operations_explicitly_represents_unrepairable_violation() -> None:
    plan = FeedbackPlan(
        reasoning="The source does not support a safe repair.",
        repairs=[
            ViolationRepair(
                violation_fingerprint=FINGERPRINT_A,
                reasoning="Do not invent the missing fact.",
                operations=[],
            )
        ],
    )

    assert plan.repairs[0].operations == []


@pytest.mark.parametrize(
    "iri",
    [
        "relative/path",
        "person",
        "urn:",
        "http://example.com/white space",
        "http://example.com/<unsafe>",
    ],
)
def test_subject_predicate_and_object_require_safe_absolute_iris(iri: str) -> None:
    with pytest.raises(ValidationError):
        AddTriple.model_validate(
            {
                "operation": "add_triple",
                "subject": iri,
                "predicate": "urn:predicate",
                "object": _iri("urn:object"),
            }
        )


def test_literal_rejects_datatype_and_language_together() -> None:
    with pytest.raises(
        ValidationError,
        match="both datatype and language",
    ):
        LiteralObject.model_validate(
            _literal(
                "hello",
                datatype="http://www.w3.org/2001/XMLSchema#string",
                language="en",
            )
        )


def test_literal_rejects_invalid_language_tag() -> None:
    with pytest.raises(ValidationError, match="BCP 47"):
        LiteralObject.model_validate(
            _literal("hello", language="not_a_language")
        )


def test_replace_literal_rejects_noop() -> None:
    literal = _literal("1950", datatype=XSD_INTEGER)

    with pytest.raises(ValidationError, match="must change"):
        ReplaceLiteral.model_validate(
            {
                "operation": "replace_literal",
                "subject": "urn:person:alex",
                "predicate": "urn:family:hasBirthYear",
                "old_literal": literal,
                "new_literal": literal,
            }
        )


def test_contract_rejects_full_turtle_rewrite_and_unknown_fields() -> None:
    with pytest.raises(ValidationError, match="Extra inputs are not permitted"):
        FeedbackPlan.model_validate(
            {
                "reasoning": "Unsafe rewrite attempt.",
                "repairs": [],
                "corrected_graph": "@prefix ex: <urn:ex:> .",
            }
        )


def test_contract_uses_strict_types_without_coercion() -> None:
    with pytest.raises(ValidationError):
        FeedbackPlan.model_validate({"reasoning": 123, "repairs": []})


def test_repair_rejects_duplicate_operations() -> None:
    operation = {
        "operation": "add_triple",
        "subject": "urn:person:alex",
        "predicate": "urn:family:hasFather",
        "object": _iri("urn:person:john"),
    }

    with pytest.raises(ValidationError, match="duplicate edit operations"):
        ViolationRepair.model_validate(
            {
                "violation_fingerprint": FINGERPRINT_A,
                "reasoning": "Duplicate operation.",
                "operations": [operation, operation],
            }
        )


def test_plan_rejects_duplicate_violation_fingerprints() -> None:
    repair = {
        "violation_fingerprint": FINGERPRINT_A,
        "reasoning": "First.",
        "operations": [],
    }

    with pytest.raises(ValidationError, match="duplicate violation fingerprints"):
        FeedbackPlan.model_validate(
            {
                "reasoning": "Duplicate repair.",
                "repairs": [repair, repair],
            }
        )


def test_plan_rejects_duplicate_operations_across_repairs() -> None:
    operation = {
        "operation": "add_triple",
        "subject": "urn:person:alex",
        "predicate": "urn:family:hasFather",
        "object": _iri("urn:person:john"),
    }

    with pytest.raises(
        ValidationError,
        match="duplicate edit operations across repairs",
    ):
        FeedbackPlan.model_validate(
            {
                "reasoning": "Ambiguous duplicate edits.",
                "repairs": [
                    {
                        "violation_fingerprint": FINGERPRINT_A,
                        "reasoning": "First.",
                        "operations": [operation],
                    },
                    {
                        "violation_fingerprint": FINGERPRINT_B,
                        "reasoning": "Second.",
                        "operations": [operation],
                    },
                ],
            }
        )


def test_plan_enforces_total_operation_limit(monkeypatch) -> None:
    monkeypatch.setattr("feedback.models.MAX_TOTAL_OPERATIONS", 1)

    with pytest.raises(ValidationError, match="exceeds 1 total operations"):
        FeedbackPlan.model_validate(
            {
                "reasoning": "Too many operations.",
                "repairs": [
                    {
                        "violation_fingerprint": FINGERPRINT_A,
                        "reasoning": "Two distinct edits.",
                        "operations": [
                            {
                                "operation": "add_triple",
                                "subject": "urn:person:alex",
                                "predicate": "urn:family:hasFather",
                                "object": _iri("urn:person:john"),
                            },
                            {
                                "operation": "add_triple",
                                "subject": "urn:person:alex",
                                "predicate": "urn:family:hasMother",
                                "object": _iri("urn:person:jane"),
                            },
                        ],
                    }
                ],
            }
        )


def test_feedback_json_schema_is_strict_and_has_no_graph_rewrite_field() -> None:
    response_format = build_feedback_response_format()
    schema = response_format["json_schema"]["schema"]
    serialized_schema = json.dumps(schema)

    assert response_format["type"] == "json_schema"
    assert response_format["json_schema"]["strict"] is True
    assert "corrected_graph" not in serialized_schema
    assert "turtle" not in serialized_schema.lower()
    assert schema.get("type") == "object"
    assert "anyOf" not in schema

    unsupported_keywords = {
        "oneOf",
        "allOf",
        "not",
        "dependentRequired",
        "dependentSchemas",
        "if",
        "then",
        "else",
        "discriminator",
        "const",
    }

    def assert_strict_objects(node: object) -> None:
        if isinstance(node, dict):
            assert unsupported_keywords.isdisjoint(node)
            if node.get("type") == "object":
                assert node.get("additionalProperties") is False
                properties = node.get("properties", {})
                assert set(node.get("required", [])) == set(properties)
            for value in node.values():
                assert_strict_objects(value)
        elif isinstance(node, list):
            for value in node:
                assert_strict_objects(value)

    assert_strict_objects(schema)
