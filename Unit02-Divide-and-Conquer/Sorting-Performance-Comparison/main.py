# Python implementation of Sorting-Performance-Comparison

import random
import time
import csv
from pathlib import Path
import matplotlib.pyplot as plt


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[-1]
    left = [x for x in arr[:-1] if x <= pivot]
    right = [x for x in arr[:-1] if x > pivot]

    return quick_sort(left) + [pivot] + quick_sort(right)


def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heap_sort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)

    return arr


def measure_time(function, data):
    start = time.perf_counter()
    function(data.copy())
    end = time.perf_counter()
    return end - start


def main():
    sizes = [100, 500, 1000, 2000, 3000]

    results = {
        "Merge Sort": [],
        "Quick Sort": [],
        "Heap Sort": []
    }

    print("Sorting Performance Comparison")
    print("-" * 55)
    print(f"{'Size':<10}{'Merge Sort':<15}{'Quick Sort':<15}{'Heap Sort':<15}")

    for size in sizes:
        data = random.sample(range(size * 10), size)

        merge_time = measure_time(merge_sort, data)
        quick_time = measure_time(quick_sort, data)
        heap_time = measure_time(heap_sort, data)

        results["Merge Sort"].append(merge_time)
        results["Quick Sort"].append(quick_time)
        results["Heap Sort"].append(heap_time)

        print(
            f"{size:<10}{merge_time:<15.6f}"
            f"{quick_time:<15.6f}{heap_time:<15.6f}"
        )

    output_dir = Path(__file__).parent / "outputs"
    output_dir.mkdir(exist_ok=True)

    csv_path = output_dir / "sorting_results.csv"

    with open(csv_path, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            "Input Size", "Merge Sort",
            "Quick Sort", "Heap Sort"
        ])

        for i, size in enumerate(sizes):
            writer.writerow([
                size,
                results["Merge Sort"][i],
                results["Quick Sort"][i],
                results["Heap Sort"][i]
            ])

    plt.figure(figsize=(9, 5))

    for name, times in results.items():
        plt.plot(sizes, times, marker="o", label=name)

    plt.xlabel("Input Size")
    plt.ylabel("Execution Time (seconds)")
    plt.title("Sorting Algorithm Performance Comparison")
    plt.legend()
    plt.grid(True)

    plt.savefig(output_dir / "sorting_comparison.png")
    plt.show()

    print("\nCSV saved:", csv_path)
    print("Graph saved:", output_dir / "sorting_comparison.png")


if __name__ == "__main__":
    main()
