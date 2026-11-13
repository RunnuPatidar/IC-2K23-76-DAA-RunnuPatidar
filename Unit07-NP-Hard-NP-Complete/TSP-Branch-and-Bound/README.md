# Travelling Salesperson Problem using Branch and Bound

## Aim
To solve the Travelling Salesperson Problem using Branch and Bound.

## Theory
The Travelling Salesperson Problem finds a minimum-cost
tour that visits every city exactly once and returns
to the starting city.

Branch and Bound uses lower bounds to eliminate
unpromising partial tours.

## Algorithm
1. Define the cost matrix.
2. Fix the starting city.
3. Generate possible next cities.
4. Calculate a lower bound for each partial tour.
5. Prune branches whose lower bound cannot improve
   the current best solution.
6. Continue searching promising branches.
7. Display the optimal tour and its cost.

## Time Complexity
O(n!) in the worst case.

## Space Complexity
O(n) auxiliary recursion space, excluding input storage.

## Sample Output
Optimal Tour: 0 -> 1 -> 3 -> 2 -> 0
Minimum Tour Cost: 80

## Learning Outcome
Learned how Branch and Bound can reduce the search
space in the Travelling Salesperson Problem.