#!/usr/bin/env python3
"""Paired exact-triple evaluation before and after ontology inference."""

from __future__ import annotations

import argparse
import json
import re
import statistics
import tempfile
from pathlib import Path

from evaluation_scope import graph_evaluation_exclusion
from urllib.parse import unquote, urlsplit

from rdflib import Graph, Literal, RDF, URIRef
from rdflib.namespace import XSD


ROOT = Path(__file__).resolve().parent
ONTOLOGY_NAMESPACE = "http://example.org/2wiki-ontology#"
HAS_COUNTRY = URIRef(ONTOLOGY_NAMESPACE + "hasCountry")
COUNTRY_RELATION_PREDICATES = {
    HAS_COUNTRY,
    URIRef(ONTOLOGY_NAMESPACE + "hasCitizenship"),
    URIRef(ONTOLOGY_NAMESPACE + "hasNationality"),
    URIRef(ONTOLOGY_NAMESPACE + "hasCountryOfOrigin"),
}
HAS_PARENT = URIRef(ONTOLOGY_NAMESPACE + "hasParent")
HAS_CHILD = URIRef(ONTOLOGY_NAMESPACE + "hasChild")
HAS_SIBLING = URIRef(ONTOLOGY_NAMESPACE + "hasSibling")
FAMILY_PARENT_PREDICATES = {
    HAS_PARENT,
    URIRef(ONTOLOGY_NAMESPACE + "hasFather"),
    URIRef(ONTOLOGY_NAMESPACE + "hasMother"),
    URIRef(ONTOLOGY_NAMESPACE + "isSonOf"),
    URIRef(ONTOLOGY_NAMESPACE + "isDaughterOf"),
}
FAMILY_CHILD_PREDICATES = {
    HAS_CHILD,
    URIRef(ONTOLOGY_NAMESPACE + "hasSon"),
    URIRef(ONTOLOGY_NAMESPACE + "hasDaughter"),
}
FAMILY_SIBLING_PREDICATES = {
    HAS_SIBLING,
    URIRef(ONTOLOGY_NAMESPACE + "hasBrother"),
    URIRef(ONTOLOGY_NAMESPACE + "hasSister"),
    URIRef(ONTOLOGY_NAMESPACE + "isBrotherOf"),
    URIRef(ONTOLOGY_NAMESPACE + "isSisterOf"),
}
DATE_PREDICATES = {
    URIRef(ONTOLOGY_NAMESPACE + "hasBirthDate"),
    URIRef(ONTOLOGY_NAMESPACE + "hasDeathDate"),
    URIRef(ONTOLOGY_NAMESPACE + "hasPublicationDate"),
    URIRef(ONTOLOGY_NAMESPACE + "hasInception"),
}


def parse_ids(value: str) -> list[int]:
    result = set()
    for part in value.split(","):
        part = part.strip()
        if not part:
            continue
        if "-" in part:
            start, end = map(int, part.split("-", 1))
            if start < 0 or end < start:
                raise argparse.ArgumentTypeError(f"Invalid range: {part}")
            result.update(range(start, end + 1))
        else:
            result.add(int(part))
    if not result or min(result) < 0:
        raise argparse.ArgumentTypeError("IDs must be non-negative")
    return sorted(result)


def local_name(term) -> str:
    value = str(term)
    split = urlsplit(value)
    name = split.fragment or split.path.rsplit("/", 1)[-1]
    return unquote(name)


def render_term(term, *, predicate=False) -> str:
    if predicate and term == RDF.type:
        return "type"
    if isinstance(term, Literal):
        return term.n3()
    if isinstance(term, URIRef):
        return local_name(term)
    return str(term)


def triple_sort_key(triple):
    return tuple(str(value) for value in triple)


def rendered_triples(triples) -> list[dict[str, str]]:
    return [
        {
            "subject": render_term(subject),
            "predicate": render_term(predicate, predicate=True),
            "object": render_term(obj),
            "subject_uri": str(subject),
            "predicate_uri": str(predicate),
            "object_term": obj.n3() if isinstance(obj, Literal) else str(obj),
        }
        for subject, predicate, obj in sorted(triples, key=triple_sort_key)
    ]


def canonicalize_evaluation_graph(graph: Graph, *, semantic_projection: bool = True) -> set[tuple]:
    """Normalize RDF representation, optionally projecting benchmark semantics.

    String normalization is representational. Country/family predicate projection is
    semantic and can overlap with ontology inference, so callers must select it
    explicitly and reports record the selected scoring profile.
    """
    canonical = set()
    for subject, predicate, obj in graph:
        if semantic_projection:
            if predicate in COUNTRY_RELATION_PREDICATES:
                predicate = HAS_COUNTRY
            elif predicate in FAMILY_PARENT_PREDICATES:
                predicate = HAS_PARENT
            elif predicate in FAMILY_CHILD_PREDICATES:
                predicate = HAS_CHILD
            elif predicate in FAMILY_SIBLING_PREDICATES:
                predicate = HAS_SIBLING
        if isinstance(obj, Literal) and (
            obj.datatype is None
            or str(obj.datatype) == "http://www.w3.org/2001/XMLSchema#string"
        ):
            obj = Literal(str(obj))
        canonical.add((subject, predicate, obj))
    return canonical


def _date_year(value: Literal) -> str | None:
    text = str(value)
    if value.datatype == XSD.gYear and re.fullmatch(r"\d{4}", text):
        return text
    if value.datatype == XSD.date and re.fullmatch(r"\d{4}-\d{2}-\d{2}", text):
        return text[:4]
    return None


def align_compatible_date_precision(
    extracted: set[tuple], ground_truth: set[tuple]
) -> tuple[set[tuple], set[tuple]]:
    """Align YYYY with YYYY-MM-DD only where one graph claims year precision.

    Two full dates remain exact and therefore still expose wrong month/day values. The
    alignment is scoped to the same canonical subject and predicate, so unrelated dates
    cannot match merely because they share a year.
    """
    year_precision_keys = {
        (subject, predicate)
        for graph in (extracted, ground_truth)
        for subject, predicate, obj in graph
        if predicate in DATE_PREDICATES
        and isinstance(obj, Literal)
        and obj.datatype == XSD.gYear
        and _date_year(obj) is not None
    }

    def aligned(graph: set[tuple]) -> set[tuple]:
        result = set()
        for subject, predicate, obj in graph:
            if (
                (subject, predicate) in year_precision_keys
                and isinstance(obj, Literal)
                and (year := _date_year(obj)) is not None
            ):
                obj = Literal(year, datatype=XSD.gYear)
            result.add((subject, predicate, obj))
        return result

    return aligned(extracted), aligned(ground_truth)


def compare_graphs(
    extracted_path: Path,
    ground_truth_path: Path,
    accepted_pairs: int,
    *,
    scoring_profile: str = "projected",
) -> dict:
    if scoring_profile not in {"strict", "projected"}:
        raise ValueError(f"Unsupported scoring profile: {scoring_profile}")
    semantic_projection = scoring_profile == "projected"
    extracted = canonicalize_evaluation_graph(
        Graph().parse(extracted_path, format="turtle"),
        semantic_projection=semantic_projection,
    )
    ground_truth = canonicalize_evaluation_graph(
        Graph().parse(ground_truth_path, format="turtle"),
        semantic_projection=semantic_projection,
    )
    extracted, ground_truth = align_compatible_date_precision(extracted, ground_truth)
    matched = extracted & ground_truth
    extracted_only = extracted - ground_truth
    ground_truth_only = ground_truth - extracted
    tp, fp, fn = len(matched), len(extracted_only), len(ground_truth_only)
    precision = tp / (tp + fp) if tp + fp else 0.0
    recall = tp / (tp + fn) if tp + fn else 0.0
    f1 = 2 * precision * recall / (precision + recall) if precision + recall else 0.0
    return {
        "inputs": {"extracted": str(extracted_path), "ground_truth": str(ground_truth_path)},
        "scoring_profile": scoring_profile,
        "semantic_projection": semantic_projection,
        "comparison": (
            "exact RDF term equality after entity canonicalization, string/date representation "
            + ("normalization, and family/country semantic projection" if semantic_projection else "normalization only; no semantic predicate projection")
        ),
        "matched_triples": rendered_triples(matched),
        "ground_truth_only_triples": rendered_triples(ground_truth_only),
        "extracted_only_triples": rendered_triples(extracted_only),
        "metrics": {
            "accepted_entity_pairs": accepted_pairs,
            "extracted_triples_in_scope": len(extracted),
            "ground_truth_triples_in_scope": len(ground_truth),
            "union_triples_in_scope": len(extracted | ground_truth),
            "true_positives": tp,
            "false_positives": fp,
            "false_negatives": fn,
            "precision": precision,
            "recall": recall,
            "f1": f1,
        },
    }


def escape_cell(value: str) -> str:
    return value.replace("|", "\\|").replace("\n", " ")


def table(rows: list[dict[str, str]]) -> list[str]:
    lines = ["| Subject | Predicate | Object |", "|---|---|---|"]
    lines.extend(
        f"| {escape_cell(row['subject'])} | {escape_cell(row['predicate'])} | {escape_cell(row['object'])} |"
        for row in rows
    )
    return lines


def markdown_report(index: int, payload: dict) -> str:
    matched = payload["matched_triples"]
    gt_only = payload["ground_truth_only_triples"]
    extracted_only = payload["extracted_only_triples"]
    metrics = payload["metrics"]
    lines = [
        f"# Triple matching report: {index}", "",
        "# 1. Matched triples", "", f"**Count: {len(matched)}**", "", *table(matched), "",
        "# 2. Unmatched triples", "",
        f"**Total unmatched count: {len(gt_only) + len(extracted_only)}**", "",
        "## 2.1 Ground-truth-only triples", "", f"**Count: {len(gt_only)}**", "", *table(gt_only), "",
        "## 2.2 Extracted-only triples", "", f"**Count: {len(extracted_only)}**", "", *table(extracted_only), "",
        "# 3. Scope metrics", "",
        "| Metric | Value |", "|---|---:|",
        f"| Accepted entity pairs | {metrics['accepted_entity_pairs']} |",
        f"| Extracted triples in scope | {metrics['extracted_triples_in_scope']} |",
        f"| Ground-truth triples in scope | {metrics['ground_truth_triples_in_scope']} |",
        f"| Union triples in scope | {metrics['union_triples_in_scope']} |",
        f"| True positives (matched) | {metrics['true_positives']} |",
        f"| False positives (extracted-only) | {metrics['false_positives']} |",
        f"| False negatives (ground-truth-only) | {metrics['false_negatives']} |",
        f"| Precision | {metrics['precision']:.6f} |",
        f"| Recall | {metrics['recall']:.6f} |",
        f"| F1 score | {metrics['f1']:.6f} |", "",
        "_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._", "",
    ]
    return "\n".join(lines)


def aggregate_markdown(payload: dict) -> str:
    results = payload["results"]
    totals = payload["totals"]
    micro, macro = payload["micro"], payload["macro"]
    lines = [
        "# Overall Triple Matching Report", "",
        "## 1. Overall totals", "",
        "| Metric | Value |", "|---|---:|",
        f"| Evaluated examples | {totals['evaluated_examples']} |",
        f"| Accepted entity pairs | {totals['accepted_entity_pairs']} |",
        f"| Matched triples (TP) | {totals['true_positives']} |",
        f"| Ground-truth-only triples (FN) | {totals['false_negatives']} |",
        f"| Extracted-only triples (FP) | {totals['false_positives']} |",
        f"| Total unmatched triples | {totals['unmatched']} |",
        f"| Extracted triples in scope | {totals['extracted_triples_in_scope']} |",
        f"| Ground-truth triples in scope | {totals['ground_truth_triples_in_scope']} |",
        f"| Union triples in scope | {totals['union_triples_in_scope']} |", "",
        "## 2. Micro-average metrics", "",
        "| Metric | Value |", "|---|---:|",
        f"| Micro precision | {micro['precision']:.6f} |",
        f"| Micro recall | {micro['recall']:.6f} |",
        f"| Micro F1 score | {micro['f1']:.6f} |", "",
        "## 3. Macro-average metrics", "",
        "| Metric | Value |", "|---|---:|",
        f"| Macro precision | {macro['precision']:.6f} |",
        f"| Macro recall | {macro['recall']:.6f} |",
        f"| Macro F1 score | {macro['f1']:.6f} |", "",
        "## 4. Per-example results", "",
        "| Example ID | Entity pairs | Matched | GT-only | Extracted-only | Precision | Recall | F1 |",
        "|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for row in results:
        lines.append(
            f"| {row['id']} | {row['accepted_entity_pairs']} | {row['true_positives']} | "
            f"{row['false_negatives']} | {row['false_positives']} | {row['precision']:.6f} | "
            f"{row['recall']:.6f} | {row['f1']:.6f} |"
        )
    lines.extend([
        f"| **Micro total / score** | **{totals['accepted_entity_pairs']}** | **{totals['true_positives']}** | "
        f"**{totals['false_negatives']}** | **{totals['false_positives']}** | **{micro['precision']:.6f}** | "
        f"**{micro['recall']:.6f}** | **{micro['f1']:.6f}** |",
        f"| **Macro average** | — | — | — | — | **{macro['precision']:.6f}** | "
        f"**{macro['recall']:.6f}** | **{macro['f1']:.6f}** |", "",
        "## 5. Distribution summary", "",
        "| Metric | Mean | Median | Population SD | Minimum | Maximum |",
        "|---|---:|---:|---:|---|---|",
    ])
    labels = (("Precision", "precision"), ("Recall", "recall"), ("F1 score", "f1"))
    for label, key in labels:
        values = [row[key] for row in results]
        minimum = min(results, key=lambda row: (row[key], row["id"]))
        maximum = max(results, key=lambda row: (row[key], -row["id"]))
        lines.append(
            f"| {label} | {statistics.mean(values):.6f} | {statistics.median(values):.6f} | "
            f"{statistics.pstdev(values):.6f} | {minimum[key]:.6f} (ID {minimum['id']}) | "
            f"{maximum[key]:.6f} (ID {maximum['id']}) |"
        )
    highest_fp = max(results, key=lambda row: (row["false_positives"], -row["id"]))
    highest_fn = max(results, key=lambda row: (row["false_negatives"], -row["id"]))
    lines.extend([
        "", "| Error concentration | Example ID | Count |", "|---|---:|---:|",
        f"| Highest extracted-only count | {highest_fp['id']} | {highest_fp['false_positives']} |",
        f"| Highest ground-truth-only count | {highest_fn['id']} | {highest_fn['false_negatives']} |", "",
    ])
    return "\n".join(lines)


def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = None
    try:
        with tempfile.NamedTemporaryFile("w", encoding="utf-8", dir=path.parent, delete=False) as handle:
            handle.write(content)
            temporary = Path(handle.name)
        temporary.replace(path)
    finally:
        if temporary and temporary.exists():
            temporary.unlink()


def aggregate_results(summaries: list[dict], stage: str) -> dict:
    """Aggregate one fixed cohort at one graph stage."""
    micro_tp = sum(row["true_positives"] for row in summaries)
    micro_fp = sum(row["false_positives"] for row in summaries)
    micro_fn = sum(row["false_negatives"] for row in summaries)
    micro_p = micro_tp / (micro_tp + micro_fp) if micro_tp + micro_fp else 0.0
    micro_r = micro_tp / (micro_tp + micro_fn) if micro_tp + micro_fn else 0.0
    micro_f1 = 2 * micro_p * micro_r / (micro_p + micro_r) if micro_p + micro_r else 0.0
    return {
        "stage": stage,
        "examples": len(summaries),
        "results": summaries,
        "totals": {
            "evaluated_examples": len(summaries),
            "accepted_entity_pairs": sum(row["accepted_entity_pairs"] for row in summaries),
            "true_positives": micro_tp,
            "false_positives": micro_fp,
            "false_negatives": micro_fn,
            "unmatched": micro_fp + micro_fn,
            "extracted_triples_in_scope": sum(row["extracted_triples_in_scope"] for row in summaries),
            "ground_truth_triples_in_scope": sum(row["ground_truth_triples_in_scope"] for row in summaries),
            "union_triples_in_scope": sum(row["union_triples_in_scope"] for row in summaries),
        },
        "micro": {
            "true_positives": micro_tp,
            "false_positives": micro_fp,
            "false_negatives": micro_fn,
            "precision": micro_p,
            "recall": micro_r,
            "f1": micro_f1,
        },
        "macro": {
            key: sum(row[key] for row in summaries) / len(summaries) if summaries else 0.0
            for key in ("precision", "recall", "f1")
        },
    }


def paired_inference_delta(pre: dict, post: dict) -> dict:
    """Calculate paired changes; both inputs must contain the identical cohort."""
    pre_by_id = {row["id"]: row for row in pre["results"]}
    post_by_id = {row["id"]: row for row in post["results"]}
    if pre_by_id.keys() != post_by_id.keys():
        raise ValueError("Pre- and post-inference cohorts differ; paired comparison is invalid")
    rows = []
    for index in sorted(pre_by_id):
        before, after = pre_by_id[index], post_by_id[index]
        row = {"id": index}
        for key in ("true_positives", "false_positives", "false_negatives", "precision", "recall", "f1"):
            row[f"pre_{key}"] = before[key]
            row[f"post_{key}"] = after[key]
            row[f"delta_{key}"] = after[key] - before[key]
        rows.append(row)
    return {
        "comparison": "post_inference minus pre_inference on the same entity-aligned examples",
        "examples": len(rows),
        "improved_f1": sum(row["delta_f1"] > 0 for row in rows),
        "unchanged_f1": sum(row["delta_f1"] == 0 for row in rows),
        "decreased_f1": sum(row["delta_f1"] < 0 for row in rows),
        "micro_delta": {
            key: post["micro"][key] - pre["micro"][key]
            for key in ("precision", "recall", "f1")
        },
        "macro_delta": {
            key: post["macro"][key] - pre["macro"][key]
            for key in ("precision", "recall", "f1")
        },
        "triple_count_delta": {
            key: post["totals"][key] - pre["totals"][key]
            for key in ("true_positives", "false_positives", "false_negatives")
        },
        "results": rows,
    }


def delta_markdown(payload: dict) -> str:
    micro, macro = payload["micro_delta"], payload["macro_delta"]
    lines = [
        "# Inference impact report", "",
        "All deltas are post-inference minus pre-inference on the same examples.", "",
        "| Outcome | Examples |", "|---|---:|",
        f"| F1 improved | {payload['improved_f1']} |",
        f"| F1 unchanged | {payload['unchanged_f1']} |",
        f"| F1 decreased | {payload['decreased_f1']} |", "",
        "| Metric | Micro delta | Macro delta |", "|---|---:|---:|",
        f"| Precision | {micro['precision']:+.6f} | {macro['precision']:+.6f} |",
        f"| Recall | {micro['recall']:+.6f} | {macro['recall']:+.6f} |",
        f"| F1 | {micro['f1']:+.6f} | {macro['f1']:+.6f} |", "",
        "| ID | Pre TP | Post TP | ΔTP | Pre FP | Post FP | ΔFP | Pre FN | Post FN | ΔFN | Pre F1 | Post F1 | ΔF1 |",
        "|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for row in payload["results"]:
        lines.append(
            f"| {row['id']} | {row['pre_true_positives']} | {row['post_true_positives']} | "
            f"{row['delta_true_positives']:+d} | {row['pre_false_positives']} | "
            f"{row['post_false_positives']} | {row['delta_false_positives']:+d} | "
            f"{row['pre_false_negatives']} | {row['post_false_negatives']} | "
            f"{row['delta_false_negatives']:+d} | {row['pre_f1']:.6f} | "
            f"{row['post_f1']:.6f} | {row['delta_f1']:+.6f} |"
        )
    return "\n".join(lines) + "\n"


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input-dir", type=Path, required=True)
    parser.add_argument(
        "--inference-dir",
        type=Path,
        help="Deprecated compatibility option; aligned final graphs are read from input-dir.",
    )
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--ids", type=parse_ids, required=True)
    parser.add_argument("--summary-dir", type=Path, default=None)
    parser.add_argument(
        "--stage",
        choices=("pre", "post", "both"),
        default="both",
        help="Evaluate matched asserted graphs, reasoned graphs, or both (default: both).",
    )
    parser.add_argument(
        "--scoring-profile",
        choices=("strict", "projected", "both"),
        default="both",
        help=(
            "Strict keeps ontology predicates distinct; projected preserves the legacy "
            "family/country compatibility scoring; default evaluates both."
        ),
    )
    parser.add_argument(
        "--include-excluded",
        action="store_true",
        help="Evaluate examples marked as excluded from graph evaluation.",
    )
    args = parser.parse_args(argv)
    stages = ("pre", "post") if args.stage == "both" else (args.stage,)
    profiles = (
        ("strict", "projected")
        if args.scoring_profile == "both"
        else (args.scoring_profile,)
    )
    summaries_by_cell = {(stage, profile): [] for stage in stages for profile in profiles}
    for index in args.ids:
        example = args.input_dir.resolve() / str(index)
        exclusion = graph_evaluation_exclusion(example)
        if exclusion and not args.include_excluded:
            print(f"id={index} status=excluded")
            continue
        matching = example / "evaluation" / "entity_alignment"
        matching_artifact = matching / "artifacts" / f"mapping_{index}.json"
        inputs_by_stage = {
            "pre": (
                matching / f"baseline_extracted_aligned_{index}.ttl",
                matching / f"baseline_ground_truth_aligned_{index}.ttl",
            ),
            "post": (
                matching / f"final_extracted_aligned_{index}.ttl",
                matching / f"final_ground_truth_aligned_{index}.ttl",
            ),
        }
        required = [matching_artifact, *(path for stage in stages for path in inputs_by_stage[stage])]
        if not all(path.is_file() for path in required):
            raise FileNotFoundError(f"Missing triple-matching input for id {index}")
        accepted = json.loads(matching_artifact.read_text(encoding="utf-8"))["summary"]["matched"]
        for stage in stages:
            for profile in profiles:
                payload = compare_graphs(
                    *inputs_by_stage[stage], accepted_pairs=accepted, scoring_profile=profile
                )
                payload["stage"] = "pre_inference" if stage == "pre" else "post_inference"
                output = (
                    args.output_dir.resolve() / str(index) / "triple_matching"
                    / payload["stage"] / profile
                )
                write_text(output / f"report_{index}.md", markdown_report(index, payload))
                write_text(output / "artifacts" / f"result_{index}.json", json.dumps(payload, ensure_ascii=False, indent=2) + "\n")
                summaries_by_cell[(stage, profile)].append({"id": index, **payload["metrics"]})
                print(
                    f"id={index} stage={stage} profile={profile} "
                    f"tp={payload['metrics']['true_positives']} "
                    f"fp={payload['metrics']['false_positives']} fn={payload['metrics']['false_negatives']}"
                )

    summary_dir = args.summary_dir.resolve() if args.summary_dir else args.output_dir.resolve()
    aggregates = {}
    for stage in stages:
        for profile in profiles:
            stage_label = "pre_inference" if stage == "pre" else "post_inference"
            label = f"{stage_label}_{profile}"
            aggregate = aggregate_results(summaries_by_cell[(stage, profile)], label)
            aggregate["scoring_profile"] = profile
            aggregates[(stage, profile)] = aggregate
            write_text(summary_dir / f"triple_matching_{label}_summary.json", json.dumps(aggregate, ensure_ascii=False, indent=2) + "\n")
            write_text(summary_dir / f"triple_matching_{label}_summary.md", aggregate_markdown(aggregate))
            print(
                f"stage={stage} profile={profile} micro_precision={aggregate['micro']['precision']:.6f} "
                f"micro_recall={aggregate['micro']['recall']:.6f} micro_f1={aggregate['micro']['f1']:.6f}"
            )
    if args.stage == "both":
        for profile in profiles:
            delta = paired_inference_delta(
                aggregates[("pre", profile)], aggregates[("post", profile)]
            )
            delta["scoring_profile"] = profile
            write_text(summary_dir / f"triple_matching_inference_delta_{profile}.json", json.dumps(delta, ensure_ascii=False, indent=2) + "\n")
            write_text(summary_dir / f"triple_matching_inference_delta_{profile}.md", delta_markdown(delta))

    # The four-cell ablation makes semantic projection visible instead of
    # silently attributing it to inference. The projected/post cell preserves
    # the legacy final score; strict pre->post is the inference-only comparison.
    if args.stage == "both" and args.scoring_profile == "both":
        ablation = {
            "design": {
                "strict_pre": "asserted graphs; representation normalization only",
                "projected_pre": "asserted graphs plus evaluation-level family/country projection",
                "strict_post": "reasoned graphs; representation normalization only",
                "projected_post": "reasoned graphs plus legacy family/country projection",
            },
            "recommended_interpretation": {
                "inference_effect": "strict_post minus strict_pre",
                "normalization_effect_pre": "projected_pre minus strict_pre",
                "normalization_effect_post": "projected_post minus strict_post",
                "legacy_final_result": "projected_post",
            },
            "micro": {
                f"{stage}_{profile}": aggregates[(stage, profile)]["micro"]
                for stage in stages for profile in profiles
            },
            "macro": {
                f"{stage}_{profile}": aggregates[(stage, profile)]["macro"]
                for stage in stages for profile in profiles
            },
        }
        write_text(summary_dir / "triple_matching_ablation.json", json.dumps(ablation, ensure_ascii=False, indent=2) + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
