# Python implementation of Optimization-Comparison
# Comparison of Dynamic Programming and Branch and Bound

import time

weights = [10, 20, 30]
profits = [60, 100, 120]
capacity = 50
n = len(weights)


# Dynamic Programming
def knapsack_dp():
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(
                    profits[i - 1] + dp[i - 1][w - weights[i - 1]],
                    dp[i - 1][w]
                )
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]


# Branch and Bound
def knapsack_bb():
    items = sorted(
        zip(weights, profits),
        key=lambda item: item[1] / item[0],
        reverse=True
    )

    best_profit = 0

    def bound(index, current_weight, current_profit):
        if current_weight >= capacity:
            return current_profit

        result = current_profit
        total_weight = current_weight
        j = index

        while j < n and total_weight + items[j][0] <= capacity:
            total_weight += items[j][0]
            result += items[j][1]
            j += 1

        if j < n:
            result += (
                (capacity - total_weight)
                * items[j][1] / items[j][0]
            )

        return result

    def search(index, current_weight, current_profit):
        nonlocal best_profit

        best_profit = max(best_profit, current_profit)

        if index == n:
            return

        if bound(index, current_weight, current_profit) <= best_profit:
            return

        weight, profit = items[index]

        if current_weight + weight <= capacity:
            search(
                index + 1,
                current_weight + weight,
                current_profit + profit
            )

        search(index + 1, current_weight, current_profit)

    search(0, 0, 0)
    return best_profit


# Measure DP execution time
start = time.perf_counter()
dp_result = knapsack_dp()
dp_time = time.perf_counter() - start

# Measure Branch and Bound execution time
start = time.perf_counter()
bb_result = knapsack_bb()
bb_time = time.perf_counter() - start

print("Optimization Comparison")
print("-----------------------")

print("Dynamic Programming Profit:", dp_result)
print("Dynamic Programming Time:", format(dp_time, ".8f"), "seconds")

print("\nBranch and Bound Profit:", bb_result)
print("Branch and Bound Time:", format(bb_time, ".8f"), "seconds")

print("\nBoth methods give the same optimal profit:",
      dp_result == bb_result)