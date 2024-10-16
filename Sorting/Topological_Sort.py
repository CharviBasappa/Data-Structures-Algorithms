from collections import defaultdict, deque

class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.vertices = vertices

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def topological_sort(self):
        in_degree = {i: 0 for i in range(self.vertices)}

        for u in self.graph:
            for v in self.graph[u]:
                in_degree[v] += 1

        queue = deque([i for i in in_degree if in_degree[i] == 0])
        top_order = []

        while queue:
            u = queue.popleft()
            top_order.append(u)

            for v in self.graph[u]:
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    queue.append(v)

        if len(top_order) == self.vertices:
            print("Topological Sort:", top_order)
        else:
            print("Graph has a cycle, topological sort not possible")

# Example usage
g = Graph(6)
g.add_edge(5, 2)
g.add_edge(5, 0)
g.add_edge(4, 0)
g.add_edge(4, 1)
g.add_edge(2, 3)
g.add_edge(3, 1)
g.topological_sort()
