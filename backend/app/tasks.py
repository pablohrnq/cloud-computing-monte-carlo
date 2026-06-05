import random
from .celery_app import celery_app

@celery_app.task(name="montecarlo.calculate_chunk")
def calculate_chunk(iterations: int, seed: int) -> int:
    """Executa uma fração independente do cálculo de Pi por Monte Carlo."""
    rng = random.Random(seed)
    inside = 0
    for _ in range(iterations):
        x = rng.random()
        y = rng.random()
        if x * x + y * y <= 1.0:
            inside += 1
    return inside
