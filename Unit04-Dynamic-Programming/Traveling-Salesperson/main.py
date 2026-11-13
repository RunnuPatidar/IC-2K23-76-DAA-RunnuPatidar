# Python implementation of Traveling-Salesperson

def tsp(graph):
    n = len(graph)
    start = 0

    # dp[mask][i] = minimum cost to reach city i
    # after visiting cities represented by mask
    size = 1 << n
    dp = [[float("inf")] * n for _ in range(size)]

    dp[1 << start][start] = 0

    for mask in range(size):
        for u in range(n):
            if not (mask & (1 << u)):
                continue

            if dp[mask][u] == float("inf"):
                continue

            for v in range(n):
                if not (mask & (1 << v)):
                    new_mask = mask | (1 << v)
                    new_cost = dp[mask][u] + graph[u][v]

                    dp[new_mask][v] = min(
                        dp[new_mask][v], new_cost
                    )

    full_mask = size - 1
    minimum_cost = float("inf")
    last_city = -1

    for city in range(n):
        tour_cost = dp[full_mask][city] + graph[city][start]

        if tour_cost < minimum_cost:
            minimum_cost = tour_cost
            last_city = city

    # Reconstruct the optimal tour
    path = [last_city]
    mask = full_mask
    current = last_city

    while current != start:
        previous = None

        for city in range(n):
            if city == current or not (mask & (1 << city)):
                continue

            previous_mask = mask ^ (1 << current)

            if dp[previous_mask][city] + graph[city][current] == dp[mask][current]:
                previous = city
                break

        if previous is None:
            raise ValueError("Unable to reconstruct tour.")

        path.append(previous)
        mask ^= (1 << current)
        current = previous

    path.reverse()
    path.append(start)

    return minimum_cost, path


graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

minimum_cost, path = tsp(graph)

print("Traveling Salesperson Problem")
print("Minimum Tour Cost:", minimum_cost)
print("Optimal Tour:", " -> ".join(map(str, path)))
