import sys
import networkx as nx
import numpy as np
import random

# G = nx.readedgelist()

with open(sys.argv[1], 'rb') as file:
    G = nx.read_adjlist(file, create_using=nx.DiGraph())


edges = G.edges()
print(edges)
