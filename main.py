import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import json

from functions import hamilton, simulated_annealing


with open('./15_vertices.json') as f:
	json_data = json.load(f)
	graph = json_data['graph']
	best_path = json_data['best_path_value']
	G = nx.from_numpy_matrix(np.array(graph))


hamiltonian_cycle = hamilton(G)
edges = [(hamiltonian_cycle[-1], hamiltonian_cycle[0])]
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
