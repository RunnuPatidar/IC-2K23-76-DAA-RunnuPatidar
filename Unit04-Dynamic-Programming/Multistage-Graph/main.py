# Python implementation of Multistage-Graph

def multistage_graph(graph, stages, source, destination):
    n = len(graph)

    cost = [float("inf")] * n
    next_vertex = [-1] * n

    cost[destination] = 0

    # Process vertices stage by stage, backwards
    for stage in range(len(stages) - 2, -1, -1):
        for u in stages[stage]:
            for v, weight in graph[u]:
                if cost[v] != float("inf"):
                    if weight + cost[v] < cost[u]:
                        cost[u] = weight + cost[v]
                        next_vertex[u] = v

    path = []
    current = source

    while current != -1:
        path.append(current)
        if current == destination:
            break
        current = next_vertex[current]

    return cost[source], path


# Vertices: 0, 1, 2, 3, 4, 5, 6, 7
graph = {
    0: [(1, 2), (2, 1)],
    1: [(3, 2), (4, 3)],
    2: [(3, 6), (4, 7)],
    3: [(5, 1)],
    4: [(5, 2), (6, 3)],
    5: [(7, 3)],
    6: [(7, 2)],
    7: []
}

stages = [
    [0],
    [1, 2],
    [3, 4],
    [5, 6],
    [7]
]

minimum_cost, path = multistage_graph(
    graph, stages, 0, 7
)

print("Multistage Graph")
print("Minimum Cost:", minimum_cost)
print("Optimal Path:", " -> ".join(map(str, path)))
