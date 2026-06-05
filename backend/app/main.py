import time
from typing import List
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from celery import group
from .tasks import calculate_chunk

app = FastAPI(title="Cloud Monte Carlo Distribuído", version="1.0.0")

class ProcessRequest(BaseModel):
    iterations: int = Field(default=1_000_000, ge=10_000, le=100_000_000)
    workers: int = Field(default=4, ge=1, le=16)

class ProcessResponse(BaseModel):
    iterations: int
    workers: int
    pi_estimate: float
    points_inside_circle: int
    elapsed_seconds: float
    chunks: List[int]

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/process", response_model=ProcessResponse)
def process(req: ProcessRequest):
    """Divide a carga em N chunks e envia para os workers Celery via Redis."""
    base = req.iterations // req.workers
    chunks = [base for _ in range(req.workers)]
    chunks[-1] += req.iterations - sum(chunks)

    start = time.perf_counter()
    job = group(calculate_chunk.s(chunks[i], 20260608 + i) for i in range(req.workers))()

    try:
        results = job.get(timeout=600)
    except Exception as exc:
        raise HTTPException(status_code=500, detail=f"Falha no processamento distribuído: {exc}")

    elapsed = time.perf_counter() - start
    inside = sum(results)
    pi = 4 * inside / req.iterations
    return ProcessResponse(
        iterations=req.iterations,
        workers=req.workers,
        pi_estimate=pi,
        points_inside_circle=inside,
        elapsed_seconds=round(elapsed, 4),
        chunks=chunks,
    )
