# Python implementation of Algorithm-Performance-Analyzer

# Experiment 6: Algorithm Performance Analyzer

import time
import csv
import matplotlib.pyplot as plt


def linear_search(arr, target):
    for i, value in enumerate(arr):
        if value == target:
            return i
    return -1


def measure_performance():
    sizes = [1000, 2000, 5000, 10000, 20000, 50000]
    results = []

    print("\nALGORITHM PERFORMANCE ANALYZER")
    print("-" * 55)

    for n in sizes:
        arr = list(range(n))
        target = -1

        start = time.perf_counter()
        linear_search(arr, target)
        end = time.perf_counter()

        execution_time = end - start

        results.append((n, execution_time))

        print(
            f"Size: {n:6d} | "
            f"Time: {execution_time:.8f} seconds"
        )

    return results


def save_results(results):
    with open(
        "Unit01-Introduction-Algorithms/Algorithm-Performance-Analyzer/outputs/analysis.csv",
        "w",
        newline=""
    ) as file:

        writer = csv.writer(file)
        writer.writerow(["Input Size", "Execution Time"])
        writer.writerows(results)


def generate_graph(results):
    sizes = [item[0] for item in results]
    times = [item[1] for item in results]

    plt.plot(sizes, times, marker="o", label="Experimental")

    # Theoretical O(n) reference, normalized for comparison
    reference = [
        times[-1] * (n / sizes[-1])
        for n in sizes
    ]

    plt.plot(
        sizes,
        reference,
        linestyle="--",
        label="Theoretical O(n) reference"
    )

    plt.xlabel("Input Size (n)")
    plt.ylabel("Execution Time (seconds)")
    plt.title("Algorithm Performance Analyzer")
    plt.legend()
    plt.grid(True)

    plt.savefig(
        "Unit01-Introduction-Algorithms/Algorithm-Performance-Analyzer/outputs/analyzer_graph.png"
    )

    plt.show()


def main():
    results = measure_performance()

    save_results(results)
    generate_graph(results)

    print("\nTheoretical Complexity: O(n)")
    print("Space Complexity: O(n) including input array")
    print("Analysis saved successfully.")


if __name__ == "__main__":
    main()
