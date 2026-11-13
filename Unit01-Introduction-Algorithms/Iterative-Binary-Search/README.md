
# Experiment 2: Iterative Binary Search

## Aim
To implement Binary Search using an iterative approach.

## Problem Statement
Search for a given element in a sorted array using
the Binary Search algorithm.

## Algorithm
1. Initialize low = 0 and high = n - 1.
2. Calculate the middle index.
3. Compare the middle element with the target.
4. If equal, return its index.
5. If the target is greater, search the right half.
6. Otherwise, search the left half.
7. Repeat until found or the search space is empty.

## Pseudocode
START
Set low = 0, high = n - 1
WHILE low <= high
    mid = (low + high) // 2
    IF arr[mid] == target
        RETURN mid
    ELSE IF arr[mid] < target
        low = mid + 1
    ELSE
        high = mid - 1
RETURN -1
STOP

## Complexity Analysis

| Case | Time Complexity |
|---|---|
| Best | O(1) |
| Average | O(log n) |
| Worst | O(log n) |

Space Complexity: O(1)

## Sample Output
Element found at index: 3

## Experimental Results
The program successfully searches for elements
in a sorted array.

## Learning Outcomes
- Understood Binary Search.
- Learned iterative searching.
- Understood divide-and-conquer concepts.
- Analyzed time and space complexity.
