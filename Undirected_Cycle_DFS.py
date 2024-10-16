from collections import defaultdict
class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.vertices = vertices

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def dfs(self, node, parent, visited):
        visited[node] = True
        for neighbor in self.graph[node]:
            if not visited[neighbor]:
                if self.dfs(neighbor, node, visited):
                    return True
            elif neighbor != parent:
                return True
        return False

    def detect_cycle(self):
        visited = [False] * self.vertices
        for vertex in range(self.vertices):
            if not visited[vertex]:
                if self.dfs(vertex, -1, visited):
                    return True
        return False

# Example usage
g = Graph(5)
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(3, 4)

if g.detect_cycle():
    print("Graph contains a cycle")
else:
    print("Graph doesn't contain a cycle")
