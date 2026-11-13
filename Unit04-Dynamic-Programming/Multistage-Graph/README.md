
# Multistage Graph using Dynamic Programming

## Aim
To find the minimum-cost path in a multistage graph.

## Algorithm
1. Divide the graph into stages.
2. Set the destination cost to zero.
3. Process the stages in reverse order.
4. Calculate the minimum cost from each vertex to the destination.
5. Store the next vertex for the optimal path.
6. Reconstruct the minimum-cost path.

## Pseudocode
COST[DESTINATION] = 0

FOR each stage in reverse order:
    FOR each vertex u in stage:
        COST[u] = MIN(weight(u,v) + COST[v])

RECONSTRUCT path from source to destination

## Complexity Analysis
- Time Complexity: O(V + E)
- Space Complexity: O(V + E)

## Sample Output
Minimum Cost: 8
Optimal Path: 0 -> 1 -> 3 -> 5 -> 7

## Learning Outcomes
- Understood multistage graphs.
- Learned backward Dynamic Programming.
- Found an optimal path with minimum cost.
