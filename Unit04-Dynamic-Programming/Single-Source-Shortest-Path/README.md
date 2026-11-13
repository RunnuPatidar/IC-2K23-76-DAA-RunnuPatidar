
# Single-Source Shortest Path using Bellman-Ford

## Aim
To find shortest distances from a source vertex to all other vertices.

## Algorithm
1. Initialize all distances as infinity.
2. Set the source distance to zero.
3. Relax all edges V-1 times.
4. Update distances whenever a shorter path is found.
5. Check for negative-weight cycles.
6. Display the shortest distances.

## Pseudocode
DIST[SOURCE] = 0
ALL OTHER DISTANCES = INFINITY

REPEAT V-1 TIMES:
    FOR each edge (u,v,w):
        IF DIST[u] + w < DIST[v]:
            DIST[v] = DIST[u] + w

CHECK for negative-weight cycles

## Complexity Analysis
- Time Complexity: O(VE)
- Space Complexity: O(V)

## Sample Output
A to A: 0
A to B: -1
A to C: 2
A to D: -2
A to E: 1

## Learning Outcomes
- Understood single-source shortest paths.
- Learned edge relaxation.
- Learned negative-weight cycle detection.
