
# Quick Sort using Divide and Conquer

## Aim
To sort an array using the Quick Sort algorithm.

## Algorithm
1. Select a pivot element.
2. Divide the elements into smaller and greater groups.
3. Recursively sort both groups.
4. Combine the smaller elements, pivot, and greater elements.

## Pseudocode
QUICK_SORT(A):
    IF length(A) <= 1:
        RETURN A

    SELECT PIVOT
    SMALLER = elements <= PIVOT
    GREATER = elements > PIVOT

    RETURN QUICK_SORT(SMALLER) + PIVOT + QUICK_SORT(GREATER)

## Complexity Analysis
- Best Case: O(n log n)
- Average Case: O(n log n)
- Worst Case: O(n^2)
- Auxiliary Space: O(n) in this implementation, including recursive lists.

## Sample Output
Sorted array: [9, 12, 23, 34, 45, 56, 67, 89]

## Learning Outcomes
- Learned pivot selection and partitioning.
- Understood recursive sorting.
- Studied best, average, and worst-case performance.
