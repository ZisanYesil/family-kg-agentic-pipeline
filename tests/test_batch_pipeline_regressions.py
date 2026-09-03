import json
import tempfile
import unittest
from pathlib import Path

from rdflib import Graph, Namespace, RDF, URIRef

import build_dataset
from agents import kg_builder_agent
from agents.validation_agent import validation_agent
import triple_matching
import run_agent_pipeline


class GroundTruthConstructionTests(unittest.TestCase):
    @staticmethod
    def quality_row(**overrides):
        row = {
            "_id": "row-1",
            "type": "compositional",
            "question": "Who directed Example Film?",
            "answer": "Jane Director",
            "context": json.dumps([["Example Film", ["Example Film was directed by Jane Director."]]]),
            "supporting_facts": json.dumps([["Example Film", 0]]),
            "evidences": json.dumps([["Example Film", "director", "Jane Director"]]),
        }
        row.update(overrides)
        return row

    def test_quality_audit_accepts_well_grounded_example(self):
        assessment = build_dataset.assess_example_quality(self.quality_row())
        self.assertEqual("pass", assessment.status)

    def test_quality_audit_rejects_answer_not_licensed_by_evidence(self):
        assessment = build_dataset.assess_example_quality(
            self.quality_row(answer="Someone Else")
        )
        self.assertEqual("reject", assessment.status)
        self.assertIn("answer_not_licensed_by_evidence", {i.code for i in assessment.issues})

    def test_quality_audit_rejects_invalid_support_index(self):
        assessment = build_dataset.assess_example_quality(
            self.quality_row(supporting_facts=json.dumps([["Example Film", 9]]))
        )
        self.assertEqual("reject", assessment.status)
        self.assertIn("invalid_support_index", {i.code for i in assessment.issues})

    def test_quality_audit_warns_instead_of_rejecting_surface_variant(self):
        assessment = build_dataset.assess_example_quality(
            self.quality_row(
                context=json.dumps([["John V, Prince of Anhalt-Zerbst", [
                    "His father was Ernest I, Prince of Anhalt-Dessau."
                ]]]),
                supporting_facts=json.dumps([["John V, Prince of Anhalt-Zerbst", 0]]),
                question="Who was John V's father?",
                answer="Ernest I, Prince of Anhalt-Dessau",
                evidences=json.dumps([["John V of Anhalt-Zerbst", "father", "Ernest I, Prince of Anhalt-Dessau"]]),
            )
        )
        self.assertEqual("review", assessment.status)
        self.assertIn("evidence_term_not_in_context", {i.code for i in assessment.issues})

    def test_primary_selection_not_derived_from_prefix_of_expanded_sample(self):
        source = Path("build_dataset.py").read_text(encoding="utf-8")
        self.assertIn("select_primary_and_reserve", source)
        self.assertIn("selected[: args.n]", source)

    def test_case_only_entity_variants_share_one_uri(self):
        evidence = json.dumps([
            ["Eleanor de Clare", "spouse", "Hugh Despenser the Younger"],
            ["Hugh Despenser the younger", "cause of death", "hanged"],
        ])
        ttl, _ = build_dataset.evidences_to_ttl(evidence, "example4")
        graph = Graph().parse(data=ttl, format="turtle")
        hughs = {
            term
            for triple in graph
            for term in (triple[0], triple[2])
            if "Hugh_Despenser" in str(term)
        }
        self.assertEqual(1, len(hughs))

    def test_semantic_demonyms_are_not_blindly_merged(self):
        self.assertNotEqual(
            build_dataset.canonical_entity_key("Bolivia"),
            build_dataset.canonical_entity_key("Bolivian"),
        )

    def test_regular_country_demonym_variants_share_one_uri(self):
        evidence = json.dumps([
            ["Mountain A", "country", "Bolivian"],
            ["Mountain B", "country", "Bolivia"],
        ])
        ttl, _ = build_dataset.evidences_to_ttl(evidence, "example22")
        graph = Graph().parse(data=ttl, format="turtle")
        country_objects = {
            obj
            for _, predicate, obj in graph
            if str(predicate).endswith("hasCountry")
        }
        self.assertEqual(1, len(country_objects))

    def test_country_prompt_preserves_source_demonym_as_alias(self):
        source = Path("agents/extraction_agent.py").read_text(encoding="utf-8")
        self.assertIn("preserve", source)
        self.assertIn("American", source)


class KGBuilderTests(unittest.TestCase):
    def test_extracted_entity_type_is_written_to_rdf(self):
        schema = run_agent_pipeline.load_ontology_schema("ontology/ontology.ttl")
        extraction = {
            "entities": [
                {
                    "id": "example_film",
                    "label": "Example Film",
                    "type": "Film",
                    "aliases": [],
                    "attributes": {},
                }
            ],
            "relations": [],
        }

        ttl = kg_builder_agent.kg_builder_agent(extraction, schema)
        graph = Graph().parse(data=ttl, format="turtle")
        entity = URIRef("http://example.org/extracted/example_film")
        ontology = Namespace("http://example.org/2wiki-ontology#")

        self.assertIn((entity, RDF.type, ontology.Film), graph)


class ValidationIntegrationTests(unittest.TestCase):
    def test_batch_validation_uses_the_api_validation_contract(self):
        schema = run_agent_pipeline.load_ontology_schema("ontology/ontology.ttl")
        mapping = {
            "entities": [
                {
                    "id": "example_film",
                    "label": "Example Film",
                    "type": "Film",
                    "aliases": [],
                    "attributes": {"hasPublicationDate": "1999"},
                }
            ],
            "relations": [],
            "unmapped_relations": [],
        }
        built = kg_builder_agent.kg_builder_agent_with_diagnostics(mapping, schema)

        batch_result = run_agent_pipeline._validate_graph(
            built.turtle_graph,
            schema,
            mapping,
            built,
        )
        api_result = validation_agent(
            Graph().parse(data=built.turtle_graph, format="turtle"),
            schema,
            unmapped_relations=(),
            dangling_references=built.dangling_references,
            entities=mapping["entities"],
        )

        self.assertEqual(api_result.conforms, batch_result["conforms"])
        self.assertEqual(api_result.fingerprint, batch_result["fingerprint"])
        self.assertEqual(
            [violation.as_dict() for violation in api_result.violations],
            batch_result["violations"],
        )
        self.assertEqual(
            run_agent_pipeline.VALIDATION_CONTRACT_VERSION,
            batch_result["validation_contract_version"],
        )


class TripleScoringTests(unittest.TestCase):
    def test_paired_inference_delta_uses_same_cohort_and_post_minus_pre(self):
        def row(index, tp, fp, fn, precision, recall, f1):
            return {
                "id": index,
                "accepted_entity_pairs": 1,
                "true_positives": tp,
                "false_positives": fp,
                "false_negatives": fn,
                "extracted_triples_in_scope": tp + fp,
                "ground_truth_triples_in_scope": tp + fn,
                "union_triples_in_scope": tp + fp + fn,
                "precision": precision,
                "recall": recall,
                "f1": f1,
            }

        pre = triple_matching.aggregate_results(
            [row(1, 1, 1, 1, 0.5, 0.5, 0.5)], "pre_inference"
        )
        post = triple_matching.aggregate_results(
            [row(1, 2, 1, 0, 2 / 3, 1.0, 0.8)], "post_inference"
        )
        delta = triple_matching.paired_inference_delta(pre, post)
        self.assertEqual(1, delta["improved_f1"])
        self.assertEqual(1, delta["triple_count_delta"]["true_positives"])
        self.assertAlmostEqual(0.3, delta["results"][0]["delta_f1"])

    def test_paired_inference_delta_rejects_different_cohorts(self):
        pre = {"results": [{"id": 1}]}
        post = {"results": [{"id": 2}]}
        with self.assertRaisesRegex(ValueError, "cohorts differ"):
            triple_matching.paired_inference_delta(pre, post)

    def test_country_and_country_of_origin_score_as_equivalent(self):
        extracted = """\
@prefix ex: <http://example.org/2wiki-ontology#> .
@prefix inst: <http://example.org/entity/> .
inst:Film ex:hasCountry inst:Britain .
"""
        ground_truth = """\
@prefix ex: <http://example.org/2wiki-ontology#> .
@prefix inst: <http://example.org/entity/> .
inst:Film ex:hasCountryOfOrigin inst:Britain .
"""
        with tempfile.TemporaryDirectory() as tmp:
            extracted_path = Path(tmp) / "extracted.ttl"
            ground_truth_path = Path(tmp) / "ground_truth.ttl"
            extracted_path.write_text(extracted, encoding="utf-8")
            ground_truth_path.write_text(ground_truth, encoding="utf-8")
            result = triple_matching.compare_graphs(
                extracted_path, ground_truth_path, accepted_pairs=0
            )
        self.assertEqual(1.0, result["metrics"]["f1"])

    def test_strict_profile_does_not_supply_country_subproperty_inference(self):
        extracted = """\
@prefix ex: <http://example.org/2wiki-ontology#> .
@prefix inst: <http://example.org/entity/> .
inst:Film ex:hasCountry inst:Britain .
"""
        ground_truth = """\
@prefix ex: <http://example.org/2wiki-ontology#> .
@prefix inst: <http://example.org/entity/> .
inst:Film ex:hasCountryOfOrigin inst:Britain .
"""
        with tempfile.TemporaryDirectory() as tmp:
            extracted_path = Path(tmp) / "extracted.ttl"
            ground_truth_path = Path(tmp) / "ground_truth.ttl"
            extracted_path.write_text(extracted, encoding="utf-8")
            ground_truth_path.write_text(ground_truth, encoding="utf-8")
            strict = triple_matching.compare_graphs(
                extracted_path,
                ground_truth_path,
                accepted_pairs=0,
                scoring_profile="strict",
            )
            projected = triple_matching.compare_graphs(
                extracted_path,
                ground_truth_path,
                accepted_pairs=0,
                scoring_profile="projected",
            )
        self.assertEqual(0.0, strict["metrics"]["f1"])
        self.assertEqual(1.0, projected["metrics"]["f1"])


class ExtractionQualityTests(unittest.TestCase):
    def test_scoreable_wrong_fact_remains_evaluation_eligible(self):
        extraction = {
            "entities": [
                {"id": "film", "label": "Example Film", "aliases": [], "attributes": {}},
                {"id": "wrong", "label": "Wrong Director", "aliases": [], "attributes": {}},
            ],
            "relations": [{"subject": "film", "object": "wrong", "relation_phrase": "directed by"}],
        }
        mapping = {
            "relations": [{"subject": "film", "object": "wrong", "predicate": "hasDirector"}],
            "unmapped_relations": [],
        }
        quality = run_agent_pipeline.assess_extraction_quality(
            extraction,
            mapping,
            question="Who directed Example Film?",
            source_text="Example Film was directed by Jane Director.",
        )
        self.assertEqual("scoreable", quality["status"])
        self.assertTrue(quality["eligible_for_graph_evaluation"])
        self.assertIn("entities_not_source_grounded", {i["code"] for i in quality["issues"]})

    def test_unmapped_relation_only_extraction_is_unscoreable(self):
        extraction = {
            "entities": [
                {"id": "a", "label": "A", "aliases": [], "attributes": {}},
                {"id": "b", "label": "B", "aliases": [], "attributes": {}},
            ],
            "relations": [{"subject": "a", "object": "b", "relation_phrase": "unknown"}],
        }
        quality = run_agent_pipeline.assess_extraction_quality(
            extraction,
            {"relations": [], "unmapped_relations": [{"relation_phrase": "unknown"}]},
            question="How is A related?",
            source_text="A and B are mentioned.",
        )
        self.assertEqual("unscoreable", quality["status"])
        self.assertFalse(quality["eligible_for_graph_evaluation"])
        self.assertIn("no_mapped_semantic_facts", {i["code"] for i in quality["issues"]})

    def test_attribute_fact_is_scoreable_without_object_relation(self):
        extraction = {
            "entities": [{
                "id": "film", "label": "Example Film", "aliases": [],
                "attributes": {"hasPublicationDate": "1999"},
            }],
            "relations": [],
        }
        quality = run_agent_pipeline.assess_extraction_quality(
            extraction,
            {"relations": [], "unmapped_relations": []},
            question="When was Example Film published?",
            source_text="Example Film was published in 1999.",
        )
        self.assertEqual("scoreable", quality["status"])

    def test_attribute_only_extraction_is_not_empty(self):
        payload = {
            "entities": [{"attributes": {"hasPublicationDate": "1999"}}],
            "relations": [],
        }
        self.assertTrue(run_agent_pipeline.extraction_has_usable_facts(payload))

    def test_entity_without_any_fact_is_empty(self):
        payload = {
            "entities": [{"attributes": {"hasPublicationDate": None}}],
            "relations": [],
        }
        self.assertFalse(run_agent_pipeline.extraction_has_usable_facts(payload))


if __name__ == "__main__":
    unittest.main()
