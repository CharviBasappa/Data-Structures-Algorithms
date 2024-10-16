from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.vertices = vertices

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def dfs(self, node, visited, rec_stack):
        visited[node] = True
        rec_stack[node] = True

        for neighbor in self.graph[node]:
            if not visited[neighbor]:
                if self.dfs(neighbor, visited, rec_stack):
                    return True
            elif rec_stack[neighbor]:
                return True

        rec_stack[node] = False
        return False

    def detect_cycle(self):
        visited = [False] * self.vertices
        rec_stack = [False] * self.vertices

        for node in range(self.vertices):
            if not visited[node]:
                if self.dfs(node, visited, rec_stack):
                    return True
        return False

# Example usage
g = Graph(4)
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)

if g.detect_cycle():
    print("Graph contains a cycle")
else:
    print("Graph doesn't contain a cycle")
