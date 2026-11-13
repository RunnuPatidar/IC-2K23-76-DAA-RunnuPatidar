# Eight Queens Problem

## Aim
To solve the Eight Queens problem using backtracking.

## Theory
The Eight Queens problem involves placing eight queens
on an 8x8 chessboard so that no two queens attack each other.

## Algorithm
1. Start from the first row.
2. Try placing a queen in each column.
3. Check whether the position is safe.
4. If safe, place the queen and move to the next row.
5. If no safe position exists, remove the previously placed queen.
6. Continue until all possible solutions are explored.

## Time Complexity
O(N!) as an upper bound for row-wise placement.

## Space Complexity
O(N^2) for the board, with O(N) recursion depth.

## Sample Output
Total solutions for Eight Queens: 92

## Learning Outcome
Learned to solve a larger constraint satisfaction problem
using recursive backtracking.