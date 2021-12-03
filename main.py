import json
import numpy as np

from src.functions import simulated_annealing, visualise_path


with open('./inputs/15_vertices.json') as f:
    json_data = json.load(f)
    graph = np.triu(json_data['graph'])
    best_path = json_data['best_path_value']

best_path = simulated_annealing(graph, best_path)
visualise_path(graph, best_path)
