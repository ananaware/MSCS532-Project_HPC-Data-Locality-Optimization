import time
import random

# dataset size (smaller to allow multiple runs)
N = 5_000_000
data = list(range(N))


def non_contiguous_access(data):
    total = 0
    indices = list(range(len(data)))
    random.shuffle(indices)
    for i in indices:
        total += data[i]
    return total


def contiguous_access(data):
    total = 0
    for i in range(len(data)):
        total += data[i]
    return total


def run_benchmark():
    results = []

    for i in range(3):
        print(f"\nRun {i+1}")

        start = time.time()
        non_contiguous_access(data)
        nc_time = time.time() - start
        print(f"Non-contiguous: {nc_time:.4f} sec")

        start = time.time()
        contiguous_access(data)
        c_time = time.time() - start
        print(f"Contiguous: {c_time:.4f} sec")

        results.append((nc_time, c_time))

    return results


def save_results(results):
    with open("results/benchmark_results.txt", "w") as f:
        f.write("Run,Non-Contiguous,Contiguous\n")
        for i, (nc, c) in enumerate(results):
            f.write(f"{i+1},{nc:.4f},{c:.4f}\n")


results = run_benchmark()
save_results(results)

print("\nResults saved to results/benchmark_results.txt")