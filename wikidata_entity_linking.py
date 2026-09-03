#!/usr/bin/env python3
"""Ground-truth-free entity linking against the project's local Wikidata alias index."""

from __future__ import annotations

import re
import unicodedata
from collections import Counter, defaultdict
from dataclasses import dataclass
from difflib import SequenceMatcher
from pathlib import Path
from typing import Any

from rdflib import Graph, Namespace, OWL, URIRef

from agents.kg_builder_agent import DEFAULT_ENTITY_NAMESPACE, _entity_uri
from vector_entity_matching import load_alias_index


WIKIDATA_ENTITY = "http://www.wikidata.org/entity/"

def normalize_name(value: object) -> str:
    text = unicodedata.normalize("NFKC", str(value)).casefold()
    text = re.sub(r"[^\w]+", " ", text, flags=re.UNICODE)
    return " ".join(text.split())


@dataclass(frozen=True)
class AliasCandidateIndex:
    aliases_by_qid: dict[str, tuple[str, ...]]
    types_by_qid: dict[str, tuple[str, ...]]
    qids_by_alias: dict[str, tuple[str, ...]]
    qids_by_token: dict[str, tuple[str, ...]]


TYPE_ANCESTORS = {
    "Agent": {"Agent"},
    "Artifact": {"Artifact"},
    "Company": {"Company", "Organization", "Agent"},
    "Country": {"Country", "Place"},
    "CreativeWork": {"CreativeWork", "Artifact"},
    "EducationalInstitution": {"EducationalInstitution", "Organization", "Agent"},
    "Film": {"Film", "CreativeWork", "Artifact"},
    "MusicalWork": {"MusicalWork", "CreativeWork", "Artifact"},
    "Organization": {"Organization", "Agent"},
    "Person": {"Person", "Agent"},
    "Place": {"Place"},
    "WrittenWork": {"WrittenWork", "CreativeWork", "Artifact"},
}


def build_candidate_index(alias_path: Path) -> AliasCandidateIndex:
    source = load_alias_index(alias_path)
    aliases_by_qid: dict[str, tuple[str, ...]] = {}
    types_by_qid: dict[str, tuple[str, ...]] = {}
    alias_postings: dict[str, set[str]] = defaultdict(set)
    token_postings: dict[str, set[str]] = defaultdict(set)
    for qid, row in source.items():
        aliases = {
            normalized
            for value in row.get("aliases", []) + row.get("demonyms", [])
            if (normalized := normalize_name(value))
        }
        aliases_by_qid[qid] = tuple(sorted(aliases))
        types_by_qid[qid] = tuple(sorted({str(value) for value in row.get("types", []) if value}))
        for alias in aliases:
            alias_postings[alias].add(qid)
            for token in set(alias.split()):
                if len(token) >= 3:
                    token_postings[token].add(qid)
    return AliasCandidateIndex(
        aliases_by_qid=aliases_by_qid,
        types_by_qid=types_by_qid,
        qids_by_alias={key: tuple(sorted(value)) for key, value in alias_postings.items()},
        qids_by_token={key: tuple(sorted(value)) for key, value in token_postings.items()},
    )


def _types_compatible(entity_type: object, candidate_types: tuple[str, ...]) -> bool:
    """Treat missing candidate metadata as unknown, never as incompatible."""
    if not candidate_types:
        return True
    entity_ancestors = TYPE_ANCESTORS.get(str(entity_type), {str(entity_type)})
    return any(
        candidate_type in entity_ancestors
        or str(entity_type) in TYPE_ANCESTORS.get(candidate_type, {candidate_type})
        for candidate_type in candidate_types
    )


def _entity_names(entity: dict[str, Any]) -> list[str]:
    values = [entity.get("label", ""), *(entity.get("aliases") or [])]
    return list(dict.fromkeys(name for value in values if (name := normalize_name(value))))


def _fuzzy_candidates(names: list[str], index: AliasCandidateIndex, limit: int = 5):
    votes: Counter[str] = Counter()
    for name in names:
        for token in set(name.split()):
            if len(token) >= 3:
                votes.update(index.qids_by_token.get(token, ()))
    pool = [qid for qid, _ in votes.most_common(1000)]
    ranked = []
    for qid in pool:
        score = max(
            (SequenceMatcher(None, left, right).ratio()
             for left in names for right in index.aliases_by_qid.get(qid, ())),
            default=0.0,
        )
        ranked.append((score, qid))
    return sorted(ranked, key=lambda item: (-item[0], item[1]))[:limit]


def link_entities(entities: list[dict[str, Any]], index: AliasCandidateIndex) -> dict[str, Any]:
    """Link only unambiguous exact aliases; fuzzy results remain review suggestions."""
    rows = []
    for entity in entities:
        names = _entity_names(entity)
        evidence: dict[str, list[str]] = defaultdict(list)
        for name in names:
            for qid in index.qids_by_alias.get(name, ()):
                evidence[qid].append(name)

        exact = sorted(evidence, key=lambda qid: (-len(evidence[qid]), qid))
        compatible_exact = [
            qid for qid in exact if _types_compatible(entity.get("type"), index.types_by_qid.get(qid, ()))
        ]
        if len(compatible_exact) == 1:
            qid = compatible_exact[0]
            decision, score, method = "matched", 1.0, "unique_exact_alias"
            candidates = [{
                "qid": qid,
                "score": score,
                "matched_names": evidence[qid],
                "candidate_types": list(index.types_by_qid.get(qid, ())),
                "type_compatible": True,
            }]
        else:
            fuzzy = _fuzzy_candidates(names, index)
            decision, qid, score = ("review" if exact or fuzzy else "unmatched"), None, None
            method = (
                "type_incompatible_exact_alias"
                if exact and not compatible_exact
                else ("ambiguous_exact_alias" if exact else ("fuzzy_suggestion" if fuzzy else "no_candidate"))
            )
            candidates = [
                {
                    "qid": candidate,
                    "score": candidate_score,
                    "matched_names": evidence.get(candidate, []),
                    "candidate_types": list(index.types_by_qid.get(candidate, ())),
                    "type_compatible": _types_compatible(
                        entity.get("type"), index.types_by_qid.get(candidate, ())
                    ),
                }
                for candidate_score, candidate in fuzzy
            ]
            if exact:
                exact_set = set(exact)
                candidates.sort(key=lambda row: (row["qid"] not in exact_set, -row["score"], row["qid"]))

        rows.append({
            "entity_id": str(entity["id"]),
            "label": entity.get("label"),
            "entity_type": entity.get("type"),
            "decision": decision,
            "method": method,
            "qid": qid,
            "wikidata_uri": f"{WIKIDATA_ENTITY}{qid}" if qid else None,
            "score": score,
            "candidates": candidates,
        })

    matched_by_qid: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        if row["decision"] == "matched" and row["qid"]:
            matched_by_qid[row["qid"]].append(row)
    for qid, conflicting_rows in matched_by_qid.items():
        if len(conflicting_rows) < 2:
            continue
        conflicting_ids = sorted(str(row["entity_id"]) for row in conflicting_rows)
        for row in conflicting_rows:
            row.update({
                "decision": "review",
                "method": "duplicate_qid_conflict",
                "qid": None,
                "wikidata_uri": None,
                "score": None,
                "conflicting_qid": qid,
                "conflicting_entity_ids": conflicting_ids,
            })
    counts = Counter(row["decision"] for row in rows)
    return {
        "mode": "local_wikidata_alias_index",
        "uses_ground_truth": False,
        "policy": (
            "Only a unique exact normalized label/alias with compatible known type metadata is "
            "auto-linked; a QID may be assigned to at most one extracted entity."
        ),
        "summary": {key: counts.get(key, 0) for key in ("matched", "review", "unmatched")},
        "entities": rows,
    }


def accepted_links(payload: dict[str, Any]) -> dict[str, str]:
    return {
        str(row["entity_id"]): str(row["wikidata_uri"])
        for row in payload.get("entities", [])
        if row.get("decision") == "matched" and row.get("wikidata_uri")
    }


def add_same_as_links(
    turtle: str,
    links: dict[str, str],
    *,
    entity_namespace: str = DEFAULT_ENTITY_NAMESPACE,
    include_in_graph: bool = False,
) -> tuple[str, str]:
    """Build a separate identity artifact without enriching the ABox by default."""
    graph = Graph().parse(data=turtle, format="turtle")
    same_as = Graph()
    same_as.bind("owl", OWL)
    same_as.bind("wd", Namespace(WIKIDATA_ENTITY))
    entity_ns = Namespace(entity_namespace)
    for entity_id, wikidata_uri in links.items():
        triple = (_entity_uri(entity_ns, entity_id), OWL.sameAs, URIRef(wikidata_uri))
        if include_in_graph:
            graph.add(triple)
        same_as.add(triple)
    return graph.serialize(format="turtle"), same_as.serialize(format="turtle")
