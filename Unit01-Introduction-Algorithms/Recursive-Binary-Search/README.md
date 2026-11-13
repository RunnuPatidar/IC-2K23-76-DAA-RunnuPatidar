
# Experiment 3: Recursive Binary Search

## Aim
To implement Binary Search using recursion.

## Problem Statement
Search for a given element in a sorted array
using a recursive Binary Search algorithm.

## Algorithm
1. Set low = 0 and high = n - 1.
2. Check whether low is greater than high.
3. Calculate the middle index.
4. Compare the middle element with the target.
5. If equal, return the index.
6. If target is greater, recursively search right half.
7. Otherwise, recursively search left half.

## Pseudocode
START
FUNCTION BinarySearch(arr, low, high, target)
    IF low > high
        RETURN -1
    mid = (low + high) // 2
    IF arr[mid] == target
        RETURN mid
    ELSE IF arr[mid] < target
        RETURN BinarySearch(arr, mid+1, high, target)
    ELSE
        RETURN BinarySearch(arr, low, mid-1, target)
STOP

## Complexity Analysis

| Case | Time Complexity |
|---|---|
| Best | O(1) |
| Average | O(log n) |
| Worst | O(log n) |

Space Complexity: O(log n) due to recursion stack.

## Sample Output
Element found at index: 4

## Experimental Results
The recursive algorithm successfully searches
for an element in a sorted array.

## Learning Outcomes
- Understood recursion.
- Implemented recursive Binary Search.
- Learned divide-and-conquer technique.
- Analyzed recursive space complexity.
