from __future__ import annotations

from fastapi.testclient import TestClient

from api.main import app
from storage import database


def test_api_and_sqlite_round_trip_with_repair_audit(tmp_path, monkeypatch) -> None:
    db_path = tmp_path / "api.db"
    monkeypatch.setenv("DATABASE_URL", f"sqlite:///{db_path}")
    monkeypatch.setenv("DEFAULT_ONTOLOGY_PATH", "ontology/family_extended.ttl")
    dispatched = []
    monkeypatch.setattr(
        "api.routers.jobs.dispatch_extraction_job",
        lambda job_id: dispatched.append(job_id),
    )

    with TestClient(app) as client:
        create_response = client.post(
            "/jobs",
            json={"text": "Jane Doe is a person in this family narrative.","question": "When was Jane Doe born?",},
        )
        assert create_response.status_code == 202
        job_id = create_response.json()["job_id"]
        assert dispatched == [job_id]

        database.add_iteration_detail(
            job_id,
            1,
            ["structured violation"],
            "Applied one safe edit.",
            2,
            3,
            edit_log=[
                {
                    "operation": "add_triple",
                    "subject": "http://example.com/family#jane",
                    "triples_before": 2,
                    "triples_after": 3,
                }
            ],
            unresolved_violation_fingerprints=["b" * 64],
        )

        status_response = client.get(f"/jobs/{job_id}/status")
        assert status_response.status_code == 200
        assert status_response.json()["status"] == "Pending"

        iterations_response = client.get(f"/jobs/{job_id}/iterations")
        assert iterations_response.status_code == 200
        item = iterations_response.json()["iterations"][0]
        assert item["edit_log"][0]["operation"] == "add_triple"
        assert item["unresolved_violation_fingerprints"] == ["b" * 64]

    with database._connect(str(db_path)) as conn:
        assert conn.execute("PRAGMA foreign_keys").fetchone()[0] == 1
        assert conn.execute("SELECT COUNT(*) FROM jobs").fetchone()[0] == 1
        assert conn.execute("SELECT COUNT(*) FROM iterations").fetchone()[0] == 1
