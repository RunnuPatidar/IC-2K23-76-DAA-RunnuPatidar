# Graph Representation – Adjacency List

## Aim
To represent a graph using an adjacency list.

## Theory
An adjacency list stores each vertex along with a list
of all vertices directly connected to it.

## Algorithm
1. Create an empty list for every vertex.
2. Define the edges of the graph.
3. Add each connected vertex to the corresponding list.
4. Display the adjacency list.

## Time Complexity
O(V + E) for constructing the adjacency list.

## Space Complexity
O(V + E)

## Sample Output
A : ['B', 'C']
B : ['A', 'D']
C : ['A', 'D']
D : ['B', 'C']

## Learning Outcome
Learned how to represent graphs using adjacency lists.