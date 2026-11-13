
# Merge Sort using Divide and Conquer

## Aim
To sort an array using Merge Sort.

## Algorithm
1. Divide the array into two halves.
2. Recursively sort both halves.
3. Merge the sorted halves.
4. Continue until the complete array is sorted.

## Pseudocode
MERGE_SORT(A):
    IF length(A) <= 1:
        RETURN A

    DIVIDE A INTO LEFT AND RIGHT
    LEFT = MERGE_SORT(LEFT)
    RIGHT = MERGE_SORT(RIGHT)

    RETURN MERGE(LEFT, RIGHT)

## Complexity Analysis
- Best Case: O(n log n)
- Average Case: O(n log n)
- Worst Case: O(n log n)
- Auxiliary Space: O(n)

## Sample Output
Sorted array: [3, 9, 10, 27, 38, 43, 82]

## Learning Outcomes
- Understood the Merge Sort technique.
- Learned recursive sorting.
- Understood merging of sorted arrays.
