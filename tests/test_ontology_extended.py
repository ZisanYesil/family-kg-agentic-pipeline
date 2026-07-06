from __future__ import annotations

from pathlib import Path

import pytest
from rdflib import Graph, Namespace
from rdflib.namespace import OWL, RDF, RDFS, XSD

from utils.rdf import load_family_ontology_graph

PROJECT_ROOT = Path(__file__).resolve().parents[1]
ORIGINAL_ONTOLOGY_PATH = PROJECT_ROOT / "ontology" / "family_orig.owl"
EXTENDED_ONTOLOGY_PATH = PROJECT_ROOT / "ontology" / "family_extended.ttl"

FHKB = Namespace("http://www.example.com/genealogy.owl#")

REDECLARED_DATATYPE_PROPERTIES = (
    FHKB.hasBirthYear,
    FHKB.hasDeathYear,
    FHKB.hasMarriageYear,
)

NAMING_ANNOTATION_PROPERTIES = (
    FHKB.knownAs,
    FHKB.alsoKnownAs,
    FHKB.formerlyKnownAs,
)


def load_extended_graph() -> Graph:
    return load_family_ontology_graph()


def load_original_graph() -> Graph:
    return Graph().parse(ORIGINAL_ONTOLOGY_PATH, format="xml")


def format_uri_list(values: set[object]) -> str:
    return "\n".join(f"  - {value}" for value in sorted(str(value) for value in values))


def test_family_extended_turtle_is_merged_artifact_without_imports() -> None:
    graph = Graph().parse(EXTENDED_ONTOLOGY_PATH, format="turtle")
    imports = {str(imported) for imported in graph.objects(None, OWL.imports)}
    classes = set(graph.subjects(RDF.type, OWL.Class))
    individuals = set(graph.subjects(RDF.type, OWL.NamedIndividual))

    print("\nfamily_extended.ttl merge artifact check")
    print(f"  triples: {len(graph)}")
    print(f"  owl:imports declarations: {sorted(imports)}")
    print(f"  owl:Class count: {len(classes)}")
    print(f"  owl:NamedIndividual count: {len(individuals)}")

    assert not imports, (
        "Merged family_extended.ttl must not contain owl:imports. If an import-based "
        "artifact is introduced later, it should import the ontology IRI, not a relative file path."
    )
    assert len(classes) >= 14, "Merged family_extended.ttl should include classes from family_orig.owl"
    assert len(individuals) >= 508, "Merged family_extended.ttl should include individuals from family_orig.owl"


def test_pipeline_loader_uses_merged_extended_ontology_only() -> None:
    direct_graph = Graph().parse(EXTENDED_ONTOLOGY_PATH, format="turtle")
    loaded_graph = load_extended_graph()

    direct_classes = set(direct_graph.subjects(RDF.type, OWL.Class))
    loaded_classes = set(loaded_graph.subjects(RDF.type, OWL.Class))
    direct_individuals = set(direct_graph.subjects(RDF.type, OWL.NamedIndividual))
    loaded_individuals = set(loaded_graph.subjects(RDF.type, OWL.NamedIndividual))

    print("\npipeline merged ontology loader")
    print(f"  direct merged triples: {len(direct_graph)}")
    print(f"  loader triples: {len(loaded_graph)}")
    print(f"  direct owl:Class count: {len(direct_classes)}")
    print(f"  loader owl:Class count: {len(loaded_classes)}")
    print(f"  direct owl:NamedIndividual count: {len(direct_individuals)}")
    print(f"  loader owl:NamedIndividual count: {len(loaded_individuals)}")

    assert len(loaded_graph) == len(direct_graph)
    assert len(loaded_classes) == len(direct_classes)
    assert len(loaded_individuals) == len(direct_individuals)
    assert FHKB.Person in loaded_classes
    assert FHKB.Marriage in loaded_classes


def test_extended_ontology_preserves_all_named_individuals_and_subject_triples() -> None:
    original_graph = load_original_graph()
    extended_graph = Graph().parse(EXTENDED_ONTOLOGY_PATH, format="turtle")

    original_individuals = set(original_graph.subjects(RDF.type, OWL.NamedIndividual))
    extended_individuals = set(extended_graph.subjects(RDF.type, OWL.NamedIndividual))
    missing_individuals = original_individuals - extended_individuals
    extra_individuals = extended_individuals - original_individuals

    partial_data_loss = []
    for individual in sorted(original_individuals & extended_individuals, key=str):
        original_triple_count = len(list(original_graph.triples((individual, None, None))))
        extended_triple_count = len(list(extended_graph.triples((individual, None, None))))
        if original_triple_count != extended_triple_count:
            partial_data_loss.append(
                (individual, original_triple_count, extended_triple_count)
            )

    print("\nNamed individual preservation check")
    print(f"  original individual count: {len(original_individuals)}")
    print(f"  extended individual count: {len(extended_individuals)}")
    print(f"  missing individual count: {len(missing_individuals)}")
    if missing_individuals:
        print("  missing individuals:")
        print(format_uri_list(missing_individuals))
    print(f"  extra individual count: {len(extra_individuals)}")
    if extra_individuals:
        print("  extra individuals:")
        print(format_uri_list(extra_individuals))
    print(f"  partial data loss count: {len(partial_data_loss)}")
    if partial_data_loss:
        print("  partial data loss:")
        for individual, original_count, extended_count in partial_data_loss:
            print(f"  - {individual}: original={original_count}, extended={extended_count}")

    assert not missing_individuals, (
        "family_extended.ttl is missing owl:NamedIndividual subjects from family_orig.owl:\n"
        + format_uri_list(missing_individuals)
    )
    assert not partial_data_loss, (
        "family_extended.ttl changed subject triple counts for existing individuals:\n"
        + "\n".join(
            f"  - {individual}: original={original_count}, extended={extended_count}"
            for individual, original_count, extended_count in partial_data_loss
        )
    )


def test_jack_william_usher_facts_are_preserved_in_extended_ontology() -> None:
    graph = Graph().parse(EXTENDED_ONTOLOGY_PATH, format="turtle")
    jack = FHKB.jack_william_usher_1999

    birth_year_objects = sorted(str(value) for value in graph.objects(jack, FHKB.hasBirthYear))
    son_of_objects = sorted(str(value) for value in graph.objects(jack, FHKB.isSonOf))

    print("\nManual individual fact check")
    print(f"  individual: {jack}")
    print(f"  hasBirthYear objects: {birth_year_objects}")
    print(f"  isSonOf objects: {son_of_objects}")

    assert (jack, FHKB.hasBirthYear, None) in graph, (
        f"{jack} must retain an fhkb:hasBirthYear triple in family_extended.ttl"
    )
    assert (jack, FHKB.isSonOf, None) in graph, (
        f"{jack} must retain an fhkb:isSonOf triple in family_extended.ttl"
    )


def test_year_property_usage_subject_counts_match_original_ontology() -> None:
    original_graph = load_original_graph()
    extended_graph = Graph().parse(EXTENDED_ONTOLOGY_PATH, format="turtle")
    failures = []

    print("\nYear property usage counts")
    for prop in REDECLARED_DATATYPE_PROPERTIES:
        original_subjects = {
            row.subject
            for row in original_graph.query(
                "SELECT DISTINCT ?subject WHERE { ?subject ?predicate ?value . }",
                initBindings={"predicate": prop},
            )
        }
        extended_subjects = {
            row.subject
            for row in extended_graph.query(
                "SELECT DISTINCT ?subject WHERE { ?subject ?predicate ?value . }",
                initBindings={"predicate": prop},
            )
        }
        missing_subjects = original_subjects - extended_subjects
        extra_subjects = extended_subjects - original_subjects

        print(f"  {prop}")
        print(f"    original subject count: {len(original_subjects)}")
        print(f"    extended subject count: {len(extended_subjects)}")
        if missing_subjects:
            print("    missing subjects:")
            print(format_uri_list(missing_subjects))
        if extra_subjects:
            print("    extra subjects:")
            print(format_uri_list(extra_subjects))

        if original_subjects != extended_subjects:
            failures.append(
                f"{prop}: original={len(original_subjects)}, extended={len(extended_subjects)}"
                + (
                    "\nmissing:\n" + format_uri_list(missing_subjects)
                    if missing_subjects
                    else ""
                )
                + ("\nextra:\n" + format_uri_list(extra_subjects) if extra_subjects else "")
            )

    assert not failures, (
        "Year property usage subject counts differ between original and extended ontology:\n"
        + "\n".join(failures)
    )


def test_year_properties_are_redeclared_as_datatype_properties() -> None:
    graph = load_extended_graph()

    print("\nRe-declared year properties")
    for prop in REDECLARED_DATATYPE_PROPERTIES:
        types = sorted(str(value) for value in graph.objects(prop, RDF.type))
        ranges = sorted(str(value) for value in graph.objects(prop, RDFS.range))
        print(f"  {prop}")
        print(f"    rdf:type: {types}")
        print(f"    rdfs:range: {ranges}")

        assert (prop, RDF.type, OWL.DatatypeProperty) in graph, (
            f"{prop} must be re-declared as owl:DatatypeProperty in family_extended.ttl"
        )
        assert (prop, RDF.type, OWL.AnnotationProperty) not in graph, (
            f"{prop} must not remain owl:AnnotationProperty in the merged OWL 2 DL artifact"
        )
        assert (prop, RDF.type, OWL.FunctionalProperty) in graph, (
            f"{prop} must be functional because the model expects a single year value"
        )
        assert (prop, RDFS.range, XSD.integer) in graph, f"{prop} must have range xsd:integer"

    assert (FHKB.hasBirthYear, RDFS.domain, FHKB.Person) in graph
    assert (FHKB.hasDeathYear, RDFS.domain, FHKB.Person) in graph
    assert (FHKB.hasMarriageYear, RDFS.domain, FHKB.Marriage) in graph


def test_naming_properties_remain_annotation_properties() -> None:
    graph = load_extended_graph()

    print("\nNaming annotation properties")
    for prop in NAMING_ANNOTATION_PROPERTIES:
        types = sorted(str(value) for value in graph.objects(prop, RDF.type))
        print(f"  {prop}: {types}")

        assert (prop, RDF.type, OWL.AnnotationProperty) in graph, (
            f"{prop} should remain owl:AnnotationProperty; naming metadata is not "
            "part of the structural year-property patch"
        )
        assert (prop, RDF.type, OWL.DatatypeProperty) not in graph, (
            f"{prop} must not be changed to owl:DatatypeProperty"
        )


def test_owlrl_expansion_if_available() -> None:
    """Run OWL RL rule expansion when owlrl is installed; skipped here if absent."""
    owlrl = pytest.importorskip("owlrl", reason="owlrl is not installed in this environment")

    graph = load_extended_graph()
    try:
        owlrl.DeductiveClosure(owlrl.OWLRL_Semantics).expand(graph)
    except Exception as exc:
        pytest.fail(f"OWL RL expansion failed on family_extended.ttl combined graph: {exc}")

    print(f"\nOWL RL expansion completed; expanded triple count: {len(graph)}")
