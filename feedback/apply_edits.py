from __future__ import annotations

import unicodedata
import re
from dataclasses import dataclass
from typing import Any

from rdflib import Graph, Literal, URIRef
from rdflib.namespace import RDF, RDFS, XSD
from rdflib.term import Identifier

from feedback.models import (
    AddTriple,
    EditOperation,
    FeedbackPlan,
    IriObject,
    LiteralObject,
    RemoveTriple,
    ReplaceLiteral,
)
from ontology.schema_loader import DatatypeProperty, ObjectProperty, OntologySchema
from utils.rdf import clone_graph
from validation.models import ValidationViolation, ViolationKind


_RANGE_TYPE_TO_XSD = {
    "integer": XSD.integer,
    "string": XSD.string,
    "boolean": XSD.boolean,
    "decimal": XSD.decimal,
    "date": XSD.date,
}


class ApplyEditsError(Exception):
    """Raised when a feedback plan cannot be applied safely and atomically."""


@dataclass(frozen=True)
class EditLogEntry:
    violation_fingerprint: str
    operation_index: int
    operation: str
    subject: str
    predicate: str
    old_value: str | None
    new_value: str | None
    triples_before: int
    triples_after: int


@dataclass(frozen=True)
class ApplyEditsResult:
    graph: Graph
    edit_log: tuple[EditLogEntry, ...]
    unresolved_violation_fingerprints: tuple[str, ...]


def _fail(
    message: str,
    *,
    fingerprint: str | None = None,
    operation_index: int | None = None,
) -> ApplyEditsError:
    context = []
    if fingerprint is not None:
        context.append(f"violation={fingerprint}")
    if operation_index is not None:
        context.append(f"operation={operation_index}")
    prefix = f"[{', '.join(context)}] " if context else ""
    return ApplyEditsError(prefix + message)


def _literal_term(value: LiteralObject) -> Literal:
    if value.language is not None:
        return Literal(value.value, lang=value.language)
    if value.datatype is not None:
        literal = Literal(value.value, datatype=URIRef(value.datatype))
        if getattr(literal, "ill_typed", False):
            raise ApplyEditsError(
                f"Literal {value.value!r} is not valid for datatype {value.datatype}"
            )
        return literal
    return Literal(value.value)


def _object_term(value: IriObject | LiteralObject) -> Identifier:
    if isinstance(value, IriObject):
        return URIRef(value.value)
    return _literal_term(value)


def _normalized_text(value: str) -> str:
    return unicodedata.normalize("NFKC", value).casefold()


def _literal_is_source_grounded(literal: Literal, source_text: str) -> bool:
    lexical = _normalized_text(str(literal))
    if not lexical:
        return False
    source = _normalized_text(source_text)
    pattern = re.escape(lexical)
    if lexical[0].isalnum():
        pattern = rf"(?<!\w){pattern}"
    if lexical[-1].isalnum():
        pattern = rf"{pattern}(?!\w)"
    return re.search(pattern, source, flags=re.UNICODE) is not None


def _known_resource_iris(graph: Graph) -> set[str]:
    resources: set[str] = set()
    for subject, _predicate, obj in graph:
        if isinstance(subject, URIRef):
            resources.add(str(subject))
        if isinstance(obj, URIRef):
            resources.add(str(obj))
    return resources


def _violation_context_iris(violation: ValidationViolation) -> set[str]:
    return {
        value
        for value in (violation.focus_node, violation.value)
        if value is not None
    }


def _allowed_predicates(
    violation: ValidationViolation,
    schema: OntologySchema,
) -> set[str]:
    allowed: set[str] = set()
    if violation.path is not None:
        allowed.add(violation.path)

    if violation.kind == ViolationKind.UNMAPPED_RELATION:
        # The model must choose by meaning from the declared ontology. Restricting this
        # to type-compatible properties caused semantically false substitutions (for
        # example, mapping "composed by" to hasDirector). SHACL checks domain/range
        # after the edit, and rdf:type may be repaired when the source supports it.
        allowed.update(prop.uri for prop in schema.object_properties)
        allowed.add(str(RDF.type))

    if violation.kind == ViolationKind.DANGLING_REFERENCE:
        allowed.add(str(RDF.type))
        allowed.add(str(RDFS.label))
    elif (
        violation.path == str(RDF.type)
        or (
            violation.constraint_component is not None
            and violation.constraint_component.endswith("ClassConstraintComponent")
        )
    ):
        allowed.add(str(RDF.type))
    return allowed


def _validate_operation_scope(
    operation: EditOperation,
    violation: ValidationViolation,
    schema: OntologySchema,
) -> None:
    allowed_predicates = _allowed_predicates(violation, schema)
    if operation.predicate not in allowed_predicates:
        raise ApplyEditsError(
            f"Predicate {operation.predicate} is outside the violation repair scope"
        )

    context_iris = _violation_context_iris(violation)
    touches_context = operation.subject in context_iris
    if isinstance(operation, (AddTriple, RemoveTriple)):
        if isinstance(operation.object, IriObject):
            touches_context = touches_context or operation.object.value in context_iris
    if not touches_context:
        raise ApplyEditsError(
            "Edit operation does not touch the violation focus_node or value"
        )


def _validate_iri_object_grounding(
    value: URIRef,
    *,
    graph: Graph,
    violation: ValidationViolation,
) -> None:
    iri = str(value)
    allowed = _known_resource_iris(graph) | _violation_context_iris(violation)
    if iri in allowed:
        return
    expected_iris = {
        candidate.strip()
        for candidate in (violation.expected or "").split(",")
        if candidate.strip()
    }
    if iri in expected_iris:
        return
    raise ApplyEditsError(
        f"IRI object {iri} is not grounded in the graph or violation context"
    )


def _validate_datatype_property_object(
    prop: DatatypeProperty,
    obj: Identifier,
) -> None:
    if not isinstance(obj, Literal):
        raise ApplyEditsError(
            f"Datatype property {prop.uri} requires a literal object"
        )

    expected_datatype = _RANGE_TYPE_TO_XSD.get(prop.range_type, XSD.string)
    if expected_datatype == XSD.string:
        if obj.language is not None:
            raise ApplyEditsError(
                f"Datatype property {prop.uri} does not accept language-tagged literals"
            )
        if obj.datatype not in (None, XSD.string):
            raise ApplyEditsError(
                f"Datatype property {prop.uri} requires xsd:string"
            )
        return

    if obj.datatype != expected_datatype:
        raise ApplyEditsError(
            f"Datatype property {prop.uri} requires {expected_datatype}"
        )
    if getattr(obj, "ill_typed", False):
        raise ApplyEditsError(
            f"Literal {str(obj)!r} is invalid for {expected_datatype}"
        )


def _validate_predicate_and_object(
    predicate: URIRef,
    obj: Identifier,
    *,
    schema: OntologySchema,
    graph: Graph,
    violation: ValidationViolation,
) -> None:
    predicate_text = str(predicate)
    datatype_properties = {
        prop.uri: prop for prop in schema.datatype_properties
    }
    object_properties = {
        prop.uri: prop for prop in schema.object_properties
    }
    class_uris = {cls.uri for cls in schema.classes}

    if predicate == RDF.type:
        if not isinstance(obj, URIRef) or str(obj) not in class_uris:
            raise ApplyEditsError(
                "rdf:type object must be a class declared by the ontology schema"
            )
        return

    if predicate == RDFS.label:
        if (
            violation.kind != ViolationKind.DANGLING_REFERENCE
            or not isinstance(obj, Literal)
        ):
            raise ApplyEditsError(
                "rdfs:label is allowed only as a literal dangling-entity repair"
            )
        return

    datatype_prop = datatype_properties.get(predicate_text)
    if datatype_prop is not None:
        _validate_datatype_property_object(datatype_prop, obj)
        return

    object_prop = object_properties.get(predicate_text)
    if object_prop is not None:
        if not isinstance(obj, URIRef):
            raise ApplyEditsError(
                f"Object property {object_prop.uri} requires an IRI object"
            )
        _validate_iri_object_grounding(
            obj,
            graph=graph,
            violation=violation,
        )
        return

    raise ApplyEditsError(
        f"Predicate {predicate_text} is not in the ontology edit allowlist"
    )


def _validate_existing_triple_predicate(
    predicate: URIRef,
    *,
    schema: OntologySchema,
    violation: ValidationViolation,
) -> None:
    """Validate a removal target without requiring its existing object to be valid."""
    predicate_text = str(predicate)
    if predicate == RDF.type:
        return
    if predicate == RDFS.label and violation.kind == ViolationKind.DANGLING_REFERENCE:
        return
    if any(prop.uri == predicate_text for prop in schema.datatype_properties):
        return
    if any(prop.uri == predicate_text for prop in schema.object_properties):
        return
    raise ApplyEditsError(
        f"Predicate {predicate_text} is not in the ontology edit allowlist"
    )


def _validate_subject_grounding(
    subject: URIRef,
    *,
    graph: Graph,
    violation: ValidationViolation,
) -> None:
    subject_text = str(subject)
    allowed = _known_resource_iris(graph) | _violation_context_iris(violation)
    if subject_text not in allowed:
        raise ApplyEditsError(
            f"Subject {subject_text} is not grounded in the graph or violation context"
        )


def _log_entry(
    *,
    fingerprint: str,
    operation_index: int,
    operation: EditOperation,
    old_value: Identifier | None,
    new_value: Identifier | None,
    triples_before: int,
    triples_after: int,
) -> EditLogEntry:
    return EditLogEntry(
        violation_fingerprint=fingerprint,
        operation_index=operation_index,
        operation=operation.operation,
        subject=operation.subject,
        predicate=operation.predicate,
        old_value=old_value.n3() if old_value is not None else None,
        new_value=new_value.n3() if new_value is not None else None,
        triples_before=triples_before,
        triples_after=triples_after,
    )


def _apply_operation(
    graph: Graph,
    operation: EditOperation,
    *,
    violation: ValidationViolation,
    source_text: str,
    schema: OntologySchema,
    fingerprint: str,
    operation_index: int,
) -> EditLogEntry:
    _validate_operation_scope(operation, violation, schema)
    subject = URIRef(operation.subject)
    predicate = URIRef(operation.predicate)
    _validate_subject_grounding(
        subject,
        graph=graph,
        violation=violation,
    )
    triples_before = len(graph)

    if isinstance(operation, AddTriple):
        obj = _object_term(operation.object)
        _validate_predicate_and_object(
            predicate,
            obj,
            schema=schema,
            graph=graph,
            violation=violation,
        )
        if isinstance(obj, Literal) and not _literal_is_source_grounded(
            obj,
            source_text,
        ):
            raise ApplyEditsError(
                f"Literal {str(obj)!r} is not grounded in the source text"
            )
        triple = (subject, predicate, obj)
        if triple in graph:
            raise ApplyEditsError("add_triple would be a no-op; triple already exists")
        graph.add(triple)
        return _log_entry(
            fingerprint=fingerprint,
            operation_index=operation_index,
            operation=operation,
            old_value=None,
            new_value=obj,
            triples_before=triples_before,
            triples_after=len(graph),
        )

    if isinstance(operation, RemoveTriple):
        obj = _object_term(operation.object)
        _validate_existing_triple_predicate(
            predicate,
            schema=schema,
            violation=violation,
        )
        triple = (subject, predicate, obj)
        if triple not in graph:
            raise ApplyEditsError(
                "remove_triple target does not exist in the graph"
            )
        graph.remove(triple)
        return _log_entry(
            fingerprint=fingerprint,
            operation_index=operation_index,
            operation=operation,
            old_value=obj,
            new_value=None,
            triples_before=triples_before,
            triples_after=len(graph),
        )

    if isinstance(operation, ReplaceLiteral):
        old_literal = _literal_term(operation.old_literal)
        new_literal = _literal_term(operation.new_literal)
        _validate_predicate_and_object(
            predicate,
            new_literal,
            schema=schema,
            graph=graph,
            violation=violation,
        )
        if not _literal_is_source_grounded(new_literal, source_text):
            raise ApplyEditsError(
                f"Replacement literal {str(new_literal)!r} is not grounded in the source text"
            )
        old_triple = (subject, predicate, old_literal)
        new_triple = (subject, predicate, new_literal)
        if old_triple not in graph:
            raise ApplyEditsError(
                "replace_literal old triple does not exist in the graph"
            )
        if new_triple in graph:
            raise ApplyEditsError(
                "replace_literal target triple already exists"
            )
        graph.remove(old_triple)
        graph.add(new_triple)
        return _log_entry(
            fingerprint=fingerprint,
            operation_index=operation_index,
            operation=operation,
            old_value=old_literal,
            new_value=new_literal,
            triples_before=triples_before,
            triples_after=len(graph),
        )

    raise ApplyEditsError(f"Unsupported edit operation: {type(operation).__name__}")


def apply_feedback_plan(
    graph: Graph,
    plan: FeedbackPlan,
    *,
    violations: tuple[ValidationViolation, ...],
    schema: OntologySchema,
    source_text: str,
) -> ApplyEditsResult:
    """Validate and atomically apply a structured feedback plan to a graph copy."""
    if not isinstance(graph, Graph):
        raise TypeError("graph must be an rdflib.Graph")
    if not source_text.strip():
        raise ApplyEditsError("source_text must not be empty")

    violations_by_fingerprint = {
        violation.fingerprint: violation for violation in violations
    }
    expected_fingerprints = set(violations_by_fingerprint)
    provided_fingerprints = {
        repair.violation_fingerprint for repair in plan.repairs
    }
    unknown = provided_fingerprints - expected_fingerprints
    missing = expected_fingerprints - provided_fingerprints
    if unknown:
        raise _fail(
            f"Feedback plan targets unknown violation fingerprint(s): {sorted(unknown)}"
        )
    if missing:
        raise _fail(
            f"Feedback plan is missing violation fingerprint(s): {sorted(missing)}"
        )

    working_graph = clone_graph(graph)
    edit_log: list[EditLogEntry] = []
    unresolved = []

    for repair in plan.repairs:
        violation = violations_by_fingerprint[repair.violation_fingerprint]
        if not repair.operations:
            unresolved.append(repair.violation_fingerprint)
            continue
        for operation_index, operation in enumerate(repair.operations):
            try:
                entry = _apply_operation(
                    working_graph,
                    operation,
                    violation=violation,
                    source_text=source_text,
                    schema=schema,
                    fingerprint=repair.violation_fingerprint,
                    operation_index=operation_index,
                )
            except ApplyEditsError as exc:
                raise _fail(
                    str(exc),
                    fingerprint=repair.violation_fingerprint,
                    operation_index=operation_index,
                ) from exc
            edit_log.append(entry)

    return ApplyEditsResult(
        graph=working_graph,
        edit_log=tuple(edit_log),
        unresolved_violation_fingerprints=tuple(sorted(unresolved)),
    )
