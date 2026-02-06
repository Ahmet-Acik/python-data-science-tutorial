"""
Profiling Introduction: Measuring Code Performance

Use cProfile to identify bottlenecks in your code.
"""

import cProfile
import time

def slow_function(n):
    """A function that simulates slow computation."""
    result = 0
    for i in range(n):
        result += i ** 2
    return result

def fast_function(n):
    """Optimized version using math formula."""
    return n * (n - 1) * (2 * n - 1) // 6

if __name__ == "__main__":
    n = 100000

    print("Profiling slow function:")
    cProfile.run('slow_function(n)')

    print("\nProfiling fast function:")
    cProfile.run('fast_function(n)')

    # Time comparison
    start = time.time()
    slow_result = slow_function(n)
    slow_time = time.time() - start

    start = time.time()
    fast_result = fast_function(n)
    fast_time = time.time() - start

    print(f"\nSlow function result: {slow_result}, time: {slow_time:.4f}s")
    print(f"Fast function result: {fast_result}, time: {fast_time:.4f}s")
    print(f"Speedup: {slow_time / fast_time:.2f}x")