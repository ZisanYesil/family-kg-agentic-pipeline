from enum import Enum
from pathlib import Path
from typing import Any

from rdflib import Graph

EMPTY_TURTLE_PLACEHOLDER = "<empty turtle graph>"
PROJECT_ROOT = Path(__file__).resolve().parents[1]
FAMILY_EXTENDED_ONTOLOGY_PATH = PROJECT_ROOT / "ontology" / "ontology.ttl"


class TurtleParseError(ValueError):
    pass


def rdflib_format(graph_format: Enum) -> str:
    """Map public API format enum values to rdflib serializer plugin names."""
    return {
        "turtle": "turtle",
        "json_ld": "json-ld",
        "rdf_xml": "xml",
    }[graph_format.value]


def parse_turtle_graph(graph_turtle: str) -> Graph:
    graph = Graph()
    if not graph_turtle.strip() or graph_turtle.strip() == EMPTY_TURTLE_PLACEHOLDER:
        return graph

    try:
        graph.parse(data=graph_turtle, format="turtle")
        return graph
    except Exception as exc:
        raise TurtleParseError("Invalid Turtle graph") from exc


def serialize_graph(graph: Graph, graph_format: Enum) -> str:
    serialized: Any = graph.serialize(format=rdflib_format(graph_format))
    if isinstance(serialized, bytes):
        return serialized.decode("utf-8")
    return serialized


def serialize_turtle_graph(graph: Graph) -> str:
    """Serialize an in-memory pipeline graph at a persistence/API boundary."""
    if not isinstance(graph, Graph):
        raise TypeError("graph must be an rdflib.Graph")
    serialized: Any = graph.serialize(format="turtle")
    if isinstance(serialized, bytes):
        return serialized.decode("utf-8")
    return serialized


def clone_graph(graph: Graph) -> Graph:
    """Return an independent graph copy while preserving namespace bindings."""
    if not isinstance(graph, Graph):
        raise TypeError("graph must be an rdflib.Graph")
    cloned = Graph()
    for prefix, namespace in graph.namespaces():
        cloned.bind(prefix, namespace)
    for triple in graph:
        cloned.add(triple)
    return cloned


def count_turtle_triples(graph_turtle: str) -> int:
    return len(parse_turtle_graph(graph_turtle))


def load_family_ontology_graph() -> Graph:
    """Load the current default ontology graph."""
    graph = Graph()
    graph.parse(FAMILY_EXTENDED_ONTOLOGY_PATH, format="turtle")
    return graph
