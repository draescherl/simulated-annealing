from typing import List, Tuple
import networkx as nx
import numpy as np
import json


# Credit : https://gist.github.com/mikkelam/ab7966e7ab1c441f947b
def hamilton(graph):
    F = [(graph, [list(graph.nodes())[0]])]
    n = graph.number_of_nodes()
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


def edges_to_vertices(edges: List[Tuple[str]]) -> List[str]:
    vertices = []
    for edge in edges:
        vertices.append(edge[0])
    return vertices


def vertices_to_edges(vertices: List[str]) -> List[Tuple[str]]:
    res = [(vertices[-1], vertices[0])]
    for i in range(len(vertices) - 1):
        res.append((vertices[i], vertices[i + 1]))
    return res


def generate_initial_solution(graph: nx.Graph) -> List[Tuple[str]]:
    hamiltonian_cycle = hamilton(graph)
    return vertices_to_edges(hamiltonian_cycle)


def matrix_to_graph(matrix: List[List[int]]) -> nx.Graph:
    return nx.from_numpy_matrix(np.array(matrix))


def read_file(filename: str) -> Tuple[List[List[int]], int]:
    actual_filename = './inputs/default.json' if filename == '' else filename
    with open(actual_filename) as f:
        json_data = json.load(f)
        graph = np.triu(json_data['graph'])
        best_fitness = json_data['best_path_value']
    return graph, best_fitness