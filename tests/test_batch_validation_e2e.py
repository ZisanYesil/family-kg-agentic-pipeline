from __future__ import annotations

import json
from pathlib import Path
from unittest.mock import patch

from rdflib import Graph, Literal, URIRef
from rdflib.namespace import XSD

from agents.ontology_mapping_agent import OntologyMappingResult, UnmappedRelation
from agents.kg_builder_agent import kg_builder_agent_with_diagnostics
from feedback.models import FeedbackPlan
import run_agent_pipeline


ONTOLOGY = "http://example.org/2wiki-ontology#"
DATA = "http://example.org/extracted/"


def _attributes(**values: object) -> dict[str, object]:
    attributes: dict[str, object] = {
        "hasBirthDate": None,
        "hasDeathDate": None,
        "hasDemonym": None,
        "hasInception": None,
        "hasPublicationDate": None,
    }
    attributes.update(values)
    return attributes


def _example_directory(tmp_path: Path, index: int, question: str) -> Path:
    originals = tmp_path / "inputs" / str(index) / "originals"
    originals.mkdir(parents=True)
    (originals / f"text_{index}.txt").write_text(
        "Example Film was published in 1999.",
        encoding="utf-8",
    )
    (originals / f"example{index}_question.txt").write_text(
        question,
        encoding="utf-8",
    )
    return originals


def test_valid_batch_example_runs_to_canonical_artifacts_and_resumes(
    tmp_path: Path,
) -> None:
    originals = _example_directory(tmp_path, 0, "When was Example Film published?")
    output = tmp_path / "output"
    extraction = {
        "entities": [
            {
                "id": "example_film",
                "label": "Example Film",
                "type": "Film",
                "aliases": [],
                "attributes": _attributes(hasPublicationDate="1999"),
            }
        ],
        "relations": [],
    }
    argv = [
        str(originals),
        "--output-dir",
        str(output),
        "--no-entity-linking",
    ]

    with patch("run_agent_pipeline.extraction_agent", return_value=extraction) as extract:
        assert run_agent_pipeline.main(argv) == 0
        # The second run must consume the versioned canonical artifacts instead of
        # invoking extraction or validation again.
        assert run_agent_pipeline.main(argv) == 0

    assert extract.call_count == 1
    validation_path = output / "0" / "originals" / "artifacts" / "shacl_0.json"
    manifest_path = output / "manifest.json"
    graph_path = output / "0" / "originals" / "extracted_0.ttl"

    validation = json.loads(validation_path.read_text(encoding="utf-8"))
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    graph = Graph().parse(graph_path, format="turtle")

    assert validation == {
        "validation_contract_version": run_agent_pipeline.VALIDATION_CONTRACT_VERSION,
        "conforms": True,
        "fingerprint": validation["fingerprint"],
        "violations": [],
        "dangling_references": [],
    }
    assert len(validation["fingerprint"]) == 64
    assert manifest[0]["status"] == "skipped"
    assert manifest[0]["shacl_conforms"] is True
    assert (
        URIRef(DATA + "example_film"),
        URIRef(ONTOLOGY + "hasPublicationDate"),
        Literal("1999", datatype=XSD.gYear),
    ) in graph


def test_unmapped_relation_blocks_batch_completion_through_canonical_validator(
    tmp_path: Path,
) -> None:
    originals = _example_directory(tmp_path, 1, "How is Alpha related to Beta?")
    output = tmp_path / "output"
    entities = [
        {
            "id": entity_id,
            "label": label,
            "type": "Person",
            "aliases": [],
            "attributes": _attributes(),
        }
        for entity_id, label in (("alpha", "Alpha"), ("beta", "Beta"))
    ]
    extraction = {
        "entities": entities,
        "relations": [
            {
                "subject": "alpha",
                "object": "beta",
                "relation_phrase": "mysteriously connected to",
                "qualifiers": {"year": None, "note": None},
            }
        ],
    }
    mapping = OntologyMappingResult(
        entities=entities,
        relations=[],
        unmapped_relations=(
            UnmappedRelation(
                subject="alpha",
                object="beta",
                relation_phrase="mysteriously connected to",
                reason="relation_phrase did not match any ontology predicate",
            ),
        ),
    )

    with (
        patch("run_agent_pipeline.extraction_agent", return_value=extraction),
        patch(
            "run_agent_pipeline.ontology_mapping_agent_with_diagnostics",
            return_value=mapping,
        ),
    ):
        exit_code = run_agent_pipeline.main(
            [
                str(originals),
                "--output-dir",
                str(output),
                "--no-entity-linking",
            ]
        )

    validation = json.loads(
        (output / "1" / "originals" / "artifacts" / "shacl_1.json").read_text(
            encoding="utf-8"
        )
    )
    manifest = json.loads((output / "manifest.json").read_text(encoding="utf-8"))

    assert exit_code == 1
    assert validation["conforms"] is False
    assert [item["kind"] for item in validation["violations"]] == [
        "unmapped_relation"
    ]
    assert manifest[0]["status"] == "review"
    assert manifest[0]["unmapped_relations"] == 1
    assert manifest[0]["shacl_conforms"] is False


def test_batch_feedback_loop_repairs_then_revalidates_unmapped_fact() -> None:
    schema = run_agent_pipeline.load_ontology_schema("ontology/ontology.ttl")
    entities = [
        {
            "id": entity_id,
            "label": label,
            "type": "Person",
            "aliases": [],
            "attributes": _attributes(),
        }
        for entity_id, label in (("alpha", "Alpha"), ("beta", "Beta"))
    ]
    mapping = {
        "entities": entities,
        "relations": [],
        "unmapped_relations": [
            {
                "subject": "alpha",
                "object": "beta",
                "relation_phrase": "spouse",
                "reason": "mapping confidence was below threshold",
            }
        ],
    }
    built = kg_builder_agent_with_diagnostics(mapping, schema)
    graph = Graph().parse(data=built.turtle_graph, format="turtle")

    def grounded_plan(_graph, violations, _schema, _source_text):
        assert len(violations) == 1
        return FeedbackPlan.model_validate(
            {
                "reasoning": "The source explicitly states the spouse relation.",
                "repairs": [
                    {
                        "violation_fingerprint": violations[0].fingerprint,
                        "reasoning": "Add the compatible ontology predicate.",
                        "operations": [
                            {
                                "operation": "add_triple",
                                "subject": DATA + "alpha",
                                "predicate": ONTOLOGY + "hasSpouse",
                                "object": {"kind": "iri", "value": DATA + "beta"},
                            }
                        ],
                    }
                ],
            }
        )

    with patch("run_agent_pipeline.feedback_agent", side_effect=grounded_plan):
        repaired, result, audit = run_agent_pipeline.repair_graph_with_feedback(
            graph,
            schema,
            mapping,
            built,
            "Alpha is Beta's spouse.",
        )

    assert audit["status"] == "repaired", audit
    assert result.conforms is True
    assert len(audit["iterations"]) == 1
    assert (
        URIRef(DATA + "alpha"),
        URIRef(ONTOLOGY + "hasSpouse"),
        URIRef(DATA + "beta"),
    ) in repaired
