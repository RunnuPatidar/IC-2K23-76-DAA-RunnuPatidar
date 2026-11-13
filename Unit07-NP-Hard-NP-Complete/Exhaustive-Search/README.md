# Exhaustive Search – Travelling Salesperson Problem

## Aim
To solve the Travelling Salesperson Problem using exhaustive search.

## Theory
Exhaustive search is a technique that checks all possible solutions
to find the optimal solution.

In TSP, it checks every possible tour and selects the tour
with the minimum total cost.

## Algorithm
1. Define the distance matrix.
2. Fix the starting city.
3. Generate all permutations of the remaining cities.
4. Calculate the cost of every possible tour.
5. Compare the tour costs.
6. Display the minimum-cost tour.

## Time Complexity
O(n!)

## Space Complexity
O(n), excluding permutation-generation internals.

## Sample Output
Best Tour: 0 -> 1 -> 3 -> 2 -> 0
Minimum Tour Cost: 80

## Learning Outcome
Learned how exhaustive search checks all possible solutions
to obtain an optimal result.