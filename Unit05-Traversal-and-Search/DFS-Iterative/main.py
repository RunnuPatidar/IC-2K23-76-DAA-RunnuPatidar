# Python implementation of DFS-Iterative
# Graph representation
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}


def dfs_iterative(graph, start):
    visited = set()
    stack = [start]

    print("DFS Iterative Traversal:", end=" ")

    while stack:
        vertex = stack.pop()

        if vertex not in visited:
            visited.add(vertex)
            print(vertex, end=" ")

            for neighbour in reversed(graph[vertex]):
                if neighbour not in visited:
                    stack.append(neighbour)


dfs_iterative(graph, 'A')
print()