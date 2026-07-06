import json
import os
import sqlite3
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Optional

import structlog

logger = structlog.get_logger(__name__)

DEFAULT_DATABASE_URL = "sqlite:///storage/jobs.db"


def get_database_path() -> str:
    database_url = os.getenv("DATABASE_URL", DEFAULT_DATABASE_URL)
    if not database_url.startswith("sqlite:///"):
        raise ValueError("DATABASE_URL must start with sqlite:///")
    return database_url.removeprefix("sqlite:///")


def _utc_timestamp() -> str:
    return datetime.now(timezone.utc).isoformat()


def _connect(db_path: Optional[str] = None) -> sqlite3.Connection:
    path = db_path or get_database_path()
    Path(path).parent.mkdir(parents=True, exist_ok=True)

    conn = sqlite3.connect(path, timeout=30)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def _row_to_dict(row: sqlite3.Row) -> dict[str, Any]:
    result = dict(row)
    result["passed_validation"] = bool(result["passed_validation"])
    result["webhook_delivered"] = bool(result["webhook_delivered"])
    return result


def init_db(db_path: str) -> None:
    try:
        with _connect(db_path) as conn:
            conn.execute(
                """
                CREATE TABLE IF NOT EXISTS jobs (
                    job_id TEXT PRIMARY KEY,
                    status TEXT NOT NULL,
                    input_text TEXT NOT NULL,
                    current_iteration INTEGER NOT NULL DEFAULT 0,
                    max_iterations INTEGER NOT NULL,
                    last_error TEXT,
                    graph_turtle TEXT,
                    passed_validation BOOLEAN NOT NULL DEFAULT FALSE,
                    webhook_url TEXT,
                    webhook_delivered BOOLEAN NOT NULL DEFAULT FALSE,
                    created_at TIMESTAMP NOT NULL,
                    updated_at TIMESTAMP NOT NULL
                )
                """
            )
            conn.execute(
                """
                CREATE TABLE IF NOT EXISTS iterations (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    job_id TEXT NOT NULL,
                    iteration_number INTEGER NOT NULL,
                    violations_json TEXT NOT NULL,
                    llm_reasoning TEXT NOT NULL,
                    triples_before INTEGER NOT NULL,
                    triples_after INTEGER NOT NULL,
                    timestamp TIMESTAMP NOT NULL,
                    FOREIGN KEY (job_id) REFERENCES jobs(job_id)
                )
                """
            )
            conn.commit()
        logger.info("sqlite_database_initialized", db_path=db_path)
    except sqlite3.Error:
        logger.exception("sqlite_database_init_failed", db_path=db_path)
        raise


def create_job(
    job_id: str,
    input_text: str,
    max_iterations: int,
    webhook_url: Optional[str],
) -> None:
    now = _utc_timestamp()
    try:
        with _connect() as conn:
            conn.execute(
                """
                INSERT INTO jobs (
                    job_id, status, input_text, current_iteration, max_iterations,
                    last_error, graph_turtle, passed_validation, webhook_url,
                    webhook_delivered, created_at, updated_at
                )
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    job_id,
                    "Pending",
                    input_text,
                    0,
                    max_iterations,
                    None,
                    None,
                    False,
                    webhook_url,
                    False,
                    now,
                    now,
                ),
            )
            conn.commit()
        logger.info("job_created", job_id=job_id)
    except sqlite3.Error:
        logger.exception("job_create_failed", job_id=job_id)
        raise


def get_job(job_id: str) -> Optional[dict[str, Any]]:
    try:
        with _connect() as conn:
            row = conn.execute(
                "SELECT * FROM jobs WHERE job_id = ?",
                (job_id,),
            ).fetchone()
        return _row_to_dict(row) if row else None
    except sqlite3.Error:
        logger.exception("job_get_failed", job_id=job_id)
        raise


def update_job_status(
    job_id: str,
    status: Any,
    last_error: Optional[str] = None,
) -> None:
    now = _utc_timestamp()
    status_value = getattr(status, "value", status)
    try:
        with _connect() as conn:
            conn.execute(
                """
                UPDATE jobs
                SET status = ?, last_error = ?, updated_at = ?
                WHERE job_id = ?
                """,
                (status_value, last_error, now, job_id),
            )
            conn.commit()
        logger.info("job_status_updated", job_id=job_id, status=status_value)
    except sqlite3.Error:
        logger.exception("job_status_update_failed", job_id=job_id)
        raise


def update_job_iteration(job_id: str, current_iteration: int) -> None:
    now = _utc_timestamp()
    try:
        with _connect() as conn:
            conn.execute(
                """
                UPDATE jobs
                SET current_iteration = ?, updated_at = ?
                WHERE job_id = ?
                """,
                (current_iteration, now, job_id),
            )
            conn.commit()
        logger.info(
            "job_iteration_updated",
            job_id=job_id,
            current_iteration=current_iteration,
        )
    except sqlite3.Error:
        logger.exception("job_iteration_update_failed", job_id=job_id)
        raise


def save_final_graph(
    job_id: str,
    graph_turtle: str,
    passed_validation: bool,
) -> None:
    now = _utc_timestamp()
    try:
        with _connect() as conn:
            conn.execute(
                """
                UPDATE jobs
                SET graph_turtle = ?, passed_validation = ?, updated_at = ?
                WHERE job_id = ?
                """,
                (graph_turtle, passed_validation, now, job_id),
            )
            conn.commit()
        logger.info(
            "final_graph_saved",
            job_id=job_id,
            passed_validation=passed_validation,
        )
    except sqlite3.Error:
        logger.exception("final_graph_save_failed", job_id=job_id)
        raise


def add_iteration_detail(
    job_id: str,
    iteration_number: int,
    violations: list[str],
    llm_reasoning: str,
    triples_before: int,
    triples_after: int,
) -> None:
    timestamp = _utc_timestamp()
    violations_json = json.dumps(violations)
    try:
        with _connect() as conn:
            conn.execute(
                """
                INSERT INTO iterations (
                    job_id, iteration_number, violations_json, llm_reasoning,
                    triples_before, triples_after, timestamp
                )
                VALUES (?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    job_id,
                    iteration_number,
                    violations_json,
                    llm_reasoning,
                    triples_before,
                    triples_after,
                    timestamp,
                ),
            )
            conn.execute(
                """
                UPDATE jobs
                SET updated_at = ?
                WHERE job_id = ?
                """,
                (timestamp, job_id),
            )
            conn.commit()
        logger.info(
            "iteration_detail_added",
            job_id=job_id,
            iteration_number=iteration_number,
        )
    except sqlite3.Error:
        logger.exception("iteration_detail_add_failed", job_id=job_id)
        raise


def get_iterations(job_id: str) -> list[dict[str, Any]]:
    try:
        with _connect() as conn:
            rows = conn.execute(
                """
                SELECT iteration_number, violations_json, llm_reasoning,
                       triples_before, triples_after, timestamp
                FROM iterations
                WHERE job_id = ?
                ORDER BY iteration_number ASC
                """,
                (job_id,),
            ).fetchall()

        iterations = []
        for row in rows:
            item = dict(row)
            item["violations"] = json.loads(item.pop("violations_json"))
            iterations.append(item)
        return iterations
    except sqlite3.Error:
        logger.exception("iterations_get_failed", job_id=job_id)
        raise


def set_webhook_delivered(job_id: str) -> None:
    now = _utc_timestamp()
    try:
        with _connect() as conn:
            conn.execute(
                """
                UPDATE jobs
                SET webhook_delivered = TRUE, updated_at = ?
                WHERE job_id = ?
                """,
                (now, job_id),
            )
            conn.commit()
        logger.info("webhook_marked_delivered", job_id=job_id)
    except sqlite3.Error:
        logger.exception("webhook_mark_delivered_failed", job_id=job_id)
        raise
