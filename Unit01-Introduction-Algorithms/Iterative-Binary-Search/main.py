# Python implementation of Iterative-Binary-Search

# Experiment 2: Iterative Binary Search

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid

        elif arr[mid] < target:
            low = mid + 1

        else:
            high = mid - 1

    return -1


def main():
    arr = [10, 20, 30, 40, 50, 60, 70]

    print("Array:", arr)

    try:
        target = int(input("Enter element to search: "))

        result = binary_search(arr, target)

        if result != -1:
            print("Element found at index:", result)
        else:
            print("Element not found.")

    except ValueError:
        print("Please enter a valid integer.")


if __name__ == "__main__":
    main()
