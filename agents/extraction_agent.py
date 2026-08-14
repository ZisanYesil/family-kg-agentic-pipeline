from __future__ import annotations

import json
import re
from datetime import date
from collections.abc import Mapping
from typing import Any

import openai
import structlog
from openai import APIConnectionError, APITimeoutError, RateLimitError
from tenacity import retry, retry_if_exception_type, stop_after_attempt, wait_exponential

from core.deepseek import JSON_RESPONSE_FORMAT, completion_options, create_client, get_model
from ontology.schema_loader import OntologySchema

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
    "year": "string",
    "date_or_year": "string",
}

_GYEAR_PATTERN = re.compile(r"^-?\d{4,}(?:Z|[+-]\d{2}:\d{2})?$")


def _is_date(value: Any) -> bool:
    if not isinstance(value, str):
        return False
    try:
        date.fromisoformat(value)
    except ValueError:
        return False
    return True


def _is_year(value: Any) -> bool:
    return isinstance(value, str) and _GYEAR_PATTERN.fullmatch(value) is not None

# Python-level type checks used when validating attribute values coming back from the
# model, keyed by the same range_type names as above.
_RANGE_TYPE_VALIDATORS = {
    "integer": lambda v: isinstance(v, int) and not isinstance(v, bool),
    "boolean": lambda v: isinstance(v, bool),
    "decimal": lambda v: isinstance(v, (int, float)) and not isinstance(v, bool),
    "string": lambda v: isinstance(v, str),
    "date": lambda v: isinstance(v, str),
    "year": _is_year,
    "date_or_year": lambda v: _is_date(v) or _is_year(v),
}


class ExtractionAgentError(Exception):
    """Raised when extraction cannot produce a usable structured result."""


def _attribute_json_type(range_type: str) -> str:
    return _RANGE_TYPE_TO_JSON_TYPE.get(range_type, "string")


def build_extraction_system_prompt(schema: OntologySchema) -> str:
    """Build a system prompt describing exactly the classes and attributes declared in
    `schema`, so the agent extracts entities/relations for whatever domain ontology it is
    given (family, vehicles, organizations, ...) rather than a hardcoded domain.
    """
    class_lines = [
        f"- {cls.local_name}: {cls.comment}" if cls.comment else f"- {cls.local_name}"
        for cls in schema.classes
    ]

    attrs_by_class: dict[str, list] = {}
    global_attrs: list = []
    for prop in schema.datatype_properties:
        if prop.domain_class is None:
            global_attrs.append(prop)
        else:
            attrs_by_class.setdefault(prop.domain_class, []).append(prop)

    attribute_lines = []
    for cls in schema.classes:
        props = attrs_by_class.get(cls.local_name, [])
        if not props:
            continue
        described = ", ".join(
            f"{p.local_name} ({p.range_type})" + (f": {p.comment}" if p.comment else "")
            for p in props
        )
        attribute_lines.append(f"- {cls.local_name}: {described}")
    if global_attrs:
        described = ", ".join(f"{p.local_name} ({p.range_type})" for p in global_attrs)
        attribute_lines.append(f"- (any entity type): {described}")

    class_block = "\n".join(class_lines) or "(no classes declared)"
    attribute_block = "\n".join(attribute_lines) or "(no attributes declared)"

    return f"""You extract structured knowledge from narrative text according to a specific
domain ontology. Only the ontology described below is relevant: ignore any entities or
facts in the text that do not belong to one of the listed types, even if the text also
discusses other, unrelated subjects.

Ontology classes (use exactly one of these as each entity's "type"):
{class_block}

Attributes available per class (fill in only what is explicitly stated in the text; use
null for anything not stated; never invent values; an attribute that belongs to a
different class than the entity's own type should also be left null):
{attribute_block}

For each entity found in the text that belongs to one of the classes above, assign a
stable lowercase underscore id that stays consistent every time the same entity is
referenced again (for example, include a distinguishing detail such as a year, number, or
short qualifier when the label alone would be ambiguous). Record any alternative names or
labels for the entity as aliases.

Identify every stated or clearly implied relationship between two extracted entities as a
relation triple: subject, object, and a short free-text relation_phrase written in your own
words describing how subject relates to object (for example: "father of", "married to",
"owner of", "manufactured by", "employed by"). Do NOT normalize the phrase to any fixed
vocabulary or predicate name, and do NOT restrict yourself to a predefined list of relation
types; describe the relationship as it is expressed or implied in the text, however unusual
it is, as long as both endpoints are entities of one of the ontology classes above. Prefer
the most specific direct relation stated in the text over an inferred indirect one.

Always include a qualifiers object for every relation. If the relation carries an
additional fact directly tied to it (such as a year it started, ended, or occurred, or a
short qualifying note), record it in qualifiers.year and/or qualifiers.note. Use null for
qualifier values that are not stated.

Never invent facts that are not stated or clearly implied. If no entities or relations
belonging to this ontology can be found anywhere in the text, return empty arrays for both
entities and relations.
"""


def build_extraction_json_schema(schema: OntologySchema) -> dict[str, Any]:
    """Build the JSON schema included in the prompt for DeepSeek JSON mode.

    The schema describes `schema`'s classes and datatype
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
    }


def build_extraction_response_format(schema: OntologySchema) -> dict[str, str]:
    """Return DeepSeek's supported JSON response mode."""
    # Keep the early ontology validation previously performed while building the
    # Structured Outputs wrapper.
    build_extraction_json_schema(schema)
    return JSON_RESPONSE_FORMAT.copy()


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


def _validate_attributes(value: Any, item_name: str, schema: OntologySchema) -> None:
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

    _validate_attributes(entity_obj["attributes"], f"{item_name}.attributes", schema)


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
def _create_completion(
    client: "openai.OpenAI",
    model: str,
    system_prompt: str,
    text: str,
) -> Any:
    return client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": text},
        ],
        **completion_options(),
    )


def extraction_agent(
    text: str,
    schema: OntologySchema,
    *,
    client: "openai.OpenAI | None" = None,
) -> dict[str, Any]:
    """Extract entities and relations from `text` for the domain described by `schema`.

    Works for any ontology, not just the family ontology: the set of valid entity types,
    the attributes available per type, and the system prompt are all built from `schema`
    (see ontology/schema_loader.py) rather than hardcoded. Relations are always returned as
    free-text relation_phrase triples; mapping those phrases onto the ontology's actual
    object properties is the ontology_mapping_agent's job, not this one's.
    """
    try:
        if not text.strip():
            raise ExtractionAgentError("Input text is empty")
    except ExtractionAgentError:
        logger.exception("extraction_agent_failed")
        raise

    model = get_model()
    api_client = client or create_client()

    try:
        build_extraction_response_format(schema)
        output_schema = json.dumps(build_extraction_json_schema(schema), ensure_ascii=False)
        system_prompt = (
            build_extraction_system_prompt(schema)
            + "\nReturn only one valid JSON object matching this JSON Schema exactly:\n"
            + output_schema
        )

        logger.info(
            "extraction_agent_calling_deepseek",
            text_length=len(text),
            model=model,
            ontology_namespace=schema.namespace,
            class_count=len(schema.classes),
        )
        response = _create_completion(api_client, model, system_prompt, text)
        content = response.choices[0].message.content
        if not isinstance(content, str):
            raise ExtractionAgentError("Model returned non-string content")
        try:
            parsed = json.loads(content)
        except json.JSONDecodeError as exc:
            raise ExtractionAgentError(f"Model returned malformed JSON: {content!r}") from exc
        parsed = _validate_extraction_result(parsed, schema)

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
        raise ExtractionAgentError(f"DeepSeek API error after retries exhausted: {exc}") from exc
    except openai.OpenAIError as exc:
        logger.exception("extraction_agent_failed", error=str(exc))
        raise ExtractionAgentError(f"DeepSeek API error: {exc}") from exc
    except Exception as exc:
        logger.exception("extraction_agent_failed", error=str(exc))
        raise
