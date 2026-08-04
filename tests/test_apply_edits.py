from __future__ import annotations

import pytest
from rdflib import Graph, Literal, Namespace, URIRef
from rdflib.namespace import RDF, RDFS, XSD

from feedback.apply_edits import ApplyEditsError, apply_feedback_plan
from feedback.models import FeedbackPlan
from ontology.schema_loader import (
    DatatypeProperty,
    ObjectProperty,
    OntologyClass,
    OntologySchema,
)
from validation.models import (
    ValidationViolation,
    ViolationKind,
    ViolationSource,
)


EX = Namespace("http://example.com/family#")
SCHEMA = OntologySchema(
    namespace=str(EX),
    classes=(
        OntologyClass(local_name="Man", uri=str(EX.Man)),
        OntologyClass(local_name="Person", uri=str(EX.Person)),
    ),
    datatype_properties=(
        DatatypeProperty(
            local_name="birthYear",
            uri=str(EX.birthYear),
            domain_class="Person",
            range_type="integer",
        ),
        DatatypeProperty(
            local_name="name",
            uri=str(EX.name),
            domain_class="Person",
            range_type="string",
        ),
    ),
    object_properties=(
        ObjectProperty(
            local_name="hasFather",
            uri=str(EX.hasFather),
            domain_class="Person",
            range_class="Man",
        ),
    ),
)


def _violation(
    *,
    kind: ViolationKind = ViolationKind.SHACL,
    focus_node: str = str(EX.alex),
    path: str | None = str(EX.birthYear),
    value: str | None = "recent",
    expected: str | None = str(XSD.integer),
) -> ValidationViolation:
    return ValidationViolation(
        kind=kind,
        source=ViolationSource.SHACL_GENERATOR,
        message="Invalid graph value",
        focus_node=focus_node,
        path=path,
        value=value,
        expected=expected,
    )


def _plan(
    violation: ValidationViolation,
    operations: list[dict[str, object]],
) -> FeedbackPlan:
    return FeedbackPlan.model_validate(
        {
            "reasoning": "Apply only grounded repairs.",
            "repairs": [
                {
                    "violation_fingerprint": violation.fingerprint,
                    "reasoning": "Repair this exact violation.",
                    "operations": operations,
                }
            ],
        }
    )


def _literal(
    value: str,
    datatype: str | None = None,
) -> dict[str, object]:
    return {
        "kind": "literal",
        "value": value,
        "datatype": datatype,
        "language": None,
    }


def _iri(value: str) -> dict[str, object]:
    return {"kind": "iri", "value": value}


def _base_graph() -> Graph:
    graph = Graph()
    graph.add((EX.alex, RDF.type, EX.Person))
    graph.add((EX.alex, EX.birthYear, Literal("recent")))
    graph.add((EX.john, RDF.type, EX.Man))
    return graph


def test_replace_literal_is_grounded_typed_logged_and_non_mutating() -> None:
    graph = _base_graph()
    violation = _violation()
    plan = _plan(
        violation,
        [
            {
                "operation": "replace_literal",
                "subject": str(EX.alex),
                "predicate": str(EX.birthYear),
                "old_literal": _literal("recent"),
                "new_literal": _literal("1950", str(XSD.integer)),
            }
        ],
    )

    result = apply_feedback_plan(
        graph,
        plan,
        violations=(violation,),
        schema=SCHEMA,
        source_text="Alex was born in 1950.",
    )

    assert (EX.alex, EX.birthYear, Literal("recent")) in graph
    assert (EX.alex, EX.birthYear, Literal("recent")) not in result.graph
    assert (EX.alex, EX.birthYear, Literal("1950", datatype=XSD.integer)) in result.graph
    assert result.unresolved_violation_fingerprints == ()
    assert len(result.edit_log) == 1
    assert result.edit_log[0].operation == "replace_literal"
    assert result.edit_log[0].old_value == '"recent"'
    assert result.edit_log[0].new_value == (
        '"1950"^^<http://www.w3.org/2001/XMLSchema#integer>'
    )
    assert result.edit_log[0].triples_before == result.edit_log[0].triples_after


def test_remove_can_delete_an_existing_schema_invalid_value() -> None:
    graph = _base_graph()
    violation = _violation()
    plan = _plan(
        violation,
        [
            {
                "operation": "remove_triple",
                "subject": str(EX.alex),
                "predicate": str(EX.birthYear),
                "object": _literal("recent"),
            }
        ],
    )

    result = apply_feedback_plan(
        graph,
        plan,
        violations=(violation,),
        schema=SCHEMA,
        source_text="Alex has no stated birth year.",
    )

    assert (EX.alex, EX.birthYear, Literal("recent")) not in result.graph
    assert (EX.alex, EX.birthYear, Literal("recent")) in graph


def test_unmapped_relation_can_add_only_the_suggested_object_property() -> None:
    graph = _base_graph()
    violation = _violation(
        kind=ViolationKind.UNMAPPED_RELATION,
        path=None,
        value=str(EX.john),
        expected=str(EX.hasFather),
    )
    plan = _plan(
        violation,
        [
            {
                "operation": "add_triple",
                "subject": str(EX.alex),
                "predicate": str(EX.hasFather),
                "object": _iri(str(EX.john)),
            }
        ],
    )

    result = apply_feedback_plan(
        graph,
        plan,
        violations=(violation,),
        schema=SCHEMA,
        source_text="John is Alex's father.",
    )

    assert (EX.alex, EX.hasFather, EX.john) in result.graph


def test_dangling_resource_can_receive_declared_type_and_grounded_label() -> None:
    graph = Graph()
    graph.add((EX.alex, RDF.type, EX.Person))
    graph.add((EX.alex, EX.hasFather, EX.john))
    violation = _violation(
        kind=ViolationKind.DANGLING_REFERENCE,
        focus_node=str(EX.john),
        path=str(EX.hasFather),
        value=str(EX.john),
        expected="Man",
    )
    plan = _plan(
        violation,
        [
            {
                "operation": "add_triple",
                "subject": str(EX.john),
                "predicate": str(RDF.type),
                "object": _iri(str(EX.Man)),
            },
            {
                "operation": "add_triple",
                "subject": str(EX.john),
                "predicate": str(RDFS.label),
                "object": _literal("John"),
            },
        ],
    )

    result = apply_feedback_plan(
        graph,
        plan,
        violations=(violation,),
        schema=SCHEMA,
        source_text="Alex's father is John.",
    )

    assert (EX.john, RDF.type, EX.Man) in result.graph
    assert (EX.john, RDFS.label, Literal("John")) in result.graph
    assert [entry.operation_index for entry in result.edit_log] == [0, 1]


@pytest.mark.parametrize(
    ("operation", "error"),
    [
        (
            {
                "operation": "add_triple",
                "subject": str(EX.alex),
                "predicate": str(EX.birthYear),
                "object": _literal("2042", str(XSD.integer)),
            },
            "not grounded in the source text",
        ),
        (
            {
                "operation": "add_triple",
                "subject": str(EX.alex),
                "predicate": str(EX.birthYear),
                "object": _literal("1950", str(XSD.string)),
            },
            "requires http://www.w3.org/2001/XMLSchema#integer",
        ),
        (
            {
                "operation": "add_triple",
                "subject": str(EX.alex),
                "predicate": "http://example.com/family#invented",
                "object": _literal("1950", str(XSD.integer)),
            },
            "outside the violation repair scope",
        ),
    ],
)
def test_rejects_ungrounded_or_schema_invalid_additions(
    operation: dict[str, object],
    error: str,
) -> None:
    violation = _violation()

    with pytest.raises(ApplyEditsError, match=error):
        apply_feedback_plan(
            _base_graph(),
            _plan(violation, [operation]),
            violations=(violation,),
            schema=SCHEMA,
            source_text="Alex was born in 1950 and his father is John.",
        )


def test_object_property_rejects_a_literal_object() -> None:
    violation = _violation(
        kind=ViolationKind.UNMAPPED_RELATION,
        path=None,
        value=str(EX.john),
        expected=str(EX.hasFather),
    )
    operation = {
        "operation": "add_triple",
        "subject": str(EX.alex),
        "predicate": str(EX.hasFather),
        "object": _literal("John"),
    }

    with pytest.raises(ApplyEditsError, match="requires an IRI object"):
        apply_feedback_plan(
            _base_graph(),
            _plan(violation, [operation]),
            violations=(violation,),
            schema=SCHEMA,
            source_text="John is Alex's father.",
        )


def test_operation_must_touch_the_violation_context() -> None:
    graph = _base_graph()
    graph.add((EX.mary, RDF.type, EX.Person))
    violation = _violation()
    plan = _plan(
        violation,
        [
            {
                "operation": "add_triple",
                "subject": str(EX.mary),
                "predicate": str(EX.birthYear),
                "object": _literal("1950", str(XSD.integer)),
            }
        ],
    )

    with pytest.raises(ApplyEditsError, match="does not touch"):
        apply_feedback_plan(
            graph,
            plan,
            violations=(violation,),
            schema=SCHEMA,
            source_text="Mary was born in 1950.",
        )


def test_failure_rolls_back_all_prior_operations() -> None:
    graph = _base_graph()
    violation = _violation()
    plan = _plan(
        violation,
        [
            {
                "operation": "remove_triple",
                "subject": str(EX.alex),
                "predicate": str(EX.birthYear),
                "object": _literal("recent"),
            },
            {
                "operation": "add_triple",
                "subject": str(EX.alex),
                "predicate": str(EX.birthYear),
                "object": _literal("invented", str(XSD.integer)),
            },
        ],
    )

    with pytest.raises(ApplyEditsError):
        apply_feedback_plan(
            graph,
            plan,
            violations=(violation,),
            schema=SCHEMA,
            source_text="No birth year was provided.",
        )

    assert (EX.alex, EX.birthYear, Literal("recent")) in graph


def test_plan_must_cover_exactly_the_current_violation_fingerprints() -> None:
    first = _violation()
    second = _violation(path=str(EX.name), value=None, expected=str(XSD.string))

    with pytest.raises(ApplyEditsError, match="missing violation"):
        apply_feedback_plan(
            _base_graph(),
            _plan(first, []),
            violations=(first, second),
            schema=SCHEMA,
            source_text="Alex is described.",
        )


def test_empty_operation_list_marks_violation_unresolved() -> None:
    violation = _violation()
    result = apply_feedback_plan(
        _base_graph(),
        _plan(violation, []),
        violations=(violation,),
        schema=SCHEMA,
        source_text="The source does not support a correction.",
    )

    assert result.unresolved_violation_fingerprints == (violation.fingerprint,)
    assert result.edit_log == ()
