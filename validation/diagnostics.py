from __future__ import annotations

from urllib.parse import quote

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


def _entity_uri(graph: Graph, raw_id: str, schema: OntologySchema) -> URIRef:
    """Resolve an extracted entity ID to the namespace actually used by the graph.

    Ontology terms and extracted individuals intentionally use different namespaces.
    Falling back to the ontology namespace retains compatibility for coarse diagnostics
    on an empty graph, while populated pipeline graphs resolve their concrete node IRI.
    """
    suffix = quote(str(raw_id), safe="-._~")
    candidates = sorted(
        {
            str(subject)
            for subject in graph.subjects()
            if isinstance(subject, URIRef)
            and str(subject).rsplit("/", 1)[-1].rsplit("#", 1)[-1] == suffix
        }
    )
    if candidates:
        return URIRef(candidates[0])
    return URIRef(str(Namespace(schema.namespace)[suffix]))


def _entity_namespace_from_known_node(
    graph: Graph,
    raw_id: str,
    schema: OntologySchema,
) -> str:
    uri = str(_entity_uri(graph, raw_id, schema))
    suffix = quote(str(raw_id), safe="-._~")
    return uri[: -len(suffix)] if suffix and uri.endswith(suffix) else schema.namespace


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
    properties = {prop.local_name: prop for prop in schema.object_properties}
    violations: list[ValidationViolation] = []

    for reference in references:
        entity_namespace = _entity_namespace_from_known_node(
            graph, reference.subject_id, schema
        )
        namespace = Namespace(entity_namespace)
        entity_uri = namespace[quote(reference.entity_id, safe="-._~")]
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

        relation_subject = namespace[quote(reference.subject_id, safe="-._~")]
        relation_object = namespace[quote(reference.object_id, safe="-._~")]
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

    A relation is considered repaired when feedback adds an ontology predicate between
    its original subject and object. Predicate semantics are deliberately left to the
    source-grounded feedback step; domain/range compatibility alone is not evidence that
    a predicate expresses the extracted phrase. SHACL validates the chosen predicate's
    endpoint types separately.
    """
    entity_types = {
        str(entity.get("id", "")): entity.get("type")
        for entity in entities
    }
    violations: list[ValidationViolation] = []

    for relation in relations:
        subject_uri = _entity_uri(graph, relation.subject, schema)
        object_uri = _entity_uri(graph, relation.object, schema)
        ontology_predicates = tuple(prop.uri for prop in schema.object_properties)
        if any(
            (subject_uri, URIRef(predicate), object_uri) in graph
            for predicate in ontology_predicates
        ):
            continue

        violations.append(
            ValidationViolation(
                kind=ViolationKind.UNMAPPED_RELATION,
                source=ViolationSource.ONTOLOGY_MAPPING,
                focus_node=str(subject_uri),
                path=None,
                value=str(object_uri),
                expected=None,
                message=(
                    f"Relation phrase {relation.relation_phrase!r} from "
                    f"{subject_uri} to {object_uri} was not mapped: "
                    f"{relation.reason}. Select a predicate only when its meaning is "
                    "supported by the relation phrase and source text; do not substitute "
                    "a merely type-compatible predicate."
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
