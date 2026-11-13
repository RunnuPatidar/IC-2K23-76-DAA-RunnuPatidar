# N-Queens Problem

## Aim
To solve the N-Queens problem for a user-defined board size.

## Theory
The N-Queens problem is a constraint satisfaction problem.
It requires placing N queens on an N x N chessboard so that
no two queens attack each other.

## Algorithm
1. Read the value of N.
2. Create an N x N chessboard.
3. Place one queen in each row.
4. Check the column and both diagonals for conflicts.
5. If the position is safe, move to the next row.
6. If no safe position exists, backtrack.
7. Display all possible solutions.

## Time Complexity
O(N!) as an upper bound for row-wise placement.

## Space Complexity
O(N^2) for the board, with O(N) recursion depth.

## Sample Input
4

## Sample Output
Total solutions: 2

## Learning Outcome
Learned to solve the generalized N-Queens problem using backtracking.