
# Heap Sort

## Aim
To sort an array using the Heap Sort algorithm.

## Algorithm
1. Build a max heap from the given array.
2. Swap the root with the last element.
3. Reduce the heap size.
4. Apply heapify to restore the max heap.
5. Repeat until the array is sorted.

## Pseudocode
BUILD_MAX_HEAP(A)

FOR i = n - 1 DOWN TO 1:
    SWAP A[0] AND A[i]
    HEAPIFY(A, i, 0)

## Complexity Analysis
- Best Case: O(n log n)
- Average Case: O(n log n)
- Worst Case: O(n log n)
- Auxiliary Space: O(log n) recursion stack

## Sample Output
Sorted array: [11, 12, 22, 25, 34, 64, 90]

## Learning Outcomes
- Understood the max heap data structure.
- Learned heap construction and heapify.
- Implemented Heap Sort.
