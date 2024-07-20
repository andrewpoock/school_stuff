# listgraph.py
# Adjacency List implementation of graphs
# Andrew Poock

from graph import Graph


class ListGraph(Graph):
    
    def __init__(self, labels, directed):
        super().__init__(labels, directed)
        self._adjlist = {v: [] for v in range(self.n_verts)}

    def add_edge(self, v1, v2, weight=1):
        assert v2 not in self._adjlist[v1]
        self._adjlist[v1].append((v2, weight))
        if not self.directed:
            self._adjlist[v2].append((v1, weight))
        self.n_edges += 1
    
    def edge(self, v1, v2):
        for v, w in self._adjlist[v1]:
            if v == v2:
                return Graph.Edge(v1, v2, w)
        return None

    def edges(self, start=None):
        if start is not None:
            starts = [start]
        else:
            starts = self.verticies()
        for v1 in starts:
            for v2, weight in self._adjlist.get(v1, []):
                yield Graph.Edge(v1, v2, weight)

    def delete_edge(self, v1, v2):
        self._adjlist[v1] = [(v, w) for v, w in self._adjlist[v1] if v != v2]
        if not self.directed:
            self._adjlist[v2] = [(v, w) for v, w in self._adjlist[v2] if v != v1]
        self.n_edges -= 1