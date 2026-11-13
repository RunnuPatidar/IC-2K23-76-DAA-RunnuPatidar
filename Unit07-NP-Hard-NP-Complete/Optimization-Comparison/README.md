# Optimization Comparison

## Aim
To compare Dynamic Programming and Branch and Bound
for solving the 0/1 Knapsack problem.

## Theory
Dynamic Programming solves a problem by storing results
of overlapping subproblems.

Branch and Bound explores possible solutions and prunes
branches that cannot improve the current best solution.

## Algorithm
1. Define the weights, profits and capacity.
2. Implement the Dynamic Programming approach.
3. Implement the Branch and Bound approach.
4. Measure the execution time of both methods.
5. Compare their maximum profits and execution times.

## Time Complexity
Dynamic Programming: O(nW)

Branch and Bound: O(2^n) worst case.

## Space Complexity
Dynamic Programming: O(nW)

Branch and Bound: O(n) auxiliary recursion space,
excluding sorting and input storage.

## Sample Result
Dynamic Programming Profit: 220
Branch and Bound Profit: 220

Both methods give the same optimal profit: True

## Learning Outcome
Learned to compare two optimization techniques
based on solution quality and execution time.