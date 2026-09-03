from __future__ import annotations

import re
from datetime import date
from dataclasses import dataclass
from typing import Any
from urllib.parse import quote

import structlog
from rdflib import Graph, Literal, Namespace, URIRef
from rdflib.namespace import OWL, RDF, RDFS, SKOS, XSD

from ontology.schema_loader import OntologySchema

logger = structlog.get_logger(__name__)

REQUIRED_EXTRACTION_KEYS = ("entities", "relations")
REQUIRED_ENTITY_KEYS = ("id", "type")
RELATION_FIELDS = ("subject", "predicate", "object")
DEFAULT_ENTITY_NAMESPACE = "http://example.org/extracted/"

# Deliberately excludes "string": xsd:string and a plain (untyped) literal are not the
# same term as far as rdflib equality is concerned, and every other string-valued triple in
# this module (rdfs:label, aliases) is written as a plain literal, so string-valued
# attributes follow the same convention here for consistency.
_RANGE_TYPE_TO_XSD = {
    "integer": XSD.integer,
    "boolean": XSD.boolean,
    "decimal": XSD.decimal,
    "date": XSD.date,
    "gYear": XSD.gYear,
}


class KGBuilderError(Exception):
    """Raised when extracted data cannot be converted into RDF safely."""


@dataclass(frozen=True)
class DanglingRelationReference:
    """A relation endpoint that was not present in the extracted entities list."""

    role: str
    entity_id: str
    predicate: str
    subject_id: str
    object_id: str


@dataclass(frozen=True)
class KGBuilderResult:
    turtle_graph: str
    dangling_references: tuple[DanglingRelationReference, ...]


def _sanitize_local_name(raw_id: str) -> str:
    return quote(raw_id, safe="-._~")


def _bind_prefixes(graph: Graph, ns: Namespace) -> None:
    graph.bind("onto", ns)
    graph.bind("rdf", RDF)
    graph.bind("rdfs", RDFS)
    graph.bind("owl", OWL)
    graph.bind("xsd", XSD)
    graph.bind("skos", SKOS)


def _entity_uri(ns: Namespace, raw_id: object) -> URIRef:
    return ns[_sanitize_local_name(str(raw_id))]


def _validate_required_object_fields(
    items: list[Any],
    item_name: str,
    required_fields: tuple[str, ...],
) -> None:
    for index, item in enumerate(items):
        if not isinstance(item, dict):
            raise KGBuilderError(f"{item_name} at index {index} must be an object")
        for key in required_fields:
            if key not in item:
                raise KGBuilderError(
                    f"{item_name} at index {index} is missing required field: {key}"
                )


def _validate_functional_attribute_fields(entities: list[Any], schema: OntologySchema) -> None:
    """Flag conflicting values for the same (entity, attribute) pair across the entities
    list, e.g. the same id extracted twice with two different birthYear values."""
    seen_values: dict[tuple[str, str], object] = {}

    functional_names = {prop.local_name for prop in schema.datatype_properties if prop.is_functional}
    for entity in entities:
        entity_id = str(entity["id"])
        attributes = entity.get("attributes") or {}
        if not isinstance(attributes, dict):
            continue
        for field, value in attributes.items():
            if value is None or field not in functional_names:
                continue
            key = (entity_id, field)
            existing = seen_values.get(key)
            if existing is None:
                seen_values[key] = value
                continue
            if existing != value:
                raise KGBuilderError(
                    f"Conflicting {field} values for entity {entity_id}: {existing} and {value}"
                )


def _validate_entity_iri_local_names(entities: list[Any]) -> None:
    """Ensure distinct extracted ids cannot collapse into the same RDF individual."""
    raw_id_by_local_name: dict[str, str] = {}

    for entity in entities:
        raw_id = str(entity["id"])
        local_name = _sanitize_local_name(raw_id)
        if not local_name:
            raise KGBuilderError(f"Entity id {raw_id!r} cannot be converted into a valid IRI local name")

        existing_raw_id = raw_id_by_local_name.get(local_name)
        if existing_raw_id is None:
            raw_id_by_local_name[local_name] = raw_id
            continue
        if existing_raw_id != raw_id:
            raise KGBuilderError(
                f"Entity ids {existing_raw_id!r} and {raw_id!r} both map to IRI local name {local_name!r}"
            )


def _validate_extractions(extractions: dict[str, list[Any]], schema: OntologySchema) -> None:
    for key in REQUIRED_EXTRACTION_KEYS:
        if key not in extractions:
            raise KGBuilderError(f"Missing required extraction key: {key}")
        if not isinstance(extractions[key], list):
            raise KGBuilderError(f"Extraction key must be a list: {key}")

    _validate_required_object_fields(extractions["entities"], "Entity", REQUIRED_ENTITY_KEYS)
    _validate_required_object_fields(extractions["relations"], "Relation", RELATION_FIELDS)
    _validate_entity_iri_local_names(extractions["entities"])
    _validate_functional_attribute_fields(extractions["entities"], schema)

    class_names = {cls.local_name for cls in schema.classes}
    seen_ids: set[str] = set()
    datatype_properties_by_name = {
        prop.local_name: prop for prop in schema.datatype_properties
    }
    datatype_names = set(datatype_properties_by_name)
    for index, entity in enumerate(extractions["entities"]):
        entity_id = str(entity["id"])
        if entity_id in seen_ids:
            raise KGBuilderError(f"Duplicate entity id: {entity_id}")
        seen_ids.add(entity_id)
        entity_type = str(entity["type"])
        if entity_type not in class_names:
            raise KGBuilderError(f"Entity at index {index} has unsupported type: {entity_type}")
        attributes = entity.get("attributes") or {}
        if not isinstance(attributes, dict):
            raise KGBuilderError(f"Entity at index {index} attributes must be an object")
        unknown_attributes = set(attributes) - datatype_names
        if unknown_attributes:
            raise KGBuilderError(
                f"Entity at index {index} has unsupported attributes: {', '.join(sorted(unknown_attributes))}"
            )
        for attribute_name, value in attributes.items():
            if value is None:
                continue
            prop = datatype_properties_by_name[attribute_name]
            if not schema.class_satisfies(entity_type, prop.domain_class):
                raise KGBuilderError(
                    f"Entity type {entity_type} does not satisfy {attribute_name} "
                    f"domain {prop.domain_class}"
                )

    predicate_names = {prop.local_name for prop in schema.object_properties}
    entity_type_by_id = {str(entity["id"]): str(entity["type"]) for entity in extractions["entities"]}
    properties_by_name = {prop.local_name: prop for prop in schema.object_properties}
    for relation in extractions["relations"]:
        predicate = str(relation["predicate"])
        if predicate not in predicate_names:
            raise KGBuilderError(f"Unsupported relation predicate: {predicate}")
        subject_type = entity_type_by_id.get(str(relation["subject"]))
        object_type = entity_type_by_id.get(str(relation["object"]))
        prop = properties_by_name[predicate]
        if subject_type is not None and not schema.class_satisfies(subject_type, prop.domain_class):
            raise KGBuilderError(
                f"Subject type {subject_type} does not satisfy {predicate} domain {prop.domain_class}"
            )
        if object_type is not None and not schema.class_satisfies(object_type, prop.range_class):
            raise KGBuilderError(
                f"Object type {object_type} does not satisfy {predicate} range {prop.range_class}"
            )


def _typed_literal(value: Any, range_type: str) -> Literal:
    if range_type == "date_or_year":
        text = str(value)
        if re.fullmatch(r"\d{4}", text):
            return Literal(text, datatype=XSD.gYear)
        if re.fullmatch(r"\d{4}-\d{2}-\d{2}", text):
            try:
                date.fromisoformat(text)
            except ValueError as exc:
                raise KGBuilderError(f"Invalid ISO date value: {text}") from exc
            return Literal(text, datatype=XSD.date)
        raise KGBuilderError(f"Date value must be YYYY or YYYY-MM-DD: {text!r}")
    xsd_type = _RANGE_TYPE_TO_XSD.get(range_type)
    return Literal(value, datatype=xsd_type) if xsd_type is not None else Literal(value)


def _add_entity(
    graph: Graph,
    entity_ns: Namespace,
    ontology_ns: Namespace,
    entity: dict[str, Any],
    schema: OntologySchema,
) -> None:
    subject = _entity_uri(entity_ns, entity["id"])
    graph.add((subject, RDF.type, OWL.NamedIndividual))
    # Preserve the class selected during extraction.  Previously the builder
    # validated ``entity["type"]`` but discarded it when serializing RDF, so
    # downstream reasoning could recover a type only when a relation happened
    # to have a sufficiently narrow rdfs:domain/range.  Properties such as
    # hasCountry intentionally have no domain, which made correctly extracted
    # Film entities lose Film -> CreativeWork -> Artifact altogether.
    graph.add((subject, RDF.type, ontology_ns[str(entity["type"])]))

    label = str(entity.get("label", ""))
    if label:
        graph.add((subject, RDFS.label, Literal(label)))

    datatype_props_by_name = {prop.local_name: prop for prop in schema.datatype_properties}
    attributes = entity.get("attributes") or {}
    if isinstance(attributes, dict):
        for name, value in attributes.items():
            if value is None:
                continue
            prop = datatype_props_by_name.get(name)
            if prop is None:
                raise KGBuilderError(f"Unsupported attribute: {name}")
            literal = _typed_literal(value, prop.range_type)
            graph.add((subject, ontology_ns[prop.local_name], literal))

    aliases = entity.get("aliases", [])
    if isinstance(aliases, list):
        for alias in aliases:
            graph.add((subject, SKOS.altLabel, Literal(str(alias))))


def _add_relation(
    graph: Graph,
    entity_ns: Namespace,
    ontology_ns: Namespace,
    relation: dict[str, Any],
    known_entity_ids: set[str],
    dangling_references: list[DanglingRelationReference],
) -> None:
    subject_id = str(relation.get("subject", ""))
    object_id = str(relation.get("object", ""))
    predicate = str(relation.get("predicate", ""))

    has_dangling_reference = False
    for role, entity_id in (("subject", subject_id), ("object", object_id)):
        if entity_id not in known_entity_ids:
            has_dangling_reference = True
            dangling_references.append(
                DanglingRelationReference(
                    role=role,
                    entity_id=entity_id,
                    predicate=predicate,
                    subject_id=subject_id,
                    object_id=object_id,
                )
            )
            logger.warning(
                "kg_builder_unknown_relation_entity",
                role=role,
                entity_id=entity_id,
                predicate=predicate,
            )

    if not has_dangling_reference:
        graph.add(
            (
                _entity_uri(entity_ns, subject_id),
                ontology_ns[predicate],
                _entity_uri(entity_ns, object_id),
            )
        )


def kg_builder_agent(
    extractions: dict[str, list[Any]],
    schema: OntologySchema,
    *,
    entity_namespace: str = DEFAULT_ENTITY_NAMESPACE,
) -> str:
    """Convert extracted entities/relations into Turtle, for whatever ontology `schema`
    describes."""
    return kg_builder_agent_with_diagnostics(
        extractions, schema, entity_namespace=entity_namespace
    ).turtle_graph


def kg_builder_agent_with_diagnostics(
    extractions: dict[str, list[Any]],
    schema: OntologySchema,
    *,
    entity_namespace: str = DEFAULT_ENTITY_NAMESPACE,
) -> KGBuilderResult:
    """Convert extracted entities/relations into a Turtle-serialized RDF graph and collect
    non-fatal diagnostics. Works for any ontology: the namespace, valid entity types (rdf:type
    values), datatype property URIs, and valid relation predicates all come from `schema`
    (see schema_loader.py) rather than being hardcoded to the family ontology.
    """
    try:
        _validate_extractions(extractions, schema)
        entities = extractions["entities"]
        relations = extractions["relations"]
        logger.info(
            "kg_builder_agent_called",
            entity_count=len(entities),
            relation_count=len(relations),
            ontology_namespace=schema.namespace,
        )

        ns = Namespace(entity_namespace)
        ontology_ns = Namespace(schema.namespace)
        graph = Graph()
        _bind_prefixes(graph, ontology_ns)
        graph.bind("data", ns)
        known_entity_ids = {str(entity["id"]) for entity in entities}
        dangling_references: list[DanglingRelationReference] = []

        for entity in entities:
            _add_entity(graph, ns, ontology_ns, entity, schema)
        for relation in relations:
            _add_relation(graph, ns, ontology_ns, relation, known_entity_ids, dangling_references)

        serialized = graph.serialize(format="turtle")
        if isinstance(serialized, bytes):
            serialized = serialized.decode("utf-8")

        logger.info(
            "kg_builder_agent_succeeded",
            triple_count=len(graph),
            dangling_reference_count=len(dangling_references),
        )
        return KGBuilderResult(
            turtle_graph=serialized,
            dangling_references=tuple(dangling_references),
        )
    except KGBuilderError:
        logger.exception("kg_builder_agent_failed")
        raise
    except Exception as exc:
        logger.exception("kg_builder_agent_failed", error=str(exc))
        raise KGBuilderError(f"Failed to build RDF graph from extractions: {exc}") from exc
