from contextlib import asynccontextmanager
from collections.abc import AsyncIterator

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.routers import health, jobs
from core.logging_config import configure_logging
from storage.database import get_database_path, init_db

configure_logging()


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    configure_logging()
    init_db(get_database_path())
    yield


app = FastAPI(
    title="Family KG Agentic Pipeline",
    description=(
        "REST API for asynchronously extracting ontology-consistent family "
        "knowledge graphs from unstructured text."
    ),
    version="0.1.0",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health.router)
app.include_router(jobs.router)
