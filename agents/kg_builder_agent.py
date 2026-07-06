from __future__ import annotations

from dataclasses import dataclass
import re
from typing import Any

import structlog
from rdflib import Graph, Literal, Namespace, URIRef
from rdflib.namespace import OWL, RDF, RDFS, XSD

logger = structlog.get_logger(__name__)

FHKB = Namespace("http://www.example.com/genealogy.owl#")

REQUIRED_EXTRACTION_KEYS = ("entities", "relations", "marriages")
REQUIRED_ENTITY_KEYS = ("id",)
RELATION_FIELDS = ("subject", "predicate", "object")
MARRIAGE_FIELDS = ("male_partner", "female_partner", "marriage_year")
VALID_RELATION_PREDICATES = (
    "hasFather",
    "hasMother",
    "hasBrother",
    "hasSister",
    "hasSon",
    "hasDaughter",
    "hasHusband",
    "hasWife",
)


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
    dangling_marriage_references: tuple["DanglingMarriagePartnerReference", ...] = ()


@dataclass(frozen=True)
class DanglingMarriagePartnerReference:
    """A marriage partner that was not present in the extracted entities list."""

    role: str
    entity_id: str
    marriage_uri: str
    male_partner: str
    female_partner: str


def _sanitize_local_name(raw_id: str) -> str:
    sanitized = re.sub(r"[^a-zA-Z0-9_]", "_", raw_id.lower())
    if sanitized and sanitized[0].isdigit():
        return f"e_{sanitized}"
    return sanitized


def _sanitize_local_part(raw_value: object) -> str:
    return re.sub(r"[^a-zA-Z0-9_]", "_", str(raw_value).lower())


def _bind_prefixes(graph: Graph) -> None:
    graph.bind("fhkb", FHKB)
    graph.bind("rdf", RDF)
    graph.bind("rdfs", RDFS)
    graph.bind("owl", OWL)
    graph.bind("xsd", XSD)


def _entity_uri(raw_id: object) -> URIRef:
    return FHKB[_sanitize_local_name(str(raw_id))]


def _relation_predicate_uri(predicate: str) -> URIRef:
    if predicate not in VALID_RELATION_PREDICATES:
        raise KGBuilderError(f"Unsupported relation predicate: {predicate}")
    return FHKB[predicate]


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


def _validate_functional_year_fields(entities: list[Any]) -> None:
    seen_years: dict[tuple[URIRef, str], object] = {}

    for entity in entities:
        entity_uri = _entity_uri(entity["id"])
        for field in ("birth_year", "death_year"):
            year = entity.get(field)
            if year is None:
                continue

            key = (entity_uri, field)
            existing_year = seen_years.get(key)
            if existing_year is None:
                seen_years[key] = year
                continue
            if existing_year != year:
                raise KGBuilderError(
                    f"Conflicting {field} values for entity {entity['id']}: "
                    f"{existing_year} and {year}"
                )


def _validate_extractions(extractions: dict[str, list[Any]]) -> None:
    for key in REQUIRED_EXTRACTION_KEYS:
        if key not in extractions:
            raise KGBuilderError(f"Missing required extraction key: {key}")
        if not isinstance(extractions[key], list):
            raise KGBuilderError(f"Extraction key must be a list: {key}")

    _validate_required_object_fields(extractions["entities"], "Entity", REQUIRED_ENTITY_KEYS)
    _validate_required_object_fields(extractions["relations"], "Relation", RELATION_FIELDS)
    _validate_required_object_fields(extractions["marriages"], "Marriage", MARRIAGE_FIELDS)

    _validate_functional_year_fields(extractions["entities"])

    for relation in extractions["relations"]:
        _relation_predicate_uri(str(relation["predicate"]))


def _add_entity(graph: Graph, entity: dict[str, Any]) -> None:
    subject = _entity_uri(entity["id"])
    graph.add((subject, RDF.type, FHKB.Person))
    graph.add((subject, RDF.type, OWL.NamedIndividual))

    label = str(entity.get("label", ""))
    if label:
        graph.add((subject, RDFS.label, Literal(label)))

    sex = entity.get("sex")
    if sex == "Male":
        graph.add((subject, FHKB.hasSex, FHKB.Male))
    elif sex == "Female":
        graph.add((subject, FHKB.hasSex, FHKB.Female))

    birth_year = entity.get("birth_year")
    if birth_year is not None:
        graph.add((subject, FHKB.hasBirthYear, Literal(birth_year, datatype=XSD.integer)))

    death_year = entity.get("death_year")
    if death_year is not None:
        graph.add((subject, FHKB.hasDeathYear, Literal(death_year, datatype=XSD.integer)))

    aliases = entity.get("aliases", [])
    if isinstance(aliases, list):
        for alias in aliases:
            graph.add((subject, FHKB.alsoKnownAs, Literal(str(alias))))


def _add_relation(
    graph: Graph,
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

    graph.add((_entity_uri(subject_id), _relation_predicate_uri(predicate), _entity_uri(object_id)))


def _marriage_uri(marriage: dict[str, Any], occurrence_index: int) -> URIRef:
    male_local = _sanitize_local_name(str(marriage.get("male_partner", "")))
    female_local = _sanitize_local_name(str(marriage.get("female_partner", "")))
    marriage_year = marriage.get("marriage_year")
    if marriage_year is None:
        return FHKB[f"marriage_{male_local}_{female_local}_unknown_year_{occurrence_index}"]

    year_local = _sanitize_local_part(marriage_year)
    return FHKB[f"marriage_{male_local}_{female_local}_{year_local}"]


def _add_marriage(
    graph: Graph,
    marriage: dict[str, Any],
    occurrence_index: int,
    known_entity_ids: set[str],
    dangling_marriage_references: list[DanglingMarriagePartnerReference],
) -> None:
    male_partner = str(marriage.get("male_partner", ""))
    female_partner = str(marriage.get("female_partner", ""))
    marriage_uri = _marriage_uri(marriage, occurrence_index)

    graph.add((marriage_uri, RDF.type, FHKB.Marriage))
    graph.add((marriage_uri, RDF.type, OWL.NamedIndividual))

    for role, partner_id in (("male_partner", male_partner), ("female_partner", female_partner)):
        if partner_id and partner_id not in known_entity_ids:
            dangling_marriage_references.append(
                DanglingMarriagePartnerReference(
                    role=role,
                    entity_id=partner_id,
                    marriage_uri=str(marriage_uri),
                    male_partner=male_partner,
                    female_partner=female_partner,
                )
            )
            logger.warning(
                "kg_builder_unknown_marriage_partner",
                role=role,
                entity_id=partner_id,
                male_partner=male_partner,
                female_partner=female_partner,
                marriage_uri=str(marriage_uri),
            )

    if male_partner:
        graph.add((marriage_uri, FHKB.hasMalePartner, _entity_uri(male_partner)))
    if female_partner:
        graph.add((marriage_uri, FHKB.hasFemalePartner, _entity_uri(female_partner)))

    marriage_year = marriage.get("marriage_year")
    if marriage_year is not None:
        graph.add((marriage_uri, FHKB.hasMarriageYear, Literal(marriage_year, datatype=XSD.integer)))


def kg_builder_agent(extractions: dict[str, list[Any]]) -> str:
    """Convert extracted entities/relations/marriages into Turtle."""
    return kg_builder_agent_with_diagnostics(extractions).turtle_graph


def kg_builder_agent_with_diagnostics(extractions: dict[str, list[Any]]) -> KGBuilderResult:
    """Convert extracted entities/relations/marriages into a Turtle-serialized RDF graph
    and collect non-fatal diagnostics.
    """
    try:
        _validate_extractions(extractions)
        entities = extractions["entities"]
        relations = extractions["relations"]
        marriages = extractions["marriages"]
        logger.info(
            "kg_builder_agent_called",
            entity_count=len(entities),
            relation_count=len(relations),
            marriage_count=len(marriages),
        )

        graph = Graph()
        _bind_prefixes(graph)
        known_entity_ids = {str(entity["id"]) for entity in entities}
        dangling_references: list[DanglingRelationReference] = []
        dangling_marriage_references: list[DanglingMarriagePartnerReference] = []

        for entity in entities:
            _add_entity(graph, entity)
        for relation in relations:
            _add_relation(graph, relation, known_entity_ids, dangling_references)
        for occurrence_index, marriage in enumerate(marriages, start=1):
            _add_marriage(
                graph,
                marriage,
                occurrence_index,
                known_entity_ids,
                dangling_marriage_references,
            )

        serialized = graph.serialize(format="turtle")
        if isinstance(serialized, bytes):
            serialized = serialized.decode("utf-8")

        logger.info(
            "kg_builder_agent_succeeded",
            triple_count=len(graph),
            dangling_reference_count=len(dangling_references),
            dangling_marriage_reference_count=len(dangling_marriage_references),
        )
        return KGBuilderResult(
            turtle_graph=serialized,
            dangling_references=tuple(dangling_references),
            dangling_marriage_references=tuple(dangling_marriage_references),
        )
    except KGBuilderError:
        logger.exception("kg_builder_agent_failed")
        raise
    except Exception as exc:
        logger.exception("kg_builder_agent_failed", error=str(exc))
        raise KGBuilderError(f"Failed to build RDF graph from extractions: {exc}") from exc
