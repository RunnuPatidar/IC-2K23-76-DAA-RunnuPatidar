
# Memoized Fibonacci using Dynamic Programming

## Aim
To generate the Fibonacci series using memoization.

## Algorithm
1. Create an empty memoization dictionary.
2. Return n if n is 0 or 1.
3. Check whether the result is already stored.
4. If not, calculate the result recursively.
5. Store the result and return it.

## Pseudocode
FIBONACCI(n):
    IF n <= 1:
        RETURN n
    IF n EXISTS IN MEMO:
        RETURN MEMO[n]
    MEMO[n] = FIBONACCI(n-1) + FIBONACCI(n-2)
    RETURN MEMO[n]

## Complexity Analysis
- Time Complexity: O(n)
- Auxiliary Space: O(n)

## Sample Output
0 1 1 2 3 5 8 13 21 34

## Learning Outcomes
- Understood memoization.
- Learned to avoid repeated calculations.
- Understood overlapping subproblems.
