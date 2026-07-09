from __future__ import annotations

import json
import os
from collections.abc import Mapping
from typing import Any

import openai
import structlog
from openai import APIConnectionError, APITimeoutError, RateLimitError
from tenacity import retry, retry_if_exception_type, stop_after_attempt, wait_exponential

logger = structlog.get_logger(__name__)

TOP_LEVEL_FIELDS = {"entities", "relations"}
ENTITY_FIELDS = {"id", "label", "sex", "birth_year", "death_year", "aliases"}
RELATION_FIELDS = {"subject", "object", "relation_phrase", "qualifiers"}
QUALIFIER_FIELDS = {"year", "note"}
VALID_SEX_VALUES = {"Male", "Female", "Unknown"}


class ExtractionAgentError(Exception):
    """Raised when extraction cannot produce a usable structured result."""


EXTRACTION_SYSTEM_PROMPT = """You extract structured family knowledge from narrative text.

Identify people, their sex, birth/death years, and known aliases. Use stable lowercase
underscore ids, including the birth year when known, such as john_doe_1900. Reuse the
same entity id consistently whenever the same person is referenced again in the same text.

Identify every stated or clearly implied relationship between two people as a relation
triple: subject, object, and a short free-text relation_phrase written in your own words
describing how subject relates to object (for example: "father of", "married to",
"sister of", "adopted son of", "godmother of"). Do NOT normalize the phrase to any fixed
vocabulary or ontology property name, and do NOT restrict yourself to a predefined list of
relation types; describe the relationship as it is expressed or implied in the text,
however unusual it is. Prefer the most specific direct relation stated in the text over an
inferred indirect one.

Always include a qualifiers object for every relation. If the relation carries an
additional fact directly tied to it (such as a marriage year, an adoption year, or a short
qualifying note), record it in qualifiers.year and/or qualifiers.note. Use null for
qualifier values that are not stated.

Never invent facts that are not stated or clearly implied. If no entities or relations can
be found, return empty arrays for both entities and relations.
"""


EXTRACTION_RESPONSE_FORMAT: dict[str, Any] = {
    "type": "json_schema",
    "json_schema": {
        "name": "family_extraction",
        "strict": True,
        "schema": {
            "type": "object",
            "additionalProperties": False,
            "required": ["entities", "relations"],
            "properties": {
                "entities": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "additionalProperties": False,
                        "required": [
                            "id",
                            "label",
                            "sex",
                            "birth_year",
                            "death_year",
                            "aliases",
                        ],
                        "properties": {
                            "id": {"type": "string"},
                            "label": {"type": "string"},
                            "sex": {"type": "string", "enum": ["Male", "Female", "Unknown"]},
                            "birth_year": {"type": ["integer", "null"]},
                            "death_year": {"type": ["integer", "null"]},
                            "aliases": {"type": "array", "items": {"type": "string"}},
                        },
                    },
                },
                "relations": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "additionalProperties": False,
                        "required": ["subject", "object", "relation_phrase", "qualifiers"],
                        "properties": {
                            "subject": {"type": "string"},
                            "object": {"type": "string"},
                            "relation_phrase": {"type": "string"},
                            "qualifiers": {
                                "type": "object",
                                "additionalProperties": False,
                                "required": ["year", "note"],
                                "properties": {
                                    "year": {"type": ["integer", "null"]},
                                    "note": {"type": ["string", "null"]},
                                },
                            },
                        },
                    },
                },
            },
        },
    },
}


def _validate_object(
    value: Any,
    item_name: str,
    required_fields: set[str],
) -> Mapping[str, Any]:
    if not isinstance(value, dict):
        raise ExtractionAgentError(f"{item_name} must be an object")

    keys = set(value)
    missing = required_fields - keys
    if missing:
        missing_fields = ", ".join(sorted(missing))
        raise ExtractionAgentError(f"{item_name} is missing required field(s): {missing_fields}")

    extra = keys - required_fields
    if extra:
        extra_fields = ", ".join(sorted(extra))
        raise ExtractionAgentError(f"{item_name} has unsupported field(s): {extra_fields}")

    return value


def _validate_string_field(item: Mapping[str, Any], field: str, item_name: str) -> None:
    if not isinstance(item[field], str):
        raise ExtractionAgentError(f"{item_name}.{field} must be a string")


def _validate_optional_int_field(item: Mapping[str, Any], field: str, item_name: str) -> None:
    value = item[field]
    if value is not None and (not isinstance(value, int) or isinstance(value, bool)):
        raise ExtractionAgentError(f"{item_name}.{field} must be an integer or null")


def _validate_optional_string_field(item: Mapping[str, Any], field: str, item_name: str) -> None:
    value = item[field]
    if value is not None and not isinstance(value, str):
        raise ExtractionAgentError(f"{item_name}.{field} must be a string or null")


def _validate_entity(entity: Any, index: int) -> None:
    item_name = f"entities[{index}]"
    entity_obj = _validate_object(entity, item_name, ENTITY_FIELDS)

    for field in ("id", "label", "sex"):
        _validate_string_field(entity_obj, field, item_name)

    if entity_obj["sex"] not in VALID_SEX_VALUES:
        raise ExtractionAgentError(
            f"{item_name}.sex must be one of: {', '.join(sorted(VALID_SEX_VALUES))}"
        )

    _validate_optional_int_field(entity_obj, "birth_year", item_name)
    _validate_optional_int_field(entity_obj, "death_year", item_name)

    aliases = entity_obj["aliases"]
    if not isinstance(aliases, list) or not all(isinstance(alias, str) for alias in aliases):
        raise ExtractionAgentError(f"{item_name}.aliases must be a list of strings")


def _validate_relation(relation: Any, index: int) -> None:
    item_name = f"relations[{index}]"
    relation_obj = _validate_object(relation, item_name, RELATION_FIELDS)

    for field in ("subject", "object", "relation_phrase"):
        _validate_string_field(relation_obj, field, item_name)

    qualifiers = _validate_object(
        relation_obj["qualifiers"],
        f"{item_name}.qualifiers",
        QUALIFIER_FIELDS,
    )
    _validate_optional_int_field(qualifiers, "year", f"{item_name}.qualifiers")
    _validate_optional_string_field(qualifiers, "note", f"{item_name}.qualifiers")


def _validate_extraction_result(parsed: Any) -> dict[str, Any]:
    result = dict(_validate_object(parsed, "extraction result", TOP_LEVEL_FIELDS))

    entities = result["entities"]
    if not isinstance(entities, list):
        raise ExtractionAgentError("extraction result.entities must be a list")
    for index, entity in enumerate(entities):
        _validate_entity(entity, index)

    relations = result["relations"]
    if not isinstance(relations, list):
        raise ExtractionAgentError("extraction result.relations must be a list")
    for index, relation in enumerate(relations):
        _validate_relation(relation, index)

    return result


@retry(
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=0.1, min=0.1, max=1),
    retry=retry_if_exception_type((APIConnectionError, APITimeoutError, RateLimitError)),
    reraise=True,
)
def _create_completion(client: "openai.OpenAI", model: str, text: str) -> Any:
    return client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": EXTRACTION_SYSTEM_PROMPT},
            {"role": "user", "content": text},
        ],
        response_format=EXTRACTION_RESPONSE_FORMAT,
    )


def extraction_agent(text: str, *, client: "openai.OpenAI | None" = None) -> dict[str, Any]:
    try:
        if not text.strip():
            raise ExtractionAgentError("Input text is empty")
    except ExtractionAgentError:
        logger.exception("extraction_agent_failed")
        raise

    model = os.getenv("OPENAI_MODEL", "gpt-oss:120b")

    api_client = client or openai.OpenAI(
        api_key=os.getenv("OPENAI_API_KEY"),
        base_url=os.getenv("OPENAI_BASE_URL"),
    )

    try:
        logger.info("extraction_agent_calling_openai", text_length=len(text), model=model)
        response = _create_completion(api_client, model, text)
        content = response.choices[0].message.content
        if not isinstance(content, str):
            raise ExtractionAgentError("Model returned non-string content")
        try:
            parsed = json.loads(content)
        except json.JSONDecodeError as exc:
            raise ExtractionAgentError(f"Model returned malformed JSON: {content!r}") from exc
        parsed = _validate_extraction_result(parsed)

        logger.info(
            "extraction_agent_succeeded",
            entity_count=len(parsed.get("entities", [])),
            relation_count=len(parsed.get("relations", [])),
        )
        return parsed
    except ExtractionAgentError:
        logger.exception("extraction_agent_failed")
        raise
    except (APIConnectionError, APITimeoutError, RateLimitError) as exc:
        logger.exception("extraction_agent_failed", error=str(exc))
        raise ExtractionAgentError(f"OpenAI API error after retries exhausted: {exc}") from exc
    except openai.OpenAIError as exc:
        logger.exception("extraction_agent_failed", error=str(exc))
        raise ExtractionAgentError(f"OpenAI API error: {exc}") from exc
    except Exception as exc:
        logger.exception("extraction_agent_failed", error=str(exc))
        raise
