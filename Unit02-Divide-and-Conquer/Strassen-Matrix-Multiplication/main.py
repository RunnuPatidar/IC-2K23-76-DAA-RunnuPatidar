# Python implementation of Strassen-Matrix-Multiplication

def add(A, B):
    n = len(A)
    return [[A[i][j] + B[i][j] for j in range(n)]
            for i in range(n)]


def subtract(A, B):
    n = len(A)
    return [[A[i][j] - B[i][j] for j in range(n)]
            for i in range(n)]


def strassen(A, B):
    n = len(A)

    if n == 1:
        return [[A[0][0] * B[0][0]]]

    mid = n // 2

    A11 = [row[:mid] for row in A[:mid]]
    A12 = [row[mid:] for row in A[:mid]]
    A21 = [row[:mid] for row in A[mid:]]
    A22 = [row[mid:] for row in A[mid:]]

    B11 = [row[:mid] for row in B[:mid]]
    B12 = [row[mid:] for row in B[:mid]]
    B21 = [row[:mid] for row in B[mid:]]
    B22 = [row[mid:] for row in B[mid:]]

    M1 = strassen(add(A11, A22), add(B11, B22))
    M2 = strassen(add(A21, A22), B11)
    M3 = strassen(A11, subtract(B12, B22))
    M4 = strassen(A22, subtract(B21, B11))
    M5 = strassen(add(A11, A12), B22)
    M6 = strassen(subtract(A21, A11), add(B11, B12))
    M7 = strassen(subtract(A12, A22), add(B21, B22))

    C11 = add(subtract(add(M1, M4), M5), M7)
    C12 = add(M3, M5)
    C21 = add(M2, M4)
    C22 = add(subtract(add(M1, M3), M2), M6)

    top = [C11[i] + C12[i] for i in range(mid)]
    bottom = [C21[i] + C22[i] for i in range(mid)]

    return top + bottom


def next_power_of_two(n):
    power = 1
    while power < n:
        power *= 2
    return power


def strassen_multiply(A, B):
    rows_a, cols_a = len(A), len(A[0])
    rows_b, cols_b = len(B), len(B[0])

    if cols_a != rows_b:
        raise ValueError("Matrix dimensions are incompatible.")

    size = next_power_of_two(max(rows_a, cols_a, rows_b, cols_b))

    padded_a = [[0] * size for _ in range(size)]
    padded_b = [[0] * size for _ in range(size)]

    for i in range(rows_a):
        for j in range(cols_a):
            padded_a[i][j] = A[i][j]

    for i in range(rows_b):
        for j in range(cols_b):
            padded_b[i][j] = B[i][j]

    result = strassen(padded_a, padded_b)

    return [row[:cols_b] for row in result[:rows_a]]


A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

B = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

print("Matrix A:")
for row in A:
    print(row)

print("\nMatrix B:")
for row in B:
    print(row)

print("\nProduct of A and B:")
for row in strassen_multiply(A, B):
    print(row)
