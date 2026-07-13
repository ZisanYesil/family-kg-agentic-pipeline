# Weekly Report 2 - 13.07.2026

## Project

**Family KG Agentic Pipeline**  
Agentic AI for Ontology-Based Knowledge Graph Construction and Iterative Improvement

## Summary

During the last week, I focused on an important design issue I noticed in the pipeline: the implementation was too tightly coupled to the Family Ontology. The Extraction Agent, Ontology Mapping Agent, KG Builder Agent, API flow, and tests all assumed family-specific classes, attributes, and predicates. I refactored the system so that the pipeline can load an ontology schema dynamically and use that schema throughout the extraction, mapping, and RDF generation stages.

## 1. Ontology Schema Loading

I added a new ontology schema loader under `ontology/schema_loader.py`. This component parses an OWL/Turtle ontology file and extracts the ontology namespace, classes, datatype properties, object properties, domain/range constraints, inverse properties, and excluded predicates.

The loader also filters out properties that should not be directly offered to the LLM, such as reasoner-derived properties, superproperties, and duplicate inverse directions. This makes the predicate list cleaner and more reliable for the mapping step.

## 2. Ontology-Agnostic Extraction Agent

I refactored the Extraction Agent so it no longer extracts only hardcoded family fields such as sex, birth year, and death year. Instead, it now builds its system prompt and structured-output JSON schema from the loaded ontology.

Entities now include a generic `type` and an `attributes` object based on the ontology's datatype properties. Relations remain free-text `relation_phrase` triples, so the extraction stage is responsible for reading the source text while the mapping stage handles ontology predicate selection.

## 3. Ontology-Agnostic Mapping and KG Building

I updated the Ontology Mapping Agent to build its available predicate list from the ontology's object properties instead of a fixed family predicate list. It now also checks domain and range constraints before accepting a mapped relation.

I also refactored the KG Builder Agent so RDF generation uses the loaded ontology namespace, classes, datatype properties, and object properties. This removed the direct dependency on the old `fhkb` constants and made graph construction work for other schemas as well. The builder still keeps useful diagnostics, such as unsupported predicates, invalid entity types, conflicting attribute values, and dangling relation references.

## 4. API, Storage, and Pipeline Updates

I added ontology selection to the job creation flow. A job can now receive an `ontology_path`, or the system can fall back to `DEFAULT_ONTOLOGY_PATH`. The selected ontology path is stored in SQLite and loaded when the background pipeline starts.

The pipeline now loads the ontology schema before extraction and passes the same schema through the Extraction Agent, Ontology Mapping Agent, and KG Builder Agent. I also added error handling for missing ontology paths and ontology parsing failures, so these cases are reported as job errors instead of failing silently.

## 5. Test Updates

I updated the tests to reflect the new ontology-agnostic behavior. The tests now use mixed-domain schemas, such as people and cars, to prove that the agents are not hardcoded to family-only data.

The updated tests cover:

- dynamic extraction prompts and response schemas,
- ontology-based predicate mapping,
- domain/range validation during mapping,
- schema-driven RDF generation,
- API handling of `ontology_path`,
- pipeline behavior when ontology loading succeeds or fails,
- namespace consistency in generated RDF.

## Current Outcome

By the end of the week, the main pipeline is no longer fully dependent on the Family Ontology. The system can load an ontology file, derive the usable schema from it, and use that schema consistently across extraction, mapping, and KG construction.

Validation run: `python3 -m pytest tests/test_extraction_agent.py tests/test_ontology_mapping_agent.py tests/test_kg_builder_agent.py tests/test_jobs_api.py tests/test_pipeline_task.py tests/test_ontology_namespace.py` passed with 78 tests.
