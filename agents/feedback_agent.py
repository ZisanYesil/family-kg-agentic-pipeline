from __future__ import annotations

import json
from typing import Any

import openai
import structlog
from openai import APIConnectionError, APITimeoutError, RateLimitError
from rdflib import Graph
from tenacity import retry, retry_if_exception_type, stop_after_attempt, wait_exponential

from core.llm_config import (
    LLMSettings,
    completion_parameters,
    create_client,
    load_llm_settings,
)
from feedback.models import FeedbackPlan
from ontology.schema_loader import OntologySchema
from utils.rdf import serialize_turtle_graph
from validation.models import ValidationViolation

logger = structlog.get_logger(__name__)


class FeedbackAgentError(Exception):
    """Raised when the feedback model cannot produce a valid repair plan."""


def _schema_reference(schema: OntologySchema) -> dict[str, Any]:
    return {
        "namespace": schema.namespace,
        "classes": [{"name": item.local_name, "iri": item.uri} for item in schema.classes],
        "datatype_properties": [
            {
                "name": item.local_name,
                "iri": item.uri,
                "domain": item.domain_class,
                "range": item.range_type,
            }
            for item in schema.datatype_properties
        ],
        "object_properties": [
            {
                "name": item.local_name,
                "iri": item.uri,
                "domain": item.domain_class,
                "range": item.range_class,
            }
            for item in schema.object_properties
        ],
    }


def build_feedback_system_prompt() -> str:
    return """You repair an RDF knowledge graph using a strictly limited edit plan.
Every repair must target exactly one supplied validation fingerprint. Return one repair
entry for every violation, even when it cannot be repaired safely; use an empty operations
array for an unresolved violation and explain why.

Only use facts grounded in the supplied source text, current graph, validation finding,
and ontology reference. Never invent people, resources, relationships, or literal values.
Use absolute IRIs exactly as supplied. Only edit the predicate named by the finding, a
listed expected candidate predicate, or rdf:type/rdfs:label when the finding permits it.
For an unmapped_relation finding, choose any declared ontology predicate only when its
documented meaning matches the relation phrase and source text. Domain/range compatibility
alone is never semantic evidence. If the meaning is absent from the ontology, return no
operations. If a correct predicate is blocked only by an overly broad rdf:type and the
source clearly supports a declared subtype, repair the type as part of the same finding.
Prefer the smallest possible change. A remove operation must exactly match an existing
triple. A replacement must exactly match the existing old literal. Literal lexical values
must occur in the source text. Do not attempt broad cleanup or unrelated improvements.

RDF term and operation rules:
- rdf:type always has an IRI object. Never represent a class IRI as a literal.
- Object properties always have IRI objects.
- Datatype properties have literal objects, with datatype/language matching the graph and
  ontology.
- replace_literal is only for a datatype-property value whose RDF object is a literal.
- To change an IRI object (including an rdf:type class), emit remove_triple for the exact
  old IRI triple followed by add_triple for the new IRI triple. Both objects use kind=iri.
- Use add_triple alone when the required triple is absent and no conflicting triple needs
  removal. Use remove_triple alone only when the finding is fixed by deletion.
"""


def build_feedback_payload(
    graph: Graph,
    violations: tuple[ValidationViolation, ...],
    schema: OntologySchema,
    source_text: str,
) -> str:
    return json.dumps(
        {
            "source_text": source_text,
            "graph_turtle": serialize_turtle_graph(graph),
            "ontology": _schema_reference(schema),
            "violations": [
                {"fingerprint": item.fingerprint, **item.as_dict()}
                for item in violations
            ],
        },
        ensure_ascii=False,
        sort_keys=True,
    )
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
    payload: str,
    response_format: dict[str, Any],
    settings: LLMSettings,
) -> Any:
    return client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": payload},
        ],
        **completion_parameters(settings, response_format),
    )


def feedback_agent(
    graph: Graph,
    violations: tuple[ValidationViolation, ...],
    schema: OntologySchema,
    source_text: str,
    *,
    client: "openai.OpenAI | None" = None,
) -> FeedbackPlan:
    """Generate a source-grounded, structured RDF edit plan for every violation."""
    if not isinstance(graph, Graph):
        raise TypeError("graph must be an rdflib.Graph")
    if not violations:
        raise FeedbackAgentError("violations must not be empty")
    if not source_text.strip():
        raise FeedbackAgentError("source_text must not be empty")

    try:
        settings = load_llm_settings()
    except ValueError as exc:
        raise FeedbackAgentError(str(exc)) from exc

    model = settings.model
    api_client = client or create_client(settings)
    response_format = {
        "type": "json_schema",
        "json_schema": {
            "name": "feedback_plan",
            "strict": True,
            "schema": FeedbackPlan.model_json_schema(),
        },
    }

    system_prompt = build_feedback_system_prompt()
    if settings.provider == "deepseek":
        system_prompt += (
            "\nReturn only one valid JSON object matching this JSON Schema exactly:\n"
            + json.dumps(FeedbackPlan.model_json_schema(), ensure_ascii=False)
        )

    try:
        response = _create_completion(
            api_client,
            model,
            system_prompt,
            build_feedback_payload(graph, violations, schema, source_text),
            response_format,
            settings,
        )
        content = response.choices[0].message.content
        if not isinstance(content, str):
            raise FeedbackAgentError("Model returned non-string content")

        try:
            plan = FeedbackPlan.model_validate_json(content)
        except Exception as exc:
            raise FeedbackAgentError(
                f"Model returned an invalid feedback plan: {exc}"
            ) from exc

        logger.info(
            "feedback_agent_succeeded",
            model=model,
            violation_count=len(violations),
            repair_count=len(plan.repairs),
            operation_count=sum(len(repair.operations) for repair in plan.repairs),
        )
        return plan
    except FeedbackAgentError:
        logger.exception("feedback_agent_failed")
        raise
    except (APIConnectionError, APITimeoutError, RateLimitError) as exc:
        logger.exception("feedback_agent_failed", error=str(exc))
        raise FeedbackAgentError(
            f"OpenAI-compatible API error after retries exhausted: {exc}"
        ) from exc
    except openai.OpenAIError as exc:
        logger.exception("feedback_agent_failed", error=str(exc))
        raise FeedbackAgentError(f"OpenAI-compatible API error: {exc}") from exc
    except Exception as exc:
        logger.exception("feedback_agent_failed", error=str(exc))
        raise FeedbackAgentError(f"Feedback agent failed: {exc}") from exc
