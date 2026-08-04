from __future__ import annotations

from rdflib import Graph, Namespace, URIRef
from rdflib.namespace import RDF

from agents.kg_builder_agent import DanglingRelationReference
from agents.ontology_mapping_agent import UnmappedRelation
from ontology.schema_loader import OntologySchema
from validation.models import (
    ValidationResult,
    ValidationViolation,
    ViolationKind,
    ViolationSource,
)


def dangling_reference_violations(
    references: tuple[DanglingRelationReference, ...],
    schema: OntologySchema,
    graph: Graph,
) -> tuple[ValidationViolation, ...]:
    """Convert unresolved KG-builder diagnostics into blocking validation findings.

    A feedback edit can resolve a dangling reference by adding an rdf:type for the
    referenced individual. Re-checking the current graph on every iteration prevents a
    stale builder diagnostic from blocking a graph after it has been repaired.
    """
    namespace = Namespace(schema.namespace)
    properties = {prop.local_name: prop for prop in schema.object_properties}
    violations: list[ValidationViolation] = []

    for reference in references:
        entity_uri = namespace[reference.entity_id]
        if any(graph.objects(entity_uri, RDF.type)):
            continue

        prop = properties.get(reference.predicate)
        expected_class = None
        property_uri = str(namespace[reference.predicate])
        if prop is not None:
            property_uri = prop.uri
            expected_class = (
                prop.domain_class if reference.role == "subject" else prop.range_class
            )

        relation_subject = namespace[reference.subject_id]
        relation_object = namespace[reference.object_id]
        expectation = (
            f" Expected rdf:type {expected_class}."
            if expected_class is not None
            else " Expected an explicit rdf:type."
        )
        violations.append(
            ValidationViolation(
                kind=ViolationKind.DANGLING_REFERENCE,
                source=ViolationSource.KG_BUILDER,
                focus_node=str(entity_uri),
                path=property_uri,
                value=str(entity_uri),
                expected=expected_class,
                message=(
                    f"Relation {relation_subject} {property_uri} {relation_object} "
                    f"references unknown {reference.role} entity "
                    f"{reference.entity_id!r}.{expectation}"
                ),
                constraint_component="DanglingReferenceConstraint",
            )
        )

    return _deduplicate(violations)


def _compatible_predicate_uris(
    *,
    subject_type: object,
    object_type: object,
    schema: OntologySchema,
) -> tuple[str, ...]:
    candidates = []
    for prop in schema.object_properties:
        domain_matches = (
            subject_type is None
            or prop.domain_class is None
            or subject_type == prop.domain_class
        )
        range_matches = (
            object_type is None
            or prop.range_class is None
            or object_type == prop.range_class
        )
        if domain_matches and range_matches:
            candidates.append(prop.uri)
    return tuple(sorted(set(candidates)))


def _deduplicate(
    violations: list[ValidationViolation],
) -> tuple[ValidationViolation, ...]:
    unique = {violation.canonical_key(): violation for violation in violations}
    return tuple(unique[key] for key in sorted(unique))


def unmapped_relation_violations(
    relations: tuple[UnmappedRelation, ...],
    entities: list[dict[str, object]],
    schema: OntologySchema,
    graph: Graph,
) -> tuple[ValidationViolation, ...]:
    """Convert unresolved ontology-mapping diagnostics into blocking findings.

    A relation is considered repaired when feedback adds one of the type-compatible
    ontology predicates between its original subject and object. Until then the source
    fact remains absent from the graph and must prevent a successful validation result.
    """
    namespace = Namespace(schema.namespace)
    entity_types = {
        str(entity.get("id", "")): entity.get("type")
        for entity in entities
    }
    violations: list[ValidationViolation] = []

    for relation in relations:
        subject_uri = namespace[relation.subject]
        object_uri = namespace[relation.object]
        candidates = _compatible_predicate_uris(
            subject_type=entity_types.get(relation.subject),
            object_type=entity_types.get(relation.object),
            schema=schema,
        )
        if any((subject_uri, URIRef(predicate), object_uri) in graph for predicate in candidates):
            continue

        expected = ", ".join(candidates) if candidates else None
        candidate_message = (
            f" Compatible predicates: {expected}."
            if expected is not None
            else " No ontology predicate satisfies the known endpoint types."
        )
        violations.append(
            ValidationViolation(
                kind=ViolationKind.UNMAPPED_RELATION,
                source=ViolationSource.ONTOLOGY_MAPPING,
                focus_node=str(subject_uri),
                path=None,
                value=str(object_uri),
                expected=expected,
                message=(
                    f"Relation phrase {relation.relation_phrase!r} from "
                    f"{subject_uri} to {object_uri} was not mapped: "
                    f"{relation.reason}.{candidate_message}"
                ),
                constraint_component="OntologyMappingConstraint",
            )
        )

    return _deduplicate(violations)


def normalize_diagnostics(
    *,
    unmapped_relations: tuple[UnmappedRelation, ...],
    dangling_references: tuple[DanglingRelationReference, ...],
    entities: list[dict[str, object]],
    schema: OntologySchema,
    graph: Graph,
) -> ValidationResult:
    """Normalize, merge, and deduplicate all pre-validation diagnostics."""
    violations = [
        *unmapped_relation_violations(
            unmapped_relations,
            entities,
            schema,
            graph,
        ),
        *dangling_reference_violations(
            dangling_references,
            schema,
            graph,
        ),
    ]
    return ValidationResult(violations=_deduplicate(violations))
