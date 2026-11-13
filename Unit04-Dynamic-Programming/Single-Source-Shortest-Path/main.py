# Python implementation of Single-Source-Shortest-Path

def bellman_ford(vertices, edges, source):
    distance = {v: float("inf") for v in vertices}
    distance[source] = 0

    # Relax all edges V-1 times
    for _ in range(len(vertices) - 1):
        updated = False

        for u, v, weight in edges:
            if distance[u] != float("inf"):
                if distance[u] + weight < distance[v]:
                    distance[v] = distance[u] + weight
                    updated = True

        if not updated:
            break

    # Check for negative-weight cycles
    for u, v, weight in edges:
        if distance[u] != float("inf"):
            if distance[u] + weight < distance[v]:
                return None

    return distance


vertices = ["A", "B", "C", "D", "E"]

edges = [
    ("A", "B", -1),
    ("A", "C", 4),
    ("B", "C", 3),
    ("B", "D", 2),
    ("B", "E", 2),
    ("D", "B", 1),
    ("D", "C", 5),
    ("E", "D", -3)
]

source = "A"

result = bellman_ford(vertices, edges, source)

print("Bellman-Ford Single-Source Shortest Path")

if result is None:
    print("Graph contains a reachable negative-weight cycle.")
else:
    print("Source Vertex:", source)
    print("\nShortest Distances:")

    for vertex, distance in result.items():
        print(f"{source} to {vertex}: {distance}")
