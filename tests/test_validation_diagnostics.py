from __future__ import annotations

from rdflib import Graph, Namespace
from rdflib.namespace import RDF

from agents.kg_builder_agent import DanglingRelationReference
from agents.ontology_mapping_agent import UnmappedRelation
from ontology.schema_loader import ObjectProperty, OntologySchema
from validation.diagnostics import (
    dangling_reference_violations,
    normalize_diagnostics,
    unmapped_relation_violations,
)
from validation.models import ViolationKind, ViolationSource


SCHEMA = OntologySchema(
    namespace="http://example.com/family#",
    classes=(),
    datatype_properties=(),
    object_properties=(
        ObjectProperty(
            local_name="hasFather",
            uri="http://example.com/family#hasFather",
            domain_class="Person",
            range_class="Man",
        ),
    ),
)
REFERENCE = DanglingRelationReference(
    role="object",
    entity_id="unknown_father",
    predicate="hasFather",
    subject_id="known_child",
    object_id="unknown_father",
)


def test_dangling_reference_becomes_structured_blocking_violation() -> None:
    violations = dangling_reference_violations((REFERENCE,), SCHEMA, Graph())

    assert len(violations) == 1
    violation = violations[0]
    assert violation.kind == ViolationKind.DANGLING_REFERENCE
    assert violation.source == ViolationSource.KG_BUILDER
    assert violation.focus_node == "http://example.com/family#unknown_father"
    assert violation.path == "http://example.com/family#hasFather"
    assert violation.expected == "Man"
    assert "unknown_father" in violation.message


def test_dangling_reference_is_removed_after_feedback_adds_type() -> None:
    graph = Graph()
    namespace = Namespace(SCHEMA.namespace)
    graph.add((namespace["unknown_father"], RDF.type, namespace["Man"]))

    assert dangling_reference_violations((REFERENCE,), SCHEMA, graph) == ()


ENTITIES = [
    {"id": "known_child", "type": "Person"},
    {"id": "known_father", "type": "Man"},
]
UNMAPPED = UnmappedRelation(
    subject="known_child",
    object="known_father",
    relation_phrase="father",
    reason="relation_phrase did not match any ontology predicate",
)


def test_unmapped_relation_contains_type_compatible_predicate_candidates() -> None:
    violations = unmapped_relation_violations(
        (UNMAPPED,),
        ENTITIES,
        SCHEMA,
        Graph(),
    )

    assert len(violations) == 1
    violation = violations[0]
    assert violation.kind == ViolationKind.UNMAPPED_RELATION
    assert violation.source == ViolationSource.ONTOLOGY_MAPPING
    assert violation.focus_node == "http://example.com/family#known_child"
    assert violation.path is None
    assert violation.value == "http://example.com/family#known_father"
    assert violation.expected == "http://example.com/family#hasFather"
    assert "father" in violation.message


def test_unmapped_relation_excludes_predicates_with_wrong_endpoint_types() -> None:
    wrong_types = [
        {"id": "known_child", "type": "Man"},
        {"id": "known_father", "type": "Person"},
    ]

    violation = unmapped_relation_violations(
        (UNMAPPED,),
        wrong_types,
        SCHEMA,
        Graph(),
    )[0]

    assert violation.expected is None
    assert "No ontology predicate satisfies" in violation.message


def test_unmapped_relation_is_removed_after_feedback_adds_candidate_triple() -> None:
    graph = Graph()
    namespace = Namespace(SCHEMA.namespace)
    graph.add((namespace["known_child"], namespace["hasFather"], namespace["known_father"]))

    assert unmapped_relation_violations(
        (UNMAPPED,),
        ENTITIES,
        SCHEMA,
        graph,
    ) == ()


def test_duplicate_diagnostics_are_deduplicated_deterministically() -> None:
    result = normalize_diagnostics(
        unmapped_relations=(UNMAPPED, UNMAPPED),
        dangling_references=(REFERENCE, REFERENCE),
        entities=ENTITIES,
        schema=SCHEMA,
        graph=Graph(),
    )

    assert result.conforms is False
    assert len(result.violations) == 2
    assert {
        violation.kind for violation in result.violations
    } == {
        ViolationKind.UNMAPPED_RELATION,
        ViolationKind.DANGLING_REFERENCE,
    }
