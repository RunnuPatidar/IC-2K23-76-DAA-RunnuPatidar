# Python implementation of Memoized-Fibonacci

def fibonacci(n, memo):
    if n <= 1:
        return n

    if n in memo:
        return memo[n]

    memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    return memo[n]


n = 10
memo = {}

print("Memoized Fibonacci")
print("Number of terms:", n)
print("Fibonacci Series:")

for i in range(n):
    print(fibonacci(i, memo), end=" ")

print()
print("Memoized values:", len(memo))
