
# Floyd-Warshall Algorithm

## Aim
To find the shortest paths between all pairs of vertices in a weighted graph.

## Algorithm
1. Initialize the distance matrix using graph edge weights.
2. Consider each vertex as an intermediate vertex.
3. Check whether a path through the intermediate vertex is shorter.
4. Update the distance matrix.
5. Repeat for all intermediate vertices.

## Pseudocode
FOR k = 0 TO n-1:
    FOR i = 0 TO n-1:
        FOR j = 0 TO n-1:
            DIST[i][j] = MIN(
                DIST[i][j],
                DIST[i][k] + DIST[k][j]
            )

RETURN DIST

## Complexity Analysis
- Time Complexity: O(V^3)
- Space Complexity: O(V^2)

## Sample Output
[0, 5, 8, 9]
[INF, 0, 3, 4]
[INF, INF, 0, 1]
[INF, INF, INF, 0]

## Learning Outcomes
- Understood all-pairs shortest paths.
- Learned Dynamic Programming on graphs.
- Learned to update distance matrices.
