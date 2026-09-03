from __future__ import annotations

import json
import os
import re
import time
from dataclasses import dataclass
from typing import Any

import openai
import structlog
from openai import APIConnectionError, APITimeoutError, RateLimitError
from tenacity import retry, retry_if_exception_type, stop_after_attempt, wait_exponential

from ontology.schema_loader import ObjectProperty, OntologySchema
from core.llm_config import LLMSettings, completion_parameters, create_client, load_llm_settings

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


def _normalized_phrase(value: str) -> str:
    value = re.sub(r"([a-z0-9])([A-Z])", r"\1 \2", value)
    return " ".join(re.sub(r"[^a-z0-9]+", " ", value.casefold()).split())


def _property_phrases(prop: ObjectProperty) -> set[str]:
    phrases = {_normalized_phrase(prop.local_name)}
    if prop.label:
        phrases.add(_normalized_phrase(prop.label))
    expanded = set(phrases)
    for phrase in phrases:
        if phrase.startswith("has "):
            expanded.add(phrase[4:])
    return expanded


def _deterministic_mapping(
    relation: dict[str, Any],
    entity_type_by_id: dict[str, str],
    schema: OntologySchema,
) -> dict[str, Any] | None:
    phrase = _normalized_phrase(relation["relation_phrase"])
    candidates = []
    for prop in schema.object_properties:
        direct_phrases = {_normalized_phrase(value) for value in prop.direct_phrases}
        inverse_phrases = {_normalized_phrase(value) for value in prop.inverse_phrases}
        if phrase in inverse_phrases:
            candidates.append((prop, True))
        elif phrase in direct_phrases:
            candidates.append((prop, False))
        elif phrase in _property_phrases(prop):
            candidates.append((prop, None))
    if len(candidates) != 1:
        return None
    prop, explicit_swap = candidates[0]
    subject = relation["subject"]
    object_ = relation["object"]
    subject_type = entity_type_by_id[subject]
    object_type = entity_type_by_id[object_]
    direct = schema.class_satisfies(subject_type, prop.domain_class) and schema.class_satisfies(
        object_type, prop.range_class
    )
    swapped = schema.class_satisfies(object_type, prop.domain_class) and schema.class_satisfies(
        subject_type, prop.range_class
    )
    if explicit_swap is None:
        if not direct and not swapped:
            return None
        effective_swap = bool(swapped and not direct)
    else:
        oriented_valid = swapped if explicit_swap else direct
        if not oriented_valid:
            return None
        effective_swap = explicit_swap
    return {
        "subject": subject,
        "object": object_,
        "predicate": prop.local_name,
        "swap_endpoints": effective_swap,
    }


def _build_predicate_reference(schema: OntologySchema) -> str:
    """Render schema.object_properties as a numbered reference the model can pick from,
    stating each predicate's domain/range class constraints (if any) and comment."""
    lines = []
    for prop in schema.object_properties:
        domain = prop.domain_class or "any type"
        range_ = prop.range_class or "any type"
        label = f" ({prop.label})" if prop.label else ""
        line = f"- {prop.local_name}{label}: subject must be {domain}, object must be {range_}."
        if prop.comment:
            line += f" {prop.comment}"
        if prop.direct_phrases:
            line += f" Direct phrases: {', '.join(prop.direct_phrases)}."
        if prop.inverse_phrases:
            line += f" Inverse phrases (swap endpoints): {', '.join(prop.inverse_phrases)}."
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
same subject and object you were given for that relation. Set swap_endpoints to true when
the phrase is expressed in the opposite direction from the ontology predicate. For example,
"Alice is director of Film" must become Film hasDirector Alice by swapping the endpoints.
Return JSON only, without markdown, commentary, or reasoning text.
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
                            "required": ["subject", "object", "predicate", "swap_endpoints"],
                            "properties": {
                                "subject": {"type": "string"},
                                "object": {"type": "string"},
                                "predicate": {
                                    "type": ["string", "null"],
                                    "enum": [*predicate_names, None],
                                },
                                "swap_endpoints": {"type": "boolean"},
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
        if not isinstance(mapping, dict) or set(mapping) != {
            "subject", "object", "predicate", "swap_endpoints"
        }:
            raise OntologyMappingAgentError(f"mappings[{index}] has an unexpected shape")
        if mapping["subject"] != relation.get("subject") or mapping["object"] != relation.get("object"):
            raise OntologyMappingAgentError(
                f"mappings[{index}] subject/object does not match relations[{index}]"
            )
        predicate = mapping["predicate"]
        if predicate is not None and predicate not in object_properties_by_name:
            raise OntologyMappingAgentError(f"mappings[{index}] has unsupported predicate: {predicate}")
        if not isinstance(mapping["swap_endpoints"], bool):
            raise OntologyMappingAgentError(f"mappings[{index}].swap_endpoints must be boolean")

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
    settings: LLMSettings,
) -> Any:
    return client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_payload},
        ],
        **completion_parameters(settings, response_format),
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
        "unmapped_relations": [item.__dict__ for item in result.unmapped_relations],
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
        if not isinstance(entities, list) or not isinstance(relations, list):
            raise OntologyMappingAgentError("'entities' and 'relations' must be lists")
        entity_type_by_id: dict[str, str] = {}
        valid_types = {cls.local_name for cls in schema.classes}
        for index, entity in enumerate(entities):
            if not isinstance(entity, dict) or not isinstance(entity.get("id"), str):
                raise OntologyMappingAgentError(f"entities[{index}] must contain a string id")
            entity_id = entity["id"]
            entity_type = entity.get("type")
            if not entity_id or entity_id in entity_type_by_id:
                raise OntologyMappingAgentError(f"Duplicate or empty entity id: {entity_id!r}")
            if entity_type not in valid_types:
                raise OntologyMappingAgentError(f"entities[{index}] has unsupported type: {entity_type!r}")
            entity_type_by_id[entity_id] = entity_type
        for index, relation in enumerate(relations):
            if not isinstance(relation, dict):
                raise OntologyMappingAgentError(f"relations[{index}] must be an object")
            for field in ("subject", "object", "relation_phrase"):
                if not isinstance(relation.get(field), str) or not relation[field]:
                    raise OntologyMappingAgentError(f"relations[{index}].{field} must be a non-empty string")
            if relation["subject"] not in entity_type_by_id or relation["object"] not in entity_type_by_id:
                raise OntologyMappingAgentError(f"relations[{index}] contains a dangling entity reference")

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

        mappings_by_index: dict[int, dict[str, Any]] = {}
        unresolved: list[dict[str, Any]] = []
        unresolved_indices: list[int] = []
        for index, relation in enumerate(relations):
            deterministic = _deterministic_mapping(relation, entity_type_by_id, schema)
            if deterministic is not None:
                mappings_by_index[index] = deterministic
            else:
                unresolved.append(relation)
                unresolved_indices.append(index)

        if unresolved:
            try:
                settings = load_llm_settings()
            except ValueError as exc:
                raise OntologyMappingAgentError(str(exc)) from exc
            model = settings.model
            api_client = client or create_client(settings)
            user_payload = _build_user_payload(entities, unresolved)
            system_prompt = _build_mapping_system_prompt(schema)
            response_format = _mapping_response_format(schema, len(unresolved))
            if settings.provider == "deepseek":
                system_prompt += (
                    "\nYour JSON response must satisfy this exact JSON Schema and include every "
                    "required field:\n"
                    + json.dumps(response_format["json_schema"]["schema"], ensure_ascii=False)
                )
            logger.info(
                "ontology_mapping_agent_calling_openai",
                relation_count=len(unresolved),
                deterministic_count=len(mappings_by_index),
                model=model,
                provider=settings.provider,
                thinking=settings.thinking if settings.provider == "deepseek" else "not_applicable",
                ontology_namespace=schema.namespace,
            )
            started = time.monotonic()
            response = _create_completion(
                api_client,
                model,
                system_prompt,
                response_format,
                user_payload,
                settings,
            )
            elapsed_seconds = time.monotonic() - started
            choices = getattr(response, "choices", None)
            if not choices:
                raise OntologyMappingAgentError("Model returned no choices")
            choice = choices[0]
            finish_reason = getattr(choice, "finish_reason", None)
            if finish_reason not in (None, "stop"):
                raise OntologyMappingAgentError(f"Model response did not finish normally: {finish_reason}")
            message = getattr(choice, "message", None)
            if message is None or getattr(message, "refusal", None):
                raise OntologyMappingAgentError("Model refused the mapping request")
            content = getattr(message, "content", None)
            if not isinstance(content, str):
                raise OntologyMappingAgentError("Model returned non-string content")
            try:
                parsed = json.loads(content)
            except json.JSONDecodeError as exc:
                raise OntologyMappingAgentError(f"Model returned malformed JSON: {content!r}") from exc
            llm_mappings = _validate_mapping_result(parsed, unresolved, object_properties_by_name)
            mappings_by_index.update(zip(unresolved_indices, llm_mappings))

        mappings = [mappings_by_index[index] for index in range(len(relations))]

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
            direct_valid = schema.class_satisfies(
                entity_type_by_id.get(subject_id), prop.domain_class
            ) and schema.class_satisfies(entity_type_by_id.get(object_id), prop.range_class)
            swapped_valid = schema.class_satisfies(
                entity_type_by_id.get(object_id), prop.domain_class
            ) and schema.class_satisfies(entity_type_by_id.get(subject_id), prop.range_class)

            # Domain/range constraints are authoritative. If only one direction is
            # valid, use it regardless of the LLM's swap decision.
            effective_swap = (
                mapping["swap_endpoints"] if direct_valid == swapped_valid else swapped_valid
            )
            if effective_swap:
                subject_id, object_id = object_id, subject_id

            subject_type = entity_type_by_id.get(subject_id)
            object_type = entity_type_by_id.get(object_id)

            if not schema.class_satisfies(subject_type, prop.domain_class):
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
            if not schema.class_satisfies(object_type, prop.range_class):
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

            mapped_relations.append(
                {
                    "subject": subject_id,
                    "predicate": predicate_name,
                    "object": object_id,
                    "relation_phrase": relation_phrase,
                    "qualifiers": relation.get("qualifiers", {"year": None, "note": None}),
                    "source_subject": relation.get("subject"),
                    "source_object": relation.get("object"),
                    "endpoints_swapped": effective_swap,
                }
            )

        logger.info(
            "ontology_mapping_agent_succeeded",
            mapped_relation_count=len(mapped_relations),
            unmapped_count=len(unmapped),
            elapsed_seconds=round(locals().get("elapsed_seconds", 0.0), 3),
            request_id=getattr(locals().get("response"), "_request_id", None),
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
