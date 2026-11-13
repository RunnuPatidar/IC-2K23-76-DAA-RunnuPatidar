# Python implementation of Four-Queens
# Four Queens Problem using Backtracking

N = 4

board = [[0] * N for _ in range(N)]


def is_safe(row, col):
    # Check upper column
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
    if row == N:
        print("Solution:")
        for r in board:
            print(r)
        print()
        return

    for col in range(N):
        if is_safe(row, col):
            board[row][col] = 1

            solve(row + 1)

            # Backtrack
            board[row][col] = 0


solve(0)