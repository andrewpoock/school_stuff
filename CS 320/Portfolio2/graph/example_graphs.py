# example_graphs

from listgraph import ListGraph as GraphImpl


def make_graph(verts, edges, directed=False):
    """Simple helper to build graph from sequence of vertices and
    a sequence of edge pairs, both described using labels.
    """
    g = GraphImpl(verts, directed)
    for v1, v2 in edges:
        g.add_label_edge(v1, v2)
    return g


# The graph from Figure 3.10 (and Figure 3.11)
verts = "abcdefghij"
edges = ["ac", "ad", "ae", "be", "bf", "cd", "cf", "ef",
         "gh", "gj", "hi", "ij"]
g310 = make_graph(verts, edges)


# The graph from section 3.5, exercise 1.
verts = "abcdefg"
edges = ["ab", "ac", "ad", "ae", "bd", "bf", "df", "cg", "eg"]
g351 = make_graph(verts, edges)

# graphs from section 3.5 exercise 8
verts = ["x1", "x2", "x3", "y1", "y2", "y3"]
edges = [("x1", "y1"), ("x1", "y2"),
         ("x2", "y1"), ("x2", "y2"), ("x2", "y3"),
         ("x3", "y3"), ("x3", "y1")
         ]
g358a = make_graph(verts, edges)
g358b = make_graph("abcd", ["ab", "ac", "bc", "bd", "cd"])
