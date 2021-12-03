import json
import numpy as np

from src.functions import simulated_annealing, visualise_path


with open('./inputs/15_vertices.json') as f:
    json_data = json.load(f)
    graph = np.triu(json_data['graph'])
    best_theoretical_path = json_data['best_path_value']

# Set third param to True if you want to generate the exploration GIF
output = simulated_annealing(graph, best_theoretical_path, True)
visualise_path(graph, *output)
