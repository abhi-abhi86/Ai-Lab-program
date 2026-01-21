from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)
    
    def add_edge(self, u, v):
        self.graph[u].append(v)
    
    # Depth Limited Search
    def DLS(self, src, target, max_depth):
        if src == target:
            return True
        if max_depth <= 0:
            return False
        
        for i in self.graph[src]:
            if self.DLS(i, target, max_depth - 1):
                return True
        return False
    
    # Iterative Deepening DFS
    def IDDFS(self, src, target, max_depth):
        for i in range(max_depth):
            if self.DLS(src, target, i):
                return True
        return False

# Usage
g = Graph(7)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(1, 4)
g.add_edge(2, 5)
g.add_edge(2, 6)

target = 6
max_depth = 3
src = 0

if g.IDDFS(src, target, max_depth):
    print(f"Target is reachable from source within max depth {max_depth}")
else:
    print(f"Target is NOT reachable from source within max depth {max_depth}")