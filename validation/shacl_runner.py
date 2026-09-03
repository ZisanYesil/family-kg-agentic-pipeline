from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path
from typing import Optional

import structlog
from pyshacl import validate
from rdflib import BNode, Graph, Literal, URIRef
from rdflib.namespace import OWL, RDF, RDFS, SH, XSD
from rdflib.term import Identifier

from ontology.schema_loader import OntologySchema
from validation.models import (
    ValidationResult,
    ValidationViolation,
    ViolationKind,
    ViolationSeverity,
    ViolationSource,
)
from validation.shacl_generator import generate_shacl_graph

logger = structlog.get_logger(__name__)

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATASET_ONTOLOGY_NAMESPACE = "http://example.org/2wiki-ontology#"

# Supplements are selected by the ontology's semantic namespace, never by a
# user-controlled ontology filename. Unregistered ontologies intentionally use only the
# generated structural shapes.
HAND_WRITTEN_SHAPES_BY_NAMESPACE: Mapping[str, Path] = {
    DATASET_ONTOLOGY_NAMESPACE: PROJECT_ROOT / "ontology" / "SHACL_shapes.ttl",
}

_SEVERITY_BY_URI = {
    SH.Violation: ViolationSeverity.VIOLATION,
    SH.Warning: ViolationSeverity.WARNING,
    SH.Info: ViolationSeverity.INFO,
}

_EXPECTED_CONSTRAINTS = (
    SH.datatype,
    SH["class"],
    SH.maxCount,
    SH.minCount,
    SH.hasValue,
    SH.node,
)


class ShaclRunnerError(Exception):
    """Raised when SHACL shapes cannot be loaded or validation cannot be executed."""


def _copy_graph(source: Graph, target: Graph) -> None:
    for prefix, namespace in source.namespaces():
        target.bind(prefix, namespace)
    for triple in source:
        target.add(triple)


def build_ontology_graph(schema: OntologySchema) -> Graph:
    """Reconstruct the ontology statements needed by pySHACL's RDFS inference."""
    graph = Graph()
    classes_by_name = {item.local_name: URIRef(item.uri) for item in schema.classes}

    for class_uri in classes_by_name.values():
        graph.add((class_uri, RDF.type, OWL.Class))
    for child, superclasses in schema.superclasses_by_class.items():
        child_uri = classes_by_name.get(child)
        if child_uri is None:
            continue

        for parent in superclasses:
            if child == parent:
                continue

            parent_uri = classes_by_name.get(parent)
            if parent_uri is not None:
                graph.add((child_uri, RDFS.subClassOf, parent_uri))

    datatype_uris = {
        "integer": XSD.integer,
        "string": XSD.string,
        "boolean": XSD.boolean,
        "decimal": XSD.decimal,
        "date": XSD.date,
        "year": XSD.gYear,
    }
    for prop in schema.datatype_properties:
        prop_uri = URIRef(prop.uri)
        graph.add((prop_uri, RDF.type, OWL.DatatypeProperty))
        if prop.domain_class in classes_by_name:
            graph.add((prop_uri, RDFS.domain, classes_by_name[prop.domain_class]))
        range_uri = datatype_uris.get(prop.range_type)
        if range_uri is not None:
            graph.add((prop_uri, RDFS.range, range_uri))

    for prop in schema.object_properties:
        prop_uri = URIRef(prop.uri)
        graph.add((prop_uri, RDF.type, OWL.ObjectProperty))
        if prop.domain_class in classes_by_name:
            graph.add((prop_uri, RDFS.domain, classes_by_name[prop.domain_class]))
        if prop.range_class in classes_by_name:
            graph.add((prop_uri, RDFS.range, classes_by_name[prop.range_class]))

    return graph


def build_shacl_graph(
    schema: OntologySchema,
    *,
    supplement_registry: Optional[Mapping[str, Path]] = None,
) -> Graph:
    """Build dynamic structural shapes and merge a namespace-registered supplement."""
    shapes_graph = generate_shacl_graph(schema)
    registry = (
        HAND_WRITTEN_SHAPES_BY_NAMESPACE
        if supplement_registry is None
        else supplement_registry
    )
    supplement_path = registry.get(schema.namespace)
    if supplement_path is None:
        logger.info(
            "shacl_supplement_not_registered",
            ontology_namespace=schema.namespace,
        )
        return shapes_graph

    path = Path(supplement_path)
    try:
        supplement = Graph().parse(path, format="turtle")
    except Exception as exc:
        raise ShaclRunnerError(
            f"Failed to parse SHACL supplement {str(path)!r}: {exc}"
        ) from exc

    _copy_graph(supplement, shapes_graph)
    logger.info(
        "shacl_supplement_loaded",
        ontology_namespace=schema.namespace,
        supplement_path=str(path),
        supplement_triple_count=len(supplement),
    )
    return shapes_graph


def _term_text(term: Optional[Identifier]) -> Optional[str]:
    if term is None:
        return None
    if isinstance(term, Literal):
        return str(term)
    if isinstance(term, URIRef):
        return str(term)
    if isinstance(term, BNode):
        # Generated/family paths and focus nodes are URIRefs. Keeping blank-node values
        # explicit is safer than silently dropping context, even though their identifiers
        # are only scoped to this report graph.
        return term.n3()
    return str(term)


def _message_for(results_graph: Graph, result_node: Identifier) -> str:
    messages = sorted(
        {
            str(message)
            for message in results_graph.objects(result_node, SH.resultMessage)
        }
    )
    if messages:
        return " | ".join(messages)
    return "SHACL validation constraint was not satisfied."


def _expected_for(
    results_graph: Graph,
    result_node: Identifier,
    shapes_graph: Optional[Graph],
) -> Optional[str]:
    source_shape = results_graph.value(result_node, SH.sourceShape)
    if source_shape is None:
        return None

    definition_graph = shapes_graph if shapes_graph is not None else results_graph
    expectations: list[str] = []
    for predicate in _EXPECTED_CONSTRAINTS:
        for value in definition_graph.objects(source_shape, predicate):
            text = _term_text(value)
            if text is not None:
                expectations.append(f"{_term_text(predicate)}={text}")
    return "; ".join(sorted(expectations)) or None


def _severity_for(
    results_graph: Graph,
    result_node: Identifier,
) -> ViolationSeverity:
    severity = results_graph.value(result_node, SH.resultSeverity)
    if severity is None:
        return ViolationSeverity.VIOLATION
    normalized = _SEVERITY_BY_URI.get(severity)
    if normalized is None:
        logger.warning(
            "unknown_shacl_result_severity",
            result_node=_term_text(result_node),
            severity=_term_text(severity),
        )
        return ViolationSeverity.VIOLATION
    return normalized


def normalize_shacl_report(
    results_graph: Graph,
    *,
    shapes_graph: Optional[Graph] = None,
) -> ValidationResult:
    """Normalize a pySHACL RDF report into deterministic pipeline violations."""
    result_nodes = set(results_graph.subjects(RDF.type, SH.ValidationResult))
    # A conforming report has no sh:ValidationResult nodes. A non-conforming report may
    # expose them through sh:result without explicitly typing them, so include both forms.
    result_nodes.update(results_graph.objects(None, SH.result))

    violations = []
    for result_node in result_nodes:
        violations.append(
            ValidationViolation(
                kind=ViolationKind.SHACL,
                source=ViolationSource.SHACL_GENERATOR,
                focus_node=_term_text(
                    results_graph.value(result_node, SH.focusNode)
                ),
                path=_term_text(results_graph.value(result_node, SH.resultPath)),
                value=_term_text(results_graph.value(result_node, SH.value)),
                expected=_expected_for(results_graph, result_node, shapes_graph),
                message=_message_for(results_graph, result_node),
                severity=_severity_for(results_graph, result_node),
                constraint_component=_term_text(
                    results_graph.value(
                        result_node,
                        SH.sourceConstraintComponent,
                    )
                ),
            )
        )
    return ValidationResult(violations=tuple(violations))


def run_shacl_validation(
    data_graph: Graph,
    schema: OntologySchema,
    *,
    supplement_registry: Optional[Mapping[str, Path]] = None,
) -> ValidationResult:
    """Validate an RDF data graph against generated and registered SHACL shapes."""
    if not isinstance(data_graph, Graph):
        raise TypeError("data_graph must be an rdflib.Graph")

    shapes_graph = build_shacl_graph(
        schema,
        supplement_registry=supplement_registry,
    )
    ontology_graph = build_ontology_graph(schema)
    try:
        conforms, results_graph, _results_text = validate(
            data_graph=data_graph,
            shacl_graph=shapes_graph,
            ont_graph=ontology_graph,
            inference="rdfs",
            advanced=True,
            inplace=False,
            abort_on_first=False,
            allow_infos=True,
            allow_warnings=True,
        )
    except Exception as exc:
        raise ShaclRunnerError(f"SHACL validation failed: {exc}") from exc

    if not isinstance(results_graph, Graph):
        raise ShaclRunnerError(
            f"SHACL validation did not return an RDF report graph: {results_graph}"
        )

    result = normalize_shacl_report(results_graph, shapes_graph=shapes_graph)
    if bool(conforms) != result.conforms:
        raise ShaclRunnerError(
            "pySHACL conformance flag disagrees with the normalized validation report"
        )

    logger.info(
        "shacl_validation_completed",
        ontology_namespace=schema.namespace,
        data_triple_count=len(data_graph),
        shape_triple_count=len(shapes_graph),
        violation_count=len(result.violations),
        conforms=result.conforms,
    )
    return result
