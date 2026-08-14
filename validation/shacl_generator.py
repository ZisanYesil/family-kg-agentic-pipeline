from __future__ import annotations

import hashlib
import re

from rdflib import BNode, Graph, Literal, Namespace, URIRef
from rdflib.collection import Collection
from rdflib.namespace import RDF, XSD
from rdflib.namespace import SH

from ontology.schema_loader import DatatypeProperty, ObjectProperty, OntologySchema


GENERATED_SHAPES_NAMESPACE = Namespace("urn:family-kg:validation:generated#")

_RANGE_TYPE_TO_XSD = {
    "integer": XSD.integer,
    "string": XSD.string,
    "boolean": XSD.boolean,
    "decimal": XSD.decimal,
    "date": XSD.date,
    "year": XSD.gYear,
}


def _shape_stem(local_name: str, property_uri: str) -> str:
    readable_name = re.sub(r"[^A-Za-z0-9_]", "_", local_name).strip("_") or "property"
    digest = hashlib.sha256(property_uri.encode("utf-8")).hexdigest()[:12]
    return f"{readable_name}_{digest}"


def _node_shape_uri(local_name: str, property_uri: str) -> URIRef:
    stem = _shape_stem(local_name, property_uri)
    return GENERATED_SHAPES_NAMESPACE[f"{stem}_NodeShape"]


def _property_shape_uri(local_name: str, property_uri: str, constraint: str) -> URIRef:
    stem = _shape_stem(local_name, property_uri)
    return GENERATED_SHAPES_NAMESPACE[f"{stem}_{constraint}_PropertyShape"]


def _class_uri(schema: OntologySchema, local_name: str) -> URIRef:
    ontology_class = schema.class_by_name(local_name)
    if ontology_class is not None:
        return URIRef(ontology_class.uri)
    return URIRef(f"{schema.namespace}{local_name}")


def _add_common_shape_structure(
    graph: Graph,
    schema: OntologySchema,
    *,
    local_name: str,
    property_uri: str,
    domain_class: str | None,
) -> tuple[URIRef, URIRef]:
    predicate = URIRef(property_uri)
    node_shape = _node_shape_uri(local_name, property_uri)

    graph.add((node_shape, RDF.type, SH.NodeShape))
    graph.add((node_shape, SH.targetSubjectsOf, predicate))

    if domain_class is not None:
        graph.add((node_shape, SH["class"], _class_uri(schema, domain_class)))
        graph.add(
            (
                node_shape,
                SH.message,
                Literal(f"Subjects of {local_name} must be instances of {domain_class}."),
            )
        )

    return node_shape, predicate


def _add_property_constraint(
    graph: Graph,
    *,
    node_shape: URIRef,
    local_name: str,
    property_uri: str,
    constraint: str,
) -> URIRef:
    property_shape = _property_shape_uri(local_name, property_uri, constraint)
    graph.add((node_shape, SH.property, property_shape))
    graph.add((property_shape, RDF.type, SH.PropertyShape))
    graph.add((property_shape, SH.path, URIRef(property_uri)))
    return property_shape


def _add_object_property_shape(
    graph: Graph,
    schema: OntologySchema,
    prop: ObjectProperty,
) -> None:
    node_shape, _predicate = _add_common_shape_structure(
        graph,
        schema,
        local_name=prop.local_name,
        property_uri=prop.uri,
        domain_class=prop.domain_class,
    )

    if prop.range_class is not None:
        property_shape = _add_property_constraint(
            graph,
            node_shape=node_shape,
            local_name=prop.local_name,
            property_uri=prop.uri,
            constraint="Range",
        )
        graph.add((property_shape, SH["class"], _class_uri(schema, prop.range_class)))
        graph.add(
            (
                property_shape,
                SH.message,
                Literal(f"Values of {prop.local_name} must be instances of {prop.range_class}."),
            )
        )

    if prop.is_functional:
        property_shape = _add_property_constraint(
            graph,
            node_shape=node_shape,
            local_name=prop.local_name,
            property_uri=prop.uri,
            constraint="MaxCount",
        )
        graph.add((property_shape, SH.maxCount, Literal(1)))
        graph.add(
            (
                property_shape,
                SH.message,
                Literal(f"{prop.local_name} must have at most one value per subject."),
            )
        )


def _add_datatype_property_shape(
    graph: Graph,
    schema: OntologySchema,
    prop: DatatypeProperty,
) -> None:
    node_shape, _predicate = _add_common_shape_structure(
        graph,
        schema,
        local_name=prop.local_name,
        property_uri=prop.uri,
        domain_class=prop.domain_class,
    )

    property_shape = _add_property_constraint(
        graph,
        node_shape=node_shape,
        local_name=prop.local_name,
        property_uri=prop.uri,
        constraint="Datatype",
    )
    if prop.range_type == "date_or_year":
        alternatives = []
        for datatype in (XSD.date, XSD.gYear):
            alternative = BNode()
            graph.add((alternative, SH.datatype, datatype))
            alternatives.append(alternative)
        union_head = BNode()
        Collection(graph, union_head, alternatives)
        graph.add((property_shape, SH["or"], union_head))
        expected = "xsd:date or xsd:gYear"
    else:
        datatype = _RANGE_TYPE_TO_XSD.get(prop.range_type, XSD.string)
        graph.add((property_shape, SH.datatype, datatype))
        expected = str(datatype)
    graph.add(
        (
            property_shape,
            SH.message,
            Literal(f"Values of {prop.local_name} must use datatype {expected}."),
        )
    )

    if prop.is_functional:
        property_shape = _add_property_constraint(
            graph,
            node_shape=node_shape,
            local_name=prop.local_name,
            property_uri=prop.uri,
            constraint="MaxCount",
        )
        graph.add((property_shape, SH.maxCount, Literal(1)))
        graph.add(
            (
                property_shape,
                SH.message,
                Literal(f"{prop.local_name} must have at most one value per subject."),
            )
        )


def generate_shacl_graph(schema: OntologySchema) -> Graph:
    """Generate ontology-agnostic structural SHACL constraints from ``schema``.

    The generated graph covers declared domains, ranges, datatypes, and functional
    properties. Domain-specific semantic rules belong in separately registered shape
    supplements and are intentionally not generated here.
    """
    graph = Graph()
    graph.bind("sh", SH)
    graph.bind("xsd", XSD)
    graph.bind("onto", Namespace(schema.namespace))
    graph.bind("generated", GENERATED_SHAPES_NAMESPACE)

    for prop in schema.object_properties:
        _add_object_property_shape(graph, schema, prop)
    for prop in schema.datatype_properties:
        _add_datatype_property_shape(graph, schema, prop)

    return graph
