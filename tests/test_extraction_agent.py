from __future__ import annotations

import json
from types import SimpleNamespace

import httpx
import openai
import pytest

from agents.extraction_agent import (
    EXTRACTION_RESPONSE_FORMAT,
    ExtractionAgentError,
    extraction_agent,
)


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


def test_extraction_agent_happy_path_parses_structured_response(monkeypatch: pytest.MonkeyPatch) -> None:
    payload = {
        "entities": [
            {
                "id": "john_doe_1900",
                "label": "John Doe",
                "sex": "Male",
                "birth_year": 1900,
                "death_year": None,
                "aliases": ["Johnny"],
            },
            {
                "id": "jane_doe_1925",
                "label": "Jane Doe",
                "sex": "Female",
                "birth_year": 1925,
                "death_year": None,
                "aliases": [],
            },
        ],
        "relations": [
            {
                "subject": "john_doe_1900",
                "object": "jane_doe_1925",
                "relation_phrase": "married to",
                "qualifiers": {
                    "year": 1945,
                    "note": None,
                },
            }
        ],
    }
    client = FakeClient([response_with_content(json.dumps(payload))])
    monkeypatch.setenv("OPENAI_MODEL", "test-model")

    result = extraction_agent("John Doe, also known as Johnny, married Jane Doe in 1945.", client=client)

    assert result == payload
    assert client.completions.call_count == 1
    call = client.completions.calls[0]
    assert call["model"] == "test-model"
    assert call["response_format"] == EXTRACTION_RESPONSE_FORMAT
    assert call["messages"][0]["role"] == "system"
    assert call["messages"][1]["role"] == "user"
    assert call["messages"][1]["content"] == (
        "John Doe, also known as Johnny, married Jane Doe in 1945."
    )


def test_extraction_response_format_matches_current_agent_contract() -> None:
    schema = EXTRACTION_RESPONSE_FORMAT["json_schema"]["schema"]

    assert schema["required"] == ["entities", "relations"]
    assert "marriages" not in schema["properties"]

    relation_schema = schema["properties"]["relations"]["items"]
    assert relation_schema["required"] == [
        "subject",
        "object",
        "relation_phrase",
        "qualifiers",
    ]
    assert "predicate" not in relation_schema["properties"]
    assert relation_schema["properties"]["qualifiers"]["required"] == ["year", "note"]


@pytest.mark.parametrize("text", ["", "   "])
def test_extraction_agent_empty_input_raises_without_calling_client(text: str) -> None:
    client = FakeClient([response_with_content("{}")])

    with pytest.raises(ExtractionAgentError, match="Input text is empty"):
        extraction_agent(text, client=client)

    assert client.completions.call_count == 0


def test_extraction_agent_malformed_json_raises_error_with_raw_content() -> None:
    client = FakeClient([response_with_content("not-json")])

    with pytest.raises(ExtractionAgentError, match="not-json"):
        extraction_agent("John Doe was born in 1900.", client=client)

    assert client.completions.call_count == 1


def test_extraction_agent_non_string_model_content_raises_error() -> None:
    client = FakeClient([response_with_content(None)])

    with pytest.raises(ExtractionAgentError, match="Model returned non-string content"):
        extraction_agent("John Doe was born in 1900.", client=client)

    assert client.completions.call_count == 1


@pytest.mark.parametrize(
    ("payload", "error"),
    [
        (
            {
                "entities": [],
                "relations": [],
                "marriages": [],
            },
            "extraction result has unsupported field\\(s\\): marriages",
        ),
        (
            {
                "entities": [],
            },
            "extraction result is missing required field\\(s\\): relations",
        ),
        (
            {
                "entities": "not-a-list",
                "relations": [],
            },
            "extraction result.entities must be a list",
        ),
        (
            {
                "entities": [
                    {
                        "id": "alex",
                        "label": "Alex",
                        "sex": "Nonbinary",
                        "birth_year": None,
                        "death_year": None,
                        "aliases": [],
                    }
                ],
                "relations": [],
            },
            "entities\\[0\\].sex must be one of",
        ),
        (
            {
                "entities": [
                    {
                        "id": "alex",
                        "label": "Alex",
                        "sex": "Unknown",
                        "birth_year": True,
                        "death_year": None,
                        "aliases": [],
                    }
                ],
                "relations": [],
            },
            "entities\\[0\\].birth_year must be an integer or null",
        ),
        (
            {
                "entities": [
                    {
                        "id": "alex",
                        "label": "Alex",
                        "sex": "Unknown",
                        "birth_year": None,
                        "death_year": None,
                        "aliases": ["Al", 123],
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
                    {
                        "subject": "alex",
                        "object": "sam",
                        "relation_phrase": "sibling of",
                    }
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
                        "qualifiers": {
                            "year": 1990,
                            "note": None,
                            "source": "memoir",
                        },
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
                        "qualifiers": {
                            "year": "1990",
                            "note": None,
                        },
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
                        "qualifiers": {
                            "year": None,
                            "note": ["not", "a", "string"],
                        },
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
    client = FakeClient([response_with_content(json.dumps(payload))])

    with pytest.raises(ExtractionAgentError, match=error):
        extraction_agent("Alex and Sam are siblings.", client=client)

    assert client.completions.call_count == 1


def test_extraction_agent_retries_timeout_errors_then_succeeds() -> None:
    payload = {
        "entities": [
            {
                "id": "mary_smith_1910",
                "label": "Mary Smith",
                "sex": "Female",
                "birth_year": 1910,
                "death_year": None,
                "aliases": [],
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

    result = extraction_agent("Mary Smith was born in 1910.", client=client)

    assert result == payload
    assert client.completions.call_count == 3
