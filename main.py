import random
import math
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import json


with open('./15_vertices.json') as f:
  graph_as_json = json.load(f)['graph']
  original_graph = nx.from_numpy_matrix(np.array(graph_as_json))

nx.draw(original_graph)
plt.show()