# Python implementation of Complexity-Analysis

# Experiment 4: Complexity Analysis

def linear_search(arr, target):
    comparisons = 0

    for i in range(len(arr)):
        comparisons += 1

        if arr[i] == target:
            return i, comparisons

    return -1, comparisons


def main():
    arr = [10, 20, 30, 40, 50, 60, 70]

    print("Array:", arr)

    cases = {
        "Best Case": 10,
        "Average Case": 40,
        "Worst Case": 100
    }

    for case, target in cases.items():
        result, comparisons = linear_search(arr, target)

        print("\n", case)
        print("Target:", target)
        print("Index:", result)
        print("Number of comparisons:", comparisons)


if __name__ == "__main__":
    main()
