from pathlib import Path

import pytest
from pyshacl import validate
from rdflib import Graph, Literal, Namespace
from rdflib.namespace import RDF, XSD


FHKB = Namespace("http://www.example.com/genealogy.owl#")
SHAPES_PATH = Path(__file__).resolve().parents[1] / "shapes" / "family_shapes.ttl"


def _graph(*triples):
    graph = Graph()
    graph.bind("fhkb", FHKB)
    for triple in triples:
        graph.add(triple)
    return graph


def _validate(graph: Graph):
    shapes_graph = Graph().parse(SHAPES_PATH, format="turtle")
    conforms, _results_graph, results_text = validate(
        data_graph=graph,
        shacl_graph=shapes_graph,
        inference=None,
    )
    return conforms, results_text


RELATION_CASES = [
    (FHKB.hasFather, FHKB.Male, FHKB.Female),
    (FHKB.hasMother, FHKB.Female, FHKB.Male),
    (FHKB.hasBrother, FHKB.Male, FHKB.Female),
    (FHKB.hasSister, FHKB.Female, FHKB.Male),
    (FHKB.hasSon, FHKB.Male, FHKB.Female),
    (FHKB.hasDaughter, FHKB.Female, FHKB.Male),
]


@pytest.mark.parametrize(("predicate", "required_sex", "_wrong_sex"), RELATION_CASES)
def test_relation_object_with_required_sex_conforms(predicate, required_sex, _wrong_sex):
    graph = _graph(
        (FHKB.child, predicate, FHKB.relative),
        (FHKB.relative, FHKB.hasSex, required_sex),
    )

    conforms, results_text = _validate(graph)

    assert conforms, results_text


@pytest.mark.parametrize(("predicate", "_required_sex", "wrong_sex"), RELATION_CASES)
def test_relation_object_with_wrong_sex_violates(predicate, _required_sex, wrong_sex):
    graph = _graph(
        (FHKB.child, predicate, FHKB.relative),
        (FHKB.relative, FHKB.hasSex, wrong_sex),
    )

    conforms, results_text = _validate(graph)

    assert not conforms
    assert "hasSex" in results_text


def test_relation_object_with_missing_sex_violates_even_when_subject_has_no_type():
    graph = _graph((FHKB.untyped_child, FHKB.hasFather, FHKB.untyped_father))

    conforms, results_text = _validate(graph)

    assert not conforms
    assert "fhkb:hasSex fhkb:Male" in results_text


def test_has_sex_outside_allowed_values_violates():
    graph = _graph((FHKB.alex, FHKB.hasSex, FHKB.Unknown))

    conforms, results_text = _validate(graph)

    assert not conforms
    assert "fhkb:hasSex must have at most one value and must be fhkb:Male or fhkb:Female" in results_text


def test_multiple_has_father_values_violates_max_count():
    graph = _graph(
        (FHKB.child, FHKB.hasFather, FHKB.father_one),
        (FHKB.child, FHKB.hasFather, FHKB.father_two),
        (FHKB.father_one, FHKB.hasSex, FHKB.Male),
        (FHKB.father_two, FHKB.hasSex, FHKB.Male),
    )

    conforms, results_text = _validate(graph)

    assert not conforms
    assert "fhkb:hasFather must have at most one value" in results_text


def test_parent_count_allows_two_distinct_parents_across_specific_and_inverse_edges():
    graph = _graph(
        (FHKB.child, RDF.type, FHKB.Person),
        (FHKB.father, RDF.type, FHKB.Person),
        (FHKB.mother, RDF.type, FHKB.Person),
        (FHKB.child, FHKB.hasFather, FHKB.father),
        (FHKB.mother, FHKB.isParentOf, FHKB.child),
        (FHKB.father, FHKB.hasSex, FHKB.Male),
    )

    conforms, results_text = _validate(graph)

    assert conforms, results_text


def test_is_parent_of_accepts_man_and_woman_types_without_class_inference():
    graph = _graph(
        (FHKB.father, RDF.type, FHKB.Man),
        (FHKB.child, RDF.type, FHKB.Woman),
        (FHKB.father, FHKB.isParentOf, FHKB.child),
    )

    conforms, results_text = _validate(graph)

    assert conforms, results_text


def test_parent_count_with_third_parent_via_is_parent_of_violates():
    graph = _graph(
        (FHKB.child, RDF.type, FHKB.Person),
        (FHKB.father, RDF.type, FHKB.Person),
        (FHKB.mother, RDF.type, FHKB.Person),
        (FHKB.third_parent, RDF.type, FHKB.Person),
        (FHKB.child, FHKB.hasFather, FHKB.father),
        (FHKB.child, FHKB.hasMother, FHKB.mother),
        (FHKB.third_parent, FHKB.isParentOf, FHKB.child),
        (FHKB.father, FHKB.hasSex, FHKB.Male),
        (FHKB.mother, FHKB.hasSex, FHKB.Female),
    )

    conforms, results_text = _validate(graph)

    assert not conforms
    assert "more than two distinct parents" in results_text


def test_is_partner_in_requires_marriage_value():
    graph = _graph(
        (FHKB.alex, RDF.type, FHKB.Person),
        (FHKB.not_a_marriage, RDF.type, FHKB.Person),
        (FHKB.alex, FHKB.isPartnerIn, FHKB.not_a_marriage),
    )

    conforms, results_text = _validate(graph)

    assert not conforms
    assert "fhkb:isPartnerIn" in results_text
    assert "fhkb:Marriage" in results_text


def test_is_partner_in_with_marriage_value_conforms():
    graph = _graph(
        (FHKB.alex, RDF.type, FHKB.Person),
        (FHKB.marriage_alex_jane, RDF.type, FHKB.Marriage),
        (FHKB.alex, FHKB.isPartnerIn, FHKB.marriage_alex_jane),
    )

    conforms, results_text = _validate(graph)

    assert conforms, results_text


def test_is_partner_in_accepts_man_or_woman_subject_without_class_inference():
    graph = _graph(
        (FHKB.alex, RDF.type, FHKB.Man),
        (FHKB.marriage_alex_jane, RDF.type, FHKB.Marriage),
        (FHKB.alex, FHKB.isPartnerIn, FHKB.marriage_alex_jane),
    )

    conforms, results_text = _validate(graph)

    assert conforms, results_text


def test_is_spouse_of_requires_person_value():
    graph = _graph(
        (FHKB.alex, RDF.type, FHKB.Person),
        (FHKB.marriage_alex_jane, RDF.type, FHKB.Marriage),
        (FHKB.alex, FHKB.isSpouseOf, FHKB.marriage_alex_jane),
    )

    conforms, results_text = _validate(graph)

    assert not conforms
    assert "fhkb:isSpouseOf" in results_text
    assert "fhkb:Person" in results_text


def test_is_spouse_of_with_person_value_conforms():
    graph = _graph(
        (FHKB.alex, RDF.type, FHKB.Person),
        (FHKB.jane, RDF.type, FHKB.Person),
        (FHKB.alex, FHKB.isSpouseOf, FHKB.jane),
    )

    conforms, results_text = _validate(graph)

    assert conforms, results_text


def test_is_spouse_of_accepts_man_and_woman_types_without_class_inference():
    graph = _graph(
        (FHKB.alex, RDF.type, FHKB.Man),
        (FHKB.jane, RDF.type, FHKB.Woman),
        (FHKB.alex, FHKB.isSpouseOf, FHKB.jane),
    )

    conforms, results_text = _validate(graph)

    assert conforms, results_text


def test_has_birth_year_string_literal_violates_datatype():
    graph = _graph((FHKB.alex, FHKB.hasBirthYear, Literal("1850")))

    conforms, results_text = _validate(graph)

    assert not conforms
    assert "xsd:integer" in results_text


@pytest.mark.parametrize(
    ("year", "expected_conforms"),
    [
        (1850, True),
        (500, False),
        (2030, False),
    ],
)
def test_has_birth_year_plausibility_range(year, expected_conforms):
    graph = _graph((FHKB.alex, FHKB.hasBirthYear, Literal(year, datatype=XSD.integer)))

    conforms, results_text = _validate(graph)

    assert conforms is expected_conforms, results_text


def test_death_before_birth_violates_with_specific_message():
    graph = _graph(
        (FHKB.alex, FHKB.hasBirthYear, Literal(1950, datatype=XSD.integer)),
        (FHKB.alex, FHKB.hasDeathYear, Literal(1940, datatype=XSD.integer)),
    )

    conforms, results_text = _validate(graph)

    assert not conforms
    assert "hasDeathYear must not be earlier than hasBirthYear" in results_text


def test_death_after_birth_conforms():
    graph = _graph(
        (FHKB.alex, FHKB.hasBirthYear, Literal(1900, datatype=XSD.integer)),
        (FHKB.alex, FHKB.hasDeathYear, Literal(1980, datatype=XSD.integer)),
    )

    conforms, results_text = _validate(graph)

    assert conforms, results_text


def test_valid_marriage_conforms():
    graph = _graph(
        (FHKB.marriage_alex_jane, RDF.type, FHKB.Marriage),
        (FHKB.marriage_alex_jane, FHKB.hasMalePartner, FHKB.alex),
        (FHKB.marriage_alex_jane, FHKB.hasFemalePartner, FHKB.jane),
        (FHKB.marriage_alex_jane, FHKB.hasMarriageYear, Literal(1920, datatype=XSD.integer)),
        (FHKB.alex, FHKB.hasSex, FHKB.Male),
        (FHKB.jane, FHKB.hasSex, FHKB.Female),
    )

    conforms, results_text = _validate(graph)

    assert conforms, results_text


def test_marriage_male_partner_with_female_sex_violates():
    graph = _graph(
        (FHKB.marriage_alex_jane, RDF.type, FHKB.Marriage),
        (FHKB.marriage_alex_jane, FHKB.hasMalePartner, FHKB.alex),
        (FHKB.alex, FHKB.hasSex, FHKB.Female),
    )

    conforms, results_text = _validate(graph)

    assert not conforms
    assert "fhkb:hasMalePartner" in results_text


@pytest.mark.parametrize(
    ("predicate", "value", "expected_conforms"),
    [
        (FHKB.hasDeathYear, Literal(1980, datatype=XSD.integer), True),
        (FHKB.hasDeathYear, Literal("1980"), False),
        (FHKB.hasMarriageYear, Literal(1920, datatype=XSD.integer), True),
        (FHKB.hasMarriageYear, Literal(2030, datatype=XSD.integer), False),
    ],
)
def test_death_and_marriage_year_constraints(predicate, value, expected_conforms):
    subject = FHKB.marriage_alex_jane if predicate == FHKB.hasMarriageYear else FHKB.alex
    triples = [(subject, predicate, value)]
    if predicate == FHKB.hasMarriageYear:
        triples.append((subject, RDF.type, FHKB.Marriage))
    graph = _graph(*triples)

    conforms, results_text = _validate(graph)

    assert conforms is expected_conforms, results_text
