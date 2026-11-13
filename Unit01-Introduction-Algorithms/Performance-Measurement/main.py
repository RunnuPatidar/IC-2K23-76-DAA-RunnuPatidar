# Python implementation of Performance-Measurement

# Experiment 5: Performance Measurement

import time
import csv
import matplotlib.pyplot as plt


def linear_search(arr, target):
    for i, value in enumerate(arr):
        if value == target:
            return i
    return -1


def main():
    sizes = [1000, 2000, 5000, 10000, 20000, 50000]
    results = []

    for n in sizes:
        arr = list(range(n))

        # Worst-case search: target is not present
        target = -1

        start = time.perf_counter()

        for _ in range(10):
            linear_search(arr, target)

        end = time.perf_counter()

        avg_time = (end - start) / 10

        results.append((n, avg_time))

        print(f"Input Size: {n}, Time: {avg_time:.8f} seconds")

    # Save experimental results
    with open("Unit01-Introduction-Algorithms/Performance-Measurement/outputs/results.csv",
              "w", newline="") as file:

        writer = csv.writer(file)
        writer.writerow(["Input Size", "Execution Time"])
        writer.writerows(results)

    # Generate graph
    sizes = [row[0] for row in results]
    times = [row[1] for row in results]

    plt.plot(sizes, times, marker="o")
    plt.xlabel("Input Size (n)")
    plt.ylabel("Execution Time (seconds)")
    plt.title("Linear Search Performance Analysis")
    plt.grid(True)

    plt.savefig(
        "Unit01-Introduction-Algorithms/Performance-Measurement/outputs/performance_graph.png"
    )

    plt.show()

    print("\nResults saved successfully.")
    print("Performance graph generated.")


if __name__ == "__main__":
    main()
