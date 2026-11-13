# Python implementation of Floyd-Warshall

def floyd_warshall(graph):
    n = len(graph)
    dist = [row[:] for row in graph]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] != float("inf") and \
                   dist[k][j] != float("inf"):

                    dist[i][j] = min(
                        dist[i][j],
                        dist[i][k] + dist[k][j]
                    )

    return dist


INF = float("inf")

graph = [
    [0, 5, INF, 10],
    [INF, 0, 3, INF],
    [INF, INF, 0, 1],
    [INF, INF, INF, 0]
]

result = floyd_warshall(graph)

print("Floyd-Warshall Shortest Distance Matrix")
for row in result:
    print(["INF" if x == INF else x for x in row])
