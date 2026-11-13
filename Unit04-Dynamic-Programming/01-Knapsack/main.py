# Python implementation of 01-Knapsack

def knapsack(weights, values, capacity):
    n = len(weights)

    dp = [[0 for _ in range(capacity + 1)]
          for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacity + 1):

            if weights[i - 1] <= w:
                dp[i][w] = max(
                    values[i - 1] + dp[i - 1][w - weights[i - 1]],
                    dp[i - 1][w]
                )
            else:
                dp[i][w] = dp[i - 1][w]

    selected = []
    w = capacity

    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected.append(i - 1)
            w -= weights[i - 1]

    selected.reverse()
    return dp[n][capacity], selected


weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
capacity = 5

maximum_value, selected_items = knapsack(
    weights, values, capacity
)

print("0/1 Knapsack Problem")
print("Weights:", weights)
print("Values:", values)
print("Capacity:", capacity)
print("\nSelected Items:")

for index in selected_items:
    print(
        f"Item {index + 1}: Weight={weights[index]}, "
        f"Value={values[index]}"
    )

print("\nMaximum Value:", maximum_value)
