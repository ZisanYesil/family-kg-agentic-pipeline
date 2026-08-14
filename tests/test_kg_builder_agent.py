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
from ontology.schema_loader import DatatypeProperty, ObjectProperty, OntologyClass, OntologySchema
from utils.rdf import parse_turtle_graph

NS_URI = "http://example.com/mixed-onto#"
NS = Namespace(NS_URI)


# Mixed-domain schema (people + vehicles): proves kg_builder_agent's RDF.type, datatype
# property URIs, and valid predicates all come from `schema`, not a hardcoded family
# ontology. Also declares an "alsoKnownAs" datatype property to exercise the
# naming-convention alias detection.
def make_schema() -> OntologySchema:
    return OntologySchema(
        namespace=NS_URI,
        classes=(
            OntologyClass(local_name="Person", uri=NS_URI + "Person"),
            OntologyClass(local_name="Car", uri=NS_URI + "Car"),
        ),
        datatype_properties=(
            DatatypeProperty(
                local_name="birthYear", uri=NS_URI + "birthYear", domain_class="Person", range_type="integer"
            ),
            DatatypeProperty(
                local_name="deathYear", uri=NS_URI + "deathYear", domain_class="Person", range_type="integer"
            ),
            DatatypeProperty(
                local_name="model", uri=NS_URI + "model", domain_class="Car", range_type="string"
            ),
            DatatypeProperty(
                local_name="alsoKnownAs", uri=NS_URI + "alsoKnownAs", domain_class=None, range_type="string"
            ),
        ),
        object_properties=(
            ObjectProperty(
                local_name="owns", uri=NS_URI + "owns", domain_class="Person", range_class="Car"
            ),
            ObjectProperty(
                local_name="hasFather", uri=NS_URI + "hasFather", domain_class="Person", range_class="Person"
            ),
        ),
    )


def make_schema_without_alias_property() -> OntologySchema:
    return OntologySchema(
        namespace=NS_URI,
        classes=(OntologyClass(local_name="Person", uri=NS_URI + "Person"),),
        datatype_properties=(
            DatatypeProperty(
                local_name="birthYear", uri=NS_URI + "birthYear", domain_class="Person", range_type="integer"
            ),
        ),
        object_properties=(
            ObjectProperty(
                local_name="hasFather", uri=NS_URI + "hasFather", domain_class="Person", range_class="Person"
            ),
        ),
    )


def _entity(id_: str, type_: str, label: str | None = None, attributes: dict | None = None, aliases: list | None = None) -> dict:
    return {
        "id": id_,
        "label": label if label is not None else id_,
        "type": type_,
        "aliases": aliases or [],
        "attributes": attributes or {},
    }


def test_kg_builder_agent_full_example_emits_expected_triples() -> None:
    schema = make_schema()
    extractions = {
        "entities": [
            _entity(
                "john_doe_1900",
                "Person",
                label="John Doe",
                attributes={"birthYear": 1900, "deathYear": 1970},
                aliases=["Johnny"],
            ),
            _entity("johns_civic", "Car", label="Honda Civic", attributes={"model": "Civic"}),
        ],
        "relations": [
            {"subject": "john_doe_1900", "predicate": "owns", "object": "johns_civic"},
        ],
    }

    graph = parse_turtle_graph(kg_builder_agent(extractions, schema))
    john = NS.john_doe_1900
    civic = NS.johns_civic

    assert (john, RDF.type, NS.Person) in graph
    assert (john, RDF.type, OWL.NamedIndividual) in graph
    assert (john, RDFS.label, Literal("John Doe")) in graph
    assert (john, NS.birthYear, Literal(1900, datatype=XSD.integer)) in graph
    assert (john, NS.deathYear, Literal(1970, datatype=XSD.integer)) in graph
    assert (john, NS.alsoKnownAs, Literal("Johnny")) in graph
    assert (john, NS.owns, civic) in graph

    assert (civic, RDF.type, NS.Car) in graph
    assert (civic, NS.model, Literal("Civic")) in graph


def test_date_or_year_attributes_preserve_rdf_datatypes() -> None:
    schema = OntologySchema(
        namespace=NS_URI,
        classes=(OntologyClass(local_name="Person", uri=str(NS.Person)),),
        datatype_properties=(
            DatatypeProperty(
                local_name="birthDate",
                uri=str(NS.birthDate),
                domain_class="Person",
                range_type="date_or_year",
            ),
        ),
        object_properties=(),
    )

    full_date = parse_turtle_graph(
        kg_builder_agent(
            {
                "entities": [
                    _entity("alice", "Person", attributes={"birthDate": "2001-02-03"})
                ],
                "relations": [],
            },
            schema,
        )
    )
    year_only = parse_turtle_graph(
        kg_builder_agent(
            {
                "entities": [
                    _entity("bob", "Person", attributes={"birthDate": "1984"})
                ],
                "relations": [],
            },
            schema,
        )
    )

    assert (NS.alice, NS.birthDate, Literal("2001-02-03", datatype=XSD.date)) in full_date
    assert (NS.bob, NS.birthDate, Literal("1984", datatype=XSD.gYear)) in year_only


def test_kg_builder_agent_null_attributes_emit_no_triples() -> None:
    schema = make_schema()
    graph = parse_turtle_graph(
        kg_builder_agent(
            {
                "entities": [_entity("no_years", "Person", attributes={"birthYear": None, "deathYear": None})],
                "relations": [],
            },
            schema,
        )
    )

    assert (NS.no_years, NS.birthYear, None) not in graph
    assert (NS.no_years, NS.deathYear, None) not in graph


def test_duplicate_entity_with_conflicting_attribute_raises_kg_builder_error() -> None:
    schema = make_schema()
    with pytest.raises(
        KGBuilderError,
        match="Conflicting birthYear values for entity john_doe: 1900 and 1901",
    ):
        kg_builder_agent(
            {
                "entities": [
                    _entity("john_doe", "Person", attributes={"birthYear": 1900}),
                    _entity("john_doe", "Person", attributes={"birthYear": 1901}),
                ],
                "relations": [],
            },
            schema,
        )


def test_aliases_are_skipped_when_ontology_declares_no_alias_property() -> None:
    schema = make_schema_without_alias_property()
    graph = parse_turtle_graph(
        kg_builder_agent(
            {
                "entities": [_entity("alias_person", "Person", aliases=["Al", "A.P."])],
                "relations": [],
            },
            schema,
        )
    )

    # No triple should reference "Al" or "A.P." since there's no ontology property to use.
    assert not any(str(o) == "Al" for _, _, o in graph)


def test_aliases_emit_declared_alias_property_triples() -> None:
    schema = make_schema()
    graph = parse_turtle_graph(
        kg_builder_agent(
            {
                "entities": [_entity("alias_person", "Person", aliases=["Al", "A.P."])],
                "relations": [],
            },
            schema,
        )
    )

    assert (NS.alias_person, NS.alsoKnownAs, Literal("Al")) in graph
    assert (NS.alias_person, NS.alsoKnownAs, Literal("A.P.")) in graph


def test_sanitize_local_name_is_deterministic() -> None:
    assert _sanitize_local_name("John Doe!") == "john_doe_"
    assert _sanitize_local_name("John-Doe?") == "john_doe_"


def test_distinct_entity_ids_that_sanitize_to_same_iri_raise_kg_builder_error() -> None:
    schema = make_schema()
    with pytest.raises(
        KGBuilderError,
        match="both map to IRI local name 'john_doe_'",
    ):
        kg_builder_agent(
            {
                "entities": [
                    _entity("John Doe!", "Person"),
                    _entity("John-Doe?", "Person"),
                ],
                "relations": [],
            },
            schema,
        )


def test_entity_id_that_sanitizes_to_empty_local_name_raises_kg_builder_error() -> None:
    schema = make_schema()
    with pytest.raises(KGBuilderError, match="cannot be converted into a valid IRI local name"):
        kg_builder_agent(
            {
                "entities": [_entity("", "Person")],
                "relations": [],
            },
            schema,
        )


def test_relation_with_unknown_entity_still_emits_triple() -> None:
    schema = make_schema()
    graph = parse_turtle_graph(
        kg_builder_agent(
            {
                "entities": [_entity("known_child", "Person")],
                "relations": [
                    {"subject": "known_child", "predicate": "hasFather", "object": "unknown_father"}
                ],
            },
            schema,
        )
    )

    assert (NS.known_child, NS.hasFather, NS.unknown_father) in graph


def test_relation_with_unknown_entity_collects_dangling_reference_diagnostic() -> None:
    schema = make_schema()
    result = kg_builder_agent_with_diagnostics(
        {
            "entities": [_entity("known_child", "Person")],
            "relations": [
                {"subject": "known_child", "predicate": "hasFather", "object": "unknown_father"}
            ],
        },
        schema,
    )

    graph = parse_turtle_graph(result.turtle_graph)
    assert (NS.known_child, NS.hasFather, NS.unknown_father) in graph
    assert len(result.dangling_references) == 1
    dangling_reference = result.dangling_references[0]
    assert dangling_reference.role == "object"
    assert dangling_reference.entity_id == "unknown_father"
    assert dangling_reference.predicate == "hasFather"
    assert dangling_reference.subject_id == "known_child"
    assert dangling_reference.object_id == "unknown_father"


def test_empty_extractions_returns_valid_empty_turtle_graph() -> None:
    schema = make_schema()
    turtle = kg_builder_agent({"entities": [], "relations": []}, schema)
    graph = parse_turtle_graph(turtle)

    assert len(graph) == 0


def test_missing_required_input_key_raises_kg_builder_error() -> None:
    schema = make_schema()
    with pytest.raises(KGBuilderError, match="Missing required extraction key: relations"):
        kg_builder_agent({"entities": []}, schema)


def test_entity_missing_id_raises_kg_builder_error() -> None:
    schema = make_schema()
    with pytest.raises(KGBuilderError, match="missing required field: id"):
        kg_builder_agent({"entities": [{"type": "Person", "label": "No ID"}], "relations": []}, schema)


def test_entity_missing_type_raises_kg_builder_error() -> None:
    schema = make_schema()
    with pytest.raises(KGBuilderError, match="missing required field: type"):
        kg_builder_agent({"entities": [{"id": "no_type", "label": "No Type"}], "relations": []}, schema)


def test_entity_with_unsupported_type_raises_kg_builder_error() -> None:
    schema = make_schema()
    with pytest.raises(KGBuilderError, match="unsupported type: Boat"):
        kg_builder_agent({"entities": [_entity("x", "Boat")], "relations": []}, schema)


def test_relation_missing_required_field_raises_kg_builder_error() -> None:
    schema = make_schema()
    with pytest.raises(KGBuilderError, match="Relation at index 0 is missing required field: object"):
        kg_builder_agent(
            {"entities": [], "relations": [{"subject": "child", "predicate": "hasFather"}]},
            schema,
        )


def test_relation_with_unsupported_predicate_raises_kg_builder_error() -> None:
    schema = make_schema()
    with pytest.raises(KGBuilderError, match="Unsupported relation predicate: hasPet"):
        kg_builder_agent(
            {
                "entities": [],
                "relations": [{"subject": "alex", "predicate": "hasPet", "object": "fluffy"}],
            },
            schema,
        )
