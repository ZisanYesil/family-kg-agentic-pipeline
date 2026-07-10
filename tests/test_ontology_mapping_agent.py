from __future__ import annotations

import json
from types import SimpleNamespace

import httpx
import openai
import pytest

from agents.ontology_mapping_agent import (
    OntologyMappingAgentError,
    UnmappedRelation,
    ontology_mapping_agent,
    ontology_mapping_agent_with_diagnostics,
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
    return openai.APITimeoutError(
        request=httpx.Request("POST", "https://api.openai.com/v1/chat/completions")
    )


def _entity(id_: str, sex: str) -> dict:
    return {"id": id_, "label": id_, "sex": sex, "birth_year": None, "death_year": None, "aliases": []}


def _relation(subject: str, obj: str, phrase: str, year: object = None) -> dict:
    return {
        "subject": subject,
        "object": obj,
        "relation_phrase": phrase,
        "qualifiers": {"year": year, "note": None},
    }


def test_direct_predicate_mapping_happy_path() -> None:
    extraction_result = {
        "entities": [_entity("john_1900", "Male"), _entity("jane_1925", "Female")],
        "relations": [_relation("jane_1925", "john_1900", "daughter of")],
    }
    mapping_payload = {
        "mappings": [{"subject": "jane_1925", "object": "john_1900", "predicate": "hasFather"}]
    }
    client = FakeClient([response_with_content(json.dumps(mapping_payload))])

    result = ontology_mapping_agent(extraction_result, client=client)

    assert result["relations"] == [{"subject": "jane_1925", "predicate": "hasFather", "object": "john_1900"}]
    assert result["marriages"] == []
    assert result["entities"] == extraction_result["entities"]


def test_spousal_relation_resolves_into_marriage_regardless_of_order() -> None:
    extraction_result = {
        "entities": [_entity("john_1900", "Male"), _entity("jane_1925", "Female")],
        "relations": [_relation("jane_1925", "john_1900", "married to", year=1945)],
    }
    mapping_payload = {
        "mappings": [{"subject": "jane_1925", "object": "john_1900", "predicate": "isSpouseOf"}]
    }
    client = FakeClient([response_with_content(json.dumps(mapping_payload))])

    result = ontology_mapping_agent_with_diagnostics(extraction_result, client=client)

    assert result.relations == []
    assert result.marriages == [
        {"male_partner": "john_1900", "female_partner": "jane_1925", "marriage_year": 1945}
    ]
    assert result.unmapped_relations == ()


def test_spousal_relation_with_unresolvable_sexes_is_unmapped() -> None:
    extraction_result = {
        "entities": [_entity("a", "Unknown"), _entity("b", "Unknown")],
        "relations": [_relation("a", "b", "married to")],
    }
    mapping_payload = {"mappings": [{"subject": "a", "object": "b", "predicate": "isSpouseOf"}]}
    client = FakeClient([response_with_content(json.dumps(mapping_payload))])

    result = ontology_mapping_agent_with_diagnostics(extraction_result, client=client)

    assert result.marriages == []
    assert result.relations == []
    assert len(result.unmapped_relations) == 1
    unmapped = result.unmapped_relations[0]
    assert isinstance(unmapped, UnmappedRelation)
    assert unmapped.subject == "a"
    assert unmapped.object == "b"
    assert "sex" in unmapped.reason


def test_null_predicate_is_unmapped() -> None:
    extraction_result = {
        "entities": [_entity("a", "Female"), _entity("b", "Male")],
        "relations": [_relation("a", "b", "godmother of")],
    }
    mapping_payload = {"mappings": [{"subject": "a", "object": "b", "predicate": None}]}
    client = FakeClient([response_with_content(json.dumps(mapping_payload))])

    result = ontology_mapping_agent_with_diagnostics(extraction_result, client=client)

    assert result.relations == []
    assert result.marriages == []
    assert len(result.unmapped_relations) == 1
    assert result.unmapped_relations[0].relation_phrase == "godmother of"


def test_empty_relations_skips_api_call() -> None:
    extraction_result = {"entities": [_entity("a", "Male")], "relations": []}
    client = FakeClient([])

    result = ontology_mapping_agent(extraction_result, client=client)

    assert result == {"entities": extraction_result["entities"], "relations": [], "marriages": []}
    assert client.completions.call_count == 0


def test_malformed_json_raises_error() -> None:
    extraction_result = {
        "entities": [_entity("a", "Male"), _entity("b", "Female")],
        "relations": [_relation("a", "b", "father of")],
    }
    client = FakeClient([response_with_content("not json")])

    with pytest.raises(OntologyMappingAgentError, match="malformed JSON"):
        ontology_mapping_agent(extraction_result, client=client)


def test_mapping_count_mismatch_raises_error() -> None:
    extraction_result = {
        "entities": [_entity("a", "Male"), _entity("b", "Female")],
        "relations": [_relation("a", "b", "father of")],
    }
    client = FakeClient([response_with_content(json.dumps({"mappings": []}))])

    with pytest.raises(OntologyMappingAgentError, match="Expected 1 mapping"):
        ontology_mapping_agent(extraction_result, client=client)


def test_subject_object_mismatch_raises_error() -> None:
    extraction_result = {
        "entities": [_entity("a", "Male"), _entity("b", "Female")],
        "relations": [_relation("a", "b", "father of")],
    }
    mapping_payload = {"mappings": [{"subject": "x", "object": "b", "predicate": "hasFather"}]}
    client = FakeClient([response_with_content(json.dumps(mapping_payload))])

    with pytest.raises(OntologyMappingAgentError, match="does not match"):
        ontology_mapping_agent(extraction_result, client=client)


def test_unsupported_predicate_raises_error() -> None:
    extraction_result = {
        "entities": [_entity("a", "Male"), _entity("b", "Female")],
        "relations": [_relation("a", "b", "father of")],
    }
    mapping_payload = {"mappings": [{"subject": "a", "object": "b", "predicate": "hasCousin"}]}
    client = FakeClient([response_with_content(json.dumps(mapping_payload))])

    with pytest.raises(OntologyMappingAgentError, match="unsupported predicate"):
        ontology_mapping_agent(extraction_result, client=client)


def test_has_husband_is_no_longer_a_valid_mapping_output() -> None:
    """Regression test: hasHusband/hasWife used to be offered to the model alongside
    isSpouseOf, which meant marriage_year and Marriage reification were silently lost
    whenever the model picked the direct predicate instead of isSpouseOf. They were
    removed from VALID_MAPPING_PREDICATES so every spousal relation is forced through the
    single isSpouseOf reification path."""
    extraction_result = {
        "entities": [_entity("john_1900", "Male"), _entity("jane_1925", "Female")],
        "relations": [_relation("jane_1925", "john_1900", "married to", year=1945)],
    }
    mapping_payload = {"mappings": [{"subject": "jane_1925", "object": "john_1900", "predicate": "hasHusband"}]}
    client = FakeClient([response_with_content(json.dumps(mapping_payload))])

    with pytest.raises(OntologyMappingAgentError, match="unsupported predicate"):
        ontology_mapping_agent(extraction_result, client=client)


def test_retries_on_transient_error_then_succeeds() -> None:
    extraction_result = {
        "entities": [_entity("a", "Male"), _entity("b", "Female")],
        "relations": [_relation("a", "b", "father of")],
    }
    mapping_payload = {"mappings": [{"subject": "a", "object": "b", "predicate": "hasFather"}]}
    client = FakeClient([timeout_error(), response_with_content(json.dumps(mapping_payload))])

    result = ontology_mapping_agent(extraction_result, client=client)

    assert result["relations"] == [{"subject": "a", "predicate": "hasFather", "object": "b"}]
    assert client.completions.call_count == 2