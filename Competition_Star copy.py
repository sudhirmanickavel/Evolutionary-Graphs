import random
import sys
import networkx as nx
import matplotlib.pyplot as plt
r = float(sys.argv[1]) #mutant fitness
k = int(sys.argv[2]) #node to be replaced
grid_1 = int(sys.argv[3]) #number of nodes
grid_2 = int(sys.argv[4])
#ring-star
#list_of_edges = ([(0,1),(1,2),(2,3),(3,4),(4,5),(5,9),(5,10),(5,11),(5,12),(5,13),(5,14),(5,6),(6,7),(7,8),(8,0)])

# Probably need to work out how to specify a random seed
seed = None
G = nx.star_graph(grid_1)
#G = nx.Graph()
#list_of_edges = ([(0,3), (1,3), (2,3), (4,3), (5,3), (5,6), (6,5), (6,10), (7,10), (8,10), (9,10), (11,10)])

#Loop that makes the second star graph and creates edges to connect the two star graphs
list_of_edges = []
h = grid_1
f = 1
time_step = grid_1 
if(h == grid_1):
	while (time_step <= grid_1+grid_2):
		list_of_edges.append((h+1,h+f))
		f += 1
		time_step += 1
		print (list_of_edges)
list_of_edges.append((grid_1,(grid_1+grid_2)-1))
G.add_edges_from(list_of_edges)

n = nx.number_of_nodes(G)
pos = nx.spring_layout(G)
nodes = [1]*n
random_index = random.randrange(0, n)
nodes[k] = 2 #b is the node to replace
num_mutants = nodes.count(2)

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
	
	normals = list([i for i, x in enumerate(nodes) if x == 1])
	mutants = list([i for i, x in enumerate(nodes) if x == 2])
	nx.draw_networkx_edges(G, pos, width=1.0)
	nx.draw_networkx_nodes(G, pos, nodelist=normals, node_color='g', node_size=500)
	nx.draw_networkx_nodes(G, pos, nodelist=mutants, node_color='r', node_size=500)
	plt.axis('off')
	plt.savefig("lattice" + str(time_step) + ".png")
	plt.clf()
	

	# Increment time
	time_step += 1
	#print time_step, "  ", num_mutants
print time_step, " , ", num_mutants

