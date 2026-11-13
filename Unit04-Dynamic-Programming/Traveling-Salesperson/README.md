
# Traveling Salesperson Problem using Dynamic Programming

## Aim
To find the minimum-cost tour that visits every city exactly once and returns to the starting city.

## Algorithm
1. Represent the cities using a cost matrix.
2. Start from city zero.
3. Use a bitmask to represent visited cities.
4. Calculate minimum costs for each possible state.
5. Find the minimum cost of returning to the starting city.
6. Reconstruct the optimal tour.

## Pseudocode
INITIALIZE DP[1][START] = 0

FOR each visited-city mask:
    FOR each current city:
        FOR each unvisited city:
            UPDATE minimum travel cost

FIND minimum cost to return to START
RECONSTRUCT optimal tour

## Complexity Analysis
- Time Complexity: O(n² * 2^n)
- Space Complexity: O(n * 2^n)

## Sample Output
Minimum Tour Cost: 80
Optimal Tour: 0 -> 1 -> 3 -> 2 -> 0

## Learning Outcomes
- Understood the Traveling Salesperson Problem.
- Learned bitmask representation.
- Applied Dynamic Programming to an optimization problem.
