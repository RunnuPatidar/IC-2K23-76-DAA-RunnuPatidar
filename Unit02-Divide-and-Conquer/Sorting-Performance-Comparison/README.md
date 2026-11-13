
# Sorting Performance Comparison

## Aim
To compare the performance of Merge Sort, Quick Sort, and Heap Sort.

## Algorithm
1. Generate random arrays of different sizes.
2. Apply all three sorting algorithms.
3. Measure execution time using time.perf_counter().
4. Store the results in a CSV file.
5. Plot a graph to compare their execution times.

## Complexity Analysis

| Algorithm | Best Case | Average Case | Worst Case |
|---|---|---|---|
| Merge Sort | O(n log n) | O(n log n) | O(n log n) |
| Quick Sort | O(n log n) | O(n log n) | O(n²) |
| Heap Sort | O(n log n) | O(n log n) | O(n log n) |

## Space Complexity
- Merge Sort: O(n)
- Quick Sort: O(n) auxiliary space in this implementation, including recursive lists.
- Heap Sort: O(log n) recursion stack.

## Experimental Results
Execution time is measured for different input sizes.
The CSV file and graph are generated automatically.

## Learning Outcomes
- Compared three sorting algorithms.
- Learned execution-time measurement.
- Understood theoretical and experimental complexity.
- Learned to visualize performance using Matplotlib.
