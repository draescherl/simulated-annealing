import json

from src.functions import simulated_annealing, visualise_path


with open('./15_vertices.json') as f:
    json_data = json.load(f)
    graph = json_data['graph']
    best_path = json_data['best_path_value']

best_path = simulated_annealing(graph)
visualise_path(graph, best_path)
