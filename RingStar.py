#!/usr/bin/env python

'''
Created on 16 Oct 2015
@author: Alexander Fletcher, Jacob Scott, Sudhir Manickavel

Usage: python moran.py r k
'''
import random
import sys
import networkx as nx
import matplotlib.pyplot as plt

# Parse input arguments
r = float(sys.argv[1]) #mutant fitness
k = int(sys.argv[2]) #node to be replaced
#grid = int(sys.argv[3]) #number of nodes
#ring-star
#list_of_edges = ([(0,1),(1,2),(2,3),(3,4),(4,5),(5,9),(5,10),(5,11),(5,12),(5,13),(5,14),(5,6),(6,7),(7,8),(8,0)])

# Probably need to work out how to specify a random seed
seed = None


#The periodic lattice verticies are numbered by a single integer, so the second line converts the verticies labels into a single integer
#G = nx.grid_2d_graph(grid,grid, periodic = True) #periodic lattice 
#G = nx.convert_node_labels_to_integers(G, first_label=0, ordering = 'default') 
#n = nx.number_of_nodes(G)
#G = nx.star_graph(grid) #star graph function
#G = nx.cycle_graph(grid) #ring graph function
G = nx.Graph() #//for normal graph function
G.add_edges_from(list_of_edges) #//for normal graph function 
n = nx.number_of_nodes(G) #size of network 
pos = nx.spring_layout(G) #for drawing

# Define a vector storing which nodes are normal ("1") and mutant ("2")
# (note that a more concise way of doing this may be to asssign the
# state "1" or "2" directly to each node in the graph G)
nodes = [1]*n
random_index = random.randrange(0, n)
nodes[k] = 2 #b is the node to replace
num_mutants = nodes.count(2)

# Main time loop
time_step = 0
while ((num_mutants != 0) and (num_mutants != n)):

	# Note that the following code will need to be modified
	# to allow for the inclusion of frequency-dependent fitness

	# Choose a random node to be replaced by a neighbour's daughter
	chosen_index = random.randrange(0, n)
	# Iterate over all neighbours and compute the normalised
	# relative fitness of mutant neighbours
	normal_fitness = 0.0;
	mutant_fitness = 0.0;

	for neighbour_index in G[chosen_index]:
		if nodes[neighbour_index] == 1:
			normal_fitness += 1.0;
		else:
			mutant_fitness += r;

	normalised_mutant_fitness = mutant_fitness/(normal_fitness + mutant_fitness)
	#print normalised_mutant_fitness


	# Generate a uniform random number, u, from [0.0, 1.0)
	u = random.random()

	# If the random number is less than the normalised relative
	# fitness of mutant neighbours, then the chosen node will
	# become/stay mutant; otherwise, it will become/stay normal
	if u < normalised_mutant_fitness:
		nodes[chosen_index] = 2
	else:
		nodes[chosen_index] = 1

	# Update the mutant node count
	num_mutants = nodes.count(2)

	

	# Uncomment the following 8 lines to draw the graph at each time step.
	# The script make_a_movie.sh can then be run to generate an mpeg.
	'''
	normals = list([i for i, x in enumerate(nodes) if x == 1])
	mutants = list([i for i, x in enumerate(nodes) if x == 2])
	nx.draw_networkx_edges(G, pos, width=1.0)
	nx.draw_networkx_nodes(G, pos, nodelist=normals, node_color='g', node_size=500)
	nx.draw_networkx_nodes(G, pos, nodelist=mutants, node_color='r', node_size=500)
	plt.axis('off')
	plt.savefig("lattice" + str(time_step) + ".png")
	plt.clf()
	'''

	# Increment time
	time_step += 1
	#print time_step, "  ", num_mutants
print time_step, " , ", num_mutants
