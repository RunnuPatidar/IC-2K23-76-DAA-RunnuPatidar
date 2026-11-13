
# Prim's Algorithm

## Aim
To find the Minimum Spanning Tree of a connected weighted graph using Prim's Algorithm.

## Algorithm
1. Select a starting vertex.
2. Mark it as visited.
3. Select the minimum-weight edge connecting a visited vertex to an unvisited vertex.
4. Add the selected edge to the MST.
5. Mark the new vertex as visited.
6. Repeat until all vertices are included.

## Pseudocode
SELECT starting vertex
MARK it visited

WHILE unvisited vertices remain:
    SELECT minimum weight edge
    CONNECT visited and unvisited vertices
    ADD edge to MST
    MARK new vertex visited

RETURN MST and total cost

## Complexity Analysis
Using an adjacency list and a min-heap:
- Time Complexity: O(E log V)
- Auxiliary Space: O(V + E)

## Sample Output
Total Minimum Cost: 11

## Learning Outcomes
- Understood Minimum Spanning Trees.
- Learned greedy edge selection.
- Implemented Prim's Algorithm using a priority queue.
