import random
import networkx as nx
from networkx.drawing.layout import shell_layout
import math
import numpy as np
import matplotlib.pyplot as plt

from .utils import generate_initial_solution, rand


# The fitness function we use is the sum of the weights of the edges
def fitness(G):
    return 0


def get_neighbouring_solution(current_solution):
    return current_solution


def metropolis(temperature, G_current, G_neighbour):
    return math.exp(-(abs(fitness(G_current) - fitness(G_neighbour))) / temperature)


def simulated_annealing(base_graph):
    temperature = random.randrange(150, 500, 1)
    maxit = 1000
    i = 0

    # Generate a random solution
    S = generate_initial_solution(base_graph)

    # Copy solution
    Ss = S

    while (i < maxit):
        N = get_neighbouring_solution(S)
        if fitness(N) < fitness(S) or rand() < metropolis(temperature, S, N):
            S = N
        else:
            Ss = S

        temperature *= 0.99
        i += 1

    return Ss


def visualise_path(base_graph, best_path):
    G = nx.from_numpy_matrix(np.array(base_graph))

    colours = []
    for edge in G.edges():
        if edge in best_path or tuple(reversed(edge)) in best_path:
            colours.append('red')
        else:
            colours.append('k')

    nx.draw_networkx(G, pos=shell_layout(G), arrows=True, edge_color=colours)
    plt.show()
