import os

from celery import Celery

from core.logging_config import configure_logging

configure_logging()

redis_url = os.getenv("REDIS_URL", "redis://redis:6379/0")

celery_app = Celery(
    "family_kg_agentic_pipeline",
    broker=redis_url,
    backend=redis_url,
    include=["tasks.pipeline_task"],
)

celery_app.conf.update(
    task_serializer="json",
    result_serializer="json",
    accept_content=["json"],
    timezone="UTC",
    enable_utc=True,
)
