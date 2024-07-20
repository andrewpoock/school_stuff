# graph.py

class Graph:
    """ Super class for implementations of Graph
    A Graph uses ints 0--(n-1) to represent vertices, but also maintains
    data structures to "translate" between vertices and a set of labels.

    >>> g = Graph(['a', 'b', 'c'])
    >>> g.label[0]
    'a'
    >>> g.id['b']
    1

    This class should be subclassed to create a concrete implementation of
    graphs (e.g., with an adjacency matrix or an adjacency list).

    """

    class Edge:
        """ Edge is a record to supply edge information """

        def __init__(self, v1, v2, weight=1):
            self.v1 = v1
            self.v2 = v2
            self.weight = weight

        def __repr__(self):
            return f"Edge({self.v1}, {self.v2}, {self.weight})"

    def __init__(self, vertex_labels, directed=False):
        """Create empty graph from list of vertex labels (strings)

        """
        self.label = vertex_labels
        self.id = {label: id for id, label in enumerate(vertex_labels)}
        self.n_verts = len(vertex_labels)
        self.n_edges = 0
        self.directed = directed

    def verticies(self):
        """Return an iterator for label ids

        """
        return range(self.n_verts)

    def add_label_edge(self, label1, label2, weight=1):
        self.add_edge(self.id[label1], self.id[label2], weight)

    # below are methods to be implemented in a subclass

    def add_edge(self, v1, v2, weight=1):
        """Add the edge from v1 to v2 to the graph

        """
        raise NotImplementedError

    def edge(self, v1, v2):
        """Returns an Edge object if edge (v1, v2) is in graph, otherwise None
        Can be used as an existence test

        e = g.edge(v, v1)
        if e:
            # edge exists

        """
        raise NotImplementedError

    def edges(self, vertex=None):
        """Returns an iterator over Edge objects

        If vertex is None the iterator supplies all edges of the
        graph.  When vertex is supplied, it iterates over edges from
        that vertex (i.e., the adjacency list)

        """
        raise NotImplementedError

    def delete_edge(self, v1, v2):
        """Deletes the edge. Does nothing if the edge does not exist

        """
        raise NotImplementedError


# Example start of subclass (should be in matrixgraph.py)
class MatrixGraph(Graph):

    def __init__(self, labels, directed):
        super().__init__(labels, directed)
        # other initialization here
