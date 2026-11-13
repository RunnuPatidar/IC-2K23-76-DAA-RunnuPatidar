# Python implementation of Quick-Sort

def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[-1]

    smaller = [x for x in arr[:-1] if x <= pivot]
    greater = [x for x in arr[:-1] if x > pivot]

    return quick_sort(smaller) + [pivot] + quick_sort(greater)


numbers = [45, 23, 89, 12, 67, 34, 9, 56]

print("Original array:", numbers)
print("Sorted array:", quick_sort(numbers))
