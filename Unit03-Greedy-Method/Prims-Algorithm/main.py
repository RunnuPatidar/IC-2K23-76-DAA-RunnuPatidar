# Python implementation of Prims-Algorithm

import heapq


def prims_algorithm(graph, start):
    visited = set()
    min_heap = [(0, start, None)]

    mst = []
    total_cost = 0

    while min_heap:
        weight, vertex, parent = heapq.heappop(min_heap)

        if vertex in visited:
            continue

        visited.add(vertex)

        if parent is not None:
            mst.append((parent, vertex, weight))
            total_cost += weight

        for neighbor, edge_weight in graph[vertex]:
            if neighbor not in visited:
                heapq.heappush(
                    min_heap,
                    (edge_weight, neighbor, vertex)
                )

    return mst, total_cost


graph = {
    "A": [("B", 4), ("C", 3)],
    "B": [("A", 4), ("C", 1), ("D", 2)],
    "C": [("A", 3), ("B", 1), ("D", 4), ("E", 2)],
    "D": [("B", 2), ("C", 4), ("E", 2), ("F", 3)],
    "E": [("C", 2), ("D", 2), ("F", 3)],
    "F": [("D", 3), ("E", 3)]
}

mst, cost = prims_algorithm(graph, "A")

print("Prim's Algorithm")
print("\nMinimum Spanning Tree Edges:")

for u, v, weight in mst:
    print(f"{u} - {v} : {weight}")

print("\nTotal Minimum Cost:", cost)
