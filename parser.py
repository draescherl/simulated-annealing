import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import math

f = open('wi29.tsp', 'r')

lines = f.readlines()

break_index = lines.index('NODE_COORD_SECTION\n') + 1
lines = lines[break_index:-1]

posDict = {}
for i, line in enumerate(lines):
	pts = line.split(' ')[1:]
	posDict[i] = (float(pts[0]), float(pts[1]))


cost = []
for i in range(len(posDict)):
	cost.append([])
	for j in range(len(posDict)):
		cost[i].append(math.dist(posDict[i], posDict[j]))

print(cost)