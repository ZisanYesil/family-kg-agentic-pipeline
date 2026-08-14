from __future__ import annotations

from ontology.schema_loader import load_ontology_schema


def test_load_dataset_ontology_schema_recognizes_date_or_year_ranges() -> None:
    schema = load_ontology_schema("ontology/dataset_ontology.ttl")

    datatype_props = {prop.local_name: prop for prop in schema.datatype_properties}

    assert datatype_props["hasBirthDate"].range_type == "date_or_year"
    assert datatype_props["hasDeathDate"].range_type == "date_or_year"
    assert datatype_props["hasPublicationDate"].range_type == "date_or_year"
    assert datatype_props["hasInception"].range_type == "date_or_year"
    assert schema.is_class_compatible("Film", "CreativeWork")
    assert schema.is_class_compatible("Film", "Artifact")
    assert schema.is_class_compatible("Company", "Agent")
    assert not schema.is_class_compatible("Person", "CreativeWork")
    object_props = {prop.local_name for prop in schema.object_properties}
    assert {"hasCountry", "hasCreator", "hasStudentOf"} <= object_props


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
