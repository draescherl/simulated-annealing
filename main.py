import sys

from src.cli import interpret_cli_args
from src.utils import read_file
from src.solver import simulated_annealing
from src.visualization import handle_visualization

if __name__ == "__main__":
    cli_args = interpret_cli_args(sys.argv)
    graph, best_fitness = read_file(cli_args['filename'])
    output = simulated_annealing(graph, best_fitness)
    handle_visualization(cli_args['show_result'], cli_args['generate_gif'], output)