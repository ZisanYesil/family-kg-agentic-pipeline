#!/usr/bin/env python3
"""Direct LLM baseline using exactly question + unstructured context."""

from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
import json
import time
from pathlib import Path

import openai
from dotenv import load_dotenv
from tenacity import retry, retry_if_exception_type, stop_after_attempt, wait_exponential

from core.llm_config import completion_parameters, create_client, load_llm_settings
from phase2_qa.common import aggregate, atomic_json, example_fields, parse_ids, score_answer


ROOT = Path(__file__).resolve().parents[1]
PROMPT_VERSION = "direct_text_qa_v1"
SYSTEM_PROMPT = """Answer the question using only the supplied context. Return the shortest
answer that directly answers the question: normally one entity, date, number, or yes/no.
Do not explain your reasoning and do not add information that is not in the context.
Return JSON only with exactly one string field named answer."""
RESPONSE_FORMAT = {
    "type": "json_schema",
    "json_schema": {
        "name": "direct_qa_answer",
        "strict": True,
        "schema": {
            "type": "object",
            "additionalProperties": False,
            "required": ["answer"],
            "properties": {"answer": {"type": "string"}},
        },
    },
}


@retry(
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=0.2, min=0.2, max=2),
    retry=retry_if_exception_type((openai.APIConnectionError, openai.APITimeoutError, openai.RateLimitError)),
    reraise=True,
)
def completion(client, settings, payload):
    return client.chat.completions.create(
        model=settings.model,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": json.dumps(payload, ensure_ascii=False)},
        ],
        **completion_parameters(settings, RESPONSE_FORMAT),
    )


def run_one(client, settings, dataset: Path, example_id: int) -> dict:
    fields = example_fields(dataset, example_id)
    started = time.monotonic()
    response = completion(client, settings, {
        "question": fields["question"],
        "context": fields["text"],
    })
    elapsed = time.monotonic() - started
    message = response.choices[0].message
    content = message.content
    if content is None:
        return {
            "id": example_id,
            "status": "completed",
            "execution_status": "no_content",
            "method": "direct_llm_question_plus_text",
            "prompt_version": PROMPT_VERSION,
            "question": fields["question"],
            "gold_answer": fields["answer"],
            "predicted_answer": "",
            **score_answer("", fields["answer"]),
            "response_refusal": getattr(message, "refusal", None),
            "elapsed_seconds": elapsed,
            "usage": None,
        }
    parsed = json.loads(content)
    if not isinstance(parsed, dict) or set(parsed) != {"answer"} or not isinstance(parsed["answer"], str):
        raise ValueError("Direct QA response does not match the answer-only contract")
    usage = getattr(response, "usage", None)
    return {
        "id": example_id,
        "status": "completed",
        "method": "direct_llm_question_plus_text",
        "prompt_version": PROMPT_VERSION,
        "question": fields["question"],
        "gold_answer": fields["answer"],
        "predicted_answer": parsed["answer"].strip(),
        **score_answer(parsed["answer"], fields["answer"]),
        "elapsed_seconds": elapsed,
        "usage": {
            key: getattr(usage, key, None)
            for key in ("prompt_tokens", "completion_tokens", "total_tokens")
        } if usage else None,
    }


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dataset", type=Path, required=True)
    parser.add_argument("--ids", type=parse_ids, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--overwrite", action="store_true")
    parser.add_argument("--workers", type=int, default=1)
    args = parser.parse_args(argv)
    load_dotenv(ROOT / ".env")
    settings = load_llm_settings()
    client = create_client(settings)
    existing = []
    if args.output.exists() and not args.overwrite:
        existing = json.loads(args.output.read_text(encoding="utf-8")).get("results", [])
    by_id = {row["id"]: row for row in existing}
    # Older runs parsed a valid no-content model response as JSON and recorded
    # it as an execution failure. Retain it as a completed, unanswered result.
    for example_id, row in list(by_id.items()):
        if row.get("status") == "failed" and row.get("error") == \
                "the JSON object must be str, bytes or bytearray, not NoneType":
            fields = example_fields(args.dataset.resolve(), example_id)
            by_id[example_id] = {
                "id": example_id,
                "status": "completed",
                "execution_status": "no_content",
                "method": "direct_llm_question_plus_text",
                "prompt_version": PROMPT_VERSION,
                "question": fields["question"],
                "gold_answer": fields["answer"],
                "predicted_answer": "",
                **score_answer("", fields["answer"]),
                "response_refusal": None,
                "elapsed_seconds": None,
                "usage": None,
            }
    pending = [
        example_id for example_id in args.ids
        if example_id not in by_id or by_id[example_id].get("status") != "completed"
    ]

    def evaluate(example_id):
        try:
            return run_one(client, settings, args.dataset.resolve(), example_id)
        except Exception as exc:
            return {"id": example_id, "status": "failed", "error": str(exc)}

    with ThreadPoolExecutor(max_workers=max(1, args.workers)) as executor:
        futures = {executor.submit(evaluate, example_id): example_id for example_id in pending}
        for future in as_completed(futures):
            example_id = futures[future]
            row = future.result()
            by_id[example_id] = row
            results = [by_id[key] for key in sorted(by_id)]
            atomic_json(args.output, {
                "experiment": "direct_llm_question_plus_text",
                "model": settings.model,
                "provider": settings.provider,
                "prompt_version": PROMPT_VERSION,
                "summary": aggregate(results),
                "results": results,
            })
            print(f"id={example_id} status={row['status']}", flush=True)
    results = [by_id[key] for key in sorted(by_id)]
    atomic_json(args.output, {
        "experiment": "direct_llm_question_plus_text",
        "model": settings.model,
        "provider": settings.provider,
        "prompt_version": PROMPT_VERSION,
        "summary": aggregate(results),
        "results": results,
    })
    return 1 if any(row.get("status") == "failed" for row in by_id.values()) else 0


if __name__ == "__main__":
    raise SystemExit(main())
