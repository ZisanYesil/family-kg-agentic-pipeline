from __future__ import annotations

from rdflib import Graph, Namespace
from rdflib.namespace import RDF

from utils.rdf import clone_graph, parse_turtle_graph, serialize_turtle_graph


EX = Namespace("http://example.com/data#")


def test_clone_graph_is_independent_and_preserves_content() -> None:
    graph = Graph()
    graph.bind("ex", EX)
    graph.add((EX.alex, RDF.type, EX.Person))

    cloned = clone_graph(graph)
    cloned.remove((EX.alex, RDF.type, EX.Person))

    assert (EX.alex, RDF.type, EX.Person) in graph
    assert len(cloned) == 0
    assert str(dict(cloned.namespaces()).get("ex")) == str(EX)


def test_turtle_serialization_round_trips_graph_content() -> None:
    graph = Graph()
    graph.add((EX.alex, RDF.type, EX.Person))

    serialized = serialize_turtle_graph(graph)
    reparsed = parse_turtle_graph(serialized)

    assert set(reparsed) == set(graph)
