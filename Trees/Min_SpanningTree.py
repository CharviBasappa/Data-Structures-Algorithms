import heapq

def prim(graph, start):
    mst = []
    visited = set([start])
    edges = [(weight, start, to) for to, weight in graph[start]]
    heapq.heapify(edges)

    while edges:
        weight, frm, to = heapq.heappop(edges)
        if to not in visited:
            visited.add(to)
            mst.append((frm, to, weight))

            for to_next, weight_next in graph[to]:
                if to_next not in visited:
                    heapq.heappush(edges, (weight_next, to, to_next))

    return mst

# Example usage
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}

mst = prim(graph, 'A')
print("Minimum Spanning Tree:", mst)
