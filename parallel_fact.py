import cProfile
from multiprocessing import Pool
from math import prod
import time

def factorial_chunk(start, end):
    """Calculate the product of a range of numbers."""
    return prod(range(start, end + 1))

def parallel_factorial(n):
    """Calculate factorial using parallel processing."""
    num_processes = 4  # Number of processes
    chunk_size = n // num_processes
    chunks = [(i * chunk_size + 1, (i + 1) * chunk_size) for i in range(num_processes)]
    chunks[-1] = (chunks[-1][0], n)  # Ensure the last chunk goes up to n

    with Pool(num_processes) as pool:
        partial_results = pool.starmap(factorial_chunk, chunks)

    return prod(partial_results)

if __name__ == "__main__":
    n = 500000  # Large number for factorial

    # Profile the parallel execution
    cProfile.run('parallel_factorial(n)')
