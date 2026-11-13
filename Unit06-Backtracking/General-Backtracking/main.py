# Python implementation of General-Backtracking
# Rat in a Maze using Backtracking

N = 4

maze = [
    [1, 0, 0, 0],
    [1, 1, 0, 1],
    [0, 1, 0, 0],
    [1, 1, 1, 1]
]

solution = [[0] * N for _ in range(N)]


def is_safe(x, y):
    return (
        x >= 0 and x < N and
        y >= 0 and y < N and
        maze[x][y] == 1
    )


def solve_maze(x, y):
    if x == N - 1 and y == N - 1:
        solution[x][y] = 1
        return True

    if is_safe(x, y):
        solution[x][y] = 1

        # Move right
        if solve_maze(x, y + 1):
            return True

        # Move down
        if solve_maze(x + 1, y):
            return True

        # Backtrack
        solution[x][y] = 0
        return False

    return False


if solve_maze(0, 0):
    print("Path found:")
    for row in solution:
        print(row)
else:
    print("No path exists.")