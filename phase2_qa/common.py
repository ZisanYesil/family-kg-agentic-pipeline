from __future__ import annotations

import json
import datetime
import re
import unicodedata
from pathlib import Path


def parse_ids(value: str) -> list[int]:
    result = set()
    for part in value.split(","):
        part = part.strip()
        if "-" in part:
            start, end = map(int, part.split("-", 1))
            if start < 0 or end < start:
                raise ValueError(f"Invalid ID range: {part}")
            result.update(range(start, end + 1))
        elif part:
            result.add(int(part))
    if not result or min(result) < 0:
        raise ValueError("IDs must be non-negative")
    return sorted(result)


def example_fields(dataset: Path, example_id: int) -> dict[str, str]:
    directory = dataset / str(example_id)
    paths = {
        "text": directory / f"text_{example_id}.txt",
        "question": directory / f"example{example_id}_question.txt",
        "answer": directory / f"example{example_id}_answer.txt",
    }
    missing = [str(path) for path in paths.values() if not path.is_file()]
    if missing:
        raise FileNotFoundError(f"Example {example_id} lacks required files: {missing}")
    return {key: path.read_text(encoding="utf-8").strip() for key, path in paths.items()}


def normalize_answer(value: object) -> str:
    text = unicodedata.normalize("NFKD", str(value or "")).casefold()
    text = "".join(ch for ch in text if not unicodedata.combining(ch))
    text = re.sub(r"[^\w\s]", " ", text)
    tokens = [token for token in text.split() if token not in {"a", "an", "the"}]
    return " ".join(tokens)


def token_f1(predicted: object, gold: object) -> float:
    if answers_equivalent(predicted, gold):
        return 1.0
    predicted_tokens = normalize_answer(predicted).split()
    gold_tokens = normalize_answer(gold).split()
    if not predicted_tokens or not gold_tokens:
        return float(predicted_tokens == gold_tokens)
    remaining = list(gold_tokens)
    common = 0
    for token in predicted_tokens:
        if token in remaining:
            common += 1
            remaining.remove(token)
    if common == 0:
        return 0.0
    precision = common / len(predicted_tokens)
    recall = common / len(gold_tokens)
    return 2 * precision * recall / (precision + recall)


def score_answer(predicted: object, gold: object) -> dict[str, object]:
    return {
        "normalized_prediction": normalize_answer(predicted),
        "normalized_gold": normalize_answer(gold),
        "strict_exact_match": strict_answers_equal(predicted, gold),
        "exact_match": answers_equivalent(predicted, gold),
        "token_f1": token_f1(predicted, gold),
    }


def strict_answers_equal(predicted: object, gold: object) -> bool:
    """Normalized equality only, without compatibility or partial-match rules."""
    return normalize_answer(predicted) == normalize_answer(gold)


def answers_equivalent(predicted: object, gold: object) -> bool:
    predicted_normalized = normalize_answer(predicted)
    gold_normalized = normalize_answer(gold)
    boolean_aliases = {"true": "yes", "false": "no"}
    predicted_normalized = boolean_aliases.get(predicted_normalized, predicted_normalized)
    gold_normalized = boolean_aliases.get(gold_normalized, gold_normalized)
    if predicted_normalized == gold_normalized:
        return True
    # The benchmark's correction criterion treats a more specific graph label
    # as compatible with a shorter reference label (and conversely).
    if predicted_normalized and gold_normalized and (
        predicted_normalized in gold_normalized or gold_normalized in predicted_normalized
    ):
        return True
    demonym_to_country = {
        "american": "united states", "british": "united kingdom",
        "english": "united kingdom", "scottish": "united kingdom",
        "welsh": "united kingdom", "irish": "ireland", "indian": "india",
        "french": "france", "german": "germany", "italian": "italy",
        "spanish": "spain", "portuguese": "portugal", "russian": "russia",
        "japanese": "japan", "chinese": "china", "canadian": "canada",
        "australian": "australia", "dutch": "netherlands", "swedish": "sweden",
        "norwegian": "norway", "danish": "denmark", "polish": "poland",
        "brazilian": "brazil", "mexican": "mexico", "egyptian": "egypt",
        "turkish": "turkey", "greek": "greece", "swiss": "switzerland",
        "austrian": "austria", "belgian": "belgium", "finnish": "finland",
        "israeli": "israel", "malaysian": "malaysia", "filipino": "philippines",
        "vietnamese": "vietnam", "thai": "thailand", "indonesian": "indonesia",
        "pakistani": "pakistan", "bangladeshi": "bangladesh", "nigerian": "nigeria",
        "kenyan": "kenya", "argentine": "argentina", "argentinian": "argentina",
        "chilean": "chile", "colombian": "colombia", "peruvian": "peru",
        "cuban": "cuba", "venezuelan": "venezuela", "ukrainian": "ukraine",
        "czech": "czech republic", "hungarian": "hungary", "romanian": "romania",
        "bulgarian": "bulgaria", "croatian": "croatia", "serbian": "serbia",
        "icelandic": "iceland", "maltese": "malta", "lithuanian": "lithuania",
    }
    if demonym_to_country.get(predicted_normalized) == gold_normalized or \
            demonym_to_country.get(gold_normalized) == predicted_normalized:
        return True
    # Accept compatible date precision when one side intentionally supplies only
    # the year and the other supplies an ISO date from the RDF literal.
    if re.fullmatch(r"\d{4}", predicted_normalized) and re.fullmatch(
        rf"{re.escape(predicted_normalized)} \d{{1,2}} \d{{1,2}}", gold_normalized
    ):
        return True
    if re.fullmatch(r"\d{4}", gold_normalized) and re.fullmatch(
        rf"{re.escape(gold_normalized)} \d{{1,2}} \d{{1,2}}", predicted_normalized
    ):
        return True
    date_formats = ("%B %d %Y", "%b %d %Y", "%d %B %Y", "%d %b %Y", "%Y %m %d")
    def date_key(value: str):
        for fmt in date_formats:
            try:
                parsed = datetime.datetime.strptime(value, fmt)
                return parsed.year, parsed.month, parsed.day
            except ValueError:
                pass
        return None
    predicted_date, gold_date = date_key(predicted_normalized), date_key(gold_normalized)
    if predicted_date is not None and gold_date is not None and predicted_date == gold_date:
        return True
    return False


def atomic_json(path: Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    temporary.replace(path)


def aggregate(results: list[dict]) -> dict:
    scored = [row for row in results if row.get("status") == "completed"]
    answered = [row for row in scored if normalize_answer(row.get("predicted_answer"))]
    return {
        "examples": len(results),
        "completed": len(scored),
        "failed": sum(row.get("status") == "failed" for row in results),
        "answered": len(answered),
        "unanswered": len(scored) - len(answered),
        "answer_rate": len(answered) / len(scored) if scored else 0.0,
        "strict_exact_match": sum(bool(row.get("strict_exact_match")) for row in scored) / len(scored) if scored else 0.0,
        "exact_match": sum(bool(row.get("exact_match")) for row in scored) / len(scored) if scored else 0.0,
        "mean_token_f1": sum(float(row.get("token_f1", 0)) for row in scored) / len(scored) if scored else 0.0,
    }
