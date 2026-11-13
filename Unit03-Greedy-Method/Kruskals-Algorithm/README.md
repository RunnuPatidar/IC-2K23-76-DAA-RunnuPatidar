
# Kruskal's Algorithm

## Aim
To find the Minimum Spanning Tree of a weighted graph using Kruskal's Algorithm.

## Algorithm
1. Sort all edges in ascending order of weight.
2. Initialize each vertex as a separate set.
3. Select the smallest edge.
4. Check whether adding it creates a cycle.
5. If no cycle is formed, add it to the MST.
6. Repeat until V-1 edges are selected.

## Pseudocode
SORT edges by increasing weight
INITIALIZE disjoint sets

FOR each edge (u, v):
    IF FIND(u) != FIND(v):
        ADD edge to MST
        UNION(u, v)

STOP when V-1 edges are selected

## Complexity Analysis
- Sorting Edges: O(E log E)
- Union-Find operations: Nearly O(E)
- Overall Time Complexity: O(E log E)
- Auxiliary Space: O(V)

## Sample Output
Total Minimum Cost: 11

## Learning Outcomes
- Understood Minimum Spanning Trees.
- Learned cycle detection using Disjoint Set Union.
- Implemented Greedy edge selection.
