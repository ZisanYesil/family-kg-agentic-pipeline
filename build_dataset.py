#!/usr/bin/env python3
"""
build_dataset.py
=================
2WikiMultihopQA (dev split) -> 1000-example benchmark folder structure.

What it does
------------
1. Loads the local `dev.parquet` (columns: _id, type, question, context,
   supporting_facts, evidences, answer).
2. Audits source structure, answer/evidence support, ontology coverage, date
   values, and surface-form grounding with explicit pass/review/reject logs.
3. Parses the `evidences` field (list of [subject, relation, object] triples)
   and identifies every distinct relation present in the eligible rows.
4. Selects 1000 rows via *rare-relation-first stratified sampling* so that
   every relation (director ... doctoral advisor) is represented, instead of
   being drowned out by the very frequent ones (director, date of birth,
   father, ...).
5. Writes one folder per example under `data/`:

       data/3/text_3.txt                 <- context (documentary text)
       data/3/ground_truth_3.ttl          <- gold RDF triples (Turtle)
       data/3/example3_question.txt       <- question
       data/3/example3_answer.txt         <- gold answer
       data/3/example3_evidences.json     <- original evidence triples
       data/3/example3_supporting_facts.json <- original support references

   ... one numeric folder per selected row, plus a `data/manifest.csv` index.
   Folder and file names (`text_N.txt`, `ground_truth_N.ttl`) match what
   run_agent_pipeline.py / reasoner_kg_hermit.py / vector_entity_matching.py
   expect, so this output drops straight into that pipeline with no renaming.

Silver triples are written using this project's own ontology properties
(ex:hasDirector, ex:hasFather, ...) rather than raw Wikidata predicates, so
they line up directly with what the extraction pipeline and SHACL shapes
target. The relation -> ontology-property mapping below was built from the
`skos:exactMatch` links in ontology.ttl.

Usage
-----
    python build_dataset.py --input data/dev.parquet --out data --n 1000

Requires: pandas, pyarrow
"""
import argparse
import json
import math
import random
import re
import csv
import unicodedata
from collections import Counter, defaultdict
from dataclasses import asdict, dataclass
from datetime import date as date_cls
from pathlib import Path

import pandas as pd

# --------------------------------------------------------------------------
# Relation -> ontology property mapping.
# Built from ontology.ttl's skos:exactMatch links (2wiki relation string ->
# Wikidata P-code -> ex: property). Relations whose object is a literal
# (not a KG entity) are marked in DATE_LITERAL_RELATIONS below.
#
# NOTE: the original version of this script mapped "place of detention" to
# wdt:P1399 ("convicted of"), which is the wrong Wikidata property -- the
# ontology's ex:hasDetentionPlace is matched to wdt:P2632 ("place of
# detention"). That's fixed here.
# --------------------------------------------------------------------------
RELATION_TO_ONTOLOGY_PROPERTY = {
    "director": "ex:hasDirector",
    "country of citizenship": "ex:hasCitizenship",
    "date of birth": "ex:hasBirthDate",
    "country": "ex:hasCountry",
    "date of death": "ex:hasDeathDate",
    "country of origin": "ex:hasCountryOfOrigin",
    "place of birth": "ex:hasBirthPlace",
    "father": "ex:hasFather",
    "publication date": "ex:hasPublicationDate",
    "place of death": "ex:hasDeathPlace",
    "performer": "ex:hasPerformer",
    "spouse": "ex:hasSpouse",
    "composer": "ex:hasComposer",
    "mother": "ex:hasMother",
    "cause of death": "ex:hasCauseOfDeath",
    "award received": "ex:hasAwardReceived",
    "educated at": "ex:hasEducatedAt",
    "child": "ex:hasChild",
    "place of burial": "ex:hasBurialPlace",
    "inception": "ex:hasInception",
    "occupation": "ex:hasOccupation",
    "founded by": "ex:hasFounder",
    "producer": "ex:hasProducer",
    "employer": "ex:hasEmployer",
    "sibling": "ex:hasSibling",
    "publisher": "ex:hasPublisher",
    "creator": "ex:hasCreator",
    "editor": "ex:hasEditor",
    "presenter": "ex:hasPresenter",
    "has part": "ex:hasMember",  # 2wiki's "has part" is always band->member in practice
                                  # (verified: 17/17 instances in dev.parquet), not
                                  # CreativeWork-composition -- see ex:hasMember's
                                  # comment in ontology.ttl for why ex:hasPart itself
                                  # (CreativeWork/CreativeWork) is wrong for this.
    "student of": "ex:hasStudentOf",
    "place of detention": "ex:hasDetentionPlace",  # was wrongly P1399; ontology uses P2632
    "doctoral advisor": "ex:hasDoctoralAdvisor",
    "manufacturer": "ex:hasManufacturer",  # validation-only relation
}

# Relations whose *object* is a literal value, not an entity.
#
# NOTE: "cause of death" is intentionally NOT here. ex:hasCauseOfDeath is
# declared `a owl:ObjectProperty ; rdfs:range ex:CauseOfDeath` in ontology.ttl,
# so its ground-truth object must be an entity URI like every other object
# property below -- writing it as a bare string literal made every
# hasCauseOfDeath ground-truth triple fail is_abox_fact's `isinstance(obj,
# URIRef)` check in reasoner_kg_hermit.py and get silently dropped before
# scoring, guaranteeing a spurious FP/zero-TP result for this relation no
# matter how good the extraction was.
#
# What's left here are exactly the four date-valued datatype properties,
# which schema_loader.py assigns range_type == "date_or_year" (see
# _load_datatype_properties). Their values need BOTH a format fix and a
# typing fix to exact-match what the pipeline can ever produce -- see
# normalize_date() and _date_literal_term() below.
DATE_LITERAL_RELATIONS = {
    "date of birth",
    "date of death",
    "publication date",
    "inception",
}

COUNTRY_OBJECT_RELATIONS = {
    "country",
    "country of citizenship",
    "country of origin",
}

ONTOLOGY_NS = "http://example.org/2wiki-ontology#"
INSTANCE_NS = "http://example.org/entity/"


@dataclass(frozen=True)
class QualityIssue:
    code: str
    severity: str
    message: str


@dataclass(frozen=True)
class QualityAssessment:
    status: str
    issues: tuple[QualityIssue, ...]


def _json_list(value, field: str) -> list:
    """Decode one parquet JSON field and require its expected top-level shape."""
    parsed = json.loads(value) if isinstance(value, str) else value
    if not isinstance(parsed, list):
        raise ValueError(f"{field} must be a JSON list")
    return parsed


def _surface_key(value: object) -> str:
    """Loose surface key used only for quality warnings, never URI identity."""
    normalized = unicodedata.normalize("NFKD", str(value)).casefold()
    normalized = "".join(ch for ch in normalized if not unicodedata.combining(ch))
    return "".join(ch for ch in normalized if ch.isalnum())


def assess_example_quality(row) -> QualityAssessment:
    """Run deterministic, pre-extraction checks over one source example.

    Errors mean the row cannot provide a fair, machine-scoreable benchmark item.
    Warnings identify annotation/surface-form risks that should remain visible to a
    reviewer but are too ambiguous to justify silently deleting the example.
    """
    issues: list[QualityIssue] = []

    def issue(code: str, severity: str, message: str) -> None:
        issues.append(QualityIssue(code, severity, message))

    question = str(row.get("question", "")).strip()
    answer = str(row.get("answer", "")).strip()
    if not question:
        issue("empty_question", "error", "Question is empty.")
    if not answer:
        issue("empty_answer", "error", "Gold answer is empty.")

    try:
        context = _json_list(row.get("context"), "context")
    except (TypeError, ValueError, json.JSONDecodeError) as exc:
        issue("invalid_context", "error", str(exc))
        context = []
    try:
        supporting = _json_list(row.get("supporting_facts"), "supporting_facts")
    except (TypeError, ValueError, json.JSONDecodeError) as exc:
        issue("invalid_supporting_facts", "error", str(exc))
        supporting = []
    try:
        evidences = _json_list(row.get("evidences"), "evidences")
    except (TypeError, ValueError, json.JSONDecodeError) as exc:
        issue("invalid_evidences", "error", str(exc))
        evidences = []

    documents: dict[str, list[str]] = {}
    for pos, document in enumerate(context):
        if (
            not isinstance(document, list)
            or len(document) != 2
            or not isinstance(document[0], str)
            or not isinstance(document[1], list)
            or not all(isinstance(sentence, str) for sentence in document[1])
        ):
            issue("malformed_context_document", "error", f"context[{pos}] has an invalid shape.")
            continue
        documents[document[0]] = document[1]

    if not supporting:
        issue("empty_supporting_facts", "error", "No supporting facts are supplied.")
    supporting_text: list[str] = []
    for pos, fact in enumerate(supporting):
        if not isinstance(fact, list) or len(fact) != 2 or not isinstance(fact[0], str):
            issue("malformed_supporting_fact", "error", f"supporting_facts[{pos}] has an invalid shape.")
            continue
        title, sentence_index = fact
        sentences = documents.get(title)
        if sentences is None:
            issue("missing_support_document", "error", f"Supporting document {title!r} is absent from context.")
        elif not isinstance(sentence_index, int) or not 0 <= sentence_index < len(sentences):
            issue("invalid_support_index", "error", f"Supporting sentence {title!r}[{sentence_index!r}] does not exist.")
        else:
            supporting_text.extend((title, sentences[sentence_index]))

    valid_evidences = []
    if not evidences:
        issue("empty_evidences", "error", "No gold evidence triples are supplied.")
    for pos, triple in enumerate(evidences):
        if not isinstance(triple, list) or len(triple) != 3 or not all(isinstance(v, str) and v.strip() for v in triple):
            issue("malformed_evidence", "error", f"evidences[{pos}] is not a non-empty string triple.")
            continue
        subject, relation, obj = (value.strip() for value in triple)
        valid_evidences.append((subject, relation, obj))
        if relation not in RELATION_TO_ONTOLOGY_PROPERTY:
            issue("unmapped_relation", "error", f"Relation {relation!r} is not representable by the ontology mapping.")
        if relation in DATE_LITERAL_RELATIONS:
            try:
                normalize_date(obj, str(row.get("_id", "unknown")), relation)
            except ValueError as exc:
                issue("invalid_date_literal", "error", str(exc))

    answer_key = _surface_key(answer)
    evidence_term_keys = {
        _surface_key(term)
        for subject, _, obj in valid_evidences
        for term in (subject, obj)
    }
    if answer_key and answer_key not in evidence_term_keys and answer_key not in {"yes", "no"}:
        issue(
            "answer_not_licensed_by_evidence",
            "error",
            "Gold answer is neither an evidence endpoint nor a yes/no conclusion.",
        )

    context_key = _surface_key(" ".join(
        part for title, sentences in documents.items() for part in (title, *sentences)
    ))
    support_key = _surface_key(" ".join(supporting_text))
    if answer_key not in {"yes", "no"}:
        if answer_key and answer_key not in context_key:
            issue("answer_not_supported_by_context", "error", "Gold answer has no normalized mention in the supplied context.")
        elif answer_key and answer_key not in support_key:
            issue("answer_not_supported_by_support", "error", "Gold answer has no normalized mention in the annotated supporting facts.")
    for term in sorted({term for subject, _, obj in valid_evidences for term in (subject, obj)}):
        key = _surface_key(term)
        if key and key not in context_key:
            issue("evidence_term_not_in_context", "warning", f"Evidence term {term!r} has no direct normalized context mention.")
        if key and key not in support_key:
            issue("evidence_term_not_in_support", "warning", f"Evidence term {term!r} has no direct normalized supporting-fact mention.")

    severities = {item.severity for item in issues}
    status = "reject" if "error" in severities else "review" if "warning" in severities else "pass"
    return QualityAssessment(status, tuple(issues))


def slugify(text: str) -> str:
    """Turn an entity string into a URI-safe local name."""
    text = text.strip()
    text = re.sub(r"[^\w]+", "_", text, flags=re.UNICODE)
    text = re.sub(r"_+", "_", text).strip("_")
    return text or "unnamed"


def canonical_entity_key(text: str) -> str:
    """Identify spelling-only variants of one evidence entity.

    The 2Wiki evidence list can spell the same entity with different case or
    punctuation in separate triples (for example ``the_Younger`` versus
    ``the_younger``).  Minting a URI independently for every occurrence splits
    one reasoning chain into two ground-truth nodes.  This deliberately
    conservative key removes only presentation differences; it does not try to
    infer semantic aliases such as ``Bolivia`` and ``Bolivian``.
    """
    normalized = unicodedata.normalize("NFKD", text).casefold()
    normalized = "".join(ch for ch in normalized if not unicodedata.combining(ch))
    return "".join(ch for ch in normalized if ch.isalnum())


def conservative_country_stem(text: str) -> str:
    """Collapse only regular country/demonym morphology found in one example.

    This is not a world-country lookup.  It only supplies a second key used when
    two country-valued evidence objects occur together, such as Bolivia/Bolivian.
    Irregular pairs (France/French, United States/American) remain the entity
    matcher's responsibility.
    """
    key = canonical_entity_key(text)
    for suffix in ("ian", "an"):
        if len(key) > len(suffix) + 3 and key.endswith(suffix):
            return key[: -len(suffix)]
    for suffix in ("ia", "a"):
        if len(key) > len(suffix) + 3 and key.endswith(suffix):
            return key[: -len(suffix)]
    return key


def turtle_escape(text: str) -> str:
    return text.replace("\\", "\\\\").replace('"', '\\"').replace("\n", " ").strip()


# --------------------------------------------------------------------------
# Date normalization for DATE_LITERAL_RELATIONS.
#
# extraction_agent.py's prompt instructs the LLM: "Write date attributes in
# ISO form: YYYY-MM-DD when a complete date is known, or exactly four digits
# (YYYY) when only the year is known. Zero-pad years below 1000 to four
# digits." Its own validator (_validate_date_value) rejects anything else.
#
# The raw 2wiki `evidences` field does NOT come in that form -- surveying the
# full dev.parquet split, every date-relation value falls into exactly one of
# three patterns: "YYYY", "D Month YYYY" (e.g. "12 June 1516"), or
# "Month D, YYYY" (e.g. "March 20, 1995"). None of these is ISO-8601, so even
# a perfectly correct extraction (which will be ISO-formatted, per the prompt
# above) could never exact-match a ground-truth literal carrying the raw
# 2wiki text -- independent of, and in addition to, the missing-XSD-datatype
# issue that _date_literal_term() below fixes.
# --------------------------------------------------------------------------
_YEAR_ONLY = re.compile(r"^\d{1,4}$")
_D_MONTH_Y = re.compile(r"^(\d{1,2}) ([A-Za-z]+) (\d{1,4})$")
_MONTH_D_Y = re.compile(r"^([A-Za-z]+) (\d{1,2}), (\d{1,4})$")

_MONTH_NAME_TO_NUM = {
    name: i
    for i, name in enumerate(
        [
            "January", "February", "March", "April", "May", "June",
            "July", "August", "September", "October", "November", "December",
        ],
        start=1,
    )
}


def normalize_date(raw: str, ex_id: str, rel: str) -> str:
    """Normalize a raw 2wiki date string to ISO-8601 (YYYY-MM-DD or YYYY).

    Raises ValueError rather than passing an unrecognized format through
    unchanged -- an un-normalized value would silently reintroduce the exact
    same ground-truth/extraction mismatch this function exists to close, just
    less visibly than before.
    """
    raw = raw.strip()

    if _YEAR_ONLY.fullmatch(raw):
        return raw.zfill(4)

    for pattern, order in ((_D_MONTH_Y, ("day", "month", "year")),
                            (_MONTH_D_Y, ("month", "day", "year"))):
        m = pattern.fullmatch(raw)
        if not m:
            continue
        parts = dict(zip(order, m.groups()))
        month_num = _MONTH_NAME_TO_NUM.get(parts["month"])
        if month_num is None:
            raise ValueError(
                f"[{ex_id}] unrecognized month name {parts['month']!r} in "
                f"{rel!r} value {raw!r}"
            )
        iso = f"{int(parts['year']):04d}-{month_num:02d}-{int(parts['day']):02d}"
        try:
            date_cls.fromisoformat(iso)
        except ValueError as exc:
            raise ValueError(
                f"[{ex_id}] {rel!r} value {raw!r} normalizes to invalid "
                f"calendar date {iso!r}"
            ) from exc
        return iso

    raise ValueError(
        f"[{ex_id}] date value {raw!r} for relation {rel!r} doesn't match any "
        f"known 2wiki date format (YYYY / 'D Month YYYY' / 'Month D, YYYY'). "
        f"Extend normalize_date() to handle this new format rather than "
        f"passing it through unnormalized."
    )


def _date_literal_term(iso_value: str) -> str:
    """Mirror kg_builder_agent._typed_literal's date_or_year branch exactly,
    so ground-truth literals carry the same XSD datatype a correct extraction
    would produce (Literal('1990') != Literal('1990', datatype=XSD.gYear) in
    rdflib, and triple_matching.py does exact RDF-term set intersection)."""
    if re.fullmatch(r"\d{4}", iso_value):
        return f'"{iso_value}"^^xsd:gYear'
    if re.fullmatch(r"\d{4}-\d{2}-\d{2}", iso_value):
        return f'"{iso_value}"^^xsd:date'
    raise ValueError(f"normalize_date produced a non-ISO value: {iso_value!r}")


def parse_context(context_raw: str) -> str:
    """context field: [[title, [sent1, sent2, ...]], ...] -> readable text."""
    paragraphs = json.loads(context_raw)
    blocks = []
    for title, sentences in paragraphs:
        body = " ".join(s.strip() for s in sentences)
        blocks.append(f"{title}\n{body}")
    return "\n\n".join(blocks)


def evidences_to_ttl(evidences_raw: str, ex_id: str):
    """Returns (ttl_text, used_relations).

    Every relation in the source evidences MUST have a corresponding
    ontology property in RELATION_TO_ONTOLOGY_PROPERTY. If one is missing,
    this raises rather than silently dropping the triple or writing a fake
    fallback predicate -- because an LLM extracting against this ontology
    has no predicate slot for an unmapped relation, so any gap here means
    the ontology needs a new property added (see ontology.ttl), not a code
    change here.
    """
    triples = json.loads(evidences_raw)
    country_spellings: dict[str, str] = {}
    for candidate in triples:
        if len(candidate) == 3 and candidate[1] in COUNTRY_OBJECT_RELATIONS:
            obj = candidate[2]
            country_spellings.setdefault(conservative_country_stem(obj), obj)
    lines = [
        "@prefix ex:   <%s> ." % ONTOLOGY_NS,
        "@prefix inst: <%s> ." % INSTANCE_NS,
        "@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .",
        "@prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .",
        "",
        f"# Silver ground-truth triples for {ex_id}",
        f"# Source: 2WikiMultihopQA dev split, evidences field",
        f"# Predicates use this project's ontology (see ontology.ttl)",
        "",
    ]
    used_relations = set()
    # Reuse the first URI spelling for every exact presentation variant within
    # this example.  Subjects and objects share the same table so a bridge
    # entity remains connected across evidence triples.
    canonical_uris: dict[str, str] = {}

    def entity_term(label: str, *, country_object: bool = False) -> str:
        if country_object:
            label = country_spellings[conservative_country_stem(label)]
        key = canonical_entity_key(label)
        canonical_uris.setdefault(key, slugify(label))
        return f"inst:{canonical_uris[key]}"

    for triple in triples:
        if len(triple) != 3:
            continue
        subj, rel, obj = triple
        prop = RELATION_TO_ONTOLOGY_PROPERTY.get(rel)
        if prop is None:
            raise ValueError(
                f"[{ex_id}] relation '{rel}' has no ontology property mapping. "
                f"Add a matching property (with skos:exactMatch to the relevant "
                f"Wikidata P-code, if one exists) to ontology.ttl, then add "
                f"'{rel}' -> 'ex:hasWhatever' to RELATION_TO_ONTOLOGY_PROPERTY."
            )

        used_relations.add(rel)
        subj_uri = entity_term(subj)
        pred = prop

        if rel in DATE_LITERAL_RELATIONS:
            iso_value = normalize_date(obj, ex_id, rel)
            obj_term = _date_literal_term(iso_value)
        else:
            obj_term = entity_term(obj, country_object=rel in COUNTRY_OBJECT_RELATIONS)

        lines.append(f'{subj_uri} {pred} {obj_term} .  # {rel} -> "{obj}"'
                      if rel in DATE_LITERAL_RELATIONS else
                      f'{subj_uri} {pred} {obj_term} .  # {rel}')

    return "\n".join(lines) + "\n", used_relations


def select_examples(df: pd.DataFrame, n_target: int, seed: int = 42):
    random.seed(seed)

    rel_counter = Counter()
    rows_per_rel = defaultdict(list)
    row_rels = {}

    for idx, row in df.iterrows():
        ev = json.loads(row["evidences"])
        rels = set()
        for triple in ev:
            if len(triple) == 3:
                rel_counter[triple[1]] += 1
                rels.add(triple[1])
        row_rels[idx] = rels
        for r in rels:
            rows_per_rel[r].append(idx)

    all_relations = sorted(rel_counter.keys())

    quotas = {}
    for r in all_relations:
        n = len(rows_per_rel[r])
        if n <= 30:
            q = n
        else:
            q = int(round(3 * math.sqrt(n)))
            q = max(20, min(q, 120))
        quotas[r] = q

    selected = set()
    remaining_quota = dict(quotas)
    rel_order = sorted(all_relations, key=lambda r: len(rows_per_rel[r]))

    for r in rel_order:
        need = remaining_quota[r]
        if need <= 0:
            continue
        candidates = [i for i in rows_per_rel[r] if i not in selected]
        random.shuffle(candidates)

        def score(i):
            return sum(1 for rr in row_rels[i] if remaining_quota.get(rr, 0) > 0)

        candidates.sort(key=score, reverse=True)
        take = candidates[:need]
        for i in take:
            selected.add(i)
            for rr in row_rels[i]:
                remaining_quota[rr] = remaining_quota.get(rr, 0) - 1

    if len(selected) < n_target:
        pool = [i for i in df.index if i not in selected]
        random.shuffle(pool)
        selected.update(pool[: n_target - len(selected)])
    elif len(selected) > n_target:
        # carrier_count is kept LIVE and decremented on every removal below,
        # rather than computed once from a static snapshot. Removing a row can
        # make a *different* row newly unsafe to remove (it may hold the last
        # remaining carrier of some relation that the first removal thinned
        # out to 1) -- so "safe to remove" has to be rechecked after each
        # individual removal, not decided for a whole batch up front from one
        # pre-removal count.
        carrier_count = Counter()
        for i in selected:
            for rr in row_rels[i]:
                carrier_count[rr] += 1

        sel_list = list(selected)
        random.shuffle(sel_list)
        excess = len(selected) - n_target
        removed = 0
        for i in sel_list:
            if removed >= excess:
                break
            if all(carrier_count[rr] > 1 for rr in row_rels[i]):
                selected.remove(i)
                for rr in row_rels[i]:
                    carrier_count[rr] -= 1
                removed += 1
        # If every remaining row is the sole surviving carrier of at least one
        # relation, there may not be `excess` rows that were ever safe to cut.
        # Deliberately do NOT fall back to a row-index truncation here (the
        # old `sorted(selected)[:n_target]` step) -- that has no notion of
        # which relations it would be discarding and can silently drop a rare
        # relation's only carrier. Returning more than n_target rows in this
        # rare case is intentional: main()'s post-hoc coverage check still
        # runs either way, and preserving full relation coverage takes
        # priority over hitting the exact target count. If this happens,
        # rerun with a larger --n or a different --seed to get an exact-count
        # sample instead.

    return sorted(selected), row_rels, all_relations


def select_primary_and_reserve(
    df: pd.DataFrame, n_primary: int, n_reserve: int, seed: int = 42
):
    """Select a coverage-complete primary set before appending reserves.

    Sampling ``n_primary + n_reserve`` jointly and then treating its first
    ``n_primary`` rows as primaries does not guarantee that those first rows
    retain every relation.  Select the fixed benchmark first, then append
    distinct rows from a larger coverage-aware sample and finally deterministic
    unused rows if necessary.
    """
    primary, row_rels, all_relations = select_examples(df, n_primary, seed)
    if n_reserve == 0:
        return primary, row_rels, all_relations
    expanded, _, _ = select_examples(df, n_primary + n_reserve, seed)
    primary_set = set(primary)
    reserves = [idx for idx in expanded if idx not in primary_set]
    if len(reserves) < n_reserve:
        reserves.extend(
            idx
            for idx in range(len(df))
            if idx not in primary_set and idx not in set(reserves)
        )
    return primary + reserves[:n_reserve], row_rels, all_relations


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", default="data/dev.parquet", help="path to dev.parquet")
    ap.add_argument("--out", default="data", help="output root folder")
    ap.add_argument("--n", type=int, default=1000, help="number of examples to select")
    ap.add_argument(
        "--reserve",
        type=int,
        default=0,
        help="additional candidate examples to extract as replacements for unusable graphs",
    )
    ap.add_argument("--seed", type=int, default=42)
    ap.add_argument(
        "--include-review",
        action=argparse.BooleanOptionalAction,
        default=True,
        help="Allow warning-only examples into the candidate pool (default: true).",
    )
    args = ap.parse_args()

    df = pd.read_parquet(args.input).reset_index(drop=True)
    if args.n <= 0 or args.reserve < 0:
        raise SystemExit("--n must be positive and --reserve must be non-negative")
    assessments = [assess_example_quality(row) for _, row in df.iterrows()]
    quality_counts = Counter(assessment.status for assessment in assessments)
    eligible_statuses = {"pass", "review"} if args.include_review else {"pass"}
    eligible_positions = [
        position
        for position, assessment in enumerate(assessments)
        if assessment.status in eligible_statuses
    ]
    required = args.n + args.reserve
    if len(eligible_positions) < required:
        raise SystemExit(
            f"Only {len(eligible_positions)} quality-eligible rows remain, but {required} "
            "primary + reserve examples were requested."
        )
    eligible_df = df.iloc[eligible_positions].copy().reset_index(drop=True)
    eligible_df["_source_position"] = eligible_positions
    selected, row_rels, all_relations = select_primary_and_reserve(
        eligible_df, args.n, args.reserve, args.seed
    )

    print(
        f"Quality audit: pass={quality_counts['pass']} review={quality_counts['review']} "
        f"reject={quality_counts['reject']}; eligible={len(eligible_df)}."
    )
    print(f"Loaded {len(df)} rows, selected {len(selected)} covering "
          f"{len(all_relations)} relations.")

    # Verify every relation in the source data actually survived into the
    # final sampled set. The rare-first quota logic plus the live-recount
    # trim step in select_examples() are designed to guarantee this, but
    # check for real rather than assuming the design intent held -- e.g. if
    # every remaining row is the sole carrier of some relation, trimming down
    # to exactly n_target may not be possible at all.
    covered_relations = set()
    for idx in selected[: args.n]:
        covered_relations |= row_rels[idx]
    missing_after_sampling = sorted(set(all_relations) - covered_relations)
    if missing_after_sampling:
        print(
            f"ERROR: {len(missing_after_sampling)} relation(s) present in the "
            f"source data did NOT survive into the final {len(selected)}-example "
            f"primary sample (likely dropped during the downsizing/trim step):"
        )
        for r in missing_after_sampling:
            print(f"  - {r!r}")
        print(
            "\nThis breaks the 'every relation is represented' guarantee the "
            "sampler is supposed to provide. This can happen if every "
            "remaining row is the sole carrier of some relation, so no "
            "n_target-sized subset can cover them all. Try a different "
            "--seed, or increase --n."
        )
        raise SystemExit(1)

    unmapped = sorted(r for r in all_relations if r not in RELATION_TO_ONTOLOGY_PROPERTY)
    if unmapped:
        print(f"ERROR: {len(unmapped)} relation(s) in the selected examples have no "
              f"ontology property mapping:")
        for r in unmapped:
            print(f"  - {r!r}")
        print(
            "\nAdd a matching ex:hasX property (with skos:exactMatch to the "
            "relevant wdt:Pxxx, if one exists) to ontology.ttl for each of these, "
            "then add the relation -> property pair to RELATION_TO_ONTOLOGY_PROPERTY "
            "in this script. Aborting before writing any silver files."
        )
        raise SystemExit(1)

    out_root = Path(args.out)
    out_root.mkdir(parents=True, exist_ok=True)
    manifest_path = out_root / "manifest.csv"
    quality_report_path = out_root / "quality_report.jsonl"
    quality_summary_path = out_root / "quality_summary.json"

    with quality_report_path.open("w", encoding="utf-8") as report:
        for position, (assessment, (_, row)) in enumerate(zip(assessments, df.iterrows())):
            payload = {
                "source_position": position,
                "original_id": str(row["_id"]),
                "type": str(row["type"]),
                "status": assessment.status,
                "issues": [asdict(item) for item in assessment.issues],
            }
            report.write(json.dumps(payload, ensure_ascii=False) + "\n")
    issue_counts = Counter(
        (item.severity, item.code)
        for assessment in assessments
        for item in assessment.issues
    )
    quality_summary_path.write_text(
        json.dumps(
            {
                "source_examples": len(df),
                "status_counts": dict(sorted(quality_counts.items())),
                "eligible_statuses": sorted(eligible_statuses),
                "eligible_examples": len(eligible_df),
                "issue_counts": [
                    {"severity": severity, "code": code, "count": count}
                    for (severity, code), count in sorted(issue_counts.items())
                ],
            },
            ensure_ascii=False,
            indent=2,
        ) + "\n",
        encoding="utf-8",
    )

    with open(manifest_path, "w", newline="", encoding="utf-8") as mf:
        writer = csv.writer(mf)
        writer.writerow([
            "example_id", "original_id", "type", "relations", "candidate_role",
            "quality_status", "quality_issue_codes",
        ])

        for i, idx in enumerate(selected, start=1):
            row = eligible_df.loc[idx]
            source_position = int(row["_source_position"])
            assessment = assessments[source_position]
            ex_name = f"example{i}"       # used only for the manifest / evidences_to_ttl's comment header
            ex_dir = out_root / str(i)    # pipeline expects a numeric-id folder, e.g. pilot/3/
            ex_dir.mkdir(parents=True, exist_ok=True)

            # context .txt -- pipeline's _TEXT_PATTERN requires exactly text_N.txt
            context_text = parse_context(row["context"])
            (ex_dir / f"text_{i}.txt").write_text(context_text, encoding="utf-8")

            # ground-truth .ttl -- pipeline/reasoner expect exactly ground_truth_N.ttl
            ttl_text, used_rels = evidences_to_ttl(row["evidences"], ex_name)
            (ex_dir / f"ground_truth_{i}.ttl").write_text(ttl_text, encoding="utf-8")

            # question .txt -- pipeline globs "*_question.txt", so any prefix works
            (ex_dir / f"{ex_name}_question.txt").write_text(
                row["question"].strip() + "\n", encoding="utf-8"
            )

            # answer .txt -- not read by the pipeline, naming is free
            (ex_dir / f"{ex_name}_answer.txt").write_text(
                str(row["answer"]).strip() + "\n", encoding="utf-8"
            )

            # Preserve the source annotations verbatim enough to audit how the
            # normalized RDF gold graph was derived.
            (ex_dir / f"{ex_name}_evidences.json").write_text(
                json.dumps(_json_list(row["evidences"], "evidences"), ensure_ascii=False, indent=2) + "\n",
                encoding="utf-8",
            )
            (ex_dir / f"{ex_name}_supporting_facts.json").write_text(
                json.dumps(
                    _json_list(row["supporting_facts"], "supporting_facts"),
                    ensure_ascii=False,
                    indent=2,
                ) + "\n",
                encoding="utf-8",
            )

            writer.writerow([
                str(i),
                row["_id"],
                row["type"],
                "|".join(sorted(used_rels)),
                "primary" if i <= args.n else "reserve",
                assessment.status,
                "|".join(item.code for item in assessment.issues),
            ])

    print(f"Done. Wrote {len(selected)} example folders under '{out_root}/'")
    print(f"Manifest: {manifest_path}")
    print(f"Quality report: {quality_report_path}")
    print(f"Quality summary: {quality_summary_path}")


if __name__ == "__main__":
    main()
