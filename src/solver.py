import random
import math
from typing import Any, Dict, List, Tuple
import networkx as nx

from .utils import edges_to_vertices, vertices_to_edges, generate_initial_solution, matrix_to_graph


# The fitness function we use is the sum of the weights of the edges
def fitness(graph: nx.Graph, current_solution: List[Tuple[str, str]]) -> int:
    res = 0
    for edge in current_solution:
        res += graph.get_edge_data(*edge)['weight']
    return res


def get_neighbouring_solution(current_solution):
    vertices = edges_to_vertices(current_solution)
    idx = range(len(vertices))
    i1, i2 = random.sample(idx, 2)
    vertices[i1], vertices[i2] = vertices[i2], vertices[i1]
    return vertices_to_edges(vertices)


def metropolis(t: int, graph: nx.Graph, current_solution: List[Tuple[str, str]], neighbouring_solution: List[Tuple[str, str]]) -> float:
    return math.exp(-(abs(fitness(graph, current_solution) - fitness(graph, neighbouring_solution))) / t)


def simulated_annealing(base_graph, best_fitness: int) -> Dict[str, Any]:
    initial_temperature = temperature = random.randrange(150, 500, 1)
    maxit = 10000
    i = 0

    # Convert the array to a Graph object
    G = matrix_to_graph(base_graph)

    # Generate a random solution
    S = Ss = generate_initial_solution(G)
    path_value = fitness(G, Ss)
    paths = []

    while path_value > best_fitness and i < maxit:
        N = get_neighbouring_solution(S)

        if fitness(G, N) < fitness(G, S) or random.random() < metropolis(temperature, G, S, N):
            S = N
        else:
            Ss = S

        path_value = fitness(G, Ss)
        data = {
            'path': S,
            'value': path_value,
            'temperature': temperature
        }
        paths.append(data)
        temperature *= 0.99996
        i += 1

    return {
        'input': base_graph,
        'solution': Ss,
        'final_temperature': temperature,
        'final_fitness': path_value,
        'best_fitness': best_fitness,
        'initial_temperature': initial_temperature,
        'paths': paths
    }
