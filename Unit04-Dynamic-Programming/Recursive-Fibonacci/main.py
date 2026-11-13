# Python implementation of Recursive-Fibonacci

def fibonacci(n):
    if n <= 1:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)


n = 10

print("Recursive Fibonacci")
print("Number of terms:", n)
print("Fibonacci Series:")

for i in range(n):
    print(fibonacci(i), end=" ")

print()
