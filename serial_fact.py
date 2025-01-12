import cProfile
from math import prod
import time

def serial_factorial(n):
    """Calculate factorial serially."""
    return prod(range(1, n + 1))

if __name__ == "__main__":
    n = 500000  # Large number for factorial

    # Profile the serial execution
    cProfile.run('serial_factorial(n)')
