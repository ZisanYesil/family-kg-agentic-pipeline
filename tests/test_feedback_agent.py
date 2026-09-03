from __future__ import annotations

import json
from types import SimpleNamespace

import pytest
from rdflib import Graph

from agents.feedback_agent import (
    FeedbackAgentError,
    build_feedback_payload,
    build_feedback_system_prompt,
    feedback_agent,
)
from ontology.schema_loader import OntologyClass, OntologySchema
from validation.models import ValidationViolation, ViolationKind, ViolationSource


SCHEMA = OntologySchema(
    namespace="http://example.com/family#",
    classes=(OntologyClass(local_name="Person", uri="http://example.com/family#Person"),),
    datatype_properties=(),
    object_properties=(),
)
VIOLATION = ValidationViolation(
    kind=ViolationKind.SHACL,
    source=ViolationSource.SHACL_GENERATOR,
    message="Missing Person type",
    focus_node="http://example.com/family#jane",
    path="http://www.w3.org/1999/02/22-rdf-syntax-ns#type",
    expected="http://example.com/family#Person",
)


class _Completions:
    def __init__(self, content: str) -> None:
        self.content = content
        self.calls = []

    def create(self, **kwargs):
        self.calls.append(kwargs)
        return SimpleNamespace(
            choices=[SimpleNamespace(message=SimpleNamespace(content=self.content))]
        )


def _client(content: str):
    completions = _Completions(content)
    return SimpleNamespace(chat=SimpleNamespace(completions=completions)), completions


def test_feedback_agent_returns_strict_plan_and_sends_fingerprints() -> None:
    content = json.dumps(
        {
            "reasoning": "Add the source-grounded missing type.",
            "repairs": [
                {
                    "violation_fingerprint": VIOLATION.fingerprint,
                    "reasoning": "The graph node represents Jane.",
                    "operations": [
                        {
                            "operation": "add_triple",
                            "subject": "http://example.com/family#jane",
                            "predicate": "http://www.w3.org/1999/02/22-rdf-syntax-ns#type",
                            "object": {"kind": "iri", "value": "http://example.com/family#Person"},
                        }
                    ],
                }
            ],
        }
    )
    client, completions = _client(content)

    plan = feedback_agent(
        Graph(), (VIOLATION,), SCHEMA, "Jane is a person.", client=client
    )

    assert plan.repairs[0].violation_fingerprint == VIOLATION.fingerprint
    request_payload = json.loads(completions.calls[0]["messages"][1]["content"])
    assert request_payload["violations"][0]["fingerprint"] == VIOLATION.fingerprint
    assert completions.calls[0]["model"] == "gpt-oss:120b"
    assert completions.calls[0]["response_format"]["type"] == "json_schema"
    assert (
        completions.calls[0]["response_format"]["json_schema"]["name"]
        == "feedback_plan"
    )
    assert completions.calls[0]["max_completion_tokens"] == 8000
    assert "extra_body" not in completions.calls[0]


def test_feedback_agent_rejects_invalid_model_plan() -> None:
    client, _ = _client('{"reasoning":"incomplete"}')
    with pytest.raises(FeedbackAgentError, match="invalid feedback plan"):
        feedback_agent(Graph(), (VIOLATION,), SCHEMA, "Jane is a person.", client=client)


def test_feedback_payload_contains_graph_source_and_ontology() -> None:
    payload = json.loads(
        build_feedback_payload(Graph(), (VIOLATION,), SCHEMA, "Jane is a person.")
    )
    assert payload["source_text"] == "Jane is a person."
    assert payload["ontology"]["classes"][0]["iri"].endswith("Person")
    assert payload["graph_turtle"].strip() == ""


def test_feedback_prompt_distinguishes_iri_and_literal_repairs() -> None:
    prompt = build_feedback_system_prompt()
    assert "rdf:type always has an IRI object" in prompt
    assert "replace_literal is only for a datatype-property" in prompt
    assert "Both objects use kind=iri" in prompt
