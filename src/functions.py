import random
import math
import os

from .utils import *


# The fitness function we use is the sum of the weights of the edges
def fitness(graph, current_solution):
    res = 0
    for edge in current_solution:
        res += graph.get_edge_data(*edge)['weight']
    return res


def get_neighbouring_solution(current_solution):
    list_of_vertices = tuples_to_list(current_solution)
    idx = range(len(list_of_vertices))
    i1, i2 = random.sample(idx, 2)
    list_of_vertices[i1], list_of_vertices[i2] = list_of_vertices[i2], list_of_vertices[i1]
    return list_to_tuples(list_of_vertices)


def metropolis(temperature, G, current_solution, neighbouring_solution):
    return math.exp(-(abs(fitness(G, current_solution) - fitness(G, neighbouring_solution))) / temperature)


def simulated_annealing(base_graph, best_theoretical_value, generate_gif):
    temperature = random.randrange(150, 500, 1)
    print('Initial temperature: ' + str(temperature))
    maxit = 1000
    i = 0

    # Convert the array to a Graph object
    G = arrays_to_nx_graphs(base_graph)

    # Generate a random solution
    S = generate_initial_solution(G)

    # Copy solution
    Ss = S
    path_value = fitness(G, Ss)

    if generate_gif: os.system('mkdir tmp')
    while path_value > best_theoretical_value and i < maxit:
        N = get_neighbouring_solution(S)

        if fitness(G, N) < fitness(G, S) or rand() < metropolis(temperature, G, S, N):
            S = N
        else:
            Ss = S

        path_value = fitness(G, Ss)
        if generate_gif and i % 100 == 0:
            save_image(base_graph, Ss, i, temperature, path_value, best_theoretical_value)

        temperature *= 0.99
        i += 1
    if generate_gif:
        os.system('convert -delay 100 -loop 0 tmp/*.jpeg exploration.gif')
        os.system('rm -rf tmp/')

    print('Final temperature: ' + str(temperature))
    print('Final fitness value: ' + str(path_value))
    diff = path_value - best_theoretical_value
    print('Difference with best theoretical path: ' + str(diff))
    print('Path:', end=' ')
    print(tuples_to_list(Ss))
    return Ss, temperature, path_value, best_theoretical_value
