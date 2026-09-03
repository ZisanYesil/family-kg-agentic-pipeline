from __future__ import annotations

from collections import Counter
from dataclasses import dataclass, field
from typing import Optional

import structlog
from rdflib import Graph, URIRef
from rdflib.namespace import OWL, RDF, RDFS, SKOS, XSD

logger = structlog.get_logger(__name__)

# Namespaces that are part of the RDF/OWL toolchain itself, never the domain
# ontology's own namespace. Used to pick the "real" namespace out of a parsed
# graph and to skip vocabulary terms when scanning for domain classes/properties.
_STANDARD_NAMESPACES = {
    str(RDF),
    str(RDFS),
    str(OWL),
    str(XSD),
    "http://www.w3.org/2004/02/skos/core#",
    "http://xmlns.com/foaf/0.1/",
}

# rdfs:range values for datatype properties, normalized to short type names the
# rest of the pipeline can reason about without needing to know XSD URIs.
_XSD_TYPE_NAMES = {
    str(XSD.integer): "integer",
    str(XSD.int): "integer",
    str(XSD.string): "string",
    str(XSD.boolean): "boolean",
    str(XSD.decimal): "decimal",
    str(XSD.float): "decimal",
    str(XSD.double): "decimal",
    str(XSD.date): "date",
    str(XSD.dateTime): "date",
    str(XSD.gYear): "gYear",
}


class OntologySchemaError(Exception):
    """Raised when an ontology file cannot be parsed into a usable schema."""


@dataclass(frozen=True)
class OntologyClass:
    local_name: str
    uri: str
    label: Optional[str] = None
    comment: Optional[str] = None


@dataclass(frozen=True)
class DatatypeProperty:
    local_name: str
    uri: str
    domain_class: Optional[str]  # local name of the class this attribute belongs to
    range_type: str  # normalized type name, e.g. "integer", "string"
    label: Optional[str] = None
    comment: Optional[str] = None
    # owl:FunctionalProperty: at most one value per subject (e.g. hasBirthYear). Used to
    # generate sh:maxCount 1 constraints; not propagated to/from an inverse since datatype
    # properties don't have an inverse direction.
    is_functional: bool = False


@dataclass(frozen=True)
class ObjectProperty:
    local_name: str
    uri: str
    domain_class: Optional[str]
    range_class: Optional[str]
    label: Optional[str] = None
    comment: Optional[str] = None
    inverse_of: Optional[str] = None
    direct_phrases: tuple[str, ...] = ()
    inverse_phrases: tuple[str, ...] = ()
    # owl:FunctionalProperty on THIS property's own URI, as declared in the file. Unlike
    # reasoner_derived/superproperty status, functional-ness is not propagated across an
    # inverse pair: it is a fact about this specific direction (e.g. hasFather is functional
    # because each person has at most one father, but its inverse isFatherOf is not, since a
    # father can have many children). Only meaningful for properties that survive into
    # `object_properties`; excluded/dropped inverse partners don't carry this forward.
    is_functional: bool = False


@dataclass(frozen=True)
class ExcludedObjectProperty:
    """An object property deliberately left out of `object_properties`, with
    the reason, so the exclusion is auditable instead of silent."""

    local_name: str
    uri: str
    reason: str  # "reasoner_derived" | "superproperty" | "inverse_duplicate"


@dataclass(frozen=True)
class OntologySchema:
    namespace: str
    classes: tuple[OntologyClass, ...]
    datatype_properties: tuple[DatatypeProperty, ...]
    # The final, LLM-ready predicate list: no reasoner-derived properties, no
    # superproperties, and exactly one direction per inverse pair.
    object_properties: tuple[ObjectProperty, ...]
    excluded_object_properties: tuple[ExcludedObjectProperty, ...] = ()
    # Transitive superclass closure keyed by local class name. Each set contains
    # the class itself so exact and inherited compatibility use one operation.
    superclasses_by_class: dict[str, frozenset[str]] = field(default_factory=dict)

    def class_by_name(self, local_name: str) -> Optional[OntologyClass]:
        for cls in self.classes:
            if cls.local_name == local_name:
                return cls
        return None

    def datatype_properties_for(self, class_local_name: str) -> tuple[DatatypeProperty, ...]:
        return tuple(
            prop
            for prop in self.datatype_properties
            if prop.domain_class is None or self.class_satisfies(class_local_name, prop.domain_class)
        )

    def class_satisfies(self, actual: Optional[str], expected: Optional[str]) -> bool:
        if expected is None:
            return True
        if actual is None:
            return False
        closure = self.superclasses_by_class or {}
        return expected in closure.get(actual, frozenset({actual}))


def _local_name(uri: URIRef) -> str:
    text = str(uri)
    if "#" in text:
        return text.rsplit("#", 1)[1]
    return text.rsplit("/", 1)[-1]


def _namespace_of(uri: URIRef) -> str:
    text = str(uri)
    if "#" in text:
        return text.rsplit("#", 1)[0] + "#"
    return text.rsplit("/", 1)[0] + "/"


def _infer_namespace(graph: Graph) -> str:
    """Pick the ontology's own namespace as the most common namespace among
    declared classes and properties, excluding standard RDF/OWL vocabularies."""
    declaration_types = (OWL.Class, OWL.ObjectProperty, OWL.DatatypeProperty, OWL.AnnotationProperty)
    counts: Counter[str] = Counter()
    for declaration_type in declaration_types:
        for subject in graph.subjects(RDF.type, declaration_type):
            if not isinstance(subject, URIRef):
                continue
            namespace = _namespace_of(subject)
            if namespace not in _STANDARD_NAMESPACES:
                counts[namespace] += 1

    if not counts:
        raise OntologySchemaError("Could not infer a domain namespace from the ontology file")

    return counts.most_common(1)[0][0]


def _comment_of(graph: Graph, subject: URIRef) -> Optional[str]:
    value = graph.value(subject, RDFS.comment)
    return str(value) if value is not None else None


def _label_of(graph: Graph, subject: URIRef) -> Optional[str]:
    value = graph.value(subject, RDFS.label)
    return str(value) if value is not None else None


def _has_exact_match(graph: Graph, subject: URIRef) -> bool:
    return graph.value(subject, SKOS.exactMatch) is not None


def _is_functional(graph: Graph, subject: URIRef) -> bool:
    return (subject, RDF.type, OWL.FunctionalProperty) in graph


def _class_local_name(graph: Graph, uri_value, namespace: str) -> Optional[str]:
    if not isinstance(uri_value, URIRef):
        return None
    if not str(uri_value).startswith(namespace):
        return None
    return _local_name(uri_value)


def _load_classes(graph: Graph, namespace: str) -> tuple[OntologyClass, ...]:
    classes: list[OntologyClass] = []
    seen: set[str] = set()
    for subject in graph.subjects(RDF.type, OWL.Class):
        if not isinstance(subject, URIRef) or not str(subject).startswith(namespace):
            continue
        local_name = _local_name(subject)
        if local_name in seen:
            continue
        seen.add(local_name)
        classes.append(
            OntologyClass(
                local_name=local_name,
                uri=str(subject),
                label=_label_of(graph, subject),
                comment=_comment_of(graph, subject),
            )
        )
    return tuple(sorted(classes, key=lambda c: c.local_name))


def _load_datatype_properties(graph: Graph, namespace: str) -> tuple[DatatypeProperty, ...]:
    properties: list[DatatypeProperty] = []
    seen: set[str] = set()
    # Annotation properties carry schema metadata for the agents; they are not
    # entity attributes and must never enter the extraction JSON schema.
    subjects = set(graph.subjects(RDF.type, OWL.DatatypeProperty))
    for subject in subjects:
        if not isinstance(subject, URIRef) or not str(subject).startswith(namespace):
            continue
        local_name = _local_name(subject)
        if local_name in seen:
            continue
        seen.add(local_name)

        domain_class = _class_local_name(graph, graph.value(subject, RDFS.domain), namespace)
        range_value = graph.value(subject, RDFS.range)
        range_type = _XSD_TYPE_NAMES.get(str(range_value), "string") if range_value is not None else "string"
        comment = _comment_of(graph, subject)
        # This ontology intentionally uses rdfs:Literal for date-or-year values.
        # Preserve their semantic family so the builder can choose xsd:date or
        # xsd:gYear from the lexical precision.
        if range_value == RDFS.Literal and (
            (comment and ("xsd:date" in comment or "xsd:gYear" in comment))
            or local_name.lower().endswith("date")
            or local_name.lower().endswith("inception")
        ):
            range_type = "date_or_year"

        properties.append(
            DatatypeProperty(
                local_name=local_name,
                uri=str(subject),
                domain_class=domain_class,
                range_type=range_type,
                label=_label_of(graph, subject),
                comment=comment,
                is_functional=_is_functional(graph, subject),
            )
        )
    return tuple(sorted(properties, key=lambda p: p.local_name))


def _is_reasoner_derived(graph: Graph, subject: URIRef) -> bool:
    has_chain_axiom = (subject, OWL.propertyChainAxiom, None) in graph
    is_transitive = (subject, RDF.type, OWL.TransitiveProperty) in graph
    return has_chain_axiom or is_transitive


def _build_inverse_map(graph: Graph, namespace: str) -> dict[str, str]:
    """Symmetric local_name -> local_name map from owl:inverseOf triples, since
    the file may only assert the pair in one direction."""
    inverse_map: dict[str, str] = {}
    for subject, obj in graph.subject_objects(OWL.inverseOf):
        if not (isinstance(subject, URIRef) and isinstance(obj, URIRef)):
            continue
        if not (str(subject).startswith(namespace) and str(obj).startswith(namespace)):
            continue
        subject_name, object_name = _local_name(subject), _local_name(obj)
        inverse_map[subject_name] = object_name
        inverse_map[object_name] = subject_name
    return inverse_map


def _build_superproperty_names(graph: Graph, namespace: str) -> set[str]:
    """Local names that appear as the *target* of some rdfs:subPropertyOf
    triple, i.e. properties that are a generalization of a more specific one."""
    superproperties: set[str] = set()
    for _subject, obj in graph.subject_objects(RDFS.subPropertyOf):
        if isinstance(obj, URIRef) and str(obj).startswith(namespace):
            superproperties.add(_local_name(obj))
    return superproperties


def _load_object_properties(
    graph: Graph, namespace: str
) -> tuple[tuple[ObjectProperty, ...], tuple[ExcludedObjectProperty, ...]]:
    inverse_map = _build_inverse_map(graph, namespace)
    superproperty_names = _build_superproperty_names(graph, namespace)
    direct_phrase = URIRef(namespace + "directPhrase")
    inverse_phrase = URIRef(namespace + "inversePhrase")

    raw: dict[str, ObjectProperty] = {}
    reasoner_derived_names: set[str] = set()
    for subject in graph.subjects(RDF.type, OWL.ObjectProperty):
        if not isinstance(subject, URIRef) or not str(subject).startswith(namespace):
            continue
        local_name = _local_name(subject)
        if local_name in raw:
            continue

        domain_class = _class_local_name(graph, graph.value(subject, RDFS.domain), namespace)
        range_class = _class_local_name(graph, graph.value(subject, RDFS.range), namespace)
        raw[local_name] = ObjectProperty(
            local_name=local_name,
            uri=str(subject),
            domain_class=domain_class,
            range_class=range_class,
            label=_label_of(graph, subject),
            comment=_comment_of(graph, subject),
            inverse_of=inverse_map.get(local_name),
            direct_phrases=tuple(sorted(str(value) for value in graph.objects(subject, direct_phrase))),
            inverse_phrases=tuple(sorted(str(value) for value in graph.objects(subject, inverse_phrase))),
            is_functional=_is_functional(graph, subject),
        )
        if _is_reasoner_derived(graph, subject):
            reasoner_derived_names.add(local_name)

    # Fill in missing domain/range from the inverse partner (domain(P) =
    # range(inverse(P)), range(P) = domain(inverse(P))): the file often only
    # declares the constraint on one direction of a pair, e.g. isBrotherOf
    # carries domain=Man/range=Person but its inverse hasBrother carries neither.
    for local_name, prop in list(raw.items()):
        partner_name = prop.inverse_of
        if partner_name is None or partner_name not in raw:
            continue
        partner = raw[partner_name]
        if prop.domain_class is None and partner.range_class is not None:
            prop = ObjectProperty(**{**prop.__dict__, "domain_class": partner.range_class})
        if prop.range_class is None and partner.domain_class is not None:
            prop = ObjectProperty(**{**prop.__dict__, "range_class": partner.domain_class})
        raw[local_name] = prop

    # A property's inverse is equally unsuitable for direct assertion even if
    # only one direction carries the propertyChainAxiom/TransitiveProperty
    # marker in the file (e.g. hasHusband is marked but isHusbandOf is not).
    for name in list(reasoner_derived_names):
        partner_name = raw[name].inverse_of
        if partner_name is not None:
            reasoner_derived_names.add(partner_name)

    assertable: list[ObjectProperty] = []
    excluded: list[ExcludedObjectProperty] = []
    resolved_inverse_pairs: set[frozenset[str]] = set()

    for local_name, prop in raw.items():
        if local_name in reasoner_derived_names:
            excluded.append(ExcludedObjectProperty(local_name, prop.uri, "reasoner_derived"))
            continue
        # A superproperty can still be a source predicate in its own right
        # (P17 country, P170 creator, P1066 student of). Only abstract
        # superproperties without an external exact match are inference-only.
        subject_uri = URIRef(prop.uri)
        if local_name in superproperty_names and not _has_exact_match(graph, subject_uri):
            excluded.append(ExcludedObjectProperty(local_name, prop.uri, "superproperty"))
            continue

        partner_name = prop.inverse_of
        if partner_name and partner_name in raw and partner_name not in superproperty_names:
            pair_key = frozenset({local_name, partner_name})
            if pair_key in resolved_inverse_pairs:
                continue
            resolved_inverse_pairs.add(pair_key)

            partner = raw[partner_name]
            # Prefer the "hasX" direction over "isXOf"/"isXIn" as the canonical
            # one offered to the model; fall back to alphabetical for ties so
            # the choice is deterministic.
            local_is_has = local_name.lower().startswith("has")
            partner_is_has = partner_name.lower().startswith("has")
            if local_is_has and not partner_is_has:
                keep, drop = prop, partner
            elif partner_is_has and not local_is_has:
                keep, drop = partner, prop
            else:
                keep, drop = (prop, partner) if local_name < partner_name else (partner, prop)

            assertable.append(keep)
            excluded.append(ExcludedObjectProperty(drop.local_name, drop.uri, "inverse_duplicate"))
            continue

        assertable.append(prop)

    assertable.sort(key=lambda p: p.local_name)
    excluded.sort(key=lambda e: e.local_name)
    return tuple(assertable), tuple(excluded)


def _build_superclass_closure(graph: Graph, namespace: str, classes: tuple[OntologyClass, ...]) -> dict[str, frozenset[str]]:
    direct: dict[str, set[str]] = {cls.local_name: set() for cls in classes}
    for child, parent in graph.subject_objects(RDFS.subClassOf):
        child_name = _class_local_name(graph, child, namespace)
        parent_name = _class_local_name(graph, parent, namespace)
        if child_name in direct and parent_name is not None:
            direct[child_name].add(parent_name)

    closure: dict[str, frozenset[str]] = {}
    for class_name in direct:
        seen = {class_name}
        pending = list(direct[class_name])
        while pending:
            current = pending.pop()
            if current in seen:
                continue
            seen.add(current)
            pending.extend(direct.get(current, ()))
        closure[class_name] = frozenset(seen)
    return closure


def load_ontology_schema(path: str, *, format: str = "turtle") -> OntologySchema:
    """Parse an OWL/TTL ontology file into an ontology-agnostic OntologySchema.

    Works for any ontology, not just the family ontology: the namespace, classes,
    and properties are all discovered from the file itself rather than hardcoded.
    """
    graph = Graph()
    try:
        graph.parse(path, format=format)
    except Exception as exc:  # rdflib raises a variety of parser-specific errors
        raise OntologySchemaError(f"Failed to parse ontology file {path!r}: {exc}") from exc

    try:
        namespace = _infer_namespace(graph)
        classes = _load_classes(graph, namespace)
        datatype_properties = _load_datatype_properties(graph, namespace)
        object_properties, excluded_object_properties = _load_object_properties(graph, namespace)
        superclasses_by_class = _build_superclass_closure(graph, namespace, classes)
    except OntologySchemaError:
        raise
    except Exception as exc:
        raise OntologySchemaError(f"Failed to build schema from {path!r}: {exc}") from exc

    logger.info(
        "ontology_schema_loaded",
        namespace=namespace,
        class_count=len(classes),
        datatype_property_count=len(datatype_properties),
        object_property_count=len(object_properties),
        excluded_object_property_count=len(excluded_object_properties),
    )

    return OntologySchema(
        namespace=namespace,
        classes=classes,
        datatype_properties=datatype_properties,
        object_properties=object_properties,
        excluded_object_properties=excluded_object_properties,
        superclasses_by_class=superclasses_by_class,
    )
