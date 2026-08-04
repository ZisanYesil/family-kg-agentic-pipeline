from __future__ import annotations

import pytest
from rdflib import Graph, Literal, Namespace
from rdflib.namespace import RDF, SH, XSD

from agents.ontology_mapping_agent import UnmappedRelation
from agents.validation_agent import ValidationAgentError, validation_agent
from ontology.schema_loader import (
    DatatypeProperty,
    ObjectProperty,
    OntologyClass,
    OntologySchema,
)
from validation.models import (
    ValidationResult,
    ValidationViolation,
    ViolationKind,
    ViolationSeverity,
    ViolationSource,
)
from validation.shacl_runner import ShaclRunnerError


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


def _run(
    graph: Graph,
    *,
    unmapped_relations: tuple[UnmappedRelation, ...] = (),
    entities: list[dict[str, object]] | None = None,
) -> ValidationResult:
    return validation_agent(
        graph,
        SCHEMA,
        unmapped_relations=unmapped_relations,
        dangling_references=(),
        entities=entities or [],
    )


def test_valid_graph_conforms() -> None:
    graph = Graph()
    graph.add((EX.alex, RDF.type, EX.Person))
    graph.add((EX.car, RDF.type, EX.Car))
    graph.add((EX.alex, EX.owns, EX.car))
    graph.add((EX.car, EX.modelYear, Literal(2020, datatype=XSD.integer)))

    result = _run(graph)

    assert result.conforms is True
    assert result.violations == ()


def test_shacl_and_mapping_diagnostics_are_merged() -> None:
    graph = Graph()
    graph.add((EX.alex, RDF.type, EX.Person))
    graph.add((EX.car, RDF.type, EX.Car))
    graph.add((EX.car, EX.modelYear, Literal("recent")))
    unmapped = UnmappedRelation(
        subject="alex",
        object="car",
        relation_phrase="owns",
        reason="relation_phrase did not match any ontology predicate",
    )

    result = _run(
        graph,
        unmapped_relations=(unmapped,),
        entities=[
            {"id": "alex", "type": "Person"},
            {"id": "car", "type": "Car"},
        ],
    )

    assert result.conforms is False
    assert {violation.kind for violation in result.violations} == {
        ViolationKind.SHACL,
        ViolationKind.UNMAPPED_RELATION,
    }


def test_duplicate_findings_from_sources_are_deduplicated(monkeypatch) -> None:
    duplicate = ValidationViolation(
        kind=ViolationKind.SHACL,
        source=ViolationSource.SHACL_GENERATOR,
        focus_node=str(EX.car),
        path=str(EX.modelYear),
        message="Duplicate",
    )
    duplicate_result = ValidationResult(violations=(duplicate,))
    monkeypatch.setattr(
        "agents.validation_agent.run_shacl_validation",
        lambda _graph, _schema: duplicate_result,
    )
    monkeypatch.setattr(
        "agents.validation_agent.normalize_diagnostics",
        lambda **_kwargs: duplicate_result,
    )

    result = _run(Graph())

    assert result.violations == (duplicate,)


def test_warning_only_result_conforms(monkeypatch) -> None:
    warning = ValidationViolation(
        kind=ViolationKind.SHACL,
        source=ViolationSource.SHACL_GENERATOR,
        focus_node=str(EX.alex),
        message="Review only",
        severity=ViolationSeverity.WARNING,
        constraint_component=str(SH.ClassConstraintComponent),
    )
    monkeypatch.setattr(
        "agents.validation_agent.run_shacl_validation",
        lambda _graph, _schema: ValidationResult(violations=(warning,)),
    )
    monkeypatch.setattr(
        "agents.validation_agent.normalize_diagnostics",
        lambda **_kwargs: ValidationResult(),
    )

    result = _run(Graph())

    assert result.conforms is True
    assert result.violations == (warning,)


def test_shacl_runtime_failure_is_not_converted_to_data_violation(monkeypatch) -> None:
    def fail(_graph, _schema):
        raise ShaclRunnerError("validator unavailable")

    monkeypatch.setattr("agents.validation_agent.run_shacl_validation", fail)

    with pytest.raises(
        ValidationAgentError,
        match="SHACL validation infrastructure failed",
    ):
        _run(Graph())


def test_rejects_non_graph_input() -> None:
    with pytest.raises(TypeError, match="rdflib.Graph"):
        validation_agent(  # type: ignore[arg-type]
            "not a graph",
            SCHEMA,
            unmapped_relations=(),
            dangling_references=(),
            entities=[],
        )
