#!/usr/bin/env python3
"""Run HermiT over one or more 2Wiki ABox graphs and materialize entailments.

Examples:
    python3 reasoner-inference/reasoner_kg_hermit.py dataset/0/originals/ground_truth_0.ttl
    python3 reasoner-inference/reasoner_kg_hermit.py dataset --summary-only
    python3 reasoner-inference/reasoner_kg_hermit.py dataset --output-ttl materialized.ttl
"""

import argparse
import os
import re
import sys
import tempfile
import time
from collections import Counter
from pathlib import Path

import rdflib
from rdflib import BNode, Graph, Literal, RDF, RDFS, OWL, URIRef


SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent
DEFAULT_TBOX = PROJECT_ROOT / "ontology" / "dataset_ontology.ttl"
DEFAULT_DATASET = PROJECT_ROOT / "dataset"
ONTOLOGY_NAMESPACE = "http://example.org/2wiki-ontology#"


def build_parser():
    parser = argparse.ArgumentParser(
        description="Run HermiT over 2Wiki Turtle ABox files and report new entailments."
    )
    parser.add_argument(
        "abox",
        nargs="*",
        default=[str(DEFAULT_DATASET)],
        help="ABox Turtle files or directories (default: project dataset directory)",
    )
    parser.add_argument(
        "--tbox",
        default=str(DEFAULT_TBOX),
        help="Ontology/TBox Turtle file (default: ontology/dataset_ontology.ttl)",
    )
    parser.add_argument(
        "--pattern",
        default="ground_truth_*.ttl",
        help="Filename pattern used for directory inputs (default: ground_truth_*.ttl)",
    )
    parser.add_argument("--summary-only", action="store_true")
    parser.add_argument("--max-summary-items", type=int, default=10)
    parser.add_argument("--output-ttl", help="Write asserted + inferred ABox facts")
    parser.add_argument("--inferred-output-ttl", help="Write only newly inferred ABox facts")
    parser.add_argument(
        "--no-property-closure",
        action="store_true",
        help="Do not complete subproperty, inverse, and symmetric-property entailments",
    )
    parser.add_argument(
        "--self-contained-output",
        action="store_true",
        help="Add class/property/NamedIndividual declarations to output files",
    )
    return parser


def resolve_turtle_files(raw_paths, pattern="ground_truth_*.ttl"):
    files = []
    for raw in raw_paths:
        path = Path(raw).expanduser().resolve()
        if not path.exists():
            raise FileNotFoundError(f"ABox path does not exist: {path}")
        if path.is_dir():
            matches = sorted(path.rglob(pattern))
            if pattern == "ground_truth_*.ttl":
                matches = [item for item in matches if re.fullmatch(r"ground_truth_\d+\.ttl", item.name)]
            files.extend(matches)
        elif path.is_file():
            files.append(path)
        else:
            raise ValueError(f"Unsupported ABox path: {path}")
    unique = list(dict.fromkeys(files))
    if not unique:
        raise ValueError("No .ttl ABox files found")
    return unique


def load_graph(paths, label):
    graph = Graph()
    for path in paths:
        try:
            graph.parse(path, format="turtle")
        except Exception as exc:
            raise ValueError(f"Cannot parse {label} Turtle file {path}: {exc}") from exc
    return graph


def schema_terms(tbox):
    classes = set(tbox.subjects(RDF.type, OWL.Class))
    object_properties = set(tbox.subjects(RDF.type, OWL.ObjectProperty))
    datatype_properties = set(tbox.subjects(RDF.type, OWL.DatatypeProperty))
    return classes, object_properties, datatype_properties


def is_abox_fact(triple, classes, object_properties, datatype_properties):
    subject, predicate, obj = triple
    if not isinstance(subject, URIRef):
        return False
    if predicate == RDF.type:
        return isinstance(obj, URIRef) and obj in classes
    if predicate in object_properties:
        return isinstance(obj, URIRef)
    if predicate in datatype_properties:
        return isinstance(obj, Literal)
    return False


def materialize_property_closure(facts, tbox, object_properties):
    """Complete named object-property consequences that exports may omit."""
    superproperties = {}
    inverses = {}
    symmetric = set(tbox.subjects(RDF.type, OWL.SymmetricProperty)) & object_properties

    def add_rule(rule_map, source, target):
        if source in object_properties and target in object_properties:
            rule_map.setdefault(source, set()).add(target)

    for child, parent in tbox.subject_objects(RDFS.subPropertyOf):
        add_rule(superproperties, child, parent)
    for left, right in tbox.subject_objects(OWL.equivalentProperty):
        add_rule(superproperties, left, right)
        add_rule(superproperties, right, left)
    for left, right in tbox.subject_objects(OWL.inverseOf):
        add_rule(inverses, left, right)
        add_rule(inverses, right, left)

    completed = set(facts)
    frontier = {triple for triple in completed if triple[1] in object_properties}
    while frontier:
        additions = set()
        for subject, predicate, obj in frontier:
            additions.update(
                (subject, parent, obj)
                for parent in superproperties.get(predicate, ())
            )
            additions.update(
                (obj, inverse, subject)
                for inverse in inverses.get(predicate, ())
            )
            if predicate in symmetric:
                additions.add((obj, predicate, subject))
        additions.difference_update(completed)
        completed.update(additions)
        frontier = additions
    return completed


def materialize_type_closure(
    facts, tbox, classes, object_properties, datatype_properties
):
    """Complete named superclass and property domain/range memberships."""
    superclasses = {}

    def add_superclass(child, parent):
        if child in classes and parent in classes:
            superclasses.setdefault(child, set()).add(parent)

    for child, parent in tbox.subject_objects(RDFS.subClassOf):
        add_superclass(child, parent)
    for left, right in tbox.subject_objects(OWL.equivalentClass):
        add_superclass(left, right)
        add_superclass(right, left)

    domains = {}
    ranges = {}
    for prop, domain in tbox.subject_objects(RDFS.domain):
        if prop in object_properties | datatype_properties and domain in classes:
            domains.setdefault(prop, set()).add(domain)
    for prop, value_range in tbox.subject_objects(RDFS.range):
        if prop in object_properties and value_range in classes:
            ranges.setdefault(prop, set()).add(value_range)

    completed = set(facts)
    changed = True
    while changed:
        additions = set()
        for subject, predicate, obj in completed:
            if predicate == RDF.type and obj in classes:
                additions.update(
                    (subject, RDF.type, parent)
                    for parent in superclasses.get(obj, ())
                )
            elif predicate in object_properties | datatype_properties:
                additions.update(
                    (subject, RDF.type, domain)
                    for domain in domains.get(predicate, ())
                )
                if predicate in object_properties and isinstance(obj, URIRef):
                    additions.update(
                        (obj, RDF.type, value_range)
                        for value_range in ranges.get(predicate, ())
                    )
        additions.difference_update(completed)
        changed = bool(additions)
        completed.update(additions)
    return completed


def run_hermit(tbox, abox):
    try:
        import owlready2
        import owlready2.driver
    except ModuleNotFoundError as exc:
        raise RuntimeError(
            "owlready2 is required; install dependencies with "
            "'python3 -m pip install -r requirements.txt'"
        ) from exc

    owlready2.driver.owlready2_optimized = None
    owlready2.set_log_level(0)

    merged = Graph()
    for triple in tbox:
        merged.add(triple)
    for triple in abox:
        merged.add(triple)

    temp_path = None
    try:
        with tempfile.NamedTemporaryFile(suffix=".nt", delete=False) as handle:
            temp_path = handle.name
        merged.serialize(temp_path, format="nt", encoding="utf-8")

        world = owlready2.World()
        ontology = world.get_ontology(Path(temp_path).as_uri()).load()
        started = time.time()
        try:
            with ontology:
                owlready2.sync_reasoner(
                    world,
                    infer_property_values=True,
                    ignore_unsupported_datatypes=True,
                    debug=0,
                )
        except owlready2.OwlReadyInconsistentOntologyError as exc:
            raise RuntimeError("HermiT reports that the merged ontology is inconsistent") from exc
        except owlready2.OwlReadyJavaError as exc:
            raise RuntimeError(
                "HermiT Java process failed; verify that a supported Java runtime is installed"
            ) from exc
        elapsed = time.time() - started

        reasoned = set(world.as_rdflib_graph())
        # Owlready2 syncs only direct named classes. Preserve all named class
        # memberships computed by HermiT through INDIRECT_is_a.
        for individual in world.individuals():
            if not individual.iri:
                continue
            for cls in individual.INDIRECT_is_a:
                if isinstance(cls, owlready2.ThingClass) and cls.iri:
                    reasoned.add((URIRef(individual.iri), RDF.type, URIRef(cls.iri)))
        return reasoned, elapsed
    finally:
        if temp_path and os.path.exists(temp_path):
            os.unlink(temp_path)


def bind_namespaces(graph):
    graph.bind("ex", rdflib.Namespace(ONTOLOGY_NAMESPACE))
    graph.bind("wd", rdflib.Namespace("http://www.wikidata.org/entity/"))
    graph.bind("entity", rdflib.Namespace("http://example.org/entity/"))
    graph.bind("rdf", RDF)
    graph.bind("rdfs", RDFS)
    graph.bind("owl", OWL)


def write_graph(facts, output_path, tbox, self_contained=False):
    graph = Graph()
    bind_namespaces(graph)
    for triple in facts:
        graph.add(triple)
    if self_contained:
        classes, object_properties, datatype_properties = schema_terms(tbox)
        used_classes = {obj for _, pred, obj in facts if pred == RDF.type}
        used_properties = {pred for _, pred, _ in facts if pred != RDF.type}
        individuals = {subject for subject, _, _ in facts if isinstance(subject, URIRef)}
        individuals.update(
            obj
            for _, pred, obj in facts
            if pred in object_properties and isinstance(obj, URIRef)
        )
        for cls in used_classes & classes:
            graph.add((cls, RDF.type, OWL.Class))
        for prop in used_properties & object_properties:
            graph.add((prop, RDF.type, OWL.ObjectProperty))
        for prop in used_properties & datatype_properties:
            graph.add((prop, RDF.type, OWL.DatatypeProperty))
        for individual in individuals:
            graph.add((individual, RDF.type, OWL.NamedIndividual))
    graph.serialize(Path(output_path).expanduser().resolve(), format="turtle")


def local_name(term):
    value = str(term)
    return value.rsplit("#", 1)[-1].rsplit("/", 1)[-1]


def describe_fact(triple):
    subject, predicate, obj = triple
    if predicate == RDF.type:
        return local_name(subject), "a", local_name(obj)
    rendered_object = obj.n3() if isinstance(obj, Literal) else local_name(obj)
    return local_name(subject), local_name(predicate), rendered_object


def main(argv=None):
    args = build_parser().parse_args(argv)
    try:
        abox_files = resolve_turtle_files(args.abox, args.pattern)
        tbox_path = Path(args.tbox).expanduser().resolve()
        if not tbox_path.is_file():
            raise FileNotFoundError(f"TBox file does not exist: {tbox_path}")
        tbox = load_graph([tbox_path], "TBox")
        abox = load_graph(abox_files, "ABox")
        classes, object_properties, datatype_properties = schema_terms(tbox)
        if not classes or not (object_properties or datatype_properties):
            raise ValueError("TBox does not declare OWL classes and properties")

        asserted = {
            triple
            for triple in abox
            if is_abox_fact(triple, classes, object_properties, datatype_properties)
        }
        reasoned, elapsed = run_hermit(tbox, abox)
        hermit_facts = {
            triple
            for triple in reasoned
            if is_abox_fact(triple, classes, object_properties, datatype_properties)
        }
        materialized = asserted | hermit_facts
        hermit_additions = materialized - asserted
        before_property_closure = set(materialized)
        if not args.no_property_closure:
            materialized = materialize_property_closure(
                materialized, tbox, object_properties
            )
        property_additions = materialized - before_property_closure
        before_type_closure = set(materialized)
        materialized = materialize_type_closure(
            materialized,
            tbox,
            classes,
            object_properties,
            datatype_properties,
        )
        type_additions = materialized - before_type_closure
        inferred = materialized - asserted

        if args.output_ttl:
            write_graph(materialized, args.output_ttl, tbox, args.self_contained_output)
        if args.inferred_output_ttl:
            write_graph(inferred, args.inferred_output_ttl, tbox, args.self_contained_output)

        asserted_types = {fact for fact in asserted if fact[1] == RDF.type}
        asserted_objects = {fact for fact in asserted if fact[1] in object_properties}
        asserted_literals = {fact for fact in asserted if fact[1] in datatype_properties}
        inferred_types = {fact for fact in inferred if fact[1] == RDF.type}
        inferred_objects = {fact for fact in inferred if fact[1] in object_properties}
        inferred_literals = {fact for fact in inferred if fact[1] in datatype_properties}

        print(
            f"HermiT reasoned {len(abox_files)} file(s) in {elapsed:.1f}s | "
            f"{len(asserted)} asserted + {len(inferred)} inferred = "
            f"{len(materialized)} materialized ABox facts"
        )
        print("\n== summary ==")
        print(f"   asserted rdf:type      : {len(asserted_types)}")
        print(f"   asserted object facts  : {len(asserted_objects)}")
        print(f"   asserted literal facts : {len(asserted_literals)}")
        print(f"   inferred rdf:type      : {len(inferred_types)}")
        print(f"   inferred object facts  : {len(inferred_objects)}")
        print(f"   inferred literal facts : {len(inferred_literals)}")
        print(f"   HermiT export added    : {len(hermit_additions)}")
        print(f"   property closure added : {len(property_additions)}")
        print(f"   type closure added     : {len(type_additions)}")

        predicate_counts = Counter(local_name(p) for _, p, _ in materialized if p != RDF.type)
        subject_counts = Counter(local_name(s) for s, _, _ in materialized)
        if predicate_counts:
            print("   top predicates:")
            for predicate, count in predicate_counts.most_common(args.max_summary_items):
                print(f"      - {predicate:<24} {count}")
        if subject_counts:
            print("   most connected subjects:")
            for subject, count in subject_counts.most_common(args.max_summary_items):
                print(f"      - {subject:<28} {count}")

        if not args.summary_only:
            print(f"\n== newly inferred facts ({len(inferred)}) ==")
            for fact in sorted(inferred, key=lambda item: tuple(map(str, item))):
                subject, predicate, obj = describe_fact(fact)
                print(f"   {subject}  {predicate}  {obj}")
        return 0
    except (OSError, ValueError, RuntimeError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
