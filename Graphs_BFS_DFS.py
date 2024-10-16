from collections import defaultdict, deque

class Graph:
    def __init__(self):
        # Initialize an empty adjacency list
        self.graph = defaultdict(list)

    # Function to add an edge to the graph
    def add_edge(self, u, v):
        self.graph[u].append(v)

    # BFS traversal from a given start node
    def bfs(self, start):
        visited = set()
        queue = deque([start])
        visited.add(start)
        print("BFS Traversal:", end=" ")
        
        while queue:
            vertex = queue.popleft()
            print(vertex, end=" ")
            
            for neighbor in self.graph[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        print()  # Newline after traversal

    # DFS traversal from a given start node (recursive)
    def dfs_recursive(self, vertex, visited):
        visited.add(vertex)
        print(vertex, end=" ")
        
        for neighbor in self.graph[vertex]:
            if neighbor not in visited:
                self.dfs_recursive(neighbor, visited)

    # Wrapper function for DFS traversal
    def dfs(self, start):
        visited = set()
        print("DFS Traversal:", end=" ")
        self.dfs_recursive(start, visited)
        print()  # Newline after traversal


# Example usage
if __name__ == "__main__":
    g = Graph()
    
    # Create a graph
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 3)

    # Perform BFS and DFS traversals
    print("Starting BFS and DFS from vertex 2:")
    g.bfs(2)
    g.dfs(2)



#BFS:- It starts at a given node and explores all neighbors at the present depth level before moving on to nodes at the next depth level.We use a queue (deque) to maintain the nodes to be visited and a set (visited) to track visited nodes.
#DFS:- It starts at a given node and explores as far as possible along each branch before backtracking.In this implementation, DFS is done recursively using a helper function dfs_recursive and a visited set to track visited nodes.