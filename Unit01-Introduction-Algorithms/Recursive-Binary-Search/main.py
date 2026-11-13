# Python implementation of Recursive-Binary-Search

# Experiment 3: Recursive Binary Search

def binary_search(arr, low, high, target):

    if low > high:
        return -1

    mid = (low + high) // 2

    if arr[mid] == target:
        return mid

    elif arr[mid] < target:
        return binary_search(arr, mid + 1, high, target)

    else:
        return binary_search(arr, low, mid - 1, target)


def main():
    arr = [10, 20, 30, 40, 50, 60, 70]

    print("Array:", arr)

    try:
        target = int(input("Enter element to search: "))

        result = binary_search(arr, 0, len(arr) - 1, target)

        if result != -1:
            print("Element found at index:", result)
        else:
            print("Element not found.")

    except ValueError:
        print("Please enter a valid integer.")


if __name__ == "__main__":
    main()
