# Data Locality Optimization in HPC

## Overview
This project demonstrates the impact of data locality optimization on performance in high-performance computing (HPC).

## Technique Used
Data locality optimization improves cache efficiency by accessing data in contiguous memory locations.

## Implementation
Two approaches were implemented:
1. Non-contiguous access (random memory access)
2. Contiguous access (sequential memory access)

## How to Run

Run the main demo:
python src/data_locality_demo.py

Run benchmark:
python src/benchmark_runner.py

## Sample Results

Non-contiguous: ~5.5 sec  
Contiguous: ~0.21 sec  

~25x performance improvement due to data locality.

## Results
Benchmark results show that contiguous access is significantly faster due to improved cache utilization.

## Conclusion
This experiment demonstrates how optimizing data structures and access patterns can significantly improve performance in HPC systems.
