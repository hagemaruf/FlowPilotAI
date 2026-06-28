from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.workflows import router as workflow_router
from app.api.runs import router as run_router
from app.api.history import router as history_router
from app.api.templates import router as templates_router

app = FastAPI(
    title="FlowPilot AI",
    version="0.1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://localhost:7167",
        "http://localhost:8080"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {
        "app": "FlowPilot AI",
        "status": "running"
    }

app.include_router(
    workflow_router,
    prefix="/api/workflows",
    tags=["Workflows"]
)

app.include_router(
    run_router,
    prefix="/api/runs",
    tags=["Runs"]
)

app.include_router(
    history_router,
    prefix="/api/history",
    tags=["History"]
)

app.include_router(
    templates_router,
    prefix="/api/templates",
    tags=["Templates"]
)