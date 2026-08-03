from __future__ import annotations

from pyshacl import validate
from rdflib import Graph, Literal, Namespace
from rdflib.namespace import RDF, XSD
from rdflib.namespace import SH

from ontology.schema_loader import (
    DatatypeProperty,
    ObjectProperty,
    OntologyClass,
    OntologySchema,
)
from validation.shacl_generator import generate_shacl_graph


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
            is_functional=False,
        ),
        ObjectProperty(
            local_name="primaryVehicle",
            uri=str(EX.primaryVehicle),
            domain_class="Person",
            range_class="Car",
            is_functional=True,
        ),
    ),
)


def _validate(data_graph: Graph) -> tuple[bool, str]:
    conforms, _results_graph, results_text = validate(
        data_graph=data_graph,
        shacl_graph=generate_shacl_graph(SCHEMA),
        inference=None,
    )
    return bool(conforms), results_text


def test_generator_emits_domain_range_datatype_and_cardinality_constraints() -> None:
    shapes = generate_shacl_graph(SCHEMA)

    assert (None, SH.targetSubjectsOf, EX.owns) in shapes
    assert (None, SH.targetSubjectsOf, EX.modelYear) in shapes
    assert (None, SH["class"], EX.Person) in shapes
    assert (None, SH["class"], EX.Car) in shapes
    assert (None, SH.datatype, XSD.integer) in shapes
    assert len(list(shapes.triples((None, SH.maxCount, Literal(1))))) == 2


def test_generated_shapes_are_deterministic() -> None:
    first = generate_shacl_graph(SCHEMA)
    second = generate_shacl_graph(SCHEMA)

    assert set(first) == set(second)


def test_valid_mixed_domain_graph_conforms() -> None:
    data = Graph()
    data.add((EX.alex, RDF.type, EX.Person))
    data.add((EX.car_one, RDF.type, EX.Car))
    data.add((EX.alex, EX.owns, EX.car_one))
    data.add((EX.car_one, EX.modelYear, Literal(2020, datatype=XSD.integer)))

    conforms, results_text = _validate(data)

    assert conforms, results_text


def test_object_property_domain_violation_is_detected() -> None:
    data = Graph()
    data.add((EX.car_one, RDF.type, EX.Car))
    data.add((EX.car_two, RDF.type, EX.Car))
    data.add((EX.car_one, EX.owns, EX.car_two))

    conforms, results_text = _validate(data)

    assert not conforms
    assert "Subjects of owns must be instances of Person" in results_text


def test_object_property_range_violation_is_detected() -> None:
    data = Graph()
    data.add((EX.alex, RDF.type, EX.Person))
    data.add((EX.sam, RDF.type, EX.Person))
    data.add((EX.alex, EX.owns, EX.sam))

    conforms, results_text = _validate(data)

    assert not conforms
    assert "Values of owns must be instances of Car" in results_text


def test_datatype_violation_is_detected() -> None:
    data = Graph()
    data.add((EX.car_one, RDF.type, EX.Car))
    data.add((EX.car_one, EX.modelYear, Literal("recent")))

    conforms, results_text = _validate(data)

    assert not conforms
    assert "modelYear" in results_text
    assert str(XSD.integer) in results_text


def test_functional_object_property_violation_is_detected() -> None:
    data = Graph()
    data.add((EX.alex, RDF.type, EX.Person))
    data.add((EX.car_one, RDF.type, EX.Car))
    data.add((EX.car_two, RDF.type, EX.Car))
    data.add((EX.alex, EX.primaryVehicle, EX.car_one))
    data.add((EX.alex, EX.primaryVehicle, EX.car_two))

    conforms, results_text = _validate(data)

    assert not conforms
    assert "primaryVehicle must have at most one value" in results_text


def test_functional_datatype_property_violation_is_detected() -> None:
    data = Graph()
    data.add((EX.car_one, RDF.type, EX.Car))
    data.add((EX.car_one, EX.modelYear, Literal(2020, datatype=XSD.integer)))
    data.add((EX.car_one, EX.modelYear, Literal(2021, datatype=XSD.integer)))

    conforms, results_text = _validate(data)

    assert not conforms
    assert "modelYear must have at most one value" in results_text
