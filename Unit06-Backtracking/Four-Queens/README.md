# Four Queens Problem

## Aim
To solve the Four Queens problem using backtracking.

## Theory
The Four Queens problem involves placing four queens
on a 4x4 chessboard so that no two queens attack each other.

## Algorithm
1. Start from the first row.
2. Place a queen in a safe column.
3. Check whether the position is safe.
4. Move to the next row.
5. If no safe position is available, backtrack.
6. Continue until all four queens are placed.

## Time Complexity
O(N!), as a standard upper bound for row-wise placement.

## Space Complexity
O(N^2) for the board, with O(N) recursion depth.

## Sample Output
Two valid solutions are displayed.

## Learning Outcome
Learned how to use backtracking to solve the Four Queens problem.