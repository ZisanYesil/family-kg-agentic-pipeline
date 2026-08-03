from __future__ import annotations

from validation.models import (
    ValidationResult,
    ValidationViolation,
    ViolationKind,
    ViolationSeverity,
    ViolationSource,
)


def _violation(
    message: str,
    *,
    severity: ViolationSeverity = ViolationSeverity.VIOLATION,
    focus_node: str | None = None,
) -> ValidationViolation:
    return ValidationViolation(
        kind=ViolationKind.SHACL,
        source=ViolationSource.SHACL_GENERATOR,
        focus_node=focus_node,
        path="http://example.com/hasBirthYear",
        value="not-a-year",
        expected="xsd:integer",
        message=message,
        severity=severity,
        constraint_component="DatatypeConstraintComponent",
    )


def test_violation_serializes_enums_and_optional_context() -> None:
    violation = _violation("Birth year must be an integer", focus_node="http://example.com/alex")

    assert violation.as_dict() == {
        "kind": "shacl",
        "source": "shacl_generator",
        "focus_node": "http://example.com/alex",
        "path": "http://example.com/hasBirthYear",
        "value": "not-a-year",
        "expected": "xsd:integer",
        "message": "Birth year must be an integer",
        "severity": "violation",
        "constraint_component": "DatatypeConstraintComponent",
    }


def test_validation_result_sorts_violations_deterministically() -> None:
    later = _violation("Second finding", focus_node="http://example.com/z")
    earlier = _violation("First finding", focus_node="http://example.com/a")

    result = ValidationResult(violations=(later, earlier))

    assert result.violations == (earlier, later)


def test_validation_result_fingerprint_is_independent_of_input_order() -> None:
    first = _violation("First finding", focus_node="http://example.com/a")
    second = _violation("Second finding", focus_node="http://example.com/z")

    forward = ValidationResult(violations=(first, second))
    reversed_result = ValidationResult(violations=(second, first))

    assert forward.fingerprint == reversed_result.fingerprint


def test_validation_result_fingerprint_changes_with_finding_content() -> None:
    original = ValidationResult(violations=(_violation("Original"),))
    changed = ValidationResult(violations=(_violation("Changed"),))

    assert original.fingerprint != changed.fingerprint


def test_empty_validation_result_conforms() -> None:
    assert ValidationResult().conforms is True


def test_violation_severity_blocks_conformance() -> None:
    result = ValidationResult(violations=(_violation("Blocking defect"),))

    assert result.conforms is False


def test_warning_and_info_do_not_block_conformance() -> None:
    result = ValidationResult(
        violations=(
            _violation("Review this", severity=ViolationSeverity.WARNING),
            _violation("For context", severity=ViolationSeverity.INFO),
        )
    )

    assert result.conforms is True
