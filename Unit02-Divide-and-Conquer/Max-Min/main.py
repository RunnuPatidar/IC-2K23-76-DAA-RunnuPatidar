# Python implementation of Max-Min

def find_max_min(arr, low, high):
    # Only one element
    if low == high:
        return arr[low], arr[low]

    # Two elements
    if high == low + 1:
        if arr[low] > arr[high]:
            return arr[low], arr[high]
        return arr[high], arr[low]

    # Divide the array into two halves
    mid = (low + high) // 2

    left_max, left_min = find_max_min(arr, low, mid)
    right_max, right_min = find_max_min(arr, mid + 1, high)

    # Combine the results
    return max(left_max, right_max), min(left_min, right_min)


numbers = [45, 12, 89, 34, 7, 66, 23, 91, 5]

maximum, minimum = find_max_min(numbers, 0, len(numbers) - 1)

print("Array:", numbers)
print("Maximum element:", maximum)
print("Minimum element:", minimum)
