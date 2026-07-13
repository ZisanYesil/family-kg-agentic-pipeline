from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Any, Optional

import structlog
from rdflib import Graph, Literal, Namespace, URIRef
from rdflib.namespace import OWL, RDF, RDFS, XSD

from ontology.schema_loader import OntologySchema

logger = structlog.get_logger(__name__)

REQUIRED_EXTRACTION_KEYS = ("entities", "relations")
REQUIRED_ENTITY_KEYS = ("id", "type")
RELATION_FIELDS = ("subject", "predicate", "object")

# Common RDFS/SKOS-style naming conventions for "alternate name" datatype properties. If the
# ontology declares one of these (case-insensitively), extraction_agent's `aliases` list is
# serialized using it; otherwise aliases have nowhere ontology-defined to go and are simply
# not written to RDF. This is a naming-convention match, not a hardcoded namespace/URI, so it
# works for any ontology that follows the convention and degrades gracefully for ones that
# don't.
_ALIAS_PROPERTY_CANDIDATES = {
    "alsoknownas",
    "knownas",
    "formerlyknownas",
    "altlabel",
    "aliases",
    "alias",
}


# Deliberately excludes "string": xsd:string and a plain (untyped) literal are not the
# same term as far as rdflib equality is concerned, and every other string-valued triple in
# this module (rdfs:label, aliases) is written as a plain literal, so string-valued
# attributes follow the same convention here for consistency.
_RANGE_TYPE_TO_XSD = {
    "integer": XSD.integer,
    "boolean": XSD.boolean,
    "decimal": XSD.decimal,
    "date": XSD.date,
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
    sanitized = re.sub(r"[^a-zA-Z0-9_]", "_", raw_id.lower())
    if sanitized and sanitized[0].isdigit():
        return f"e_{sanitized}"
    return sanitized


def _bind_prefixes(graph: Graph, ns: Namespace) -> None:
    graph.bind("onto", ns)
    graph.bind("rdf", RDF)
    graph.bind("rdfs", RDFS)
    graph.bind("owl", OWL)
    graph.bind("xsd", XSD)


def _find_alias_property(schema: OntologySchema) -> Optional[str]:
    for prop in schema.datatype_properties:
        if prop.local_name.lower() in _ALIAS_PROPERTY_CANDIDATES:
            return prop.local_name
    return None


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


def _validate_functional_attribute_fields(entities: list[Any]) -> None:
    """Flag conflicting values for the same (entity, attribute) pair across the entities
    list, e.g. the same id extracted twice with two different birthYear values."""
    seen_values: dict[tuple[str, str], object] = {}

    for entity in entities:
        entity_id = str(entity["id"])
        attributes = entity.get("attributes") or {}
        if not isinstance(attributes, dict):
            continue
        for field, value in attributes.items():
            if value is None:
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
    _validate_functional_attribute_fields(extractions["entities"])

    class_names = {cls.local_name for cls in schema.classes}
    for index, entity in enumerate(extractions["entities"]):
        entity_type = str(entity["type"])
        if entity_type not in class_names:
            raise KGBuilderError(f"Entity at index {index} has unsupported type: {entity_type}")

    predicate_names = {prop.local_name for prop in schema.object_properties}
    for relation in extractions["relations"]:
        predicate = str(relation["predicate"])
        if predicate not in predicate_names:
            raise KGBuilderError(f"Unsupported relation predicate: {predicate}")


def _add_entity(
    graph: Graph,
    ns: Namespace,
    entity: dict[str, Any],
    schema: OntologySchema,
    alias_property: Optional[str],
) -> None:
    subject = _entity_uri(ns, entity["id"])
    graph.add((subject, RDF.type, ns[str(entity["type"])]))
    graph.add((subject, RDF.type, OWL.NamedIndividual))

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
                # Not declared by this ontology (shouldn't happen given schema-validated
                # extraction output, but ignore defensively rather than fail late here).
                continue
            xsd_type = _RANGE_TYPE_TO_XSD.get(prop.range_type)
            literal = Literal(value, datatype=xsd_type) if xsd_type is not None else Literal(value)
            graph.add((subject, ns[prop.local_name], literal))

    if alias_property is not None:
        aliases = entity.get("aliases", [])
        if isinstance(aliases, list):
            for alias in aliases:
                graph.add((subject, ns[alias_property], Literal(str(alias))))


def _add_relation(
    graph: Graph,
    ns: Namespace,
    relation: dict[str, Any],
    known_entity_ids: set[str],
    dangling_references: list[DanglingRelationReference],
) -> None:
    subject_id = str(relation.get("subject", ""))
    object_id = str(relation.get("object", ""))
    predicate = str(relation.get("predicate", ""))

    for role, entity_id in (("subject", subject_id), ("object", object_id)):
        if entity_id not in known_entity_ids:
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

    graph.add((_entity_uri(ns, subject_id), ns[predicate], _entity_uri(ns, object_id)))


def kg_builder_agent(extractions: dict[str, list[Any]], schema: OntologySchema) -> str:
    """Convert extracted entities/relations into Turtle, for whatever ontology `schema`
    describes."""
    return kg_builder_agent_with_diagnostics(extractions, schema).turtle_graph


def kg_builder_agent_with_diagnostics(
    extractions: dict[str, list[Any]], schema: OntologySchema
) -> KGBuilderResult:
    """Convert extracted entities/relations into a Turtle-serialized RDF graph and collect
    non-fatal diagnostics. Works for any ontology: the namespace, valid entity types (rdf:type
    values), datatype property URIs, and valid relation predicates all come from `schema`
    (see ontology/schema_loader.py) rather than being hardcoded to the family ontology.
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

        ns = Namespace(schema.namespace)
        graph = Graph()
        _bind_prefixes(graph, ns)
        alias_property = _find_alias_property(schema)
        known_entity_ids = {str(entity["id"]) for entity in entities}
        dangling_references: list[DanglingRelationReference] = []

        for entity in entities:
            _add_entity(graph, ns, entity, schema, alias_property)
        for relation in relations:
            _add_relation(graph, ns, relation, known_entity_ids, dangling_references)

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
