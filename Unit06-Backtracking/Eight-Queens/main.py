# Python implementation of Eight-Queens
# Eight Queens Problem using Backtracking

N = 8

board = [[0] * N for _ in range(N)]
solution_count = 0


def is_safe(row, col):
    # Check column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper-left diagonal
    i = row - 1
    j = col - 1

    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check upper-right diagonal
    i = row - 1
    j = col + 1

    while i >= 0 and j < N:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True


def solve(row):
    global solution_count

    if row == N:
        solution_count += 1
        return

    for col in range(N):
        if is_safe(row, col):
            board[row][col] = 1

            solve(row + 1)

            # Backtrack
            board[row][col] = 0


solve(0)

print("Total solutions for Eight Queens:", solution_count)