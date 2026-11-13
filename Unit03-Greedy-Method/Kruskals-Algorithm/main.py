# Python implementation of Kruskals-Algorithm

def find(parent, vertex):
    if parent[vertex] != vertex:
        parent[vertex] = find(parent, parent[vertex])

    return parent[vertex]


def union(parent, rank, u, v):
    root_u = find(parent, u)
    root_v = find(parent, v)

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


def kruskals_algorithm(vertices, edges):
    edges = sorted(edges, key=lambda edge: edge[2])

    parent = {v: v for v in vertices}
    rank = {v: 0 for v in vertices}

    mst = []
    total_cost = 0

    for u, v, weight in edges:
        if union(parent, rank, u, v):
            mst.append((u, v, weight))
            total_cost += weight

            if len(mst) == len(vertices) - 1:
                break

    if len(mst) != len(vertices) - 1:
        raise ValueError("Graph is disconnected; MST does not exist.")

    return mst, total_cost


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

mst, cost = kruskals_algorithm(vertices, edges)

print("Kruskal's Algorithm")
print("\nMinimum Spanning Tree Edges:")

for u, v, weight in mst:
    print(f"{u} - {v} : {weight}")

print("\nTotal Minimum Cost:", cost)
