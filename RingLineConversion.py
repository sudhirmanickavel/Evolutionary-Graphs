import networkx as nx 
import matplotlib.pyplot as plt
import sys
import random

grid = int(sys.argv[1]) #number of nodes
r = float(sys.argv[1]) #fitness constant 
f = int(sys.argv[2]) #node to be replaced
m = grid
G = nx.star_graph(grid) #star graph function
n = nx.number_of_nodes(G) 
t = 0
k = 0
mlist = []
klist = []
seed = None 
pos = nx.spring_layout(G)
nodes = [1]*n
random_index = random.randrange(0, n)
nodes[f] = 2 #f is the node to replace
num_mutants = nodes.count(2)
time_step = 0
final_num_mutants = []
final_time_step = []
graph_time_step = 0
while t < n-1: 
	G.remove_edge(0, t+1)
	G.add_edge(t,t+1)
	mlist.append(m)
	klist.append(k)
	t = t+1	
	k = k+1 
	m = m-1 
	nodes = [1]*n
	random_index = random.randrange(0, n)
	nodes[f] = 2
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

		#Increment time_step
		time_step += 1
	#nx.draw(G,pos)
	#plt.show()
		pos = nx.spring_layout(G)
		normals = list([i for i, x in enumerate(nodes) if x == 1])
		mutants = list([i for i, x in enumerate(nodes) if x == 2])
		nx.draw_networkx_edges(G, pos, width=1.0)
		nx.draw_networkx_nodes(G, pos, nodelist=normals, node_color='g', node_size=500)
		nx.draw_networkx_nodes(G, pos, nodelist=mutants, node_color='r', node_size=500)
		plt.axis('off')
		plt.savefig("RingLine" + str(graph_time_step) + "Fitness" + str(r) + ".png")
		plt.clf()
		graph_time_step += 1
	#Add mutants from each state into list final_num_mutants	
	final_num_mutants.append(num_mutants)
	final_time_step.append(time_step)	
print final_time_step, " , ", final_num_mutants
#print mlist, ",", klist


