# Python implementation of Fractional-Knapsack

def fractional_knapsack(items, capacity):
    # Sort items by value/weight ratio in descending order
    items = sorted(
        items,
        key=lambda item: item["value"] / item["weight"],
        reverse=True
    )

    total_value = 0
    selected_items = []

    for item in items:
        if capacity <= 0:
            break

        if item["weight"] <= capacity:
            # Take the complete item
            selected_items.append((item["name"], 1))
            total_value += item["value"]
            capacity -= item["weight"]
        else:
            # Take only the required fraction
            fraction = capacity / item["weight"]
            selected_items.append((item["name"], fraction))
            total_value += item["value"] * fraction
            capacity = 0

    return total_value, selected_items


items = [
    {"name": "Item 1", "weight": 10, "value": 60},
    {"name": "Item 2", "weight": 20, "value": 100},
    {"name": "Item 3", "weight": 30, "value": 120}
]

capacity = 50

maximum_value, selected = fractional_knapsack(items, capacity)

print("Fractional Knapsack Problem")
print("Knapsack Capacity:", capacity)
print("\nSelected Items:")

for name, fraction in selected:
    print(f"{name}: {fraction * 100:.2f}%")

print("\nMaximum Value:", maximum_value)
