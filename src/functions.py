import random
import networkx as nx
from networkx.drawing.layout import shell_layout
import math
import numpy as np
import matplotlib.pyplot as plt

from .utils import arrays_to_nx_graphs, generate_initial_solution, rand


# The fitness function we use is the sum of the weights of the edges
def fitness(graph, current_solution):
    res = 0
    for edge in current_solution:
        res += graph.get_edge_data(*edge)['weight']    
    return res


def get_neighbouring_solution(current_solution):
    return current_solution


def metropolis(temperature, G, current_solution, neighbouring_solution):
    return math.exp(-(abs(fitness(G, current_solution) - fitness(G, neighbouring_solution))) / temperature)


def simulated_annealing(base_graph):
    temperature = random.randrange(150, 500, 1)
    maxit = 1000
    i = 0

    # Convert the array to a Graph object
    G = arrays_to_nx_graphs(base_graph)

    # Generate a random solution
    S = generate_initial_solution(G)

    # Copy solution
    Ss = S

    while (i < maxit):
        N = get_neighbouring_solution(S)
        if fitness(G, N) < fitness(G, S) or rand() < metropolis(temperature, G, S, N):
            S = N
        else:
            Ss = S

        temperature *= 0.99
        i += 1

    print('Final fitness value: ' + str(fitness(G, Ss)))
    return Ss


def visualise_path(base_graph, best_path):
    G = nx.from_numpy_matrix(np.array(base_graph))

    colours = []
    for edge in G.edges():
        if edge in best_path or tuple(reversed(edge)) in best_path:
            colours.append('red')
        else:
            colours.append('k')

    nx.draw_networkx(G, pos=shell_layout(G), edge_color=colours)
    plt.show()
