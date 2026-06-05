import random
import time
from multiprocessing import Pool

TOTAL_ITERATIONS = 12_000_000
WORKER_OPTIONS = [1, 2, 4, 8]

def calculate_chunk(args):
    iterations, seed = args
    rng = random.Random(seed)
    inside = 0
    for _ in range(iterations):
        x = rng.random()
        y = rng.random()
        if x * x + y * y <= 1.0:
            inside += 1
    return inside

def run(workers):
    base = TOTAL_ITERATIONS // workers
    chunks = [base for _ in range(workers)]
    chunks[-1] += TOTAL_ITERATIONS - sum(chunks)
    start = time.perf_counter()
    with Pool(processes=workers) as pool:
        inside = sum(pool.map(calculate_chunk, [(chunks[i], 20260608 + i) for i in range(workers)]))
    elapsed = time.perf_counter() - start
    pi = 4 * inside / TOTAL_ITERATIONS
    return elapsed, pi

if __name__ == "__main__":
    print("workers,tempo_segundos,pi_estimado")
    for workers in WORKER_OPTIONS:
        elapsed, pi = run(workers)
        print(f"{workers},{elapsed:.3f},{pi:.6f}")
