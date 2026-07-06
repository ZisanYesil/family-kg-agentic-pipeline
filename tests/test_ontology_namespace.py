from __future__ import annotations

import re
from pathlib import Path

import pytest
import rdflib
from rdflib import Graph, Namespace, URIRef
from rdflib.namespace import OWL, RDF, RDFS, XSD

PROJECT_ROOT = Path(__file__).resolve().parents[1]
ONTOLOGY_PATH = PROJECT_ROOT / "ontology" / "family_orig.owl"

FHKB_NAMESPACE_URI = "http://www.example.com/genealogy.owl#"
BASE_NAMESPACE_URI = "http://www.co-ode.org/roberts/family-tree.owl#"

FHKB = Namespace(FHKB_NAMESPACE_URI)
BASE = Namespace(BASE_NAMESPACE_URI)

STANDARD_PREDICATE_NAMESPACE_URIS = (
    str(RDF),
    str(RDFS),
    str(OWL),
    str(XSD),
)

PIPELINE_PATHS = [
    PROJECT_ROOT / "agents",
    PROJECT_ROOT / "api",
    PROJECT_ROOT / "core",
    PROJECT_ROOT / "storage",
    PROJECT_ROOT / "tasks",
    PROJECT_ROOT / "utils",
    PROJECT_ROOT / "celery_app.py",
]

NAMESPACE_ASSIGNMENT_RE = re.compile(
    r"(?P<name>[A-Za-z_][A-Za-z0-9_]*)\s*=\s*Namespace\(\s*['\"](?P<uri>[^'\"]+)['\"]\s*\)"
)
GRAPH_BIND_RE = re.compile(
    r"\.bind\(\s*['\"](?P<prefix>[^'\"]+)['\"]\s*,\s*(?:Namespace\(\s*)?['\"](?P<uri>[^'\"]+)['\"]"
)
HAS_BIRTH_YEAR_RE = re.compile(r"\b(?P<name>[A-Za-z_][A-Za-z0-9_]*)\s*\.\s*hasBirthYear\b")


def load_ontology_graph() -> Graph:
    assert ONTOLOGY_PATH.exists(), f"Ontology file not found: {ONTOLOGY_PATH}"
    return Graph().parse(ONTOLOGY_PATH, format="xml")


def iter_pipeline_python_files() -> list[Path]:
    files: list[Path] = []
    for path in PIPELINE_PATHS:
        if path.is_file() and path.suffix == ".py":
            files.append(path)
        elif path.is_dir():
            files.extend(sorted(path.rglob("*.py")))
    return sorted(files)


def line_number(text: str, offset: int) -> int:
    return text.count("\n", 0, offset) + 1


def test_has_birth_year_namespace_split_is_explicit() -> None:
    graph = load_ontology_graph()
    fhkb_has_birth_year = URIRef(str(FHKB.hasBirthYear))
    base_has_birth_year = URIRef(str(BASE.hasBirthYear))

    print("\nNamespace split check")
    print(f"  fhkb.hasBirthYear -> {fhkb_has_birth_year}")
    print(f"  base.hasBirthYear -> {base_has_birth_year}")

    assert str(fhkb_has_birth_year) != str(base_has_birth_year), (
        "fhkb:hasBirthYear and base:hasBirthYear must remain different URIRefs. "
        f"fhkb={fhkb_has_birth_year}, base={base_has_birth_year}"
    )
    assert (fhkb_has_birth_year, RDF.type, OWL.AnnotationProperty) in graph, (
        "Expected fhkb:hasBirthYear to be declared as owl:AnnotationProperty at "
        f"{fhkb_has_birth_year}"
    )
    assert (base_has_birth_year, RDF.type, RDFS.Datatype) in graph, (
        "Expected base:hasBirthYear to be present as a separate rdfs:Datatype at "
        f"{base_has_birth_year}"
    )


def test_ontology_namespace_health_check() -> None:
    graph = load_ontology_graph()
    namespaces = {prefix: str(namespace) for prefix, namespace in graph.namespaces()}
    counts = {
        "owl:AnnotationProperty": len(set(graph.subjects(RDF.type, OWL.AnnotationProperty))),
        "owl:ObjectProperty": len(set(graph.subjects(RDF.type, OWL.ObjectProperty))),
        "owl:Class": len(set(graph.subjects(RDF.type, OWL.Class))),
        "owl:NamedIndividual": len(set(graph.subjects(RDF.type, OWL.NamedIndividual))),
    }

    print("\nOntology namespace health check")
    print(f"  ontology path: {ONTOLOGY_PATH.relative_to(PROJECT_ROOT)}")
    print(f"  rdflib version: {rdflib.__version__}")
    print("  namespaces:")
    for prefix, namespace in sorted(namespaces.items()):
        display_prefix = prefix or "<default>"
        print(f"    {display_prefix}: {namespace}")
    print("  declaration counts:")
    for label, count in counts.items():
        print(f"    {label}: {count}")

    assert namespaces.get("fhkb") == FHKB_NAMESPACE_URI, (
        "Expected fhkb prefix to resolve to the genealogy vocabulary namespace. "
        f"Actual binding: {namespaces.get('fhkb')!r}"
    )
    assert counts["owl:AnnotationProperty"] >= 1, "Expected at least one owl:AnnotationProperty"
    assert counts["owl:ObjectProperty"] >= 1, "Expected at least one owl:ObjectProperty"
    assert counts["owl:Class"] >= 1, "Expected at least one owl:Class"
    assert counts["owl:NamedIndividual"] >= 1, "Expected at least one owl:NamedIndividual"


def test_pipeline_namespace_usage_does_not_mix_fhkb_and_base() -> None:
    files = iter_pipeline_python_files()
    assert files, "No pipeline Python files found to scan"

    namespace_bindings: dict[str, list[tuple[Path, int, str]]] = {}
    has_birth_year_references: list[tuple[Path, int, str, str]] = []
    failures: list[str] = []

    for path in files:
        text = path.read_text(encoding="utf-8")
        relative_path = path.relative_to(PROJECT_ROOT)

        for match in NAMESPACE_ASSIGNMENT_RE.finditer(text):
            name = match.group("name")
            uri = match.group("uri")
            lineno = line_number(text, match.start())
            namespace_bindings.setdefault(name, []).append((relative_path, lineno, uri))

        for match in GRAPH_BIND_RE.finditer(text):
            prefix = match.group("prefix")
            uri = match.group("uri")
            lineno = line_number(text, match.start())
            namespace_bindings.setdefault(prefix, []).append((relative_path, lineno, uri))

        for match in HAS_BIRTH_YEAR_RE.finditer(text):
            name = match.group("name")
            lineno = line_number(text, match.start())
            uri = None
            for _, _, bound_uri in namespace_bindings.get(name, []):
                uri = f"{bound_uri}hasBirthYear"
            has_birth_year_references.append(
                (relative_path, lineno, name, uri or "<unresolved namespace variable>")
            )

    for name, bindings in namespace_bindings.items():
        lower_name = name.lower()
        for relative_path, lineno, uri in bindings:
            if lower_name in {"fhkb", "genealogy"} and uri == BASE_NAMESPACE_URI:
                failures.append(
                    f"{relative_path}:{lineno} binds {name!r} to base namespace {uri}, "
                    f"but it should be {FHKB_NAMESPACE_URI}"
                )
            if lower_name in {"base", "family", "family_tree", "coode", "co_ode"} and uri == FHKB_NAMESPACE_URI:
                failures.append(
                    f"{relative_path}:{lineno} binds {name!r} to fhkb namespace {uri}; "
                    f"base namespace should remain {BASE_NAMESPACE_URI}"
                )

    print("\nPipeline namespace scan")
    print("  scanned files:")
    for path in files:
        print(f"    {path.relative_to(PROJECT_ROOT)}")

    if namespace_bindings:
        print("  namespace bindings:")
        for name, bindings in sorted(namespace_bindings.items()):
            for relative_path, lineno, uri in bindings:
                print(f"    {relative_path}:{lineno} {name} -> {uri}")
    else:
        print("  namespace bindings: none found")

    if has_birth_year_references:
        print("  hasBirthYear references:")
        for relative_path, lineno, name, resolved_uri in has_birth_year_references:
            print(f"    {relative_path}:{lineno} {name}.hasBirthYear -> {resolved_uri}")
    else:
        print("  hasBirthYear references: none found in pipeline code")

    assert not failures, "Namespace mix-up detected:\n" + "\n".join(failures)


def test_kg_builder_output_predicates_never_use_base_namespace() -> None:
    from tasks.pipeline_task import kg_builder_agent

    sample_extractions = {
        "entities": [
            {
                "id": "john_doe_1900",
                "type": "Person",
                "label": "John Doe",
                "birth_year": 1900,
                "death_year": 1970,
            },
            {
                "id": "jane_doe_1930",
                "type": "Person",
                "label": "Jane Doe",
                "birth_year": 1930,
            },
        ],
        "relations": [
            {
                "subject": "jane_doe_1930",
                "predicate": "hasFather",
                "object": "john_doe_1900",
            }
        ],
        "marriages": [],
    }

    turtle_graph = kg_builder_agent(sample_extractions)
    graph = Graph()
    try:
        graph.parse(data=turtle_graph, format="turtle")
    except Exception as exc:
        pytest.fail(
            "kg_builder_agent must return a valid Turtle serialization for sample extractions. "
            f"Returned value was: {turtle_graph!r}. Parser error: {exc}"
        )

    predicates = sorted({str(predicate) for _, predicate, _ in graph})
    co_ode_predicates = [predicate for predicate in predicates if predicate.startswith(BASE_NAMESPACE_URI)]
    invalid_predicates = [
        predicate
        for predicate in predicates
        if not (
            predicate.startswith(FHKB_NAMESPACE_URI)
            or predicate.startswith(STANDARD_PREDICATE_NAMESPACE_URIS)
        )
    ]

    print("\nKG builder predicate namespace check")
    print(f"  triple count: {len(graph)}")
    print("  predicates:")
    for predicate in predicates:
        print(f"    {predicate}")

    assert len(graph) > 0, "kg_builder_agent must produce a non-empty Turtle graph for sample extractions"
    assert not co_ode_predicates, (
        "kg_builder_agent produced predicates in the ontology xml:base namespace; "
        "all family vocabulary predicates must use fhkb instead:\n"
        + "\n".join(co_ode_predicates)
    )
    assert not invalid_predicates, (
        "kg_builder_agent produced predicates outside fhkb or standard RDF/RDFS/OWL/XSD namespaces:\n"
        + "\n".join(invalid_predicates)
    )
