
# Maximum and Minimum using Divide and Conquer

## Aim
To find the maximum and minimum elements in an array using Divide and Conquer.

## Algorithm
1. Divide the array into two halves.
2. Find maximum and minimum in each half recursively.
3. Compare both maximum values.
4. Compare both minimum values.
5. Return the overall maximum and minimum.

## Pseudocode
FIND_MAX_MIN(LOW, HIGH):
    IF LOW == HIGH:
        RETURN A[LOW], A[LOW]

    MID = (LOW + HIGH) // 2

    LEFT = FIND_MAX_MIN(LOW, MID)
    RIGHT = FIND_MAX_MIN(MID + 1, HIGH)

    RETURN MAX(LEFT.MAX, RIGHT.MAX),
           MIN(LEFT.MIN, RIGHT.MIN)

## Complexity Analysis
- Time Complexity: O(n)
- Auxiliary Space: O(log n) recursion stack

## Sample Output
Maximum element: 91
Minimum element: 5

## Learning Outcomes
- Learned recursive problem division.
- Understood how to combine subproblem results.
- Studied the efficiency of finding maximum and minimum.
