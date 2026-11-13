# Python implementation of TSP-Branch-and-Bound
# Travelling Salesperson Problem using Branch and Bound

graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

n = len(graph)
start = 0

minimum_cost = float("inf")
best_path = []


def calculate_bound(current, unvisited, cost):
    if not unvisited:
        return cost + graph[current][start]

    # Minimum outgoing edge from current city
    lower_bound = cost + min(
        graph[current][city] for city in unvisited
    )

    # Minimum possible outgoing edge for each unvisited city
    for city in unvisited:
        possible_next = [
            graph[city][other]
            for other in unvisited + [start]
            if other != city
        ]

        lower_bound += min(possible_next)

    return lower_bound


def tsp(current, unvisited, path, cost):
    global minimum_cost, best_path

    if not unvisited:
        total_cost = cost + graph[current][start]

        if total_cost < minimum_cost:
            minimum_cost = total_cost
            best_path = path + [start]

        return

    bound = calculate_bound(current, unvisited, cost)

    if bound >= minimum_cost:
        return

    for city in unvisited:
        new_unvisited = [
            item for item in unvisited if item != city
        ]

        tsp(
            city,
            new_unvisited,
            path + [city],
            cost + graph[current][city]
        )


tsp(start, list(range(1, n)), [start], 0)

print("Optimal Tour:", " -> ".join(map(str, best_path)))
print("Minimum Tour Cost:", minimum_cost)