from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass
from enum import Enum
from typing import Any, Optional


class ViolationKind(str, Enum):
    """The validation mechanism or earlier-stage diagnostic that found a defect."""

    SHACL = "shacl"
    REASONER = "reasoner"
    UNMAPPED_RELATION = "unmapped_relation"
    DANGLING_REFERENCE = "dangling_reference"


class ViolationSource(str, Enum):
    """The component that emitted a normalized validation finding."""

    SHACL_GENERATOR = "shacl_generator"
    REASONER_RUNNER = "reasoner_runner"
    ONTOLOGY_MAPPING = "ontology_mapping"
    KG_BUILDER = "kg_builder"


class ViolationSeverity(str, Enum):
    """SHACL-compatible severity levels used by every validation source."""

    VIOLATION = "violation"
    WARNING = "warning"
    INFO = "info"


@dataclass(frozen=True)
class ValidationViolation:
    """A normalized, immutable validation finding.

    Optional fields remain explicit because coarse reasoner errors and diagnostics from
    earlier pipeline stages do not always identify an existing RDF focus node or path.
    """

    kind: ViolationKind
    source: ViolationSource
    message: str
    severity: ViolationSeverity = ViolationSeverity.VIOLATION
    focus_node: Optional[str] = None
    path: Optional[str] = None
    value: Optional[str] = None
    expected: Optional[str] = None
    constraint_component: Optional[str] = None

    def as_dict(self) -> dict[str, Any]:
        """Return a JSON-compatible representation with a stable field layout."""
        return {
            "kind": self.kind.value,
            "source": self.source.value,
            "focus_node": self.focus_node,
            "path": self.path,
            "value": self.value,
            "expected": self.expected,
            "message": self.message,
            "severity": self.severity.value,
            "constraint_component": self.constraint_component,
        }

    def canonical_key(self) -> str:
        """Return a deterministic key suitable for sorting and equality fingerprints."""
        return json.dumps(
            self.as_dict(),
            ensure_ascii=False,
            sort_keys=True,
            separators=(",", ":"),
        )

    @property
    def fingerprint(self) -> str:
        return hashlib.sha256(self.canonical_key().encode("utf-8")).hexdigest()


@dataclass(frozen=True)
class ValidationResult:
    """Deterministically ordered findings and their pipeline gating decision."""

    violations: tuple[ValidationViolation, ...] = ()

    def __post_init__(self) -> None:
        ordered = tuple(sorted(self.violations, key=ValidationViolation.canonical_key))
        object.__setattr__(self, "violations", ordered)

    @property
    def conforms(self) -> bool:
        """Only violation-severity findings block completion; warnings and info do not."""
        return not any(
            violation.severity == ViolationSeverity.VIOLATION
            for violation in self.violations
        )

    @property
    def fingerprint(self) -> str:
        """Identify a complete finding set independently of its input order."""
        canonical = json.dumps(
            [violation.as_dict() for violation in self.violations],
            ensure_ascii=False,
            sort_keys=True,
            separators=(",", ":"),
        )
        return hashlib.sha256(canonical.encode("utf-8")).hexdigest()
