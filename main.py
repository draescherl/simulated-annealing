import json
import numpy as np
import sys

from src.functions import simulated_annealing, visualise_path
from src.cli import interpret_cli_args

with open('./inputs/15_vertices.json') as f:
    json_data = json.load(f)
    graph = np.triu(json_data['graph'])
    best_theoretical_path = json_data['best_path_value']

# Set third param to True if you want to generate the exploration GIF
# output = simulated_annealing(graph, best_theoretical_path, True)
# visualise_path(graph, *output)

if __name__ == "__main__":
    cli_args = interpret_cli_args(sys.argv)
    # TODO: create function to turn input file into a graph
    # TODO: create function to run the AI
    # TODO: create function to handle different visualisation methods