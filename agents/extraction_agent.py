from __future__ import annotations

import json
import os
from typing import Any

import openai
import structlog
from openai import APIConnectionError, APITimeoutError, RateLimitError
from tenacity import retry, retry_if_exception_type, stop_after_attempt, wait_exponential

logger = structlog.get_logger(__name__)


class ExtractionAgentError(Exception):
    """Raised when extraction cannot produce a usable structured result."""


EXTRACTION_SYSTEM_PROMPT = """You extract structured family knowledge from narrative text.

Identify people, their sex, birth/death years, and known aliases. Use stable lowercase
underscore ids, including the birth year when known, such as john_doe_1900. Reuse the
same entity id consistently whenever the same person is referenced again in the same text.

Identify direct family relations using ONLY this predicate vocabulary:
hasFather, hasMother, hasBrother, hasSister, hasSon, hasDaughter, hasHusband, hasWife.
Choose the gender-specific predicate that matches the sex of the subject/object and the
direction of the stated relationship. For example, use hasFather when the object is male
and is the subject's parent; do not use generic parent/spouse/sibling predicates.

Identify marriages as separate entries in marriages, not as a relation between two people.
Never invent facts that are not stated or clearly implied. If no entities, relations, or
marriages can be found, return an empty array for that field.
"""


EXTRACTION_RESPONSE_FORMAT: dict[str, Any] = {
    "type": "json_schema",
    "json_schema": {
        "name": "family_extraction",
        "strict": True,
        "schema": {
            "type": "object",
            "additionalProperties": False,
            "required": ["entities", "relations", "marriages"],
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
                        "required": ["subject", "predicate", "object"],
                        "properties": {
                            "subject": {"type": "string"},
                            "predicate": {
                                "type": "string",
                                "enum": [
                                    "hasFather",
                                    "hasMother",
                                    "hasBrother",
                                    "hasSister",
                                    "hasSon",
                                    "hasDaughter",
                                    "hasHusband",
                                    "hasWife",
                                ],
                            },
                            "object": {"type": "string"},
                        },
                    },
                },
                "marriages": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "additionalProperties": False,
                        "required": ["male_partner", "female_partner", "marriage_year"],
                        "properties": {
                            "male_partner": {"type": "string"},
                            "female_partner": {"type": "string"},
                            "marriage_year": {"type": ["integer", "null"]},
                        },
                    },
                },
            },
        },
    },
}


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

    model = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
    api_client = client or openai.OpenAI()

    try:
        logger.info("extraction_agent_calling_openai", text_length=len(text), model=model)
        response = _create_completion(api_client, model, text)
        content = response.choices[0].message.content
        try:
            parsed = json.loads(content)
        except json.JSONDecodeError as exc:
            raise ExtractionAgentError(f"Model returned malformed JSON: {content!r}") from exc

        logger.info(
            "extraction_agent_succeeded",
            entity_count=len(parsed.get("entities", [])),
            relation_count=len(parsed.get("relations", [])),
            marriage_count=len(parsed.get("marriages", [])),
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
