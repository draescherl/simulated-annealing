from random import random
import networkx as nx
import math


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


# The fitness function we use is the sum of the weights of the edges
def fitness(G):
    return


def metropolis(temperature, G_current, G_neighbour):
    return math.exp(-(abs(fitness(G_current) - fitness(G_neighbour))) / temperature)