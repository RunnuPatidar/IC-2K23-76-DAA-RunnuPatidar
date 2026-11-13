# Graph Representation – Adjacency Matrix

## Aim
To represent an undirected graph using an adjacency matrix.

## Theory
An adjacency matrix is a two-dimensional array.
A value of 1 represents an edge between two vertices,
while 0 represents no edge.

## Algorithm
1. Define the vertices and edges.
2. Create a square matrix initialized with zeros.
3. For every edge, mark the corresponding matrix positions as 1.
4. Display the matrix.

## Time Complexity
O(V^2 + E) for this implementation.

## Space Complexity
O(V^2)

## Sample Output
A [0, 1, 1, 0]
B [1, 0, 0, 1]
C [1, 0, 0, 1]
D [0, 1, 1, 0]

## Learning Outcome
Learned graph representation using an adjacency matrix.