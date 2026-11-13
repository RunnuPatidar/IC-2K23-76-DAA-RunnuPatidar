# Python implementation of Graph-Adjacency-List
# Graph using adjacency list

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C']
}

print("Graph Representation using Adjacency List:")

for vertex in graph:
    print(vertex, ":", graph[vertex])