# Python implementation of Minimum-Cost-Network-Design

import heapq
import time


vertices = ["A", "B", "C", "D", "E", "F"]

edges = [
    ("A", "B", 4),
    ("A", "C", 3),
    ("B", "C", 1),
    ("B", "D", 2),
    ("C", "D", 4),
    ("C", "E", 2),
    ("D", "E", 2),
    ("D", "F", 3),
    ("E", "F", 3)
]


def prims():
    graph = {v: [] for v in vertices}

    for u, v, weight in edges:
        graph[u].append((v, weight))
        graph[v].append((u, weight))

    visited = set()
    heap = [(0, "A", None)]
    mst = []
    cost = 0

    while heap:
        weight, vertex, parent = heapq.heappop(heap)

        if vertex in visited:
            continue

        visited.add(vertex)

        if parent is not None:
            mst.append((parent, vertex, weight))
            cost += weight

        for neighbor, edge_weight in graph[vertex]:
            if neighbor not in visited:
                heapq.heappush(
                    heap, (edge_weight, neighbor, vertex)
                )

    if len(visited) != len(vertices):
        raise ValueError("Graph is disconnected.")

    return mst, cost


def kruskals():
    parent = {v: v for v in vertices}
    rank = {v: 0 for v in vertices}

    def find(v):
        if parent[v] != v:
            parent[v] = find(parent[v])
        return parent[v]

    def union(u, v):
        root_u = find(u)
        root_v = find(v)

        if root_u == root_v:
            return False

        if rank[root_u] < rank[root_v]:
            parent[root_u] = root_v
        elif rank[root_u] > rank[root_v]:
            parent[root_v] = root_u
        else:
            parent[root_v] = root_u
            rank[root_u] += 1

        return True

    mst = []
    cost = 0

    for u, v, weight in sorted(edges, key=lambda x: x[2]):
        if union(u, v):
            mst.append((u, v, weight))
            cost += weight

            if len(mst) == len(vertices) - 1:
                break

    if len(mst) != len(vertices) - 1:
        raise ValueError("Graph is disconnected.")

    return mst, cost


start = time.perf_counter()
prim_mst, prim_cost = prims()
prim_time = time.perf_counter() - start

start = time.perf_counter()
kruskal_mst, kruskal_cost = kruskals()
kruskal_time = time.perf_counter() - start


print("MINIMUM-COST NETWORK DESIGN")
print("=" * 45)

print("\nPrim's Algorithm:")
for u, v, weight in prim_mst:
    print(f"{u} - {v}: {weight}")
print("Total Cost:", prim_cost)
print(f"Execution Time: {prim_time:.8f} seconds")

print("\nKruskal's Algorithm:")
for u, v, weight in kruskal_mst:
    print(f"{u} - {v}: {weight}")
print("Total Cost:", kruskal_cost)
print(f"Execution Time: {kruskal_time:.8f} seconds")

print("\nCOMPARISON")
print("Prim's Cost:", prim_cost)
print("Kruskal's Cost:", kruskal_cost)

if prim_cost == kruskal_cost:
    print("Both algorithms produced the same minimum cost.")
else:
    print("The results differ. Check the implementations.")

print("\nBoth algorithms find a Minimum Spanning Tree.")
