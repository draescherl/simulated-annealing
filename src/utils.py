import random
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
from networkx.drawing.layout import shell_layout


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


def tuples_to_list(tuples):
    res = []

    for t in tuples:
        res.append(t[0])

    return res


def list_to_tuples(list):
    res = [(list[-1], list[0])]

    for i in range(len(list) - 1):
        res.append((list[i], list[i + 1]))

    return res


def generate_initial_solution(G):
    hamiltonian_cycle = hamilton(G)
    edges = list_to_tuples(hamiltonian_cycle)
    return edges


def arrays_to_nx_graphs(base_graph):
    return nx.from_numpy_matrix(np.array(base_graph))


def create_path_list(best_path, G):
    colours = []
    widths = []
    for edge in G.edges():
        if edge in best_path or tuple(reversed(edge)) in best_path:
            colours.append('red')
            widths.append(2)
        else:
            colours.append('k')
            widths.append(1)
    return colours, widths


def visualise_path(base_graph, best_path):
    G = nx.from_numpy_matrix(np.array(base_graph))
    colours, widths = create_path_list(best_path, G)
    nx.draw_networkx(G, pos=shell_layout(G), edge_color=colours, width=widths)
    plt.show()


def save_image(base_graph, best_path, name):
    G = nx.from_numpy_matrix(np.array(base_graph))
    colours, widths = create_path_list(best_path, G)
    nx.draw_networkx(G, pos=shell_layout(G), edge_color=colours, width=widths)
    plt.savefig('./tmp/' + name)
    plt.clf()