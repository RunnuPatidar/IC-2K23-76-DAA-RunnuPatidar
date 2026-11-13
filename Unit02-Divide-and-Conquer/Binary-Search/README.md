
# Binary Search using Divide and Conquer

## Aim
To implement Binary Search using the Divide and Conquer technique.

## Algorithm
1. Initialize low and high.
2. Find the middle index.
3. Compare the middle element with the target.
4. If equal, return its index.
5. If the target is greater, search the right half.
6. Otherwise, search the left half.
7. Repeat until found or the search range becomes empty.

## Pseudocode
LOW = 0, HIGH = N - 1
WHILE LOW <= HIGH:
    MID = (LOW + HIGH) // 2
    IF A[MID] == TARGET:
        RETURN MID
    ELSE IF A[MID] < TARGET:
        LOW = MID + 1
    ELSE:
        HIGH = MID - 1
RETURN NOT FOUND

## Complexity Analysis
- Best Case: O(1)
- Average Case: O(log n)
- Worst Case: O(log n)
- Space Complexity: O(1)

## Sample Input
50

## Sample Output
Element found at index: 4

## Learning Outcomes
- Understood Divide and Conquer.
- Learned how to divide a sorted array into smaller parts.
- Understood logarithmic time complexity.
