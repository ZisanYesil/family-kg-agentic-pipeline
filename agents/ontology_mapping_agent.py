from __future__ import annotations

import json
import os
from dataclasses import dataclass
from typing import Any

import openai
import structlog
from openai import APIConnectionError, APITimeoutError, RateLimitError
from tenacity import retry, retry_if_exception_type, stop_after_attempt, wait_exponential

from ontology.schema_loader import ObjectProperty, OntologySchema

logger = structlog.get_logger(__name__)


class OntologyMappingAgentError(Exception):
    """Raised when the extraction output cannot be mapped onto the ontology schema."""


@dataclass(frozen=True)
class UnmappedRelation:
    """A relation whose relation_phrase did not map to any ontology predicate, or whose
    endpoint entity types don't satisfy the chosen predicate's domain/range."""

    subject: str
    object: str
    relation_phrase: str
    reason: str


@dataclass(frozen=True)
class OntologyMappingResult:
    entities: list[dict[str, Any]]
    relations: list[dict[str, Any]]
    unmapped_relations: tuple[UnmappedRelation, ...]


def _build_predicate_reference(schema: OntologySchema) -> str:
    """Render schema.object_properties as a numbered reference the model can pick from,
    stating each predicate's domain/range class constraints (if any) and comment."""
    lines = []
    for prop in schema.object_properties:
        domain = prop.domain_class or "any type"
        range_ = prop.range_class or "any type"
        line = f"- {prop.local_name}: subject must be {domain}, object must be {range_}."
        if prop.comment:
            line += f" {prop.comment}"
        lines.append(line)
    return "\n".join(lines) if lines else "(no object properties declared)"


def _build_mapping_system_prompt(schema: OntologySchema) -> str:
    """Build a system prompt listing exactly the object properties declared in `schema`,
    so mapping works for whatever domain ontology is given rather than a hardcoded set of
    family predicates.
    """
    reference = _build_predicate_reference(schema)
    return f"""You map free-text relation descriptions onto a fixed ontology of predicates.
You will receive a list of entities (with id and type) and a list of relations, each with a
subject id, an object id, and a relation_phrase describing how subject relates to object in
the source text.

Available ontology predicates (choose exactly one, or null if none fit):
{reference}

For each relation, decide which single predicate from the list above best matches the
relation_phrase, respecting the subject/object type constraints given for each predicate. If
the relation_phrase does not correspond to any of these predicates, or the entity types do
not satisfy a predicate's constraints, set predicate to null. Do not force a mapping that is
not clearly supported by the relation_phrase.

Return exactly one mapping object per input relation, in the same order, echoing back the
same subject and object you were given for that relation.
"""


def _mapping_response_format(schema: OntologySchema, relation_count: int) -> dict[str, Any]:
    predicate_names = [prop.local_name for prop in schema.object_properties]
    return {
        "type": "json_schema",
        "json_schema": {
            "name": "ontology_mapping",
            "strict": True,
            "schema": {
                "type": "object",
                "additionalProperties": False,
                "required": ["mappings"],
                "properties": {
                    "mappings": {
                        "type": "array",
                        "minItems": relation_count,
                        "maxItems": relation_count,
                        "items": {
                            "type": "object",
                            "additionalProperties": False,
                            "required": ["subject", "object", "predicate"],
                            "properties": {
                                "subject": {"type": "string"},
                                "object": {"type": "string"},
                                "predicate": {
                                    "type": ["string", "null"],
                                    "enum": [*predicate_names, None],
                                },
                            },
                        },
                    }
                },
            },
        },
    }


def _build_user_payload(entities: list[dict[str, Any]], relations: list[dict[str, Any]]) -> str:
    typed_entities = [{"id": entity.get("id"), "type": entity.get("type")} for entity in entities]
    relation_prompts = [
        {
            "subject": relation.get("subject"),
            "object": relation.get("object"),
            "relation_phrase": relation.get("relation_phrase"),
        }
        for relation in relations
    ]
    return json.dumps({"entities": typed_entities, "relations": relation_prompts})


def _validate_mapping_result(
    parsed: Any,
    relations: list[dict[str, Any]],
    object_properties_by_name: dict[str, ObjectProperty],
) -> list[dict[str, Any]]:
    if not isinstance(parsed, dict) or set(parsed) != {"mappings"}:
        raise OntologyMappingAgentError("Mapping result must be an object with a single 'mappings' key")

    mappings = parsed["mappings"]
    if not isinstance(mappings, list) or len(mappings) != len(relations):
        raise OntologyMappingAgentError(
            f"Expected {len(relations)} mapping(s), got "
            f"{len(mappings) if isinstance(mappings, list) else 'non-list'}"
        )

    for index, (mapping, relation) in enumerate(zip(mappings, relations)):
        if not isinstance(mapping, dict) or set(mapping) != {"subject", "object", "predicate"}:
            raise OntologyMappingAgentError(f"mappings[{index}] has an unexpected shape")
        if mapping["subject"] != relation.get("subject") or mapping["object"] != relation.get("object"):
            raise OntologyMappingAgentError(
                f"mappings[{index}] subject/object does not match relations[{index}]"
            )
        predicate = mapping["predicate"]
        if predicate is not None and predicate not in object_properties_by_name:
            raise OntologyMappingAgentError(f"mappings[{index}] has unsupported predicate: {predicate}")

    return mappings


@retry(
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=0.1, min=0.1, max=1),
    retry=retry_if_exception_type((APIConnectionError, APITimeoutError, RateLimitError)),
    reraise=True,
)
def _create_completion(
    client: "openai.OpenAI",
    model: str,
    system_prompt: str,
    response_format: dict[str, Any],
    user_payload: str,
) -> Any:
    return client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_payload},
        ],
        response_format=response_format,
    )


def ontology_mapping_agent(
    extraction_result: dict[str, Any],
    schema: OntologySchema,
    *,
    client: "openai.OpenAI | None" = None,
) -> dict[str, Any]:
    """Convert generic extraction_agent output into the entities/relations shape
    kg_builder_agent expects, for whatever ontology `schema` describes."""
    result = ontology_mapping_agent_with_diagnostics(extraction_result, schema, client=client)
    return {
        "entities": result.entities,
        "relations": result.relations,
    }


def ontology_mapping_agent_with_diagnostics(
    extraction_result: dict[str, Any],
    schema: OntologySchema,
    *,
    client: "openai.OpenAI | None" = None,
) -> OntologyMappingResult:
    try:
        if (
            not isinstance(extraction_result, dict)
            or "entities" not in extraction_result
            or "relations" not in extraction_result
        ):
            raise OntologyMappingAgentError("extraction_result must contain 'entities' and 'relations'")

        entities = extraction_result["entities"]
        relations = extraction_result["relations"]
        entity_type_by_id = {str(e["id"]): e.get("type") for e in entities}

        if not relations:
            logger.info("ontology_mapping_agent_skipped_empty_relations")
            return OntologyMappingResult(entities=entities, relations=[], unmapped_relations=())

        object_properties_by_name = {prop.local_name: prop for prop in schema.object_properties}
        if not object_properties_by_name:
            logger.warning("ontology_mapping_agent_no_object_properties_declared")
            unmapped = tuple(
                UnmappedRelation(
                    subject=str(relation.get("subject", "")),
                    object=str(relation.get("object", "")),
                    relation_phrase=str(relation.get("relation_phrase", "")),
                    reason="ontology declares no object properties",
                )
                for relation in relations
            )
            return OntologyMappingResult(entities=entities, relations=[], unmapped_relations=unmapped)

        model = os.getenv("OPENAI_MODEL", "gpt-oss:120b")
        api_client = client or openai.OpenAI(
            api_key=os.getenv("OPENAI_API_KEY"),
            base_url=os.getenv("OPENAI_BASE_URL"),
        )

        user_payload = _build_user_payload(entities, relations)
        system_prompt = _build_mapping_system_prompt(schema)
        response_format = _mapping_response_format(schema, len(relations))
        logger.info(
            "ontology_mapping_agent_calling_openai",
            relation_count=len(relations),
            model=model,
            ontology_namespace=schema.namespace,
        )
        response = _create_completion(api_client, model, system_prompt, response_format, user_payload)
        content = response.choices[0].message.content
        if not isinstance(content, str):
            raise OntologyMappingAgentError("Model returned non-string content")
        try:
            parsed = json.loads(content)
        except json.JSONDecodeError as exc:
            raise OntologyMappingAgentError(f"Model returned malformed JSON: {content!r}") from exc

        mappings = _validate_mapping_result(parsed, relations, object_properties_by_name)

        mapped_relations: list[dict[str, Any]] = []
        unmapped: list[UnmappedRelation] = []

        for mapping, relation in zip(mappings, relations):
            predicate_name = mapping["predicate"]
            subject_id = str(relation.get("subject", ""))
            object_id = str(relation.get("object", ""))
            relation_phrase = str(relation.get("relation_phrase", ""))

            if predicate_name is None:
                unmapped.append(
                    UnmappedRelation(
                        subject=subject_id,
                        object=object_id,
                        relation_phrase=relation_phrase,
                        reason="relation_phrase did not match any ontology predicate",
                    )
                )
                continue

            prop = object_properties_by_name[predicate_name]
            subject_type = entity_type_by_id.get(subject_id)
            object_type = entity_type_by_id.get(object_id)

            # Only enforce domain/range when the endpoint's type is actually known; an
            # unknown type usually means a dangling reference, which kg_builder_agent
            # already reports separately, so it isn't re-flagged as a mapping problem here.
            if subject_type is not None and prop.domain_class is not None and subject_type != prop.domain_class:
                unmapped.append(
                    UnmappedRelation(
                        subject=subject_id,
                        object=object_id,
                        relation_phrase=relation_phrase,
                        reason=(
                            f"subject type '{subject_type}' does not satisfy {predicate_name}'s "
                            f"expected domain '{prop.domain_class}'"
                        ),
                    )
                )
                continue
            if object_type is not None and prop.range_class is not None and object_type != prop.range_class:
                unmapped.append(
                    UnmappedRelation(
                        subject=subject_id,
                        object=object_id,
                        relation_phrase=relation_phrase,
                        reason=(
                            f"object type '{object_type}' does not satisfy {predicate_name}'s "
                            f"expected range '{prop.range_class}'"
                        ),
                    )
                )
                continue

            mapped_relations.append({"subject": subject_id, "predicate": predicate_name, "object": object_id})

        logger.info(
            "ontology_mapping_agent_succeeded",
            mapped_relation_count=len(mapped_relations),
            unmapped_count=len(unmapped),
        )
        return OntologyMappingResult(
            entities=entities,
            relations=mapped_relations,
            unmapped_relations=tuple(unmapped),
        )
    except OntologyMappingAgentError:
        logger.exception("ontology_mapping_agent_failed")
        raise
    except (APIConnectionError, APITimeoutError, RateLimitError) as exc:
        logger.exception("ontology_mapping_agent_failed", error=str(exc))
        raise OntologyMappingAgentError(f"OpenAI API error after retries exhausted: {exc}") from exc
    except openai.OpenAIError as exc:
        logger.exception("ontology_mapping_agent_failed", error=str(exc))
        raise OntologyMappingAgentError(f"OpenAI API error: {exc}") from exc
    except Exception as exc:
        logger.exception("ontology_mapping_agent_failed", error=str(exc))
        raise