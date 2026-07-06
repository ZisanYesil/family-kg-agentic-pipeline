import structlog

logger = structlog.get_logger(__name__)


def dispatch_extraction_job(job_id: str) -> None:
    """Queue the asynchronous agentic KG pipeline for the given job."""
    try:
        from celery_app import celery_app
    except ImportError:
        logger.warning("celery_app_unavailable_job_dispatch_skipped", job_id=job_id)
        return

    celery_app.send_task("tasks.pipeline_task.run_pipeline", args=[job_id])
    logger.info("pipeline_task_dispatched", job_id=job_id)
