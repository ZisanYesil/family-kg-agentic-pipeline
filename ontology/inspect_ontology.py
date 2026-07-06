from __future__ import annotations

import sys
import traceback
from pathlib import Path
from typing import Iterable, Sequence

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

import structlog
from owlready2 import (
    And,
    FunctionalProperty,
    InverseFunctionalProperty,
    Or,
    Restriction,
    SymmetricProperty,
    ThingClass,
    TransitiveProperty,
    get_ontology,
)
from rdflib import Graph

from core.logging_config import configure_logging

ONTOLOGY_PATH = Path(__file__).resolve().parent / "family_orig.owl"
SUMMARY_PATH = Path(__file__).resolve().parent / "ontology_summary.md"

RESTRICTION_TYPES = {
    24: "someValuesFrom",
    25: "allValuesFrom",
    26: "cardinality",
    27: "minCardinality",
    28: "maxCardinality",
    29: "hasValue",
    30: "qualifiedCardinality",
    31: "minQualifiedCardinality",
    32: "maxQualifiedCardinality",
}


def entity_name(entity: object) -> str:
    return getattr(entity, "name", str(entity))


def entity_iri(entity: object) -> str:
    return getattr(entity, "iri", str(entity))


def format_entity(entity: object) -> str:
    return f"{entity_name(entity)} (`{entity_iri(entity)}`)"


def format_list(items: Iterable[object]) -> str:
    values = list(items)
    if not values:
        return "_None_"
    return ", ".join(format_entity(item) for item in values)


def is_named_entity(value: object) -> bool:
    return hasattr(value, "iri") and hasattr(value, "name")


def is_restriction(value: object) -> bool:
    return isinstance(value, Restriction)


def property_has_characteristic(prop: object, characteristic: type) -> bool:
    return any(item is characteristic for item in getattr(prop, "is_a", []))


def format_characteristics(prop: object) -> str:
    checks = [
        ("functional", FunctionalProperty),
        ("inverse_functional", InverseFunctionalProperty),
        ("symmetric", SymmetricProperty),
        ("transitive", TransitiveProperty),
    ]
    values = [name for name, cls in checks if property_has_characteristic(prop, cls)]
    return ", ".join(values) if values else "_None_"


def format_inverse_property(prop: object) -> str:
    inverse = getattr(prop, "inverse_property", None)
    if not inverse:
        return "_None_"
    return format_entity(inverse)


def direct_superclasses(cls: object) -> list[object]:
    return [
        item
        for item in getattr(cls, "is_a", [])
        if is_named_entity(item) and not is_restriction(item)
    ]


def restriction_type_name(restriction: Restriction) -> str:
    return RESTRICTION_TYPES.get(getattr(restriction, "type", None), str(restriction.type))


def describe_restriction(restriction: Restriction) -> str:
    parts = [
        f"property={format_entity(restriction.property)}",
        f"type={restriction_type_name(restriction)}",
    ]
    if getattr(restriction, "value", None) is not None:
        value = restriction.value
        parts.append(f"value={format_entity(value) if is_named_entity(value) else value}")
    if getattr(restriction, "cardinality", None) is not None:
        parts.append(f"cardinality={restriction.cardinality}")
    return "; ".join(parts)


def walk_restrictions(value: object) -> Iterable[Restriction]:
    if is_restriction(value):
        yield value
        return

    if isinstance(value, (And, Or)):
        for nested in value.Classes:
            yield from walk_restrictions(nested)


def collect_class_restrictions(cls: object) -> list[tuple[str, Restriction]]:
    restrictions: list[tuple[str, Restriction]] = []
    for item in getattr(cls, "is_a", []):
        for restriction in walk_restrictions(item):
            restrictions.append(("is_a", restriction))
    for item in getattr(cls, "equivalent_to", []):
        for restriction in walk_restrictions(item):
            restrictions.append(("equivalent_to", restriction))
    return restrictions


def render_classes(classes: Sequence[object]) -> list[str]:
    lines = ["## Classes", ""]
    for cls in classes:
        lines.extend(
            [
                f"### {entity_name(cls)}",
                f"- IRI: `{entity_iri(cls)}`",
                f"- Superclasses: {format_list(direct_superclasses(cls))}",
                "",
            ]
        )
    return lines


def render_object_properties(properties: Sequence[object]) -> list[str]:
    lines = ["## Object Properties", ""]
    for prop in properties:
        lines.extend(
            [
                f"### {entity_name(prop)}",
                f"- IRI: `{entity_iri(prop)}`",
                f"- Domain: {format_list(getattr(prop, 'domain', []))}",
                f"- Range: {format_list(getattr(prop, 'range', []))}",
                f"- Inverse property: {format_inverse_property(prop)}",
                f"- Characteristics: {format_characteristics(prop)}",
                "",
            ]
        )
    return lines


def render_data_properties(properties: Sequence[object]) -> list[str]:
    lines = ["## Data Properties", ""]
    if not properties:
        lines.extend(["_No data properties declared._", ""])
        return lines

    for prop in properties:
        lines.extend(
            [
                f"### {entity_name(prop)}",
                f"- IRI: `{entity_iri(prop)}`",
                f"- Domain: {format_list(getattr(prop, 'domain', []))}",
                f"- Range: {format_list(getattr(prop, 'range', []))}",
                "",
            ]
        )
    return lines


def render_restrictions(classes: Sequence[object]) -> list[str]:
    lines = ["## Restrictions", ""]
    found = False
    for cls in classes:
        restrictions = collect_class_restrictions(cls)
        if not restrictions:
            continue
        found = True
        lines.extend([f"### {entity_name(cls)}", f"- Class IRI: `{entity_iri(cls)}`"])
        for source, restriction in restrictions:
            lines.append(f"- Source: `{source}`; {describe_restriction(restriction)}")
        lines.append("")

    if not found:
        lines.extend(["_No class restrictions found._", ""])
    return lines


def render_disjoints(disjoints: Sequence[object]) -> list[str]:
    lines = ["## Disjoint Classes", ""]
    class_disjoints = [
        disjoint
        for disjoint in disjoints
        if all(isinstance(entity, ThingClass) for entity in getattr(disjoint, "entities", []))
    ]
    if not class_disjoints:
        lines.extend(["_No disjoint class declarations found._", ""])
        return lines

    for disjoint in class_disjoints:
        lines.append(f"- {format_list(disjoint.entities)}")
    lines.append("")
    return lines


def build_summary(ontology: object) -> str:
    classes = sorted(list(ontology.classes()), key=entity_iri)
    object_properties = sorted(list(ontology.object_properties()), key=entity_iri)
    data_properties = sorted(list(ontology.data_properties()), key=entity_iri)
    disjoints = list(ontology.disjoints())

    lines = [
        "# Ontology Summary",
        "",
        f"- Source: `{ONTOLOGY_PATH.relative_to(PROJECT_ROOT)}`",
        f"- Base IRI: `{ontology.base_iri}`",
        "",
    ]
    lines.extend(render_classes(classes))
    lines.extend(render_object_properties(object_properties))
    lines.extend(render_data_properties(data_properties))
    lines.extend(render_restrictions(classes))
    lines.extend(render_disjoints(disjoints))
    return "\n".join(lines).rstrip() + "\n"


def diagnose_with_rdflib(logger: structlog.stdlib.BoundLogger) -> None:
    graph = Graph()
    try:
        graph.parse(ONTOLOGY_PATH, format="xml")
    except Exception as exc:
        logger.error("rdflib_parse_failed", error=str(exc), exc_info=True)
        print("\nrdflib parse failed with this error:")
        traceback.print_exception(type(exc), exc, exc.__traceback__)
        return

    logger.info("rdflib_parse_succeeded", triples=len(graph))
    print(f"\nrdflib parse succeeded. Parsed {len(graph)} RDF triples.")


def main() -> int:
    configure_logging()
    logger = structlog.get_logger(__name__)

    try:
        ontology = get_ontology(str(ONTOLOGY_PATH)).load()
    except Exception as exc:
        logger.error("owlready2_load_failed", error=str(exc), exc_info=True)
        print("owlready2 load failed with this error:")
        traceback.print_exception(type(exc), exc, exc.__traceback__)
        diagnose_with_rdflib(logger)
        return 1

    classes = list(ontology.classes())
    object_properties = list(ontology.object_properties())
    data_properties = list(ontology.data_properties())
    disjoints = list(ontology.disjoints())

    logger.info(
        "ontology_loaded",
        classes=len(classes),
        object_properties=len(object_properties),
        data_properties=len(data_properties),
        disjoints=len(disjoints),
    )

    summary = build_summary(ontology)
    SUMMARY_PATH.write_text(summary, encoding="utf-8")
    print(summary)
    logger.info("ontology_summary_written", path=str(SUMMARY_PATH))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
