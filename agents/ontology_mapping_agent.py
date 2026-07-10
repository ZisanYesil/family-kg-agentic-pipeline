from __future__ import annotations

import json
import os
from dataclasses import dataclass
from typing import Any

import openai
import structlog
from openai import APIConnectionError, APITimeoutError, RateLimitError
from tenacity import retry, retry_if_exception_type, stop_after_attempt, wait_exponential

logger = structlog.get_logger(__name__)

# The 6 direct person-to-person predicates the ontology (and family_shapes.ttl) validates
# for non-spousal relations, plus a synthetic "isSpouseOf" marker used only inside this
# agent to flag a relation as spousal so it can be reified into a fhkb:Marriage individual
# by kg_builder_agent. This marker is never written to RDF directly. hasHusband/hasWife are
# intentionally NOT offered to the model: if the model could pick either those or
# isSpouseOf for the same kind of relation, marriage_year and Marriage reification would
# silently be lost whenever it picked the direct predicate instead. Routing every spousal
# relation through the single isSpouseOf marker removes that ambiguity entirely.
DIRECT_PREDICATES = (
    "hasFather",
    "hasMother",
    "hasBrother",
    "hasSister",
    "hasSon",
    "hasDaughter",
)
SPOUSE_MARKER = "isSpouseOf"
VALID_MAPPING_PREDICATES = DIRECT_PREDICATES + (SPOUSE_MARKER,)

PREDICATE_REFERENCE = """Available ontology predicates (choose exactly one, or null if none fit):
- hasFather: subject's father is object. object must be male.
- hasMother: subject's mother is object. object must be female.
- hasBrother: object is subject's brother. object must be male.
- hasSister: object is subject's sister. object must be female.
- hasSon: object is subject's son. object must be male.
- hasDaughter: object is subject's daughter. object must be female.
- isSpouseOf: any spousal/marriage relation (married, wed, husband, wife, spouse, partner
  in marriage), regardless of which direction the text states it or which gendered word it
  uses. Always use isSpouseOf for these, never invent a different label. A downstream step
  resolves this into the correct gendered marriage structure using each entity's recorded
  sex.
"""

MAPPING_SYSTEM_PROMPT = f"""You map free-text family relation descriptions onto a fixed
ontology of predicates. You will receive a list of people (with id and sex) and a list of
relations, each with a subject id, an object id, and a relation_phrase describing how
subject relates to object in the source text.

{PREDICATE_REFERENCE}

For each relation, decide which single predicate from the list above best matches the
relation_phrase. If the relation_phrase does not correspond to any of these predicates
(for example: "godmother of", "employer of", "neighbor of", any non-family or non-spousal
relation), set predicate to null. Do not force a mapping that is not clearly supported by
the relation_phrase. Do not use entity sex to override what the relation_phrase states;
sex is provided only as context.

Return exactly one mapping object per input relation, in the same order, echoing back the
same subject and object you were given for that relation.
"""


class OntologyMappingAgentError(Exception):
    """Raised when the extraction output cannot be mapped onto the ontology schema."""


@dataclass(frozen=True)
class UnmappedRelation:
    """A relation whose relation_phrase did not map to any ontology predicate, or a
    spousal relation whose partner genders could not be resolved."""

    subject: str
    object: str
    relation_phrase: str
    reason: str


@dataclass(frozen=True)
class OntologyMappingResult:
    entities: list[dict[str, Any]]
    relations: list[dict[str, Any]]
    marriages: list[dict[str, Any]]
    unmapped_relations: tuple[UnmappedRelation, ...]


def _mapping_response_format(relation_count: int) -> dict[str, Any]:
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
                                    "enum": [*VALID_MAPPING_PREDICATES, None],
                                },
                            },
                        },
                    }
                },
            },
        },
    }


def _build_user_payload(entities: list[dict[str, Any]], relations: list[dict[str, Any]]) -> str:
    people = [
        {"id": entity.get("id"), "sex": entity.get("sex")}
        for entity in entities
    ]
    relation_prompts = [
        {
            "subject": relation.get("subject"),
            "object": relation.get("object"),
            "relation_phrase": relation.get("relation_phrase"),
        }
        for relation in relations
    ]
    return json.dumps({"people": people, "relations": relation_prompts})


def _validate_mapping_result(parsed: Any, relations: list[dict[str, Any]]) -> list[dict[str, Any]]:
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
        if predicate is not None and predicate not in VALID_MAPPING_PREDICATES:
            raise OntologyMappingAgentError(f"mappings[{index}] has unsupported predicate: {predicate}")

    return mappings


@retry(
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=0.1, min=0.1, max=1),
    retry=retry_if_exception_type((APIConnectionError, APITimeoutError, RateLimitError)),
    reraise=True,
)
def _create_completion(
    client: "openai.OpenAI", model: str, user_payload: str, relation_count: int
) -> Any:
    return client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": MAPPING_SYSTEM_PROMPT},
            {"role": "user", "content": user_payload},
        ],
        response_format=_mapping_response_format(relation_count),
    )


def _resolve_spouse_partners(
    subject_id: str,
    object_id: str,
    entity_sex_by_id: dict[str, str],
) -> tuple[str, str] | None:
    """Return (male_partner, female_partner) for a spousal relation, or None if the pair's
    sexes cannot be used to confidently assign the ontology's gendered partner roles."""
    subject_sex = entity_sex_by_id.get(subject_id)
    object_sex = entity_sex_by_id.get(object_id)

    if subject_sex == "Male" and object_sex == "Female":
        return subject_id, object_id
    if subject_sex == "Female" and object_sex == "Male":
        return object_id, subject_id
    return None


def ontology_mapping_agent(
    extraction_result: dict[str, Any], *, client: "openai.OpenAI | None" = None
) -> dict[str, Any]:
    """Convert generic extraction_agent output into the entities/relations/marriages
    shape kg_builder_agent expects."""
    result = ontology_mapping_agent_with_diagnostics(extraction_result, client=client)
    return {
        "entities": result.entities,
        "relations": result.relations,
        "marriages": result.marriages,
    }


def ontology_mapping_agent_with_diagnostics(
    extraction_result: dict[str, Any], *, client: "openai.OpenAI | None" = None
) -> OntologyMappingResult:
    try:
        if not isinstance(extraction_result, dict) or "entities" not in extraction_result or "relations" not in extraction_result:
            raise OntologyMappingAgentError("extraction_result must contain 'entities' and 'relations'")

        entities = extraction_result["entities"]
        relations = extraction_result["relations"]
        entity_sex_by_id = {str(e["id"]): e.get("sex") for e in entities}

        if not relations:
            logger.info("ontology_mapping_agent_skipped_empty_relations")
            return OntologyMappingResult(
                entities=entities, relations=[], marriages=[], unmapped_relations=()
            )

        model = os.getenv("OPENAI_MODEL", "gpt-oss:120b")
        api_client = client or openai.OpenAI(
            api_key=os.getenv("OPENAI_API_KEY"),
            base_url=os.getenv("OPENAI_BASE_URL"),
        )

        user_payload = _build_user_payload(entities, relations)
        logger.info("ontology_mapping_agent_calling_openai", relation_count=len(relations), model=model)
        response = _create_completion(api_client, model, user_payload, len(relations))
        content = response.choices[0].message.content
        if not isinstance(content, str):
            raise OntologyMappingAgentError("Model returned non-string content")
        try:
            parsed = json.loads(content)
        except json.JSONDecodeError as exc:
            raise OntologyMappingAgentError(f"Model returned malformed JSON: {content!r}") from exc

        mappings = _validate_mapping_result(parsed, relations)

        mapped_relations: list[dict[str, Any]] = []
        marriages: list[dict[str, Any]] = []
        unmapped: list[UnmappedRelation] = []

        for mapping, relation in zip(mappings, relations):
            predicate = mapping["predicate"]
            subject_id = str(relation.get("subject", ""))
            object_id = str(relation.get("object", ""))
            relation_phrase = str(relation.get("relation_phrase", ""))

            if predicate is None:
                unmapped.append(
                    UnmappedRelation(
                        subject=subject_id,
                        object=object_id,
                        relation_phrase=relation_phrase,
                        reason="relation_phrase did not match any ontology predicate",
                    )
                )
                continue

            if predicate == SPOUSE_MARKER:
                partners = _resolve_spouse_partners(subject_id, object_id, entity_sex_by_id)
                if partners is None:
                    unmapped.append(
                        UnmappedRelation(
                            subject=subject_id,
                            object=object_id,
                            relation_phrase=relation_phrase,
                            reason=(
                                "spousal relation but partner sexes are missing, unknown, "
                                "or not male/female, so hasMalePartner/hasFemalePartner "
                                "cannot be assigned"
                            ),
                        )
                    )
                    continue
                male_partner, female_partner = partners
                qualifiers = relation.get("qualifiers") or {}
                marriages.append(
                    {
                        "male_partner": male_partner,
                        "female_partner": female_partner,
                        "marriage_year": qualifiers.get("year"),
                    }
                )
                continue

            mapped_relations.append({"subject": subject_id, "predicate": predicate, "object": object_id})

        logger.info(
            "ontology_mapping_agent_succeeded",
            mapped_relation_count=len(mapped_relations),
            marriage_count=len(marriages),
            unmapped_count=len(unmapped),
        )
        return OntologyMappingResult(
            entities=entities,
            relations=mapped_relations,
            marriages=marriages,
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