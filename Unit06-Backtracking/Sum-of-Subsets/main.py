# Python implementation of Sum-of-Subsets
# Sum of Subsets using Backtracking

weights = [3, 4, 5, 6, 7]
target = 12

solution = []


def sum_of_subsets(index, current_sum):
    if current_sum == target:
        print("Subset found:", solution)
        return

    if index == len(weights) or current_sum > target:
        return

    # Include current element
    solution.append(weights[index])
    sum_of_subsets(index + 1, current_sum + weights[index])

    # Exclude current element (backtracking)
    solution.pop()
    sum_of_subsets(index + 1, current_sum)


print("Given set:", weights)
print("Target sum:", target)
print("\nSubsets with the required sum:")

sum_of_subsets(0, 0)