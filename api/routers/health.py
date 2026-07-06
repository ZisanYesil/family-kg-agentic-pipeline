from datetime import datetime, timezone

from fastapi import APIRouter

router = APIRouter(tags=["health"])


@router.get("/health")
def health_check() -> dict[str, str]:
    """Return a lightweight health signal for Docker and load balancer checks."""
    return {"status": "ok", "timestamp": datetime.now(timezone.utc).isoformat()}
