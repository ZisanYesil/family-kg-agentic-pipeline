from __future__ import annotations

from pathlib import Path

import pytest
from rdflib import Graph, Literal, Namespace
from rdflib.namespace import RDF, SH, XSD

from ontology.schema_loader import (
    DatatypeProperty,
    ObjectProperty,
    OntologyClass,
    OntologySchema,
)
from validation.models import ViolationKind, ViolationSeverity, ViolationSource
from validation.shacl_runner import (
    DATASET_ONTOLOGY_NAMESPACE,
    ShaclRunnerError,
    build_shacl_graph,
    run_shacl_validation,
)


EX = Namespace("http://example.com/mixed#")
SCHEMA = OntologySchema(
    namespace=str(EX),
    classes=(
        OntologyClass(local_name="Car", uri=str(EX.Car)),
        OntologyClass(local_name="Person", uri=str(EX.Person)),
    ),
    datatype_properties=(
        DatatypeProperty(
            local_name="modelYear",
            uri=str(EX.modelYear),
            domain_class="Car",
            range_type="integer",
            is_functional=True,
        ),
    ),
    object_properties=(
        ObjectProperty(
            local_name="owns",
            uri=str(EX.owns),
            domain_class="Person",
            range_class="Car",
        ),
    ),
)


def test_unregistered_namespace_uses_dynamic_shapes_only() -> None:
    shapes = build_shacl_graph(SCHEMA)

    assert (None, SH.targetSubjectsOf, EX.owns) in shapes
    assert (
        None,
        SH.targetSubjectsOf,
        Namespace(DATASET_ONTOLOGY_NAMESPACE).hasFather,
    ) not in shapes


def test_registered_supplement_is_merged_with_generated_shapes(tmp_path: Path) -> None:
    supplement_path = tmp_path / "custom_shapes.ttl"
    supplement_path.write_text(
        """
        @prefix ex: <http://example.com/mixed#> .
        @prefix sh: <http://www.w3.org/ns/shacl#> .
        ex:CustomShape a sh:NodeShape ; sh:targetClass ex:Person .
        """,
        encoding="utf-8",
    )

    shapes = build_shacl_graph(
        SCHEMA,
        supplement_registry={SCHEMA.namespace: supplement_path},
    )

    assert (EX.CustomShape, RDF.type, SH.NodeShape) in shapes
    assert (None, SH.targetSubjectsOf, EX.owns) in shapes


def test_malformed_registered_supplement_is_runtime_error(tmp_path: Path) -> None:
    supplement_path = tmp_path / "broken.ttl"
    supplement_path.write_text("this is not turtle", encoding="utf-8")

    with pytest.raises(ShaclRunnerError, match="Failed to parse SHACL supplement"):
        build_shacl_graph(
            SCHEMA,
            supplement_registry={SCHEMA.namespace: supplement_path},
        )


def test_valid_graph_returns_empty_conforming_result() -> None:
    data = Graph()
    data.add((EX.alex, RDF.type, EX.Person))
    data.add((EX.car_one, RDF.type, EX.Car))
    data.add((EX.alex, EX.owns, EX.car_one))
    data.add((EX.car_one, EX.modelYear, Literal(2020, datatype=XSD.integer)))

    result = run_shacl_validation(data, SCHEMA)

    assert result.conforms is True
    assert result.violations == ()


def test_dynamic_violation_is_normalized_with_repair_context() -> None:
    data = Graph()
    data.add((EX.car_one, RDF.type, EX.Car))
    data.add((EX.car_one, EX.modelYear, Literal("recent")))

    result = run_shacl_validation(data, SCHEMA)

    assert result.conforms is False
    assert len(result.violations) == 1
    violation = result.violations[0]
    assert violation.kind == ViolationKind.SHACL
    assert violation.source == ViolationSource.SHACL_GENERATOR
    assert violation.severity == ViolationSeverity.VIOLATION
    assert violation.focus_node == str(EX.car_one)
    assert violation.path == str(EX.modelYear)
    assert violation.value == "recent"
    assert str(XSD.integer) in (violation.expected or "")
    assert violation.constraint_component == str(SH.DatatypeConstraintComponent)


def test_results_are_deterministically_sorted() -> None:
    data = Graph()
    data.add((EX.car_b, RDF.type, EX.Car))
    data.add((EX.car_a, RDF.type, EX.Car))
    data.add((EX.car_b, EX.modelYear, Literal("new")))
    data.add((EX.car_a, EX.modelYear, Literal("old")))

    first = run_shacl_validation(data, SCHEMA)
    second = run_shacl_validation(data, SCHEMA)

    assert first.violations == second.violations
    assert first.fingerprint == second.fingerprint
    assert [v.focus_node for v in first.violations] == [str(EX.car_a), str(EX.car_b)]


def test_warning_is_reported_but_does_not_block_conformance(tmp_path: Path) -> None:
    supplement_path = tmp_path / "warning.ttl"
    supplement_path.write_text(
        """
        @prefix ex: <http://example.com/mixed#> .
        @prefix sh: <http://www.w3.org/ns/shacl#> .
        ex:WarningShape
            a sh:NodeShape ;
            sh:targetNode ex:alex ;
            sh:severity sh:Warning ;
            sh:class ex:Car ;
            sh:message "Alex is not a car; review only." .
        """,
        encoding="utf-8",
    )

    result = run_shacl_validation(
        Graph(),
        SCHEMA,
        supplement_registry={SCHEMA.namespace: supplement_path},
    )

    assert result.conforms is True
    assert len(result.violations) == 1
    assert result.violations[0].severity == ViolationSeverity.WARNING


def test_dataset_namespace_automatically_loads_dataset_semantic_shapes() -> None:
    dataset = Namespace(DATASET_ONTOLOGY_NAMESPACE)
    dataset_schema = OntologySchema(
        namespace=DATASET_ONTOLOGY_NAMESPACE,
        classes=(OntologyClass(local_name="Person", uri=str(dataset.Person)),),
        datatype_properties=(),
        object_properties=(),
    )

    shapes = build_shacl_graph(dataset_schema)

    assert (dataset.PersonShape, RDF.type, SH.NodeShape) in shapes
    assert (dataset.PersonShape, SH.targetClass, dataset.Person) in shapes


def test_rdfs_inference_accepts_subclass_for_property_domain_and_range() -> None:
    hierarchical_schema = OntologySchema(
        namespace=str(EX),
        classes=(
            OntologyClass(local_name="Vehicle", uri=str(EX.Vehicle)),
            OntologyClass(local_name="Car", uri=str(EX.Car)),
            OntologyClass(local_name="Person", uri=str(EX.Person)),
        ),
        datatype_properties=(),
        object_properties=(
            ObjectProperty(
                local_name="owns",
                uri=str(EX.owns),
                domain_class="Person",
                range_class="Vehicle",
            ),
        ),
        subclass_relations=(("Car", "Vehicle"),),
    )
    data = Graph()
    data.add((EX.alex, RDF.type, EX.Person))
    data.add((EX.car_one, RDF.type, EX.Car))
    data.add((EX.alex, EX.owns, EX.car_one))

    result = run_shacl_validation(data, hierarchical_schema)

    assert result.conforms is True
