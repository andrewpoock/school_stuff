# matrixgraph.py

from graph import Graph


class MatrixGraph(Graph):

    def __init__(self, labels, directed):
        super().__init__(labels, directed)
        self._matrix = [[None] * self.n_verts
                        for _ in range(self.n_verts)]

    def add_edge(self, v1, v2, weight=1):
        assert self._matrix[v1][v2] is None
        self._matrix[v1][v2] = weight
        if not self.directed:
            self._matrix[v2][v1] = weight
        self.n_edges += 1

    def edge(self, v1, v2):
        w = self._matrix[v1][v2]
        if w is None:
            return None
        return Graph.Edge(v1, v2, w)

    def edges(self, start=None):
        if start is not None:
            starts = [start]
        else:
            starts = self.verticies()
        for v1 in starts:
            for v2 in self.verticies():
                weight = self._matrix[v1][v2]
                if weight is not None:
                    yield Graph.Edge(v1, v2, weight)

    def delete_edge(self, v1, v2):
        if self._matrix[v1][v2] is not None:
            self.n_edges -= 1
        self._matrix[v1][v2] = None
        if not self.directed:
            self._matrix[v2][v1] = None
