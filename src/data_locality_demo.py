import time
import random

# Create large dataset
N = 10_000_000
data = list(range(N))

# -------------------------------
# Version 1: Non-contiguous access (cache-unfriendly)
# -------------------------------
def non_contiguous_access(data):
    total = 0
    indices = list(range(len(data)))
    random.shuffle(indices)  # random access pattern

    for i in indices:
        total += data[i]

    return total


# -------------------------------
# Version 2: Contiguous access (cache-friendly)
# -------------------------------
def contiguous_access(data):
    total = 0
    for i in range(len(data)):  # sequential access
        total += data[i]
    return total


# -------------------------------
# Benchmark
# -------------------------------
print("Running non-contiguous access...")
start = time.time()
non_contiguous_access(data)
end = time.time()
print(f"Non-contiguous time: {end - start:.4f} seconds")

print("\nRunning contiguous access...")
start = time.time()
contiguous_access(data)
end = time.time()
print(f"Contiguous time: {end - start:.4f} seconds")