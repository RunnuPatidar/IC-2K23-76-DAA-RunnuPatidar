# Python implementation of Knapsack-Branch-and-Bound
# 0/1 Knapsack using Branch and Bound

items = [
    (10, 60),
    (20, 100),
    (30, 120)
]

capacity = 50

# Sort items by profit-to-weight ratio
items.sort(key=lambda x: x[1] / x[0], reverse=True)

n = len(items)
max_profit = 0
best_items = []


def calculate_bound(index, current_weight, current_profit):
    if current_weight >= capacity:
        return current_profit

    bound = current_profit
    total_weight = current_weight
    j = index

    # Add complete items while capacity allows
    while j < n and total_weight + items[j][0] <= capacity:
        total_weight += items[j][0]
        bound += items[j][1]
        j += 1

    # Add fractional part of the next item
    if j < n:
        remaining = capacity - total_weight
        bound += remaining * items[j][1] / items[j][0]

    return bound


def knapsack(index, current_weight, current_profit, selected):
    global max_profit, best_items

    if current_profit > max_profit:
        max_profit = current_profit
        best_items = selected.copy()

    if index == n:
        return

    bound = calculate_bound(index, current_weight, current_profit)

    if bound <= max_profit:
        return

    weight, profit = items[index]

    # Include current item if capacity allows
    if current_weight + weight <= capacity:
        selected.append(index)

        knapsack(
            index + 1,
            current_weight + weight,
            current_profit + profit,
            selected
        )

        selected.pop()

    # Exclude current item
    knapsack(index + 1, current_weight, current_profit, selected)


knapsack(0, 0, 0, [])

print("Maximum Profit:", max_profit)
print("Selected Items:")

for index in best_items:
    print("Weight:", items[index][0], "Profit:", items[index][1])

print("Total Weight:", sum(items[i][0] for i in best_items))