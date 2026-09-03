from rdflib import Graph, Namespace, RDF

from run_internal_entity_resolution import _safe_groups, duplicate_groups, resolve_graph, resolve_mapping


def test_only_shared_qid_creates_duplicate_candidate():
    payload = {"entities": [
        {"entity_id": "alice", "decision": "matched", "qid": "Q1"},
        {"entity_id": "a_smith", "decision": "matched", "qid": "Q1"},
        {"entity_id": "bob", "decision": "matched", "qid": "Q2"},
    ]}
    assert duplicate_groups(payload) == [{
        "qid": "Q1", "entity_ids": ["a_smith", "alice"],
        "evidence": "shared_unique_wikidata_qid",
    }]


def test_conflicting_attributes_prevent_merge():
    mapping = {"entities": [
        {"id": "a", "type": "Person", "attributes": {"hasBirthDate": "1900"}},
        {"id": "b", "type": "Person", "attributes": {"hasBirthDate": "1901"}},
    ]}
    accepted, review = _safe_groups(mapping, [{"qid": "Q1", "entity_ids": ["a", "b"]}])
    assert not accepted
    assert review[0]["conflicting_attributes"] == ["hasBirthDate"]


def test_merge_combines_graph_facts_and_rewrites_relation_endpoints():
    mapping = {
        "entities": [
            {"id": "alice", "label": "Alice", "type": "Person", "aliases": [], "attributes": {}},
            {"id": "a_smith", "label": "A. Smith", "type": "Person", "aliases": [], "attributes": {}},
        ],
        "relations": [{"subject": "a_smith", "predicate": "hasChild", "object": "alice"}],
    }
    groups = [{"qid": "Q1", "entity_ids": ["a_smith", "alice"], "canonical_id": "a_smith"}]
    resolved_mapping, renaming = resolve_mapping(mapping, groups)
    assert len(resolved_mapping["entities"]) == 1
    assert resolved_mapping["relations"][0]["object"] == "a_smith"
    ns = Namespace("http://example.org/extracted/")
    graph = Graph()
    graph.add((ns.alice, RDF.type, ns.Person))
    graph.add((ns.a_smith, ns.hasChild, ns.alice))
    resolved = resolve_graph(graph, renaming)
    assert (ns.a_smith, RDF.type, ns.Person) in resolved
    assert (ns.a_smith, ns.hasChild, ns.a_smith) in resolved
