import time
import random

# -------------------------------------------------------
# This script runs multiple benchmark tests
# to compare performance of both approaches.
# Results are saved for analysis.
# -------------------------------------------------------

# Dataset size (slightly smaller for repeated runs)
N = 5_000_000
data = list(range(N))


# -------------------------------------------------------
# Non-contiguous access (random)
# -------------------------------------------------------
def non_contiguous_access(data):
    """
    Simulates poor data locality by accessing elements randomly.
    This leads to inefficient cache usage and slower performance.
    """
    total = 0
    indices = list(range(len(data)))
    random.shuffle(indices)

    for i in indices:
        total += data[i]

    return total


# -------------------------------------------------------
# Contiguous access (sequential)
# -------------------------------------------------------
def contiguous_access(data):
    """
    Sequential access improves spatial locality.
    This allows CPU cache to work efficiently,
    resulting in faster execution.
    """
    total = 0

    for i in range(len(data)):
        total += data[i]

    return total


# -------------------------------------------------------
# Run benchmark multiple times
# -------------------------------------------------------
def run_benchmark():
    results = []

    # Run experiment 3 times for consistency
    for i in range(3):
        print(f"\nRun {i+1}")

        # Measure non-contiguous performance
        start = time.time()
        non_contiguous_access(data)
        nc_time = time.time() - start
        print(f"Non-contiguous: {nc_time:.4f} sec")

        # Measure contiguous performance
        start = time.time()
        contiguous_access(data)
        c_time = time.time() - start
        print(f"Contiguous: {c_time:.4f} sec")

        results.append((nc_time, c_time))

    return results


# -------------------------------------------------------
# Save results to file
# -------------------------------------------------------
def save_results(results):
    """
    Saves benchmark results into a file for reporting.
    """
    with open("results/benchmark_results.txt", "w") as f:
        f.write("Run,Non-Contiguous,Contiguous\n")

        for i, (nc, c) in enumerate(results):
            f.write(f"{i+1},{nc:.4f},{c:.4f}\n")


# -------------------------------------------------------
# Execute benchmark
# -------------------------------------------------------
results = run_benchmark()
save_results(results)

print("\nResults saved to results/benchmark_results.txt")