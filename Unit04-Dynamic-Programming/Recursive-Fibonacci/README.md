
# Recursive Fibonacci

## Aim
To generate the Fibonacci series using recursion.

## Algorithm
1. If n is 0 or 1, return n.
2. Otherwise, calculate fibonacci(n-1) + fibonacci(n-2).
3. Repeat recursively to generate the series.

## Pseudocode
FIBONACCI(n):
    IF n <= 1:
        RETURN n
    RETURN FIBONACCI(n-1) + FIBONACCI(n-2)

## Complexity Analysis
- Time Complexity: O(2^n) (upper bound)
- Auxiliary Space: O(n) recursion stack

## Sample Output
0 1 1 2 3 5 8 13 21 34

## Learning Outcomes
- Understood recursion.
- Learned the Fibonacci recurrence relation.
- Observed repeated calculations in recursion.
