"""
Generic variant of run_sparql_benchmark.py: no hardcoded per-benchmark
_PROPERTY_PATH / _TTL_PREDICATE_MAP tables. Instead:

  1. Load the ontology's own rdfs:label per property (2wiki_ontology.ttl)
     as a prior -- "hasBirthDate" declares label "has birth date", so a
     manifest relation "date of birth" can be matched to it purely by
     word-set overlap, with no hand-typed mapping.
  2. For predicates the ontology DOESN'T declare (the real extraction
     output uses some informal synonyms it never formally defines, e.g.
     hasNationality, hasMember, hasDaughter/hasSon, hasBrother/hasSister),
     discover every predicate actually used in the example's own
     extracted_{N}.ttl via a wildcard SPARQL query, and score each
     candidate PATH by word-overlap between the manifest relation's own
     words and the predicate's camelCase-split local name.

This replaces "look up the exact predicate URI in a table" with "ask the
graph what paths exist from the anchor, then rank them" -- fully
data-driven, but the tradeoff is real: lexical overlap only catches
synonyms that share words with the relation name. hasNationality/
citizenship, hasMember/part, hasDaughter,hasSon/child, and hasBrother,
hasSister/sibling share NO words with their canonical relation -- this
prototype is expected to score lower than the hardcoded-table version on
exactly those cases, and this script says so plainly in its output rather
than hiding it.
"""

from __future__ import annotations

import argparse
import csv
import datetime
import json
import re
import sys
from collections import defaultdict
from dataclasses import dataclass, field
from difflib import SequenceMatcher
from pathlib import Path

import pandas as pd
import rdflib

RDFS_LABEL = rdflib.RDFS.label
SKOS_ALT = rdflib.URIRef("http://www.w3.org/2004/02/skos/core#altLabel")
RDF_TYPE = rdflib.RDF.type
_BOOKKEEPING_PREDICATES = {RDFS_LABEL, SKOS_ALT, RDF_TYPE}

_STOPWORDS = {"has", "of", "the", "a", "an", "is"}
_MIN_HOP_SCORE = 0.20


@dataclass
class PredicateProfile:
    local_name: str
    label_terms: list[frozenset] = field(default_factory=list)
    direct_terms: list[frozenset] = field(default_factory=list)
    inverse_terms: list[frozenset] = field(default_factory=list)
    parents: set[str] = field(default_factory=set)
    inverses: set[str] = field(default_factory=set)
    external_matches: set[str] = field(default_factory=set)
    domains: set[str] = field(default_factory=set)
    ranges: set[str] = field(default_factory=set)


class OntologyPredicateIndex(dict):
    """Backward-compatible label index plus ontology relation metadata."""

    def __init__(self):
        super().__init__()
        self.profiles: dict[str, PredicateProfile] = {}

    def profile(self, local_name: str) -> PredicateProfile:
        return self.profiles.setdefault(local_name, PredicateProfile(local_name))


def words(text: str) -> frozenset:
    # camelCase -> spaced, then tokenize + drop stopwords, so
    # "hasBirthDate" and "date of birth" land on the same word set.
    text = re.sub(r"(?<!^)(?=[A-Z])", " ", str(text))
    tokens = re.findall(r"[a-z]+", text.lower())
    return frozenset(t for t in tokens if t not in _STOPWORDS)


def _local_name(uri) -> str:
    text = str(uri)
    return text.rsplit("#", 1)[-1].rsplit("/", 1)[-1]


def load_ontology_word_index(ontology_path: Path) -> OntologyPredicateIndex:
    """Build lexical and semantic profiles from ontology property metadata."""
    index = OntologyPredicateIndex()
    if not ontology_path.exists():
        return index
    g = rdflib.Graph()
    g.parse(ontology_path, format="turtle")
    props = set(g.subjects(rdflib.RDF.type, rdflib.OWL.ObjectProperty)) | \
        set(g.subjects(rdflib.RDF.type, rdflib.OWL.DatatypeProperty))
    for s in props:
        local = _local_name(s)
        profile = index.profile(local)
        label = g.value(s, RDFS_LABEL)
        if label:
            label_words = words(str(label))
            index[local] = label_words
            profile.label_terms.append(label_words)
        profile.label_terms.append(words(local))

        for predicate, value in g.predicate_objects(s):
            predicate_name = _local_name(predicate)
            if predicate_name == "directPhrase":
                profile.direct_terms.append(words(str(value)))
            elif predicate_name == "inversePhrase":
                profile.inverse_terms.append(words(str(value)))

        profile.parents.update(_local_name(value) for value in g.objects(s, rdflib.RDFS.subPropertyOf))
        profile.inverses.update(_local_name(value) for value in g.objects(s, rdflib.OWL.inverseOf))
        for match_predicate in (rdflib.SKOS.exactMatch, rdflib.SKOS.closeMatch):
            profile.external_matches.update(str(value) for value in g.objects(s, match_predicate))
        profile.domains.update(_local_name(value) for value in g.objects(s, rdflib.RDFS.domain))
        profile.ranges.update(_local_name(value) for value in g.objects(s, rdflib.RDFS.range))

    # owl:inverseOf is symmetric even when only one direction is asserted.
    for local, profile in list(index.profiles.items()):
        for inverse in list(profile.inverses):
            index.profile(inverse).inverses.add(local)
    return index


def word_overlap_score(a: frozenset, b: frozenset) -> float:
    if not a or not b:
        return 0.0
    union = a | b
    return len(a & b) / len(union) if union else 0.0


def _containment_score(a: frozenset, b: frozenset) -> float:
    if not a or not b:
        return 0.0
    return len(a & b) / min(len(a), len(b))


def _lexical_score(a: frozenset, b: frozenset) -> float:
    return 0.6 * word_overlap_score(a, b) + 0.4 * _containment_score(a, b)


def _concept_closure(index: OntologyPredicateIndex, local: str, inverse: bool) -> dict[str, float]:
    """Directional property concepts with depth-decayed hierarchy weights."""
    forward: dict[str, float] = {local: 1.0}
    pending = [(local, 0)]
    seen = set()
    while pending:
        current, depth = pending.pop(0)
        if current in seen:
            continue
        seen.add(current)
        for parent in index.profile(current).parents:
            weight = 0.88 ** (depth + 1)
            forward[parent] = max(forward.get(parent, 0.0), weight)
            pending.append((parent, depth + 1))
    for concept, weight in list(forward.items()):
        for external in index.profile(concept).external_matches:
            forward[f"external:{external}"] = max(
                forward.get(f"external:{external}", 0.0), weight * 0.92
            )
    if not inverse:
        return forward

    reversed_concepts: dict[str, float] = {}
    for concept, weight in forward.items():
        inverses = index.profile(concept).inverses
        for inverse_property in inverses:
            reversed_concepts[inverse_property] = max(
                reversed_concepts.get(inverse_property, 0.0), weight
            )
            # Include ancestors of the explicit inverse property too.
            for parent, parent_weight in _concept_closure(index, inverse_property, False).items():
                reversed_concepts[parent] = max(
                    reversed_concepts.get(parent, 0.0), weight * parent_weight
                )
    # Preserve an opaque directional key when the ontology declares no inverse;
    # it cannot create a false semantic match but still permits lexical scoring.
    if not reversed_concepts:
        reversed_concepts[f"inverse:{local}"] = 1.0
    return reversed_concepts


def _relation_concepts(relation_words: frozenset, index: OntologyPredicateIndex) -> dict[str, float]:
    concepts: dict[str, float] = {}
    for local, profile in index.profiles.items():
        terms = profile.label_terms + profile.direct_terms
        lexical = max((_lexical_score(relation_words, term) for term in terms), default=0.0)
        if lexical < 0.55:
            continue
        for concept, hierarchy_weight in _concept_closure(index, local, False).items():
            concepts[concept] = max(concepts.get(concept, 0.0), lexical * hierarchy_weight)
    return concepts


def score_predicate(
    pred_local_name: str,
    relation_words: frozenset,
    ontology_index: OntologyPredicateIndex,
    *,
    inverse: bool = False,
) -> float:
    """Hybrid label/phrase/hierarchy/character score in the traversed direction."""
    profile = ontology_index.profile(pred_local_name)
    directional_terms = profile.inverse_terms if inverse else profile.direct_terms
    lexical_terms = profile.label_terms + directional_terms
    if not lexical_terms:
        lexical_terms = [words(pred_local_name)]
    lexical = max((_lexical_score(relation_words, term) for term in lexical_terms), default=0.0)

    relation_concepts = _relation_concepts(relation_words, ontology_index)
    predicate_concepts = _concept_closure(ontology_index, pred_local_name, inverse)
    semantic = max(
        (relation_concepts[key] * predicate_concepts[key] for key in relation_concepts.keys() & predicate_concepts.keys()),
        default=0.0,
    )

    relation_text = " ".join(sorted(relation_words))
    predicate_text = " ".join(sorted(words(pred_local_name)))
    character = SequenceMatcher(None, relation_text, predicate_text).ratio()
    return min(1.0, 0.55 * lexical + 0.35 * semantic + 0.10 * character)


# ---------------------------------------------------------------------------
# Anchor matching (same text-matching logic used elsewhere in this project;
# inlined so this script stays dependency-free of data_processing.*).
# ---------------------------------------------------------------------------

def normalize_text(text: str) -> str:
    text = str(text or "").lower()
    text = re.sub(r"[^\w\s]", "", text)
    return re.sub(r"\s+", " ", text).strip()


def _normalize_for_anchor(text: str) -> str:
    return normalize_text(text.replace("'", " "))


def extract_anchor_entities(question: str, all_titles: list[str]) -> list[str]:
    q_norm = _normalize_for_anchor(question)
    matches = []
    for title in all_titles:
        title_norm = _normalize_for_anchor(title)
        if len(title_norm) < 3:
            continue
        if f" {title_norm} " in f" {q_norm} ":
            matches.append(title)

    # Entity labels frequently contain a legal/organizational suffix omitted
    # in natural-language questions. This is schema-independent and applies
    # to every title rather than any benchmark-specific entity.
    organization_suffixes = {
        "group", "company", "corporation", "inc", "incorporated", "ltd",
        "limited", "band", "university", "college",
    }
    for title in all_titles:
        title_words = _normalize_for_anchor(title).split()
        shortened = (
            " ".join(title_words[:-1])
            if title_words and title_words[-1] in organization_suffixes
            else ""
        )
        if len(shortened) >= 3 and f" {shortened} " in f" {q_norm} ":
            matches.append(title)
    matches.sort(key=len, reverse=True)
    kept: list[str] = []
    for m in matches:
        m_norm = _normalize_for_anchor(m)
        if any(f" {m_norm} " in f" {_normalize_for_anchor(k)} " for k in kept):
            continue
        kept.append(m)
    if kept:
        return kept

    # Fall back only when exact label/alias matching found nothing. This
    # handles qualified-name variation such as "Eleanor, Countess of
    # Vermandois" versus the graph label "Eleanor of Vermandois" without
    # consulting the reference answer. Require two shared informative tokens
    # and high title-token coverage to avoid loose single-name matches.
    anchor_stopwords = {
        "a", "an", "the", "of", "is", "was", "in", "from", "who",
        "what", "where", "which", "did", "does", "film", "song",
    }
    question_tokens = set(q_norm.split()) - anchor_stopwords
    fallback = []
    for title in all_titles:
        title_tokens = set(_normalize_for_anchor(title).split()) - anchor_stopwords
        shared = question_tokens & title_tokens
        coverage = len(shared) / len(title_tokens) if title_tokens else 0.0
        if len(shared) >= 2 and coverage >= 0.60:
            fallback.append((coverage, len(shared), len(title_tokens), title))
    fallback.sort(key=lambda row: (-row[0], -row[1], row[2], row[3].casefold()))
    if fallback:
        return [fallback[0][3]]
    return kept


# ---------------------------------------------------------------------------
# Discover-and-score retrieval: no predicate lookup table at all.
# ---------------------------------------------------------------------------

def load_graph_and_labels(ttl_path: Path, metadata_path: Path | None = None):
    g = rdflib.Graph()
    g.parse(ttl_path, format="turtle")
    # Some reasoners intentionally materialize only ABox/schema facts and
    # omit annotation properties. Merge the exact pre-reasoning matched graph
    # so rdfs:label/skos:altLabel remain available for anchor resolution.
    if metadata_path is not None and metadata_path.exists():
        g.parse(metadata_path, format="turtle")

    primary_label = {}
    for s, o in g.subject_objects(RDFS_LABEL):
        primary_label[s] = str(o)

    label_to_primary = {normalize_text(l): l for l in primary_label.values()}
    all_titles = list(primary_label.values())
    for s, o in g.subject_objects(SKOS_ALT):
        if s in primary_label:
            all_titles.append(str(o))
            label_to_primary[normalize_text(str(o))] = primary_label[s]

    return g, all_titles, label_to_primary


def _node_label(g: rdflib.Graph, primary_label: dict, node) -> str:
    if isinstance(node, rdflib.Literal):
        return str(node)
    return primary_label.get(node, _local_name(node))


def discover_one_hop(g: rdflib.Graph, anchor_label: str):
    """All directed and inverse (predicate, answer) pairs from anchor."""
    query = """
    SELECT ?p ?answer ?inverse WHERE {
      ?anchor rdfs:label ?anchorLabel .
      {
        ?anchor ?p ?answer .
        BIND(false AS ?inverse)
      } UNION {
        ?answer ?p ?anchor .
        BIND(true AS ?inverse)
      }
    }
    """
    primary_label = {s: str(o) for s, o in g.subject_objects(RDFS_LABEL)}
    out = []
    rows = g.query(query, initBindings={"anchorLabel": rdflib.Literal(anchor_label)})
    for row in rows:
        if row.p in _BOOKKEEPING_PREDICATES:
            continue
        marker = "^" if bool(row.inverse.toPython()) else ""
        out.append((f"{marker}{_local_name(row.p)}", _node_label(g, primary_label, row.answer)))
    return out


def discover_two_hop(g: rdflib.Graph, anchor_label: str):
    """All directed/inverse two-hop paths from anchor."""
    query = """
    SELECT ?p1 ?p2 ?answer ?inverse1 ?inverse2 WHERE {
      ?anchor rdfs:label ?anchorLabel .
      {
        ?anchor ?p1 ?mid . BIND(false AS ?inverse1)
      } UNION {
        ?mid ?p1 ?anchor . BIND(true AS ?inverse1)
      }
      {
        ?mid ?p2 ?answer . BIND(false AS ?inverse2)
      } UNION {
        ?answer ?p2 ?mid . BIND(true AS ?inverse2)
      }
      FILTER(?answer != ?anchor)
    }
    """
    primary_label = {s: str(o) for s, o in g.subject_objects(RDFS_LABEL)}
    out = []
    rows = g.query(query, initBindings={"anchorLabel": rdflib.Literal(anchor_label)})
    for row in rows:
        if row.p1 in _BOOKKEEPING_PREDICATES or row.p2 in _BOOKKEEPING_PREDICATES:
            continue
        marker1 = "^" if bool(row.inverse1.toPython()) else ""
        marker2 = "^" if bool(row.inverse2.toPython()) else ""
        p1 = f"{marker1}{_local_name(row.p1)}"
        p2 = f"{marker2}{_local_name(row.p2)}"
        out.append((p1, p2, _node_label(g, primary_label, row.answer)))
    return out


def _score_path_predicate(predicate: str, relation_words: frozenset, ontology_index: dict) -> float:
    """Score lexical meaning plus ontology semantics in traversal direction."""
    inverse = predicate.startswith("^")
    return score_predicate(
        predicate.removeprefix("^"), relation_words, ontology_index, inverse=inverse
    )


def resolve_relation_chain(g: rdflib.Graph, anchor_label: str, relation_set: list[str], ontology_index: dict):
    """Discover all candidate paths of the right length and pick the
    highest-scoring one against the manifest relation words -- order of
    relation_set is NOT assumed correct, both hop-orderings are scored.
    Returns (answer_label_or_None, debug_note).
    """
    if len(relation_set) == 1:
        rel_words = words(relation_set[0])
        candidates = discover_one_hop(g, anchor_label)
        scored = [(_score_path_predicate(p, rel_words, ontology_index), p, a) for p, a in candidates]
        scored = [c for c in scored if c[0] >= _MIN_HOP_SCORE]
        if not scored:
            return None, f"no scored candidate among {[p for p, _ in candidates]}"
        scored.sort(key=lambda c: (-c[0], c[1].casefold(), c[2].casefold()))
        best_score, best_p, best_answer = scored[0]
        return best_answer, f"{best_p} (score={best_score:.2f})"

    if len(relation_set) == 2:
        w0, w1 = words(relation_set[0]), words(relation_set[1])
        candidates = discover_two_hop(g, anchor_label)
        scored = []
        for p1, p2, answer in candidates:
            a1 = _score_path_predicate(p1, w0, ontology_index)
            a2 = _score_path_predicate(p2, w1, ontology_index)
            b1 = _score_path_predicate(p1, w1, ontology_index)
            b2 = _score_path_predicate(p2, w0, ontology_index)

            def alignment_score(first, second):
                if min(first, second) < _MIN_HOP_SCORE:
                    return 0.0
                # A chain is only as trustworthy as its weakest hop; the mean
                # provides a smaller tie-breaking contribution.
                return 0.7 * min(first, second) + 0.3 * ((first + second) / 2)

            score_a = alignment_score(a1, a2)
            score_b = alignment_score(b1, b2)
            scored.append((max(score_a, score_b), p1, p2, answer))
        scored = [c for c in scored if c[0] > 0]
        if not scored:
            return None, f"no scored candidate among {[(p1, p2) for p1, p2, _ in candidates]}"
        scored.sort(key=lambda c: (-c[0], c[1].casefold(), c[2].casefold(), c[3].casefold()))
        best_score, p1, p2, best_answer = scored[0]
        return best_answer, f"{p1}/{p2} (score={best_score:.2f})"

    return None, "relation_set length > 2 not supported by this prototype"


def resolve_relation_values(g: rdflib.Graph, anchor_label: str, relation: str, ontology_index: dict):
    """Return all values tied for the best one-hop predicate score."""
    relation_words = words(relation)
    candidates = discover_one_hop(g, anchor_label)
    scored = [
        (_score_path_predicate(predicate, relation_words, ontology_index), answer)
        for predicate, answer in candidates
    ]
    scored = [(score, answer) for score, answer in scored if score >= _MIN_HOP_SCORE]
    if not scored:
        return []
    best_score = max(score for score, _ in scored)
    return sorted({answer for score, answer in scored if score == best_score})


# ---------------------------------------------------------------------------
# Comparators (dual-branch logic is cross-graph, not itself a SPARQL
# concern; same minimal reimplementation as run_sparql_benchmark.py).
# ---------------------------------------------------------------------------

_DATE_FORMATS = ["%B %d, %Y", "%B %d,%Y", "%b %d, %Y", "%d %B %Y", "%d %b %Y", "%Y-%m-%d", "%Y"]


def parse_date_key(value):
    value = str(value).strip()
    for fmt in _DATE_FORMATS:
        try:
            dt = datetime.datetime.strptime(value, fmt)
            return (dt.year, dt.month, dt.day)
        except ValueError:
            continue
    match = re.search(r"\d{4}", value)
    return (int(match.group()), 1, 1) if match else None


_ORDERING_CUE_RE = re.compile(r"\b(first|last|earlier|later|older|younger|more recently)\b", re.IGNORECASE)
_LATEST_WINS_CUE_RE = re.compile(r"\b(last|later|more recently|younger)\b", re.IGNORECASE)
_LIFESPAN_CUE_RE = re.compile(r"\blived? longer\b", re.IGNORECASE)


def _lifespan_days(g, anchor_label, ontology_index):
    birth, _ = resolve_relation_chain(g, anchor_label, ["date of birth"], ontology_index)
    death, _ = resolve_relation_chain(g, anchor_label, ["date of death"], ontology_index)
    bk = parse_date_key(birth) if birth else None
    dk = parse_date_key(death) if death else None
    if bk is None or dk is None:
        return None
    try:
        return (datetime.date(*dk) - datetime.date(*bk)).days
    except ValueError:
        return None


def apply_dual_comparator(question, g, anchors, values, ontology_index):
    if _LIFESPAN_CUE_RE.search(question):
        lifespans = [(a, _lifespan_days(g, a, ontology_index)) for a in anchors[:2]]
        comparable = [(a, d) for a, d in lifespans if d is not None]
        if len(comparable) >= 2:
            comparable.sort(key=lambda item: item[1], reverse=True)
            return comparable[0][0], "lifespan"
        return None, "insufficient_comparable_values"

    if _ORDERING_CUE_RE.search(question):
        wants_earliest = not _LATEST_WINS_CUE_RE.search(question)
        keyed = [(parse_date_key(v), a) for a, v in zip(anchors, values) if v is not None]
        comparable = [(k, a) for k, a in keyed if k is not None]
        if len(comparable) < 2:
            return None, "insufficient_comparable_values"
        comparable.sort(key=lambda item: item[0], reverse=not wants_earliest)
        return comparable[0][1], "ordering"

    if any(v is None for v in values[:2]):
        return None, "insufficient_comparable_values"
    same = normalize_text(values[0]) == normalize_text(values[1])
    return ("yes" if same else "no"), "equality"


# ---------------------------------------------------------------------------
# Scoring + batch runner
# ---------------------------------------------------------------------------

_DEMONYM_TO_COUNTRY = {
    "american": "united states", "british": "united kingdom", "english": "united kingdom",
    "scottish": "united kingdom", "welsh": "united kingdom", "irish": "ireland",
    "indian": "india", "french": "france", "german": "germany", "italian": "italy",
    "spanish": "spain", "portuguese": "portugal", "russian": "russia", "japanese": "japan",
    "chinese": "china", "canadian": "canada", "australian": "australia", "dutch": "netherlands",
    "swedish": "sweden", "norwegian": "norway", "danish": "denmark", "polish": "poland",
    "brazilian": "brazil", "mexican": "mexico", "egyptian": "egypt", "turkish": "turkey",
    "greek": "greece", "swiss": "switzerland", "austrian": "austria", "belgian": "belgium",
    "finnish": "finland", "israeli": "israel", "malaysian": "malaysia",
    "filipino": "philippines", "vietnamese": "vietnam", "thai": "thailand",
    "indonesian": "indonesia", "pakistani": "pakistan", "bangladeshi": "bangladesh",
    "nigerian": "nigeria", "kenyan": "kenya", "argentine": "argentina",
    "argentinian": "argentina", "chilean": "chile", "colombian": "colombia",
    "peruvian": "peru", "cuban": "cuba", "venezuelan": "venezuela", "ukrainian": "ukraine",
    "czech": "czech republic", "hungarian": "hungary", "romanian": "romania",
    "bulgarian": "bulgaria", "croatian": "croatia", "serbian": "serbia",
    "icelandic": "iceland", "maltese": "malta", "lithuanian": "lithuania",
}
_DEMONYM_PAIRS = {(d, c) for d, c in _DEMONYM_TO_COUNTRY.items()} | {(c, d) for d, c in _DEMONYM_TO_COUNTRY.items()}
_DASH_VARIANTS_RE = re.compile(r"[‐‑‒–—−]")


def _answers_match(predicted, gold) -> bool:
    if predicted is None:
        return False
    p = _DASH_VARIANTS_RE.sub("-", str(predicted).strip().lower())
    gd = _DASH_VARIANTS_RE.sub("-", str(gold).strip().lower())
    if not p or not gd:
        return False
    if p == gd or p in gd or gd in p:
        return True
    if (p, gd) in _DEMONYM_PAIRS:
        return True
    pk, gk = parse_date_key(p), parse_date_key(gd)
    return pk is not None and gk is not None and pk == gk


def score_example(
    example_dir: Path,
    m_row: dict,
    ontology_index: dict,
    graph_stage: str = "extracted",
) -> dict:
    example_id = m_row["example_id"]
    q_type = m_row["type"]
    question = next(example_dir.glob(f"example{example_id}_question.txt")).read_text(encoding="utf-8").strip()
    answer_files = list(example_dir.glob(f"example{example_id}_answer.txt"))
    gold_answer = answer_files[0].read_text(encoding="utf-8").strip() if answer_files else ""

    graph_path = (
        example_dir / f"extracted_{example_id}.ttl"
        if graph_stage == "extracted"
        else example_dir / "inference" / f"extracted_reasoned_{example_id}.ttl"
    )
    if not graph_path.exists():
        return {
            "example_id": example_id,
            "type": q_type,
            "question": question,
            "gold_answer": gold_answer,
            "predicted_answer": None,
            "correct": False,
            "note": f"missing_{graph_stage}_graph",
        }
    metadata_path = None
    if graph_stage == "reasoned":
        candidates = (
            example_dir / "entity_matching" / f"matched_extracted_{example_id}.ttl",
            example_dir / "originals" / f"extracted_{example_id}.ttl",
            example_dir / f"extracted_{example_id}.ttl",
        )
        metadata_path = next((path for path in candidates if path.is_file()), None)
    g, all_titles, label_to_primary = load_graph_and_labels(graph_path, metadata_path)
    relation_set = [r.strip() for r in m_row["relations"].split("|")]

    base = {"example_id": example_id, "type": q_type, "question": question, "gold_answer": gold_answer}

    anchors_raw = extract_anchor_entities(question, all_titles)
    anchors = [label_to_primary.get(normalize_text(a), a) for a in anchors_raw]
    if not anchors:
        return {**base, "predicted_answer": None, "correct": False, "note": "no_anchor"}

    if q_type in ("compositional", "inference"):
        predicted_answer, note = resolve_relation_chain(g, anchors[0], relation_set, ontology_index)
        return {**base, "predicted_answer": predicted_answer,
                "correct": _answers_match(predicted_answer, gold_answer), "note": note}

    if len(anchors) < 2:
        return {**base, "predicted_answer": None, "correct": False, "note": "insufficient_anchors"}

    q_norm = normalize_text(question)
    cardinality_cue = re.search(
        r"\b(wider|broader|more|most|fewer|less)\b.*\b(profession|occupation|career)\b",
        q_norm,
    )
    if cardinality_cue and len(relation_set) == 1:
        value_sets = [
            resolve_relation_values(g, anchor, relation_set[0], ontology_index)
            for anchor in anchors[:2]
        ]
        if all(value_sets) and len(value_sets[0]) != len(value_sets[1]):
            wants_fewer = re.search(r"\b(fewer|less)\b", q_norm)
            choose_first = len(value_sets[0]) < len(value_sets[1]) if wants_fewer else len(value_sets[0]) > len(value_sets[1])
            predicted_answer = anchors[0] if choose_first else anchors[1]
            return {
                **base,
                "predicted_answer": predicted_answer,
                "correct": _answers_match(predicted_answer, gold_answer),
                "note": f"cardinality {len(value_sets[0])} vs {len(value_sets[1])}",
            }

    values = [resolve_relation_chain(g, a, relation_set, ontology_index)[0] for a in anchors[:2]]
    predicted_answer, note = apply_dual_comparator(question, g, anchors[:2], values, ontology_index)
    return {**base, "predicted_answer": predicted_answer,
            "correct": _answers_match(predicted_answer, gold_answer), "note": note}


def read_manifest_rows(manifest_dir: Path) -> list[dict]:
    """Read CSV, or recover the promoted metadata if manifest.csv was
    overwritten by this project's JSON extraction-status output."""
    manifest_path = manifest_dir / "manifest.csv"
    raw = manifest_path.read_text(encoding="utf-8")
    if not raw.lstrip().startswith(("[", "{")):
        return list(csv.DictReader(raw.splitlines()))

    json.loads(raw)  # Fail clearly if it is neither supported format.
    candidate_name = manifest_dir.name.replace("final_data_", "candidate_data_", 1)
    roots = [
        manifest_dir.parent / f"{candidate_name}_expanded",
        manifest_dir.parent / candidate_name,
    ]
    roots = [root for root in roots if (root / "manifest.csv").exists()]
    by_question = {}
    for root in roots:
        with (root / "manifest.csv").open(newline="", encoding="utf-8") as f:
            for row in csv.DictReader(f):
                cid = row["example_id"]
                question_path = root / cid / f"example{cid}_question.txt"
                if question_path.exists():
                    key = normalize_text(question_path.read_text(encoding="utf-8"))
                    by_question.setdefault(key, row)

    recovered = []
    dirs = sorted(
        (p for p in manifest_dir.iterdir() if p.is_dir() and p.name.isdigit()),
        key=lambda p: int(p.name),
    )
    for example_dir in dirs:
        final_id = example_dir.name
        question_path = example_dir / f"example{final_id}_question.txt"
        source = by_question.get(normalize_text(question_path.read_text(encoding="utf-8")))
        if source is None:
            raise SystemExit(f"Could not recover manifest metadata for {question_path}")
        recovered.append({**source, "example_id": final_id})
    print(f"Recovered {len(recovered)} rows from candidate manifests")
    return recovered


def run_benchmark(
    manifest_dir: Path,
    ontology_path: Path,
    only_type: str | None,
    graph_stage: str = "extracted",
    start: int | None = None,
    end: int | None = None,
) -> None:
    manifest_path = manifest_dir / "manifest.csv"
    if not manifest_path.exists():
        raise SystemExit(f"No manifest.csv found under {manifest_dir}")

    ontology_index = load_ontology_word_index(ontology_path)
    print(f"Loaded {len(ontology_index)} property labels from {ontology_path}")

    manifest_rows = read_manifest_rows(manifest_dir)
    if start is not None:
        manifest_rows = [r for r in manifest_rows if int(r["example_id"]) >= start]
    if end is not None:
        manifest_rows = [r for r in manifest_rows if int(r["example_id"]) <= end]
    if only_type:
        manifest_rows = [r for r in manifest_rows if r["type"] == only_type]

    results = []
    for m_row in manifest_rows:
        example_dir = manifest_dir / m_row["example_id"]
        if not example_dir.exists():
            print(f"[SKIP] #{m_row['example_id']}: directory not found")
            continue
        scored = score_example(example_dir, m_row, ontology_index, graph_stage)
        results.append(scored)
        mark = "PASS" if scored["correct"] else "FAIL"
        print(
            f"[{mark}] #{scored['example_id']:>3} ({scored['type']:<18}) "
            f"pred={scored['predicted_answer']!r}  gold={scored['gold_answer']!r}"
            + (f"  note={scored['note']}" if scored.get("note") else "")
        )

    df = pd.DataFrame(results)
    if df.empty:
        print("No scoreable rows.")
        return

    print()
    print(f"OVERALL GENERIC-SPARQL ACCURACY: {df['correct'].mean():.1%}  ({int(df['correct'].sum())}/{len(df)})")
    print()
    print("Per-type breakdown:")
    for t, grp in df.groupby("type"):
        print(f"  {t}: {grp['correct'].mean():.1%}  ({int(grp['correct'].sum())}/{len(grp)})")

    empty = df[df["predicted_answer"].isna()]
    if not empty.empty:
        print()
        print(f"{len(empty)}/{len(df)} returned no result at all")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("manifest_dir", type=Path)
    parser.add_argument("--ontology", type=Path, default=Path(__file__).resolve().parent / "ontology" / "ontology.ttl")
    parser.add_argument("--type", choices=["compositional", "comparison", "bridge_comparison", "inference"], default=None)
    parser.add_argument(
        "--graph-stage",
        choices=["extracted", "reasoned"],
        default="extracted",
        help="Read extracted_N.ttl or inference/extracted_reasoned_N.ttl.",
    )
    parser.add_argument("--start", type=int, default=None, help="Minimum example id (inclusive).")
    parser.add_argument("--end", type=int, default=None, help="Maximum example id (inclusive).")
    args = parser.parse_args()
    run_benchmark(
        args.manifest_dir.expanduser(),
        args.ontology.expanduser(),
        args.type,
        args.graph_stage,
        args.start,
        args.end,
    )


if __name__ == "__main__":
    main()
