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


def response_with_content(content: str) -> SimpleNamespace:
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
                "subject": "jane_doe_1925",
                "predicate": "hasFather",
                "object": "john_doe_1900",
            }
        ],
        "marriages": [
            {
                "male_partner": "john_doe_1900",
                "female_partner": "jane_doe_1925",
                "marriage_year": 1945,
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
        "marriages": [],
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
