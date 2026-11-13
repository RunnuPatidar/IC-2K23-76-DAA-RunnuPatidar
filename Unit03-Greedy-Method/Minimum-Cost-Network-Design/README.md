
# Minimum-Cost Network Design

## Aim
To design a minimum-cost network using Prim's and Kruskal's Minimum Spanning Tree algorithms.

## Algorithm
1. Represent the network as a weighted graph.
2. Apply Prim's Algorithm to find the MST.
3. Apply Kruskal's Algorithm to find the MST.
4. Calculate the total cost of both MSTs.
5. Measure and compare their execution times.
6. Verify that both algorithms produce the same minimum cost.

## Pseudocode
CREATE weighted graph

PRIM_MST = APPLY PRIM'S ALGORITHM
KRUSKAL_MST = APPLY KRUSKAL'S ALGORITHM

CALCULATE total costs
MEASURE execution times

COMPARE both results

## Complexity Analysis
Using an adjacency list and min-heap for Prim:
- Prim's Algorithm: O(E log V)
- Kruskal's Algorithm: O(E log E)
- Both produce a Minimum Spanning Tree.

## Sample Output
Prim's Minimum Cost: 11
Kruskal's Minimum Cost: 11

## Learning Outcomes
- Understood real-world network design.
- Learned to find a Minimum Spanning Tree.
- Compared Prim's and Kruskal's algorithms.
- Learned to measure execution time.
