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
    return openai.APITimeoutError(
        request=httpx.Request("POST", "https://api.openai.com/v1/chat/completions")
    )


# Mixed-domain schema (people + vehicles), same spirit as test_extraction_agent.py: proves
# mapping is driven by schema.object_properties, not a hardcoded family predicate list.
def make_schema() -> OntologySchema:
    ns = "http://example.com/mixed-onto#"
    return OntologySchema(
        namespace=ns,
        classes=(
            OntologyClass(local_name="Person", uri=ns + "Person"),
            OntologyClass(local_name="Car", uri=ns + "Car"),
        ),
        datatype_properties=(),
        object_properties=(
            ObjectProperty(
                local_name="owns", uri=ns + "owns", domain_class="Person", range_class="Car",
                comment="Subject is the registered owner of object.",
            ),
            ObjectProperty(
                local_name="hasFather", uri=ns + "hasFather", domain_class="Person", range_class="Person",
            ),
            ObjectProperty(
                local_name="manufacturedBy", uri=ns + "manufacturedBy", domain_class="Car", range_class=None,
            ),
        ),
    )


def make_schema_no_object_properties() -> OntologySchema:
    ns = "http://example.com/bare#"
    return OntologySchema(
        namespace=ns,
        classes=(OntologyClass(local_name="Thing", uri=ns + "Thing"),),
        datatype_properties=(),
        object_properties=(),
    )


def _entity(id_: str, type_: str) -> dict:
    return {"id": id_, "label": id_, "type": type_, "aliases": [], "attributes": {}}


def _relation(subject: str, obj: str, phrase: str, year: object = None) -> dict:
    return {
        "subject": subject,
        "object": obj,
        "relation_phrase": phrase,
        "qualifiers": {"year": year, "note": None},
    }


def test_direct_predicate_mapping_happy_path() -> None:
    schema = make_schema()
    extraction_result = {
        "entities": [_entity("john_1900", "Person"), _entity("johns_civic", "Car")],
        "relations": [_relation("john_1900", "johns_civic", "owner of")],
    }
    mapping_payload = {
        "mappings": [{"subject": "john_1900", "object": "johns_civic", "predicate": "owns"}]
    }
    client = FakeClient([response_with_content(json.dumps(mapping_payload))])

    result = ontology_mapping_agent(extraction_result, schema, client=client)

    assert result["relations"] == [
        {"subject": "john_1900", "predicate": "owns", "object": "johns_civic"}
    ]
    assert result["entities"] == extraction_result["entities"]
    call = client.completions.calls[0]
    assert "owns" in call["messages"][0]["content"]
    assert "Person" in call["messages"][0]["content"]


def test_predicate_incompatible_with_entity_types_is_unmapped() -> None:
    """The model picked a real predicate, but the endpoint types violate its domain/range,
    so the relation should be reported as unmapped rather than silently written to RDF."""
    schema = make_schema()
    extraction_result = {
        "entities": [_entity("johns_civic", "Car"), _entity("toyota_factory", "Car")],
        "relations": [_relation("johns_civic", "toyota_factory", "owner of")],
    }
    # "owns" requires subject=Person, but both endpoints here are Car.
    mapping_payload = {
        "mappings": [{"subject": "johns_civic", "object": "toyota_factory", "predicate": "owns"}]
    }
    client = FakeClient([response_with_content(json.dumps(mapping_payload))])

    result = ontology_mapping_agent_with_diagnostics(extraction_result, schema, client=client)

    assert result.relations == []
    assert len(result.unmapped_relations) == 1
    unmapped = result.unmapped_relations[0]
    assert isinstance(unmapped, UnmappedRelation)
    assert "domain" in unmapped.reason


def test_unknown_entity_type_does_not_block_mapping() -> None:
    """A dangling relation endpoint (not in entities) has an unknown type; that shouldn't
    itself cause a domain/range rejection, since kg_builder_agent reports dangling
    references separately."""
    schema = make_schema()
    extraction_result = {
        "entities": [_entity("john_1900", "Person")],
        "relations": [_relation("john_1900", "ghost_car", "owner of")],
    }
    mapping_payload = {
        "mappings": [{"subject": "john_1900", "object": "ghost_car", "predicate": "owns"}]
    }
    client = FakeClient([response_with_content(json.dumps(mapping_payload))])

    result = ontology_mapping_agent_with_diagnostics(extraction_result, schema, client=client)

    assert result.relations == [{"subject": "john_1900", "predicate": "owns", "object": "ghost_car"}]
    assert result.unmapped_relations == ()


def test_null_predicate_is_unmapped() -> None:
    schema = make_schema()
    extraction_result = {
        "entities": [_entity("a", "Person"), _entity("b", "Person")],
        "relations": [_relation("a", "b", "godmother of")],
    }
    mapping_payload = {"mappings": [{"subject": "a", "object": "b", "predicate": None}]}
    client = FakeClient([response_with_content(json.dumps(mapping_payload))])

    result = ontology_mapping_agent_with_diagnostics(extraction_result, schema, client=client)

    assert result.relations == []
    assert len(result.unmapped_relations) == 1
    assert result.unmapped_relations[0].relation_phrase == "godmother of"


def test_empty_relations_skips_api_call() -> None:
    schema = make_schema()
    extraction_result = {"entities": [_entity("a", "Person")], "relations": []}
    client = FakeClient([])

    result = ontology_mapping_agent(extraction_result, schema, client=client)

    assert result == {"entities": extraction_result["entities"], "relations": []}
    assert client.completions.call_count == 0


def test_schema_with_no_object_properties_skips_api_call() -> None:
    schema = make_schema_no_object_properties()
    extraction_result = {
        "entities": [_entity("a", "Thing"), _entity("b", "Thing")],
        "relations": [_relation("a", "b", "related to")],
    }
    client = FakeClient([])

    result = ontology_mapping_agent_with_diagnostics(extraction_result, schema, client=client)

    assert result.relations == []
    assert len(result.unmapped_relations) == 1
    assert "no object properties" in result.unmapped_relations[0].reason
    assert client.completions.call_count == 0


def test_malformed_json_raises_error() -> None:
    schema = make_schema()
    extraction_result = {
        "entities": [_entity("a", "Person"), _entity("b", "Car")],
        "relations": [_relation("a", "b", "owner of")],
    }
    client = FakeClient([response_with_content("not json")])

    with pytest.raises(OntologyMappingAgentError, match="malformed JSON"):
        ontology_mapping_agent(extraction_result, schema, client=client)


def test_mapping_count_mismatch_raises_error() -> None:
    schema = make_schema()
    extraction_result = {
        "entities": [_entity("a", "Person"), _entity("b", "Car")],
        "relations": [_relation("a", "b", "owner of")],
    }
    client = FakeClient([response_with_content(json.dumps({"mappings": []}))])

    with pytest.raises(OntologyMappingAgentError, match="Expected 1 mapping"):
        ontology_mapping_agent(extraction_result, schema, client=client)


def test_subject_object_mismatch_raises_error() -> None:
    schema = make_schema()
    extraction_result = {
        "entities": [_entity("a", "Person"), _entity("b", "Car")],
        "relations": [_relation("a", "b", "owner of")],
    }
    mapping_payload = {"mappings": [{"subject": "x", "object": "b", "predicate": "owns"}]}
    client = FakeClient([response_with_content(json.dumps(mapping_payload))])

    with pytest.raises(OntologyMappingAgentError, match="does not match"):
        ontology_mapping_agent(extraction_result, schema, client=client)


def test_unsupported_predicate_raises_error() -> None:
    schema = make_schema()
    extraction_result = {
        "entities": [_entity("a", "Person"), _entity("b", "Car")],
        "relations": [_relation("a", "b", "owner of")],
    }
    mapping_payload = {"mappings": [{"subject": "a", "object": "b", "predicate": "hasCousin"}]}
    client = FakeClient([response_with_content(json.dumps(mapping_payload))])

    with pytest.raises(OntologyMappingAgentError, match="unsupported predicate"):
        ontology_mapping_agent(extraction_result, schema, client=client)


def test_retries_on_transient_error_then_succeeds() -> None:
    schema = make_schema()
    extraction_result = {
        "entities": [_entity("a", "Person"), _entity("b", "Person")],
        "relations": [_relation("a", "b", "father of")],
    }
    mapping_payload = {"mappings": [{"subject": "a", "object": "b", "predicate": "hasFather"}]}
    client = FakeClient([timeout_error(), response_with_content(json.dumps(mapping_payload))])

    result = ontology_mapping_agent(extraction_result, schema, client=client)

    assert result["relations"] == [{"subject": "a", "predicate": "hasFather", "object": "b"}]
    assert client.completions.call_count == 2