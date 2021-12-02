import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import json

from functions import hamilton, simulated_annealing


with open('./15_vertices.json') as f:
    graph_as_json = json.load(f)['graph']
    G = nx.from_numpy_matrix(np.array(graph_as_json))


hamiltonian_cycle = hamilton(G)
edges = []
for i in range(len(hamiltonian_cycle) - 1):
    edges.append((hamiltonian_cycle[i], hamiltonian_cycle[i + 1]))

colours = []
for edge in G.edges():
    if edge in edges or tuple(reversed(edge)) in edges:
        colours.append('red')
    else:
        colours.append('k')

nx.draw_networkx(G, pos=nx.circular_layout(G), with_labels=True, edge_color=colours)
plt.show()
