# Python implementation of Exhaustive-Search
# Travelling Salesperson Problem using Exhaustive Search

from itertools import permutations

graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

n = len(graph)
start = 0

minimum_cost = float("inf")
best_path = []

# Generate every possible order of the remaining cities
for route in permutations(range(1, n)):
    path = [start] + list(route) + [start]

    cost = 0
    for i in range(len(path) - 1):
        cost += graph[path[i]][path[i + 1]]

    if cost < minimum_cost:
        minimum_cost = cost
        best_path = path

print("Best Tour:", " -> ".join(map(str, best_path)))
print("Minimum Tour Cost:", minimum_cost)