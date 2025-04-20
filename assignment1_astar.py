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

# A* Search
def astar(start, goal):
    open_set = []
    heapq.heappush(open_set, (0 + heuristic(start, goal), 0, start, [start]))
    visited = set()
    node_count = 0

    while open_set:
        f, g, current, path = heapq.heappop(open_set)
        node_count += 1

        if current == goal:
            return path, g, node_count

        if current in visited:
            continue
        visited.add(current)

        for neighbor in roads[current]:
            if neighbor not in visited:
                new_g = g + heuristic(current, neighbor)
                new_f = new_g + heuristic(neighbor, goal)
                heapq.heappush(open_set, (new_f, new_g, neighbor, path + [neighbor]))

    return None, float("inf"), node_count

# Eksekusi dan pengukuran waktu
start_city = "A"
goal_city = "D"
start_time = time.time()
path, cost, nodes = astar(start_city, goal_city)
end_time = time.time()
elapsed_time = (end_time - start_time) * 1000  # in milliseconds

# Output
print("A* Path:", path)
print("Total Cost:", cost)
print("Nodes Expanded:", nodes)
print("Time (ms):", elapsed_time)
