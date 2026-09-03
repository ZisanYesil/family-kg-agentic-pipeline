from __future__ import annotations

from rdflib import Graph, Literal, RDF, URIRef
from rdflib.namespace import XSD

from agents.kg_builder_agent import kg_builder_agent
from agents.ontology_mapping_agent import ontology_mapping_agent_with_diagnostics
from ontology.schema_loader import load_ontology_schema


ONTOLOGY_PATH = "ontology/ontology.ttl"
DATA = "http://example.org/extracted/"
ONTOLOGY = "http://example.org/2wiki-ontology#"


def test_deterministic_relation_mapping_uses_ontology_phrases() -> None:
    schema = load_ontology_schema(ONTOLOGY_PATH)
    extraction = {
        "entities": [
            {
                "id": "child",
                "label": "Child",
                "type": "Person",
                "aliases": [],
                "attributes": {},
            },
            {
                "id": "father",
                "label": "Father",
                "type": "Person",
                "aliases": [],
                "attributes": {},
            },
        ],
        "relations": [
            {
                "subject": "child",
                "object": "father",
                "relation_phrase": "has father",
                "qualifiers": {"year": None, "note": None},
            }
        ],
    }

    result = ontology_mapping_agent_with_diagnostics(extraction, schema)

    assert result.unmapped_relations == ()
    assert result.relations[0]["predicate"] == "hasFather"
    assert result.relations[0]["endpoints_swapped"] is False


def test_kg_builder_uses_separate_resource_namespace_and_gyear() -> None:
    schema = load_ontology_schema(ONTOLOGY_PATH)
    extraction = {
        "entities": [
            {
                "id": "john_smith",
                "label": "John Smith",
                "type": "Person",
                "aliases": [],
                "attributes": {"hasBirthDate": "1900"},
            }
        ],
        "relations": [],
    }

    graph = Graph().parse(
        data=kg_builder_agent(extraction, schema),
        format="turtle",
    )
    john = URIRef(DATA + "john_smith")

    assert (john, RDF.type, URIRef(ONTOLOGY + "Person")) in graph
    assert (
        john,
        URIRef(ONTOLOGY + "hasBirthDate"),
        Literal("1900", datatype=XSD.gYear),
    ) in graph


def test_kg_builder_reports_and_skips_dangling_relation() -> None:
    schema = load_ontology_schema(ONTOLOGY_PATH)
    extraction = {
        "entities": [
            {
                "id": "child",
                "label": "Child",
                "type": "Person",
                "aliases": [],
                "attributes": {},
            }
        ],
        "relations": [
            {
                "subject": "child",
                "predicate": "hasFather",
                "object": "missing_father",
            }
        ],
    }

    from agents.kg_builder_agent import kg_builder_agent_with_diagnostics

    result = kg_builder_agent_with_diagnostics(extraction, schema)
    graph = Graph().parse(data=result.turtle_graph, format="turtle")

    assert len(result.dangling_references) == 1
    assert not (
        URIRef(DATA + "child"),
        URIRef(ONTOLOGY + "hasFather"),
        URIRef(DATA + "missing_father"),
    ) in graph