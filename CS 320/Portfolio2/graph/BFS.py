# Breadth First Search Algorithm
# Andrew Poock

from collections import deque

class BFS():
    def __init__(self, graph):
        self.graph = graph
        self.count = 0
        self.marks = [0]*self.graph.n_verts

        """Perform Search"""
        for v in self.graph.label:
            if self.marks[self.graph.id[v]] == 0:
                self.bfs(v)

    def bfs(self, v):
        self.count += 1
        self.marks[self.graph.id[v]] = self.count
        queue = deque([v])
        while queue:
            current = queue.popleft()
            for w in self.graph.label:
                if self.graph.edge(self.graph.id[current], self.graph.id[w]):
                    if self.marks[self.graph.id[w]] == 0:
                        self.count += 1
                        self.marks[self.graph.id[w]] = self.count
                        queue.append(w)