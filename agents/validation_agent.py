from __future__ import annotations

import structlog
from rdflib import Graph

from agents.kg_builder_agent import DanglingRelationReference
from agents.ontology_mapping_agent import UnmappedRelation
from ontology.schema_loader import OntologySchema
from validation.diagnostics import normalize_diagnostics
from validation.models import ValidationResult, ValidationViolation
from validation.shacl_runner import ShaclRunnerError, run_shacl_validation

logger = structlog.get_logger(__name__)


class ValidationAgentError(Exception):
    """Raised when validation infrastructure fails rather than finding invalid data."""


def _merge_results(*results: ValidationResult) -> ValidationResult:
    """Merge validation sources without duplicating identical structured findings."""
    violations_by_key: dict[str, ValidationViolation] = {}
    for result in results:
        for violation in result.violations:
            violations_by_key[violation.canonical_key()] = violation
    return ValidationResult(violations=tuple(violations_by_key.values()))


def validation_agent(
    data_graph: Graph,
    schema: OntologySchema,
    *,
    unmapped_relations: tuple[UnmappedRelation, ...],
    dangling_references: tuple[DanglingRelationReference, ...],
    entities: list[dict[str, object]],
) -> ValidationResult:
    """Run deterministic graph validation and merge all current finding sources.

    SHACL detects defects that exist in the RDF graph. Diagnostic normalization covers
    source facts that never reached the graph (unmapped relations) and incomplete entity
    references emitted by the builder. Infrastructure failures are raised separately so
    the pipeline never mistakes a broken validator for a conforming graph.
    """
    if not isinstance(data_graph, Graph):
        raise TypeError("data_graph must be an rdflib.Graph")

    try:
        shacl_result = run_shacl_validation(data_graph, schema)
        diagnostic_result = normalize_diagnostics(
            unmapped_relations=unmapped_relations,
            dangling_references=dangling_references,
            entities=entities,
            schema=schema,
            graph=data_graph,
        )
    except ShaclRunnerError as exc:
        raise ValidationAgentError(f"SHACL validation infrastructure failed: {exc}") from exc
    except ValidationAgentError:
        raise
    except Exception as exc:
        raise ValidationAgentError(f"Validation agent failed: {exc}") from exc

    result = _merge_results(shacl_result, diagnostic_result)
    logger.info(
        "validation_agent_completed",
        ontology_namespace=schema.namespace,
        graph_triple_count=len(data_graph),
        shacl_finding_count=len(shacl_result.violations),
        diagnostic_finding_count=len(diagnostic_result.violations),
        total_finding_count=len(result.violations),
        conforms=result.conforms,
    )
    return result
