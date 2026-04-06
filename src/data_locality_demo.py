import time
import random

# -------------------------------------------------------
# This program demonstrates data locality optimization.
# We compare two approaches:
# 1. Non-contiguous access (random access) → slow
# 2. Contiguous access (sequential access) → fast
# -------------------------------------------------------

# Create a large dataset
# Large size helps highlight performance difference
N = 10_000_000
data = list(range(N))


# -------------------------------------------------------
# Version 1: Non-contiguous access (cache-unfriendly)
# -------------------------------------------------------
def non_contiguous_access(data):
    """
    This function accesses elements in random order.
    Random access reduces cache efficiency and increases memory latency.
    This simulates poor data locality.
    """
    total = 0

    # Create list of indices and shuffle them
    # This forces random memory access
    indices = list(range(len(data)))
    random.shuffle(indices)

    # Access elements using shuffled indices
    for i in indices:
        total += data[i]

    return total


# -------------------------------------------------------
# Version 2: Contiguous access (cache-friendly)
# -------------------------------------------------------
def contiguous_access(data):
    """
    This function accesses elements sequentially.
    Sequential access improves cache utilization,
    which results in faster execution.
    """
    total = 0

    # Access elements in order (0 → N)
    for i in range(len(data)):
        total += data[i]

    return total


# -------------------------------------------------------
# Benchmark execution
# -------------------------------------------------------
print("Running non-contiguous access...")
start = time.time()

# Execute slow version
non_contiguous_access(data)

end = time.time()
print(f"Non-contiguous time: {end - start:.4f} seconds")

print("\nRunning contiguous access...")
start = time.time()

# Execute optimized version
contiguous_access(data)

end = time.time()
print(f"Contiguous time: {end - start:.4f} seconds")