from rdflib import Graph, Literal, Namespace
from rdflib.namespace import RDFS

from vector_entity_matching import collect_name_variants, string_similarity


EX = Namespace("http://example.org/test/")
ONTO = Namespace("http://example.org/2wiki-ontology#")


def test_demonym_is_available_as_independent_entity_name_evidence() -> None:
    graph = Graph()
    graph.add((EX.united_kingdom, RDFS.label, Literal("United Kingdom")))
    graph.add((EX.united_kingdom, ONTO.hasDemonym, Literal("British")))

    variants = collect_name_variants(EX.united_kingdom, graph, {})

    assert {item["text"] for item in variants} == {"United Kingdom", "British"}


def test_unrelated_names_with_one_shared_surname_are_not_strong_lexical_evidence() -> None:
    assert string_similarity("Sandip Choudhury", "Chumki Chowdhury") < 0.70


def test_minor_name_variants_are_strong_lexical_evidence() -> None:
    assert string_similarity("Pepin of Heristal", "Pepin of Herstal") >= 0.70
