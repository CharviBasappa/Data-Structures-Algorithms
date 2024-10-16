import heapq

def dijkstra(graph, start):
    distance = {node: float('inf') for node in graph}
    distance[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distance[current_node]:
            continue

        for neighbor, weight in graph[current_node]:
            distance_through_u = current_distance + weight
            if distance_through_u < distance[neighbor]:
                distance[neighbor] = distance_through_u
                heapq.heappush(priority_queue, (distance_through_u, neighbor))

    return distance

# Example usage
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}
print("Shortest distances from A:", dijkstra(graph, 'A'))
