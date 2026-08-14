"""Shared validation primitives for the knowledge-graph pipeline."""

from validation.diagnostics import (
    dangling_reference_violations,
    normalize_diagnostics,
    unmapped_relation_violations,
)
from validation.models import (
    ValidationResult,
    ValidationViolation,
    ViolationKind,
    ViolationSeverity,
    ViolationSource,
)
from validation.shacl_runner import (
    ShaclRunnerError,
    build_shacl_graph,
    build_ontology_graph,
    normalize_shacl_report,
    run_shacl_validation,
)

__all__ = [
    "dangling_reference_violations",
    "normalize_diagnostics",
    "unmapped_relation_violations",
    "ValidationResult",
    "ValidationViolation",
    "ViolationKind",
    "ViolationSeverity",
    "ViolationSource",
    "ShaclRunnerError",
    "build_shacl_graph",
    "build_ontology_graph",
    "normalize_shacl_report",
    "run_shacl_validation",
]
