# Python implementation of Graph-Adjacency-Matrix
# Graph using adjacency matrix

vertices = ['A', 'B', 'C', 'D']

edges = [
    ('A', 'B'),
    ('A', 'C'),
    ('B', 'D'),
    ('C', 'D')
]

n = len(vertices)

# Initialize matrix with zeros
matrix = [[0 for _ in range(n)] for _ in range(n)]

# Add edges
for u, v in edges:
    i = vertices.index(u)
    j = vertices.index(v)

    matrix[i][j] = 1
    matrix[j][i] = 1

print("Graph Representation using Adjacency Matrix:")

print("  ", *vertices)

for i in range(n):
    print(vertices[i], matrix[i])