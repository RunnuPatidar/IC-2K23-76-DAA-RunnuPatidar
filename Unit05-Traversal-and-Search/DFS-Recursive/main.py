# Python implementation of DFS-Recursive
# Graph representation
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}


def dfs_recursive(graph, vertex, visited):
    visited.add(vertex)
    print(vertex, end=" ")

    for neighbour in graph[vertex]:
        if neighbour not in visited:
            dfs_recursive(graph, neighbour, visited)


visited = set()

print("DFS Recursive Traversal:", end=" ")
dfs_recursive(graph, 'A', visited)
print()