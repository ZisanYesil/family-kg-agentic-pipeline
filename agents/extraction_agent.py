from __future__ import annotations

import json
import os
import re
import time
from collections.abc import Mapping
from datetime import date
from typing import Any

import openai
import structlog
from openai import APIConnectionError, APITimeoutError, RateLimitError
from tenacity import retry, retry_if_exception_type, stop_after_attempt, wait_exponential

from ontology.schema_loader import OntologySchema
from core.llm_config import LLMSettings, completion_parameters, create_client, load_llm_settings

logger = structlog.get_logger(__name__)

TOP_LEVEL_FIELDS = {"entities", "relations"}
ENTITY_FIELDS = {"id", "label", "type", "aliases", "attributes"}
RELATION_FIELDS = {"subject", "object", "relation_phrase", "qualifiers"}
QUALIFIER_FIELDS = {"year", "note"}

# Maps schema_loader's normalized range_type names to JSON Schema primitive types
# used for the structured-output response_format.
_RANGE_TYPE_TO_JSON_TYPE = {
    "integer": "integer",
    "string": "string",
    "boolean": "boolean",
    "decimal": "number",
    "date": "string",  # dates are carried as ISO-8601 strings, not a native JSON type
    "gYear": "string",
    "date_or_year": "string",
}

# Python-level type checks used when validating attribute values coming back from the
# model, keyed by the same range_type names as above.
_RANGE_TYPE_VALIDATORS = {
    "integer": lambda v: isinstance(v, int) and not isinstance(v, bool),
    "boolean": lambda v: isinstance(v, bool),
    "decimal": lambda v: isinstance(v, (int, float)) and not isinstance(v, bool),
    "string": lambda v: isinstance(v, str),
    "date": lambda v: isinstance(v, str),
    "gYear": lambda v: isinstance(v, str),
    "date_or_year": lambda v: isinstance(v, str),
}


class ExtractionAgentError(Exception):
    """Raised when extraction cannot produce a usable structured result."""


def _attribute_json_type(range_type: str) -> str:
    return _RANGE_TYPE_TO_JSON_TYPE.get(range_type, "string")


def build_extraction_system_prompt(schema: OntologySchema) -> str:
    """Build a system prompt describing the LLM-ready ontology declared in
    `schema`, so the agent extracts entities/relations for whatever domain ontology it is
    given (family, vehicles, organizations, ...) rather than a hardcoded domain.
    """
    class_lines = []
    for cls in schema.classes:
        superclasses = sorted(
            set(schema.superclasses_by_class.get(cls.local_name, ())) - {cls.local_name},
            key=str.casefold,
        )
        hierarchy = f" (subclass of {', '.join(superclasses)})" if superclasses else ""
        comment = f": {cls.comment}" if cls.comment else ""
        class_lines.append(f"- {cls.local_name}{hierarchy}{comment}")

    attribute_lines = []
    for cls in schema.classes:
        props = schema.datatype_properties_for(cls.local_name)
        if not props:
            continue
        described = ", ".join(
            f"{p.local_name} ({p.range_type})" + (f": {p.comment}" if p.comment else "")
            for p in props
        )
        attribute_lines.append(f"- {cls.local_name}: {described}")

    class_block = "\n".join(class_lines) or "(no classes declared)"
    attribute_block = "\n".join(attribute_lines) or "(no attributes declared)"
    relation_lines = []
    for prop in schema.object_properties:
        domain = prop.domain_class or "any ontology class"
        range_ = prop.range_class or "any ontology class"
        description = f"- {prop.local_name}: {domain} -> {range_}"
        if prop.label and prop.label != prop.local_name:
            description += f"; label: {prop.label}"
        if prop.comment:
            description += f"; {prop.comment}"
        if prop.inverse_of:
            description += f"; inverse: {prop.inverse_of}"
        if prop.direct_phrases:
            description += f"; direct phrases: {', '.join(prop.direct_phrases)}"
        if prop.inverse_phrases:
            description += f"; inverse phrases (reverse endpoints): {', '.join(prop.inverse_phrases)}"
        relation_lines.append(description)
    relation_block = "\n".join(relation_lines) or "(no object properties declared)"

    return f"""You extract structured knowledge from narrative text in order to answer one
specific question, according to a specific domain ontology. Every request gives you both a
question and a context text. Your one objective is to output the minimal reasoning-chain
subgraph that is necessary and sufficient to answer that question -- nothing else. This
scoping rule is absolute and overrides any impression that "found in the text" alone is
reason enough to extract something.

Before writing any output, silently determine the reasoning chain the question requires.
For example, for "When did X's spouse die?" the chain is exactly: X -> spouse -> spouse's
death date. Only entities, attributes, and relations that sit on that chain belong in your
output. An entity that IS part of the chain still gets ONLY the attributes and relations
that the chain needs from it, never its full profile -- e.g. if X's own birth/death dates,
occupation, or other relationships are not part of the chain, leave them out even though
they are true and even though X is being extracted.

Preserve the evidence chain actually stated in the context. Never replace a multi-hop
family chain with a shortcut relationship inferred only from the answer. For example, if
the context states "Edward is Henry's son" and "Henry married Eleanor" and the question
asks for Edward's mother, extract Edward -> father -> Henry and Henry -> spouse -> Eleanor;
do not invent a direct Edward -> mother -> Eleanor edge unless the context itself states
that Eleanor is Edward's mother. Likewise, do not omit an intermediate relative merely
because the final answer can be guessed without representing that relative. The stated
parent-plus-spouse chain is the required benchmark evidence and must not be returned as an
empty extraction merely because the final shortcut relation is unstated. Apply the same
rule to sibling-plus-parent chains used to identify a queried person's parent.

The context text will typically contain unrelated sentences, paragraphs, or even whole
unrelated biographies mixed in as distractors. Distractor content must be ignored
completely: never extract an entity, attribute, or relation merely because it appears in
the text, and never extract a true, well-supported fact about a chain entity just because
it is available -- extract it only if it is itself a link in the chain to the answer.

Only the ontology described below is relevant on top of this scoping rule: ignore any
entities or facts that do not belong to one of the listed types, even if they are part of
the reasoning chain in the source text.

Ontology classes (use exactly one of these as each entity's "type"):
{class_block}

Attributes available per class (fill in a value only if it is explicitly stated in the
text AND is required by the reasoning chain to answer the question; use null for anything
not stated or not needed for the chain; never invent values; an attribute that belongs to
a different class than the entity's own type should also be left null):
{attribute_block}

Ontology object properties (semantic extraction guidance; domain is the subject type and
range is the object type):
{relation_block}

Write date attributes in ISO form: YYYY-MM-DD when a complete date is known, or exactly
four digits (YYYY) when only the year is known. Zero-pad years below 1000 to four digits
(for example, write the year 18 as "0018"). Never return a one-, two-, or three-digit
date value.

For each entity that is part of the reasoning chain and belongs to one of the classes
above, assign a stable lowercase underscore id that stays consistent every time the same
entity is referenced again (for example, include a distinguishing detail such as a year,
number, or short qualifier when the label alone would be ambiguous). Record any
alternative names or labels for the entity as aliases.

When a Country endpoint is expressed through a nationality adjective or demonym, preserve
that exact source expression as an alias of the resolved Country entity. For example,
"an American composer" may resolve to the Country entity labelled "United States", but
that entity must include "American" in aliases. This lets later entity alignment connect
the resolved country to silver evidence that uses the adjective as its entity label.

For each relationship that is itself a link in the reasoning chain between two extracted
entities, record it as a relation triple: subject, object, and a short free-text
relation_phrase written in your own words describing how subject relates to object (for
example: "father of", "married to", "owner of", "manufactured by", "employed by"). Do NOT
normalize the phrase to any fixed vocabulary or predicate name, and do NOT restrict
yourself to a predefined list of relation types; describe the relationship as it is
expressed or implied in the text, however unusual it is, as long as both endpoints are
entities of one of the ontology classes above and the relation is required by the chain.
Do not record a relationship just because both of its endpoints happen to be entities you
extracted for other reasons -- only record it if the relation itself is needed to answer
the question. Prefer the most specific direct relation stated in the text over an inferred
indirect one. The relation_phrase must always describe how the supplied subject relates to
the supplied object; do not reverse their roles.

For directional family phrases, check the grammar against the chosen endpoints before
returning JSON. If the subject is the child and the object is the mother, write "has
mother", "child of", or "son/daughter of"; never write "mother of". Conversely, "mother
of" requires the mother to be the subject and the child to be the object. Apply the same
endpoint check to father, son, daughter, and parent phrases. Also include the terminal
answer relation itself: a family link without the requested burial place, birth place,
date, or other final fact is an incomplete chain.

Use the ontology object properties above to recognize which relations and endpoint
entities the reasoning chain requires. If a required relation needs an endpoint entity (for
example a Country for a person's nationality), include that entity even when the text
expresses it indirectly through a demonym or adjective. Still write relation_phrase in
natural language; the later mapping stage will normalize it to the exact ontology
predicate.

Always include a qualifiers object for every relation you extract. If the relation carries
an additional fact directly tied to it (such as a year it started, ended, or occurred, or a
short qualifying note) that is itself needed by the chain, record it in qualifiers.year
and/or qualifiers.note. Use null for qualifier values that are not stated or not needed.

Never invent facts that are not stated or clearly implied. If no entities or relations
belonging to this ontology are required by the reasoning chain, return empty arrays for
both entities and relations, even if the text contains many other extractable facts.

The hasDemonym attribute is lookup metadata, not a required output when you have already
resolved a nationality adjective to its Country entity. For example, after resolving
"American" to the United States, emit the required person-to-country relationship but
leave United States.hasDemonym null. Fill hasDemonym only when the question explicitly
asks for a country's demonym itself.

Return JSON only. The JSON must have exactly the entities and relations structure requested;
do not include markdown, commentary, or reasoning text.
"""


def build_extraction_response_format(schema: OntologySchema) -> dict[str, Any]:
    """Build the structured-output JSON schema for `schema`'s classes and datatype
    properties. Every entity carries the full set of the ontology's attribute names
    (nullable), since strict JSON Schema cannot branch the property set on "type"; the
    prompt instructs the model to leave attributes for other classes null, and
    `_validate_attributes` accepts that shape.
    """
    class_names = [cls.local_name for cls in schema.classes]
    if not class_names:
        raise ExtractionAgentError("Ontology schema has no classes; cannot build extraction schema")

    attribute_names = [prop.local_name for prop in schema.datatype_properties]
    attribute_properties = {
        prop.local_name: {"type": [_attribute_json_type(prop.range_type), "null"]}
        for prop in schema.datatype_properties
    }

    return {
        "type": "json_schema",
        "json_schema": {
            "name": "ontology_extraction",
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
                            "required": ["id", "label", "type", "aliases", "attributes"],
                            "properties": {
                                "id": {"type": "string"},
                                "label": {"type": "string"},
                                "type": {"type": "string", "enum": class_names},
                                "aliases": {"type": "array", "items": {"type": "string"}},
                                "attributes": {
                                    "type": "object",
                                    "additionalProperties": False,
                                    "required": attribute_names,
                                    "properties": attribute_properties,
                                },
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


def _normalize_date_value(value: str) -> str:
    """Zero-pad historical CE years without changing date precision or meaning."""
    if re.fullmatch(r"\d{1,3}", value):
        return value.zfill(4)
    match = re.fullmatch(r"(\d{1,3})-(\d{2})-(\d{2})", value)
    if match:
        return f"{match.group(1).zfill(4)}-{match.group(2)}-{match.group(3)}"
    return value


def _validate_date_value(value: str, item_name: str) -> None:
    if re.fullmatch(r"\d{4}", value):
        return
    if re.fullmatch(r"\d{4}-\d{2}-\d{2}", value):
        try:
            date.fromisoformat(value)
        except ValueError as exc:
            raise ExtractionAgentError(f"{item_name} is not a valid ISO date") from exc
        return
    raise ExtractionAgentError(f"{item_name} must use YYYY or YYYY-MM-DD precision")


def _validate_attributes(
    value: Any,
    item_name: str,
    schema: OntologySchema,
    entity_type: str,
) -> None:
    attribute_names = {prop.local_name for prop in schema.datatype_properties}
    attrs_obj = _validate_object(value, item_name, attribute_names)

    for prop in schema.datatype_properties:
        attr_value = attrs_obj[prop.local_name]
        if attr_value is None:
            continue
        validator = _RANGE_TYPE_VALIDATORS.get(prop.range_type, _RANGE_TYPE_VALIDATORS["string"])
        if not validator(attr_value):
            raise ExtractionAgentError(
                f"{item_name}.{prop.local_name} must be a {prop.range_type} or null"
            )
        if not schema.class_satisfies(entity_type, prop.domain_class):
            raise ExtractionAgentError(
                f"{item_name}.{prop.local_name} is not valid for entity type {entity_type}"
            )
        if prop.range_type in {"date", "gYear", "date_or_year"}:
            attr_value = _normalize_date_value(attr_value)
            # _validate_object has already established that this is the model's
            # mutable JSON object. Persist representation-only normalization so
            # the KG builder receives the same validated lexical form.
            attrs_obj[prop.local_name] = attr_value
            _validate_date_value(attr_value, f"{item_name}.{prop.local_name}")


def _validate_entity(entity: Any, index: int, schema: OntologySchema, class_names: set[str]) -> None:
    item_name = f"entities[{index}]"
    entity_obj = _validate_object(entity, item_name, ENTITY_FIELDS)

    for field in ("id", "label", "type"):
        _validate_string_field(entity_obj, field, item_name)

    if entity_obj["type"] not in class_names:
        raise ExtractionAgentError(
            f"{item_name}.type must be one of: {', '.join(sorted(class_names))}"
        )

    aliases = entity_obj["aliases"]
    if not isinstance(aliases, list) or not all(isinstance(alias, str) for alias in aliases):
        raise ExtractionAgentError(f"{item_name}.aliases must be a list of strings")

    _validate_attributes(
        entity_obj["attributes"],
        f"{item_name}.attributes",
        schema,
        entity_obj["type"],
    )


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


def _validate_extraction_result(parsed: Any, schema: OntologySchema) -> dict[str, Any]:
    result = dict(_validate_object(parsed, "extraction result", TOP_LEVEL_FIELDS))
    class_names = {cls.local_name for cls in schema.classes}

    entities = result["entities"]
    if not isinstance(entities, list):
        raise ExtractionAgentError("extraction result.entities must be a list")
    for index, entity in enumerate(entities):
        _validate_entity(entity, index, schema, class_names)

    entity_ids = [entity["id"] for entity in entities]
    if any(not entity_id.strip() for entity_id in entity_ids):
        raise ExtractionAgentError("Entity ids must not be empty")
    if len(entity_ids) != len(set(entity_ids)):
        raise ExtractionAgentError("Entity ids must be unique")

    relations = result["relations"]
    if not isinstance(relations, list):
        raise ExtractionAgentError("extraction result.relations must be a list")
    for index, relation in enumerate(relations):
        _validate_relation(relation, index)
        if relation["subject"] not in set(entity_ids) or relation["object"] not in set(entity_ids):
            raise ExtractionAgentError(f"relations[{index}] contains a dangling entity reference")

    return result


def validate_extraction_result(parsed: Any, schema: OntologySchema) -> dict[str, Any]:
    """Public validation entry point for safely resuming persisted extraction JSON."""
    return _validate_extraction_result(parsed, schema)


def prune_resolution_metadata(parsed: dict[str, Any], question: str | None) -> dict[str, Any]:
    """Remove demonym lookup metadata unless it is explicitly the requested answer."""
    asks_for_demonym = bool(question and re.search(r"\bdemonym\b", question, re.I))
    if not asks_for_demonym:
        for entity in parsed["entities"]:
            if "hasDemonym" in entity["attributes"]:
                entity["attributes"]["hasDemonym"] = None
    return parsed


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
    text: str,
    settings: LLMSettings,
) -> Any:
    return client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": text},
        ],
        **completion_parameters(settings, response_format),
    )


def extraction_agent(
    text: str,
    schema: OntologySchema,
    *,
    question: str | None = None,
    client: "openai.OpenAI | None" = None,
) -> dict[str, Any]:
    """Extract entities and relations from `text` for the domain described by `schema`.

    Works for any ontology, not just the family ontology: the set of valid entity types,
    the attributes available per type, and the system prompt are all built from `schema`
    (see schema_loader.py) rather than hardcoded. Relations are always returned as
    free-text relation_phrase triples; mapping those phrases onto the ontology's actual
    object properties is the ontology_mapping_agent's job, not this one's.
    """
    try:
        if not text.strip():
            raise ExtractionAgentError("Input text is empty")
    except ExtractionAgentError:
        logger.exception("extraction_agent_failed")
        raise

    try:
        settings = load_llm_settings()
    except ValueError as exc:
        raise ExtractionAgentError(str(exc)) from exc
    model = settings.model
    api_client = client or create_client(settings)

    try:
        response_format = build_extraction_response_format(schema)
        system_prompt = build_extraction_system_prompt(schema)
        if settings.provider == "deepseek":
            system_prompt += (
                "\nYour JSON response must satisfy this exact JSON Schema. Include every required "
                "field, including every attribute key with null when no value is stated:\n"
                + json.dumps(response_format["json_schema"]["schema"], ensure_ascii=False)
            )

        logger.info(
            "extraction_agent_calling_openai",
            text_length=len(text),
            model=model,
            provider=settings.provider,
            thinking=settings.thinking if settings.provider == "deepseek" else "not_applicable",
            ontology_namespace=schema.namespace,
            class_count=len(schema.classes),
        )
        user_payload = json.dumps(
            {"question": question.strip() if question else None, "context": text},
            ensure_ascii=False,
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
            raise ExtractionAgentError("Model returned no choices")
        choice = choices[0]
        finish_reason = getattr(choice, "finish_reason", None)
        if finish_reason not in (None, "stop"):
            raise ExtractionAgentError(f"Model response did not finish normally: {finish_reason}")
        message = getattr(choice, "message", None)
        if message is None or getattr(message, "refusal", None):
            raise ExtractionAgentError("Model refused the extraction request")
        content = getattr(message, "content", None)
        if not isinstance(content, str):
            raise ExtractionAgentError("Model returned non-string content")
        try:
            parsed = json.loads(content)
        except json.JSONDecodeError as exc:
            raise ExtractionAgentError(f"Model returned malformed JSON: {content!r}") from exc
        parsed = _validate_extraction_result(parsed, schema)

        # Demonyms help resolve nationality adjectives to Country entities, but keeping
        # that lookup metadata adds facts outside the minimal answer chain. Enforce the
        # prompt deterministically because model compliance here is not reliable.
        parsed = prune_resolution_metadata(parsed, question)

        logger.info(
            "extraction_agent_succeeded",
            entity_count=len(parsed.get("entities", [])),
            relation_count=len(parsed.get("relations", [])),
            elapsed_seconds=round(elapsed_seconds, 3),
            request_id=getattr(response, "_request_id", None),
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
