"""Shared validation primitives for the knowledge-graph pipeline."""

from validation.models import (
    ValidationResult,
    ValidationViolation,
    ViolationKind,
    ViolationSeverity,
    ViolationSource,
)

__all__ = [
    "ValidationResult",
    "ValidationViolation",
    "ViolationKind",
    "ViolationSeverity",
    "ViolationSource",
]
