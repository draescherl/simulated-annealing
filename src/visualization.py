from typing import Any, Dict, List, Tuple
import networkx as nx
import matplotlib.pyplot as plt
import os
from numpy import void

from .utils import matrix_to_graph, edges_to_vertices


def get_edge_colours_and_widths(graph: nx.Graph, path: List[Tuple[int, int]]) -> Tuple[List[str], List[int]]:
    """
    Get properties for plotting the graph.

    When using networkx's graph visualisation tool it is possible to customize
    the colour and width of each edge of the graph. This function helps find 
    the values to highlight the path the algorithm is currently checking.

    Parameters:
    graph (networkx.Graph): Graph object we're working on.
    path (List[Tuple[int, int]]): List containing the edges of the current path.

    Returns:
    Tuple(List[str], List[int]): Tuple containing the list of colours (1st) and widths(2nd).
    """
    colours = []
    widths = []
    for edge in graph.edges():
        if edge in path or tuple(reversed(edge)) in path:
            colours.append('red')
            widths.append(2)
        else:
            colours.append('k')
            widths.append(1)
    return colours, widths


def visualise_path(base_graph, best_path, temperature, fitness, best_fitness) -> void:
    graph = matrix_to_graph(base_graph)
    colours, widths = get_edge_colours_and_widths(graph, best_path)
    title = f'T: {temperature}\n'
    title += f'Fitness: {fitness} -- Best: {best_fitness}'
    plt.title(title)
    nx.draw_circular(graph, edge_color=colours, width=widths, with_labels=True)
    plt.show()


def save_image(base_graph, best_path, name: str, temperature: float, current_fitness: int, best_fitness: int) -> void:
    G = matrix_to_graph(base_graph)
    colours, widths = get_edge_colours_and_widths(G, best_path)
    title = f'i: {name} -- T: {temperature}\n'
    title += f'Fitness: {current_fitness} -- Best: {best_fitness}'
    plt.title(title)
    nx.draw_circular(G, edge_color=colours, width=widths, with_labels=True)
    plt.savefig('./tmp/' + str(name) + '.jpeg')
    plt.clf()


def create_gif(graph: List[List[int]], paths: List[List[Tuple[str]]], frequence: int, best_fitness: int) -> void:
    os.system('mkdir tmp')
    for i in range(len(paths)):
        if i % frequence == 0:
            save_image(graph, paths[i]['path'], i, paths[i]['temperature'], paths[i]['value'], best_fitness)
    os.system('convert -delay 100 -loop 0 tmp/*.jpeg exploration.gif')
    os.system('rm -rf tmp/')


def handle_visualisation(show_final: bool, generate_gif: bool, output: Dict[str, Any]) -> void:
    path = edges_to_vertices(output['solution'])
    fitness = output['final_fitness']
    best = output['best_fitness']
    output_string = f'Computed path: {path}\nIts fitness: {fitness}\nBest possible fitness: {best}'
    print(output_string)
    if show_final:
        visualise_path(output['input'], output['solution'], output['final_temperature'], output['final_fitness'], output['best_fitness'])
    if generate_gif:
        create_gif(output['input'], output['paths'], 50, output['best_fitness'])