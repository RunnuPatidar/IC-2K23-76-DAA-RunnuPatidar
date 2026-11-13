# DFS – Iterative

## Aim
To implement Depth First Search using an iterative approach.

## Theory
DFS explores a graph by going as deep as possible before backtracking.
The iterative method uses a stack.

## Algorithm
1. Create an empty visited set.
2. Push the starting vertex onto the stack.
3. Pop a vertex from the stack.
4. If it is not visited, mark it visited and display it.
5. Push its unvisited adjacent vertices onto the stack.
6. Repeat until the stack becomes empty.

## Time Complexity
O(V + E)

## Space Complexity
O(V)

## Sample Output
DFS Iterative Traversal: A B D E F C

## Learning Outcome
Learned graph traversal using an iterative stack-based approach.