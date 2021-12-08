import sys
import time
import math

from src.cli import interpret_cli_args
from src.utils import read_file
from src.solver import simulated_annealing
from src.visualization import handle_visualization


def get_coordinates():
	f = open('wi29.tsp', 'r')
	lines = f.readlines()
	break_index = lines.index('NODE_COORD_SECTION\n') + 1
	lines = lines[break_index:-1]
	posDict = {}
	for i, line in enumerate(lines):
		pts = line.split(' ')[1:]
		posDict[i] = (-float(pts[1]), float(pts[0]))
	return posDict

def get_cost(posDict):
	cost = []
	for i in range(len(posDict)):
		cost.append([])
		for j in range(len(posDict)):
			cost[i].append(math.dist(posDict[i], posDict[j]))
	return cost


if __name__ == "__main__":
    coordinates = get_coordinates()
    cost = get_cost(coordinates)
    cli_args = interpret_cli_args(sys.argv)
    graph, best_fitness = read_file(cli_args['filename'])
    start_time = time.time()
    i = 1
    output = simulated_annealing(cost, best_fitness)
    while output['final_fitness'] > 28500:
        output = simulated_annealing(cost, best_fitness)
        i += 1
    print(i)

    time_to_compute = time.time() - start_time
    handle_visualization(cli_args['show_result'], cli_args['generate_gif'], output, coordinates)
    print(f'\nSolution computed in {time_to_compute:.5f} seconds.')