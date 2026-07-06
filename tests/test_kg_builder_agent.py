from __future__ import annotations

import pytest
from rdflib import Literal, Namespace
from rdflib.namespace import OWL, RDF, RDFS, XSD

from agents.kg_builder_agent import (
    KGBuilderError,
    _sanitize_local_name,
    kg_builder_agent,
    kg_builder_agent_with_diagnostics,
)
from utils.rdf import parse_turtle_graph

FHKB = Namespace("http://www.example.com/genealogy.owl#")


def test_kg_builder_agent_full_example_emits_expected_triples() -> None:
    extractions = {
        "entities": [
            {
                "id": "john_doe_1900",
                "label": "John Doe",
                "sex": "Male",
                "birth_year": 1900,
                "death_year": 1970,
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

    graph = parse_turtle_graph(kg_builder_agent(extractions))
    john = FHKB.john_doe_1900
    jane = FHKB.jane_doe_1925
    marriage = FHKB.marriage_john_doe_1900_jane_doe_1925_1945

    assert (john, RDF.type, FHKB.Person) in graph
    assert (john, RDF.type, OWL.NamedIndividual) in graph
    assert (john, RDFS.label, Literal("John Doe")) in graph
    assert (john, FHKB.hasSex, FHKB.Male) in graph
    assert (john, FHKB.hasBirthYear, Literal(1900, datatype=XSD.integer)) in graph
    assert (john, FHKB.hasDeathYear, Literal(1970, datatype=XSD.integer)) in graph
    assert (john, FHKB.alsoKnownAs, Literal("Johnny")) in graph

    assert (jane, RDF.type, FHKB.Person) in graph
    assert (jane, RDF.type, OWL.NamedIndividual) in graph
    assert (jane, RDFS.label, Literal("Jane Doe")) in graph
    assert (jane, FHKB.hasSex, FHKB.Female) in graph
    assert (jane, FHKB.hasFather, john) in graph

    assert (marriage, RDF.type, FHKB.Marriage) in graph
    assert (marriage, RDF.type, OWL.NamedIndividual) in graph
    assert (marriage, FHKB.hasMalePartner, john) in graph
    assert (marriage, FHKB.hasFemalePartner, jane) in graph
    assert (marriage, FHKB.hasMarriageYear, Literal(1945, datatype=XSD.integer)) in graph


def test_kg_builder_agent_unknown_sex_emits_no_has_sex_triple() -> None:
    graph = parse_turtle_graph(
        kg_builder_agent(
            {
                "entities": [
                    {
                        "id": "alex_unknown",
                        "label": "Alex",
                        "sex": "Unknown",
                        "birth_year": None,
                        "death_year": None,
                        "aliases": [],
                    }
                ],
                "relations": [],
                "marriages": [],
            }
        )
    )

    assert (FHKB.alex_unknown, FHKB.hasSex, None) not in graph


def test_kg_builder_agent_null_years_emit_no_year_triples() -> None:
    graph = parse_turtle_graph(
        kg_builder_agent(
            {
                "entities": [
                    {
                        "id": "no_years",
                        "label": "No Years",
                        "sex": "Female",
                        "birth_year": None,
                        "death_year": None,
                        "aliases": [],
                    }
                ],
                "relations": [],
                "marriages": [],
            }
        )
    )

    assert (FHKB.no_years, FHKB.hasBirthYear, None) not in graph
    assert (FHKB.no_years, FHKB.hasDeathYear, None) not in graph


def test_duplicate_entity_with_conflicting_birth_year_raises_kg_builder_error() -> None:
    with pytest.raises(
        KGBuilderError,
        match="Conflicting birth_year values for entity john_doe: 1900 and 1901",
    ):
        kg_builder_agent(
            {
                "entities": [
                    {
                        "id": "john_doe",
                        "label": "John Doe",
                        "sex": "Male",
                        "birth_year": 1900,
                        "death_year": None,
                        "aliases": [],
                    },
                    {
                        "id": "john_doe",
                        "label": "John Doe",
                        "sex": "Male",
                        "birth_year": 1901,
                        "death_year": None,
                        "aliases": [],
                    },
                ],
                "relations": [],
                "marriages": [],
            }
        )


def test_sanitized_entity_collision_with_conflicting_death_year_raises_kg_builder_error() -> None:
    with pytest.raises(
        KGBuilderError,
        match="Conflicting death_year values for entity John-Doe\\?: 1970 and 1971",
    ):
        kg_builder_agent(
            {
                "entities": [
                    {
                        "id": "John Doe!",
                        "label": "First John",
                        "sex": "Male",
                        "birth_year": None,
                        "death_year": 1970,
                        "aliases": [],
                    },
                    {
                        "id": "John-Doe?",
                        "label": "Second John",
                        "sex": "Male",
                        "birth_year": None,
                        "death_year": 1971,
                        "aliases": [],
                    },
                ],
                "relations": [],
                "marriages": [],
            }
        )


def test_kg_builder_agent_aliases_emit_also_known_as_triples() -> None:
    graph = parse_turtle_graph(
        kg_builder_agent(
            {
                "entities": [
                    {
                        "id": "alias_person",
                        "label": "Alias Person",
                        "sex": "Male",
                        "birth_year": None,
                        "death_year": None,
                        "aliases": ["Al", "A.P."],
                    }
                ],
                "relations": [],
                "marriages": [],
            }
        )
    )

    assert (FHKB.alias_person, FHKB.alsoKnownAs, Literal("Al")) in graph
    assert (FHKB.alias_person, FHKB.alsoKnownAs, Literal("A.P.")) in graph


def test_sanitize_local_name_is_deterministic_for_collisions() -> None:
    assert _sanitize_local_name("John Doe!") == "john_doe_"
    assert _sanitize_local_name("John-Doe?") == "john_doe_"

    graph = parse_turtle_graph(
        kg_builder_agent(
            {
                "entities": [
                    {
                        "id": "John Doe!",
                        "label": "First John",
                        "sex": "Male",
                        "birth_year": None,
                        "death_year": None,
                        "aliases": [],
                    },
                    {
                        "id": "John-Doe?",
                        "label": "Second John",
                        "sex": "Male",
                        "birth_year": None,
                        "death_year": None,
                        "aliases": [],
                    },
                ],
                "relations": [],
                "marriages": [],
            }
        )
    )

    assert (FHKB.john_doe_, RDFS.label, Literal("First John")) in graph
    assert (FHKB.john_doe_, RDFS.label, Literal("Second John")) in graph


def test_sanitize_local_name_handles_punctuation_spaces_and_leading_digit() -> None:
    assert _sanitize_local_name("Mary Jane, Jr.") == "mary_jane__jr_"
    assert _sanitize_local_name("1900 John") == "e_1900_john"


def test_relation_with_unknown_entity_still_emits_triple() -> None:
    graph = parse_turtle_graph(
        kg_builder_agent(
            {
                "entities": [
                    {
                        "id": "known_child",
                        "label": "Known Child",
                        "sex": "Female",
                        "birth_year": None,
                        "death_year": None,
                        "aliases": [],
                    }
                ],
                "relations": [
                    {
                        "subject": "known_child",
                        "predicate": "hasFather",
                        "object": "unknown_father",
                    }
                ],
                "marriages": [],
            }
        )
    )

    assert (FHKB.known_child, FHKB.hasFather, FHKB.unknown_father) in graph


def test_relation_with_unknown_entity_collects_dangling_reference_diagnostic() -> None:
    result = kg_builder_agent_with_diagnostics(
        {
            "entities": [
                {
                    "id": "known_child",
                    "label": "Known Child",
                    "sex": "Female",
                    "birth_year": None,
                    "death_year": None,
                    "aliases": [],
                }
            ],
            "relations": [
                {
                    "subject": "known_child",
                    "predicate": "hasFather",
                    "object": "unknown_father",
                }
            ],
            "marriages": [],
        }
    )

    graph = parse_turtle_graph(result.turtle_graph)
    assert (FHKB.known_child, FHKB.hasFather, FHKB.unknown_father) in graph
    assert len(result.dangling_references) == 1
    dangling_reference = result.dangling_references[0]
    assert dangling_reference.role == "object"
    assert dangling_reference.entity_id == "unknown_father"
    assert dangling_reference.predicate == "hasFather"
    assert dangling_reference.subject_id == "known_child"
    assert dangling_reference.object_id == "unknown_father"


def test_marriage_with_unknown_partner_collects_dangling_reference_diagnostic() -> None:
    result = kg_builder_agent_with_diagnostics(
        {
            "entities": [
                {
                    "id": "known_husband",
                    "label": "Known Husband",
                    "sex": "Male",
                    "birth_year": None,
                    "death_year": None,
                    "aliases": [],
                }
            ],
            "relations": [],
            "marriages": [
                {
                    "male_partner": "known_husband",
                    "female_partner": "unknown_wife",
                    "marriage_year": 1950,
                }
            ],
        }
    )

    graph = parse_turtle_graph(result.turtle_graph)
    marriage = FHKB.marriage_known_husband_unknown_wife_1950
    assert (marriage, FHKB.hasMalePartner, FHKB.known_husband) in graph
    assert (marriage, FHKB.hasFemalePartner, FHKB.unknown_wife) in graph
    assert result.dangling_references == ()
    assert len(result.dangling_marriage_references) == 1
    dangling_reference = result.dangling_marriage_references[0]
    assert dangling_reference.role == "female_partner"
    assert dangling_reference.entity_id == "unknown_wife"
    assert dangling_reference.marriage_uri == str(marriage)
    assert dangling_reference.male_partner == "known_husband"
    assert dangling_reference.female_partner == "unknown_wife"


def test_same_couple_marriages_with_different_years_get_distinct_uris() -> None:
    graph = parse_turtle_graph(
        kg_builder_agent(
            {
                "entities": [
                    {
                        "id": "alex",
                        "label": "Alex",
                        "sex": "Male",
                        "birth_year": None,
                        "death_year": None,
                        "aliases": [],
                    },
                    {
                        "id": "jane",
                        "label": "Jane",
                        "sex": "Female",
                        "birth_year": None,
                        "death_year": None,
                        "aliases": [],
                    },
                ],
                "relations": [],
                "marriages": [
                    {
                        "male_partner": "alex",
                        "female_partner": "jane",
                        "marriage_year": 1945,
                    },
                    {
                        "male_partner": "alex",
                        "female_partner": "jane",
                        "marriage_year": 1955,
                    },
                ],
            }
        )
    )

    first_marriage = FHKB.marriage_alex_jane_1945
    second_marriage = FHKB.marriage_alex_jane_1955
    assert (first_marriage, RDF.type, FHKB.Marriage) in graph
    assert (second_marriage, RDF.type, FHKB.Marriage) in graph
    assert (first_marriage, FHKB.hasMarriageYear, Literal(1945, datatype=XSD.integer)) in graph
    assert (second_marriage, FHKB.hasMarriageYear, Literal(1955, datatype=XSD.integer)) in graph


def test_same_couple_marriages_without_years_get_occurrence_uris() -> None:
    graph = parse_turtle_graph(
        kg_builder_agent(
            {
                "entities": [],
                "relations": [],
                "marriages": [
                    {
                        "male_partner": "alex",
                        "female_partner": "jane",
                        "marriage_year": None,
                    },
                    {
                        "male_partner": "alex",
                        "female_partner": "jane",
                        "marriage_year": None,
                    },
                ],
            }
        )
    )

    first_marriage = FHKB.marriage_alex_jane_unknown_year_1
    second_marriage = FHKB.marriage_alex_jane_unknown_year_2
    assert (first_marriage, RDF.type, FHKB.Marriage) in graph
    assert (second_marriage, RDF.type, FHKB.Marriage) in graph
    assert (first_marriage, FHKB.hasMarriageYear, None) not in graph
    assert (second_marriage, FHKB.hasMarriageYear, None) not in graph


def test_empty_extractions_returns_valid_empty_turtle_graph() -> None:
    turtle = kg_builder_agent({"entities": [], "relations": [], "marriages": []})
    graph = parse_turtle_graph(turtle)

    assert len(graph) == 0


def test_missing_required_input_key_raises_kg_builder_error() -> None:
    with pytest.raises(KGBuilderError, match="Missing required extraction key: relations"):
        kg_builder_agent({"entities": [], "marriages": []})


def test_entity_missing_id_raises_kg_builder_error() -> None:
    with pytest.raises(KGBuilderError, match="missing required field: id"):
        kg_builder_agent(
            {
                "entities": [{"label": "No ID"}],
                "relations": [],
                "marriages": [],
            }
        )


def test_relation_missing_required_field_raises_kg_builder_error() -> None:
    with pytest.raises(KGBuilderError, match="Relation at index 0 is missing required field: object"):
        kg_builder_agent(
            {
                "entities": [],
                "relations": [{"subject": "child", "predicate": "hasFather"}],
                "marriages": [],
            }
        )


def test_relation_with_unsupported_predicate_raises_kg_builder_error() -> None:
    with pytest.raises(KGBuilderError, match="Unsupported relation predicate: hasPet"):
        kg_builder_agent(
            {
                "entities": [],
                "relations": [
                    {
                        "subject": "alex",
                        "predicate": "hasPet",
                        "object": "fluffy",
                    }
                ],
                "marriages": [],
            }
        )


def test_marriage_missing_required_field_raises_kg_builder_error() -> None:
    with pytest.raises(
        KGBuilderError,
        match="Marriage at index 0 is missing required field: marriage_year",
    ):
        kg_builder_agent(
            {
                "entities": [],
                "relations": [],
                "marriages": [{"male_partner": "john", "female_partner": "jane"}],
            }
        )
