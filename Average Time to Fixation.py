import csv 
from decimal import *
n = 1.0
Probl = []
muts = []
mutsy = []
mutsx = []
ATl = []
averagetimelist = []
t = 0
import matplotlib.pyplot as plt
for i in range (9): 
	string = "reader" + str(i+1) 
	output = 'output_%d.csv' % n
	print (output)
	string = csv.reader(open(output, 'rU'), delimiter=',', dialect='excel')
	for row in string: 
		muts.append(row[4])
		mutsy.append(row[0])
	muts = list(map(int, muts))
	lenmuts = len(muts)	
	while t < lenmuts: 
		if muts[t] == 15:
			mutsx.append(mutsy[t])
			t = t+1 
		else: 
			t = t+1 
	count = muts.count(15)
	mutsx = list(map(int, mutsx))
	averagetime = sum(mutsx)/count 
	averagetimelist.append(averagetime)
	muts = []
	mutsy = []
	mutsx = []
	t = 0
	n = n+1 
print (averagetimelist)
