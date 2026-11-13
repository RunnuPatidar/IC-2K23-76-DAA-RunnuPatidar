# General Backtracking – Rat in a Maze

## Aim
To solve the Rat in a Maze problem using the backtracking technique.

## Theory
Backtracking is an algorithmic technique that builds a solution
step by step. If a selected path does not lead to a solution,
the algorithm returns to the previous state and tries another path.

## Algorithm
1. Start from the first cell of the maze.
2. Check whether the current cell is safe.
3. Mark the cell as part of the solution.
4. Try moving right and down.
5. If neither direction leads to the destination, backtrack.
6. Display the solution path if found.

## Time Complexity
O(2^(N*N)) as a loose upper bound for this recursive search.

## Space Complexity
O(N*N), including the solution matrix and recursion stack.

## Sample Output
Path found:
[1, 0, 0, 0]
[1, 1, 0, 0]
[0, 1, 0, 0]
[0, 1, 1, 1]

## Learning Outcome
Learned how backtracking explores possible paths and
returns when a path is unsuccessful.