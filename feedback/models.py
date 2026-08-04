from __future__ import annotations

import json
import re
from typing import Annotated, Any, Literal, Optional, Union

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    StringConstraints,
    field_validator,
    model_validator,
)


MAX_IRI_LENGTH = 2048
MAX_LITERAL_LENGTH = 10_000
MAX_REASONING_LENGTH = 4_000
MAX_REPAIRS = 100
MAX_OPERATIONS_PER_REPAIR = 20
MAX_TOTAL_OPERATIONS = 200

_ABSOLUTE_IRI_PATTERN = re.compile(r"^[A-Za-z][A-Za-z0-9+.-]*:")
_FORBIDDEN_IRI_CHARACTERS = re.compile(r'[\s<>"{}|\\^`]')
_LANGUAGE_TAG_PATTERN = re.compile(
    r"^[A-Za-z]{1,8}(?:-[A-Za-z0-9]{1,8})*$"
)

Iri = Annotated[str, StringConstraints(min_length=1, max_length=MAX_IRI_LENGTH)]
Reasoning = Annotated[
    str,
    StringConstraints(min_length=1, max_length=MAX_REASONING_LENGTH),
]
ViolationFingerprint = Annotated[
    str,
    StringConstraints(pattern=r"^[0-9a-f]{64}$"),
]


class StrictFeedbackModel(BaseModel):
    model_config = ConfigDict(extra="forbid", strict=True)


def _validate_absolute_iri(value: str) -> str:
    if not _ABSOLUTE_IRI_PATTERN.match(value):
        raise ValueError("must be an absolute IRI with a URI scheme")
    _scheme, _separator, remainder = value.partition(":")
    if not remainder:
        raise ValueError("absolute IRI must contain a scheme-specific value")
    if _FORBIDDEN_IRI_CHARACTERS.search(value):
        raise ValueError("contains characters that are not allowed in an IRI")
    return value


class IriObject(StrictFeedbackModel):
    kind: Literal["iri"]
    value: Iri

    _validate_value = field_validator("value")(_validate_absolute_iri)


class LiteralObject(StrictFeedbackModel):
    kind: Literal["literal"]
    value: Annotated[
        str,
        StringConstraints(max_length=MAX_LITERAL_LENGTH),
    ]
    datatype: Optional[Iri]
    language: Optional[
        Annotated[
            str,
            StringConstraints(min_length=1, max_length=63),
        ]
    ]

    _validate_datatype = field_validator("datatype")(
        lambda value: _validate_absolute_iri(value) if value is not None else value
    )

    @field_validator("language")
    @classmethod
    def validate_language(cls, value: str | None) -> str | None:
        if value is not None and not _LANGUAGE_TAG_PATTERN.fullmatch(value):
            raise ValueError("must be a valid BCP 47-style language tag")
        return value

    @model_validator(mode="after")
    def validate_literal_metadata(self) -> "LiteralObject":
        if self.datatype is not None and self.language is not None:
            raise ValueError("literal cannot have both datatype and language")
        return self


RdfObject = Annotated[
    Union[IriObject, LiteralObject],
    Field(discriminator="kind"),
]


class AddTriple(StrictFeedbackModel):
    operation: Literal["add_triple"]
    subject: Iri
    predicate: Iri
    object: RdfObject

    _validate_subject = field_validator("subject")(_validate_absolute_iri)
    _validate_predicate = field_validator("predicate")(_validate_absolute_iri)


class RemoveTriple(StrictFeedbackModel):
    operation: Literal["remove_triple"]
    subject: Iri
    predicate: Iri
    object: RdfObject

    _validate_subject = field_validator("subject")(_validate_absolute_iri)
    _validate_predicate = field_validator("predicate")(_validate_absolute_iri)


class ReplaceLiteral(StrictFeedbackModel):
    operation: Literal["replace_literal"]
    subject: Iri
    predicate: Iri
    old_literal: LiteralObject
    new_literal: LiteralObject

    _validate_subject = field_validator("subject")(_validate_absolute_iri)
    _validate_predicate = field_validator("predicate")(_validate_absolute_iri)

    @model_validator(mode="after")
    def reject_noop_replacement(self) -> "ReplaceLiteral":
        if self.old_literal == self.new_literal:
            raise ValueError("replace_literal must change the literal")
        return self


EditOperation = Annotated[
    Union[AddTriple, RemoveTriple, ReplaceLiteral],
    Field(discriminator="operation"),
]


class ViolationRepair(StrictFeedbackModel):
    violation_fingerprint: ViolationFingerprint
    reasoning: Reasoning
    operations: Annotated[
        list[EditOperation],
        Field(max_length=MAX_OPERATIONS_PER_REPAIR),
    ]

    @model_validator(mode="after")
    def reject_duplicate_operations(self) -> "ViolationRepair":
        serialized = [
            json.dumps(
                operation.model_dump(mode="json"),
                ensure_ascii=False,
                sort_keys=True,
                separators=(",", ":"),
            )
            for operation in self.operations
        ]
        if len(serialized) != len(set(serialized)):
            raise ValueError("repair contains duplicate edit operations")
        return self


class FeedbackPlan(StrictFeedbackModel):
    reasoning: Reasoning
    repairs: Annotated[list[ViolationRepair], Field(max_length=MAX_REPAIRS)]

    @model_validator(mode="after")
    def validate_plan_uniqueness_and_size(self) -> "FeedbackPlan":
        fingerprints = [
            repair.violation_fingerprint for repair in self.repairs
        ]
        if len(fingerprints) != len(set(fingerprints)):
            raise ValueError("feedback plan contains duplicate violation fingerprints")

        total_operations = sum(len(repair.operations) for repair in self.repairs)
        if total_operations > MAX_TOTAL_OPERATIONS:
            raise ValueError(
                f"feedback plan exceeds {MAX_TOTAL_OPERATIONS} total operations"
            )

        serialized_operations = [
            json.dumps(
                operation.model_dump(mode="json"),
                ensure_ascii=False,
                sort_keys=True,
                separators=(",", ":"),
            )
            for repair in self.repairs
            for operation in repair.operations
        ]
        if len(serialized_operations) != len(set(serialized_operations)):
            raise ValueError(
                "feedback plan contains duplicate edit operations across repairs"
            )
        return self


def build_feedback_response_format() -> dict[str, Any]:
    """Return the strict Structured Outputs wrapper used by the feedback LLM call."""
    schema = _to_openai_structured_outputs_schema(
        FeedbackPlan.model_json_schema()
    )
    return {
        "type": "json_schema",
        "json_schema": {
            "name": "knowledge_graph_feedback_plan",
            "strict": True,
            "schema": schema,
        },
    }


def _to_openai_structured_outputs_schema(node: Any) -> Any:
    """Translate Pydantic JSON Schema to OpenAI's supported strict subset.

    Pydantic discriminated unions emit ``oneOf`` plus the annotation-only
    ``discriminator`` keyword. Structured Outputs supports nested ``anyOf`` instead.
    Literal values are emitted as ``const`` by Pydantic and are represented as
    single-value enums in the API schema.
    """
    if isinstance(node, list):
        return [
            _to_openai_structured_outputs_schema(item)
            for item in node
        ]
    if not isinstance(node, dict):
        return node

    transformed: dict[str, Any] = {}
    for key, value in node.items():
        if key in {"discriminator", "title"}:
            continue
        if key == "oneOf":
            transformed["anyOf"] = _to_openai_structured_outputs_schema(value)
            continue
        if key == "const":
            transformed["enum"] = [
                _to_openai_structured_outputs_schema(value)
            ]
            continue
        transformed[key] = _to_openai_structured_outputs_schema(value)
    return transformed
