from __future__ import annotations

import json
from types import SimpleNamespace

import httpx
import openai
import pytest

from agents.extraction_agent import (
    ExtractionAgentError,
    build_extraction_json_schema,
    build_extraction_response_format,
    build_extraction_system_prompt,
    extraction_agent,
)
from ontology.schema_loader import DatatypeProperty, ObjectProperty, OntologyClass, OntologySchema


def response_with_content(content: object) -> SimpleNamespace:
    return SimpleNamespace(
        choices=[
            SimpleNamespace(
                message=SimpleNamespace(content=content),
            )
        ]
    )


class FakeCompletions:
    def __init__(self, outcomes: list[object]) -> None:
        self.outcomes = outcomes
        self.call_count = 0
        self.calls: list[dict] = []

    def create(self, **kwargs: object) -> object:
        self.call_count += 1
        self.calls.append(kwargs)
        outcome = self.outcomes.pop(0)
        if isinstance(outcome, Exception):
            raise outcome
        return outcome


class FakeClient:
    def __init__(self, outcomes: list[object]) -> None:
        self.completions = FakeCompletions(outcomes)
        self.chat = SimpleNamespace(completions=self.completions)


def timeout_error() -> openai.APITimeoutError:
    return openai.APITimeoutError(request=httpx.Request("POST", "https://api.openai.com/v1/chat/completions"))


# A small mixed-domain ontology (people + vehicles) used across these tests to prove
# extraction is driven entirely by the schema passed in, not hardcoded to family data.
# Deliberately NOT the family ontology, so a regression to hardcoded person/sex/birth_year
# fields would fail these tests immediately.
def make_schema() -> OntologySchema:
    ns = "http://example.com/mixed-onto#"
    return OntologySchema(
        namespace=ns,
        classes=(
            OntologyClass(local_name="Car", uri=ns + "Car", comment="A motor vehicle."),
            OntologyClass(local_name="Person", uri=ns + "Person"),
        ),
        datatype_properties=(
            DatatypeProperty(
                local_name="birthYear", uri=ns + "birthYear", domain_class="Person", range_type="integer"
            ),
            DatatypeProperty(
                local_name="model", uri=ns + "model", domain_class="Car", range_type="string"
            ),
            DatatypeProperty(
                local_name="year", uri=ns + "year", domain_class="Car", range_type="integer"
            ),
        ),
        object_properties=(
            ObjectProperty(local_name="owns", uri=ns + "owns", domain_class="Person", range_class="Car"),
        ),
    )


def make_single_class_schema() -> OntologySchema:
    ns = "http://example.com/family-lite#"
    return OntologySchema(
        namespace=ns,
        classes=(OntologyClass(local_name="Person", uri=ns + "Person"),),
        datatype_properties=(
            DatatypeProperty(
                local_name="birthYear", uri=ns + "birthYear", domain_class="Person", range_type="integer"
            ),
        ),
        object_properties=(),
    )


def test_extraction_agent_extracts_entities_across_mixed_domains(monkeypatch: pytest.MonkeyPatch) -> None:
    """Text mentions both a car and a family relationship; the schema covers both domains,
    so both a Car entity and a Person entity should be extractable in the same call."""
    schema = make_schema()
    payload = {
        "entities": [
            {
                "id": "john_doe_1900",
                "label": "John Doe",
                "type": "Person",
                "aliases": ["Johnny"],
                "attributes": {"birthYear": 1900, "model": None, "year": None},
            },
            {
                "id": "johns_civic",
                "label": "Honda Civic",
                "type": "Car",
                "aliases": [],
                "attributes": {"birthYear": None, "model": "Civic", "year": 2015},
            },
        ],
        "relations": [
            {
                "subject": "john_doe_1900",
                "object": "johns_civic",
                "relation_phrase": "owner of",
                "qualifiers": {"year": None, "note": None},
            }
        ],
    }
    client = FakeClient([response_with_content(json.dumps(payload))])
    monkeypatch.setenv("DEEPSEEK_MODEL", "test-model")

    result = extraction_agent(
        "John Doe, also known as Johnny, born in 1900, owns a 2015 Honda Civic.",
        schema,
        client=client,
    )

    assert result == payload
    assert client.completions.call_count == 1
    call = client.completions.calls[0]
    assert call["model"] == "test-model"
    assert call["response_format"] == build_extraction_response_format(schema)
    assert call["max_tokens"] == 8192
    assert call["extra_body"] == {"thinking": {"type": "disabled"}}
    assert call["messages"][0]["role"] == "system"
    assert "Car" in call["messages"][0]["content"]
    assert "Person" in call["messages"][0]["content"]
    assert call["messages"][1]["content"] == (
        "John Doe, also known as Johnny, born in 1900, owns a 2015 Honda Civic."
    )


def test_response_format_reflects_schema_classes_and_attributes() -> None:
    schema = make_schema()
    response_format = build_extraction_response_format(schema)
    entity_schema = build_extraction_json_schema(schema)["properties"]["entities"]["items"]

    assert response_format == {"type": "json_object"}
    assert entity_schema["properties"]["type"]["enum"] == ["Car", "Person"]
    assert set(entity_schema["properties"]["attributes"]["required"]) == {
        "birthYear",
        "model",
        "year",
    }
    assert entity_schema["properties"]["attributes"]["properties"]["birthYear"]["type"] == [
        "integer",
        "null",
    ]
    assert entity_schema["properties"]["attributes"]["properties"]["model"]["type"] == [
        "string",
        "null",
    ]


def test_response_format_raises_for_schema_with_no_classes() -> None:
    schema = OntologySchema(namespace="http://example.com/empty#", classes=(), datatype_properties=(), object_properties=())

    with pytest.raises(ExtractionAgentError, match="no classes"):
        build_extraction_response_format(schema)


def test_system_prompt_lists_classes_and_scopes_attributes_per_class() -> None:
    schema = make_schema()
    prompt = build_extraction_system_prompt(schema)

    assert "- Car: A motor vehicle." in prompt
    assert "- Person" in prompt
    assert "model (string)" in prompt
    assert "birthYear (integer)" in prompt


@pytest.mark.parametrize("text", ["", "   "])
def test_extraction_agent_empty_input_raises_without_calling_client(text: str) -> None:
    schema = make_single_class_schema()
    client = FakeClient([response_with_content("{}")])

    with pytest.raises(ExtractionAgentError, match="Input text is empty"):
        extraction_agent(text, schema, client=client)

    assert client.completions.call_count == 0


def test_extraction_agent_malformed_json_raises_error_with_raw_content() -> None:
    schema = make_single_class_schema()
    client = FakeClient([response_with_content("not-json")])

    with pytest.raises(ExtractionAgentError, match="not-json"):
        extraction_agent("John Doe was born in 1900.", schema, client=client)

    assert client.completions.call_count == 1


def test_extraction_agent_non_string_model_content_raises_error() -> None:
    schema = make_single_class_schema()
    client = FakeClient([response_with_content(None)])

    with pytest.raises(ExtractionAgentError, match="Model returned non-string content"):
        extraction_agent("John Doe was born in 1900.", schema, client=client)

    assert client.completions.call_count == 1


@pytest.mark.parametrize(
    ("payload", "error"),
    [
        (
            {"entities": [], "relations": [], "marriages": []},
            "extraction result has unsupported field\\(s\\): marriages",
        ),
        (
            {"entities": []},
            "extraction result is missing required field\\(s\\): relations",
        ),
        (
            {"entities": "not-a-list", "relations": []},
            "extraction result.entities must be a list",
        ),
        (
            {
                "entities": [
                    {
                        "id": "alex",
                        "label": "Alex",
                        "type": "Vehicle",  # not in this schema's classes
                        "aliases": [],
                        "attributes": {"birthYear": None},
                    }
                ],
                "relations": [],
            },
            "entities\\[0\\].type must be one of",
        ),
        (
            {
                "entities": [
                    {
                        "id": "alex",
                        "label": "Alex",
                        "type": "Person",
                        "aliases": [],
                        "attributes": {"birthYear": "not-an-int"},
                    }
                ],
                "relations": [],
            },
            "entities\\[0\\].attributes.birthYear must be a integer or null",
        ),
        (
            {
                "entities": [
                    {
                        "id": "alex",
                        "label": "Alex",
                        "type": "Person",
                        "aliases": ["Al", 123],
                        "attributes": {"birthYear": None},
                    }
                ],
                "relations": [],
            },
            "entities\\[0\\].aliases must be a list of strings",
        ),
        (
            {
                "entities": [],
                "relations": [
                    {"subject": "alex", "object": "sam", "relation_phrase": "sibling of"}
                ],
            },
            "relations\\[0\\] is missing required field\\(s\\): qualifiers",
        ),
        (
            {
                "entities": [],
                "relations": [
                    {
                        "subject": "alex",
                        "object": "sam",
                        "relation_phrase": "sibling of",
                        "qualifiers": {"year": 1990, "note": None, "source": "memoir"},
                    }
                ],
            },
            "relations\\[0\\].qualifiers has unsupported field\\(s\\): source",
        ),
        (
            {
                "entities": [],
                "relations": [
                    {
                        "subject": "alex",
                        "object": "sam",
                        "relation_phrase": "sibling of",
                        "qualifiers": {"year": "1990", "note": None},
                    }
                ],
            },
            "relations\\[0\\].qualifiers.year must be an integer or null",
        ),
        (
            {
                "entities": [],
                "relations": [
                    {
                        "subject": "alex",
                        "object": "sam",
                        "relation_phrase": "sibling of",
                        "qualifiers": {"year": None, "note": ["not", "a", "string"]},
                    }
                ],
            },
            "relations\\[0\\].qualifiers.note must be a string or null",
        ),
    ],
)
def test_extraction_agent_rejects_invalid_structured_payloads(
    payload: dict[str, object],
    error: str,
) -> None:
    schema = make_single_class_schema()
    client = FakeClient([response_with_content(json.dumps(payload))])

    with pytest.raises(ExtractionAgentError, match=error):
        extraction_agent("Alex and Sam are siblings.", schema, client=client)

    assert client.completions.call_count == 1


def test_extraction_agent_retries_timeout_errors_then_succeeds() -> None:
    schema = make_single_class_schema()
    payload = {
        "entities": [
            {
                "id": "mary_smith_1910",
                "label": "Mary Smith",
                "type": "Person",
                "aliases": [],
                "attributes": {"birthYear": 1910},
            }
        ],
        "relations": [],
    }
    client = FakeClient(
        [
            timeout_error(),
            timeout_error(),
            response_with_content(json.dumps(payload)),
        ]
    )

    result = extraction_agent("Mary Smith was born in 1910.", schema, client=client)

    assert result == payload
    assert client.completions.call_count == 3
