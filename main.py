import json
import numpy as np

from src.functions import simulated_annealing, visualise_path


with open('./inputs/15_vertices.json') as f:
    json_data = json.load(f)
    graph = np.triu(json_data['graph'])
    best_theoretical_path = json_data['best_path_value']

# Set third param to True if you want to generate the exploration GIF
best_path = simulated_annealing(graph, best_theoretical_path, False)
visualise_path(graph, best_path)
