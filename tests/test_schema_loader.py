from __future__ import annotations

from ontology.schema_loader import load_ontology_schema


def test_load_ontology_schema_marks_functional_properties_from_family_ontology() -> None:
    schema = load_ontology_schema("ontology/family_extended.ttl")

    datatype_props = {prop.local_name: prop for prop in schema.datatype_properties}
    object_props = {prop.local_name: prop for prop in schema.object_properties}

    assert datatype_props["hasBirthYear"].is_functional is True
    assert datatype_props["hasDeathYear"].is_functional is True
    assert datatype_props["hasMarriageYear"].is_functional is True

    assert object_props["hasFather"].is_functional is True
    assert object_props["hasMother"].is_functional is True
    assert object_props["hasSex"].is_functional is True


def test_load_ontology_schema_does_not_infer_functional_status_from_inverse(tmp_path) -> None:
    ontology_path = tmp_path / "family_directionality.ttl"
    ontology_path.write_text(
        """
        @prefix ex: <http://example.com/test#> .
        @prefix owl: <http://www.w3.org/2002/07/owl#> .
        @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

        ex:Person a owl:Class .

        ex:hasParent a owl:ObjectProperty, owl:FunctionalProperty ;
            owl:inverseOf ex:isParentOf ;
            rdfs:domain ex:Person ;
            rdfs:range ex:Person .

        ex:isParentOf a owl:ObjectProperty .
        """,
        encoding="utf-8",
    )

    schema = load_ontology_schema(str(ontology_path))

    object_props = {prop.local_name: prop for prop in schema.object_properties}
    excluded_props = {prop.local_name: prop for prop in schema.excluded_object_properties}

    assert object_props["hasParent"].is_functional is True
    assert excluded_props["isParentOf"].reason == "inverse_duplicate"
