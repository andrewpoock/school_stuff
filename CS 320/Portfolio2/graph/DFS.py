# Depth First Search Algorithm
# Andrew Poock

class DFS:
    def __init__(self, graph):
        self.graph = graph
        self.entrycount = 0
        self.exitcount = 0
        self.entrymarks = [0]*self.graph.n_verts
        self.exitmarks = [0]*self.graph.n_verts

        """Perform search"""
        for v in self.graph.label:
            if self.entrymarks[self.graph.id[v]] == 0:
                self.dfs(v)

    def dfs(self, v):
        self.entrycount += 1
        self.entrymarks[self.graph.id[v]] = self.entrycount
        for w in self.graph.label:
            if self.graph.edge(self.graph.id[v], self.graph.id[w]):
                if self.entrymarks[self.graph.id[w]] == 0:
                    self.dfs(w)
        self.exitcount += 1
        self.exitmarks[self.graph.id[v]] = self.exitcount