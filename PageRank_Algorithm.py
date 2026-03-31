import sys
import networkx as nx
import numpy as np
import random

# We set the damping factor to 0.15
m = 0.15
def Random_Surfer(G):
	cn = random.choice(list(G.nodes))
	for n in G.nodes:
	# We start every node with the number of times visited as being 0
		G.nodes[n]['visited'] = 0
	# Do 100 iterations
	for i in range(100):
		# select the probability as a number from [0,1)
		prb = random.uniform(0, 1)

		# Because the damping factor m is greated or equal to the probability OR
		# there are no edges to follow.
		# In this case, it needs to jump to a random node.
		if prb <= m or not G.edges(cn):
			cn = random.choice(list(G.nodes))
			G.nodes[cn]['visited'] += 1
		# Probablility is smaller than m, this means that it needs to pick a
		# random edge and follow it.
		else:
			pair = random.choice(list(G.edges(cn)))
			cn = pair[1]
			G.nodes[cn]['visited'] += 1
	# Put all the nodes with the the number of times they have been visited in a
	# list as pairs
	list10 = [(i, G.nodes[i]['visited']) for i in G.nodes]
	# Sort that list after the number of visitations
	list10.sort(key = lambda item: item[1], reverse = True)

	print('Top 10 visited nodes are: ',list10[:10])
	print()


def PageRank(G):
	# Initialize A
	A = []
	# Sort the nodes
	sorted_nodes = sorted(list(G.nodes))
	# Make the connections between the nodes
	for element in sorted_nodes:
		G.nodes[element]['links'] = len(G.edges(element))
	# Making the incoming links (backlinks).
	for x in sorted_nodes:
		incoming = []
		for edge in list(G.edges):
			if edge[1] == x:
				incoming.append(edge[0])

		G.nodes[x]['backlinks'] = incoming

	# Making A, A will be created one row at a time and then we will append each
	# row as it is done. For each node we will make the appropriate row then
	# append it to A
	for x in sorted_nodes:
		row = []
		# Making the row for node x in A
		for element in sorted_nodes:
			if element in G.nodes[x]['backlinks']:
				row.append((1.0 - m) / float(G.nodes[element]['links']))
			else:
				row.append(0.0)
		A.append(row)
	# Computing the transpose of A
	A_T = [[A[c][row] for c in range(len(A))] for row in range(len(A[0]))]
	# Create an empty row to be able to compare the transpose with something in
	# case we have a dangling node (dangling nodes always have a row full of
	# zeros)
	empty_row = [0.0 for i in range(len(A[0]))]
	# Initialize the list that will hold all dangling nodes
	dangling_nodes = []
	# Make dangling nodes
	row = 0
	for x in sorted_nodes:
	# If the row for node x is full of zeroes it means that it is a dangling node
	# and we need to append it to the appropriate list, then we mode to the other
	# row
	#Always know at what node we are because they are sorted
		if A_T[row] == empty_row:
			dangling_nodes.append(x)
		row += 1
	# Calculating m*S*x, for this we need to initialize S first
	x3 = m / len(G.nodes)
	# Initialize x which is a dictionary holding every node and it's score
	x = {n : 1.0 / float(len(sorted_nodes)) for n in sorted_nodes}
	# Loop that goes over the nodes and calculates the scores for every one of them
	for i in range(100):
		# Calculate x2 - (1 - m)*D*x
		x2 = 0.0
		for d in dangling_nodes:
			x2 += (1-m)*x[d]/float(len(sorted_nodes))
		# Calculate x1 - (1 - m)*A*x
		x1 = list(np.matmul(A, list(x.values())))
		# Find next x -- x1 + x2 + x3 <=> (1 - m)*A*x + (1 - m)*D*x + mSx
		count = 0
		for n in sorted_nodes:
			x[n] = x1[count] + x2 + x3
			count += 1
		total = sum(list(x.values()))
		x = {n : x[n] / total for n in x}
	# Make the top 10 best ranking nodes and display them
	list10_PR = [(n, x[n]) for n in x]
	list10_PR.sort(key = lambda item: item[1], reverse = True)
	# If the there are more than 10 nodes we know that we need to only display
	# 10 of them and that is what we are doing
	if len(G.nodes) > 10:
		list10_PR = list10_PR[:10]

	for n in list10_PR:
		print('Node:', n[0], 'Score:', n[1])

		print()
# First reading the argument from the console and then calling the two functions
with open(sys.argv[1], 'rb') as file:
	G = nx.read_adjlist(file, create_using=nx.DiGraph())
# Here we call the functions for Random Surfer and PageRank
Random_Surfer(G)
PageRank(G)
