import networkx as nx

from .network import Component


components = [
    Component(
        cc=40,
        cp=15,
        alpha=35,
        beta=2.1,
        capacity=20,
        service_time=2.4
    ),
    Component(50, 35, 46, 1.9, 15, 2.7),
    Component(27, 15, 45, 2.1, 9, 3.5),
    Component(46, 22, 55, 1.4, 11, 3.3),
    Component(29, 15, 34, 2.5, 7, 2.05),
    Component(31, 21, 55, 1.9, 8, 1.64),
    Component(55, 26, 61, 1.6, 15, 2.27),
    Component(61, 27, 58, 2.2, 21, 2.87),
    Component(45, 18, 36, 2.4, 10, 3.74),
    Component(50, 17, 39, 2.0, 9, 3.18),
]

structure = nx.DiGraph()
# Add source and sink nodes
structure.add_nodes_from(["s", "t"])
structure.add_nodes_from(components)
structure.add_edges_from([
    ("s", components[0]),
    ("s", components[1]),
    (components[0], components[2]),
    (components[0], components[3]),
    (components[1], components[4]),
    (components[1], components[5]),
    (components[2], components[6]),
    (components[3], components[6]),
    (components[3], components[7]),
    (components[4], components[7]),
    (components[5], components[7]),
    (components[6], "t"),
    (components[7], components[8]),
    (components[7], components[9]),
    (components[8], "t"),
    (components[9], "t"),
])
