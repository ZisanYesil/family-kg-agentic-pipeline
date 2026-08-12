from __future__ import annotations

import sqlite3

import pytest

from storage import database


def _create_legacy_database(path: str) -> None:
    with sqlite3.connect(path) as conn:
        conn.executescript(
            """
            CREATE TABLE jobs (
                job_id TEXT PRIMARY KEY, status TEXT NOT NULL, input_text TEXT NOT NULL,
                current_iteration INTEGER NOT NULL DEFAULT 0, max_iterations INTEGER NOT NULL,
                last_error TEXT, graph_turtle TEXT, passed_validation BOOLEAN NOT NULL DEFAULT FALSE,
                webhook_url TEXT, webhook_delivered BOOLEAN NOT NULL DEFAULT FALSE,
                created_at TIMESTAMP NOT NULL, updated_at TIMESTAMP NOT NULL
            );
            CREATE TABLE iterations (
                id INTEGER PRIMARY KEY AUTOINCREMENT, job_id TEXT NOT NULL,
                iteration_number INTEGER NOT NULL, violations_json TEXT NOT NULL,
                llm_reasoning TEXT NOT NULL, triples_before INTEGER NOT NULL,
                triples_after INTEGER NOT NULL, timestamp TIMESTAMP NOT NULL
            );
            INSERT INTO jobs VALUES (
                'old-job', 'Complete', 'legacy input', 1, 10, NULL, '', 1,
                NULL, 0, '2026-07-01', '2026-07-01'
            );
            INSERT INTO iterations (
                job_id, iteration_number, violations_json, llm_reasoning,
                triples_before, triples_after, timestamp
            ) VALUES ('old-job', 1, '[]', '', 1, 1, '2026-07-01');
            """
        )


def test_init_db_migrates_legacy_database_without_losing_history(tmp_path, monkeypatch) -> None:
    db_path = tmp_path / "legacy.db"
    _create_legacy_database(str(db_path))
    monkeypatch.setenv("DEFAULT_ONTOLOGY_PATH", "ontology/custom.ttl")

    database.init_db(str(db_path))

    with sqlite3.connect(db_path) as conn:
        job_columns = {row[1] for row in conn.execute("PRAGMA table_info(jobs)")}
        iteration_columns = {row[1] for row in conn.execute("PRAGMA table_info(iterations)")}
        old_job = conn.execute(
            "SELECT job_id, ontology_path FROM jobs WHERE job_id='old-job'"
        ).fetchone()
        version = conn.execute("SELECT max(version) FROM schema_migrations").fetchone()[0]
    assert "ontology_path" in job_columns
    assert {"edit_log_json", "unresolved_violations_json"} <= iteration_columns
    assert old_job == ("old-job", "ontology/custom.ttl")
    assert version == database.CURRENT_SCHEMA_VERSION


def test_iteration_round_trip_includes_repair_audit_data(tmp_path, monkeypatch) -> None:
    db_path = tmp_path / "jobs.db"
    monkeypatch.setenv("DATABASE_URL", f"sqlite:///{db_path}")
    database.init_db(str(db_path))
    database.create_job("job-1", "Jane is a person.", "ontology/test.ttl", 3, None)
    database.add_iteration_detail(
        "job-1",
        1,
        ["violation"],
        "Added a type.",
        1,
        2,
        edit_log=[{"operation": "add_triple"}],
        unresolved_violation_fingerprints=["a" * 64],
    )

    item = database.get_iterations("job-1")[0]
    assert item["edit_log"] == [{"operation": "add_triple"}]
    assert item["unresolved_violation_fingerprints"] == ["a" * 64]


def test_init_db_is_idempotent_and_backfills_partial_null_path(tmp_path, monkeypatch) -> None:
    db_path = tmp_path / "partial.db"
    _create_legacy_database(str(db_path))
    database.init_db(str(db_path))
    with sqlite3.connect(db_path) as conn:
        conn.execute("UPDATE jobs SET ontology_path=NULL WHERE job_id='old-job'")
    monkeypatch.setenv("DEFAULT_ONTOLOGY_PATH", "ontology/recovered.ttl")

    database.init_db(str(db_path))
    database.init_db(str(db_path))

    with sqlite3.connect(db_path) as conn:
        path = conn.execute(
            "SELECT ontology_path FROM jobs WHERE job_id='old-job'"
        ).fetchone()[0]
        versions = conn.execute("SELECT version FROM schema_migrations").fetchall()
    assert path == "ontology/recovered.ttl"
    assert versions == [(database.CURRENT_SCHEMA_VERSION,)]


def test_init_db_rejects_database_from_newer_application(tmp_path) -> None:
    db_path = tmp_path / "future.db"
    database.init_db(str(db_path))
    with sqlite3.connect(db_path) as conn:
        conn.execute(
            "INSERT INTO schema_migrations(version, applied_at) VALUES (?, 'future')",
            (database.CURRENT_SCHEMA_VERSION + 1,),
        )

    with pytest.raises(database.DatabaseSchemaError, match="newer than supported"):
        database.init_db(str(db_path))
