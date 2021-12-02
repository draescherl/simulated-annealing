import random
import networkx as nx
import numpy as np


# Credit : https://gist.github.com/mikkelam/ab7966e7ab1c441f947b
def hamilton(G):
    F = [(G, [list(G.nodes())[0]])]
    n = G.number_of_nodes()
    while F:
        graph, path = F.pop()
        confs = []
        neighbors = (node for node in graph.neighbors(path[-1])
                     if node != path[-1])  # exclude self loops
        for neighbor in neighbors:
            conf_p = path[:]
            conf_p.append(neighbor)
            conf_g = nx.Graph(graph)
            conf_g.remove_node(path[-1])
            confs.append((conf_g, conf_p))
        for g, p in confs:
            if len(p) == n:
                return p
            else:
                F.append((g, p))
    return None


def rand():
    return random.random()


def generate_initial_solution(G):
    hamiltonian_cycle = hamilton(G)
    edges = [(hamiltonian_cycle[-1], hamiltonian_cycle[0])]

    for i in range(len(hamiltonian_cycle) - 1):
        edges.append((hamiltonian_cycle[i], hamiltonian_cycle[i + 1]))

    return edges


def arrays_to_nx_graphs(base_graph):
    return nx.from_numpy_matrix(np.array(base_graph))