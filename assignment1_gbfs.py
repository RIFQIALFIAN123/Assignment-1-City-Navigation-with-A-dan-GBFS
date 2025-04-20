import heapq
import time
from math import sqrt

# Data kota dan jalan
cities = {
    "A": (0, 0),
    "B": (2, 1),
    "C": (4, 2),
    "D": (5, 5),
    "E": (1, 4)
}

roads = {
    "A": ["B", "E"],
    "B": ["A", "C"],
    "C": ["B", "D"],
    "D": ["C"],
    "E": ["A", "D"]
}

# Heuristik Euclidean
def heuristic(a, b):
    (x1, y1) = cities[a]
    (x2, y2) = cities[b]
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# GBFS Function
def gbfs(start, goal):
    open_set = []
    heapq.heappush(open_set, (heuristic(start, goal), start, [start]))
    visited = set()
    node_count = 0

    while open_set:
        _, current, path = heapq.heappop(open_set)
        node_count += 1

        if current == goal:
            return path, node_count

        if current in visited:
            continue
        visited.add(current)

        for neighbor in roads[current]:
            if neighbor not in visited:
                heapq.heappush(open_set, (heuristic(neighbor, goal), neighbor, path + [neighbor]))

    return None, node_count

# Eksekusi dan pengukuran waktu
start_city = "A"
goal_city = "D"
start_time = time.time()
path, nodes = gbfs(start_city, goal_city)
end_time = time.time()
elapsed_time = (end_time - start_time) * 1000  # in milliseconds

# Output
print("GBFS Path:", path)
print("Nodes Expanded:", nodes)
print("Time (ms):", elapsed_time)
