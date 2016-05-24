import csv 
from decimal import *
n = 1.0
Probl = []
muts = []
import matplotlib.pyplot as plt
for i in range (9): 
	string = "reader" + str(i+1) 
	print (n)
	output = 'output_%d.csv' % n
	print (output)
	string = csv.reader(open(output, 'rU'), delimiter=',', dialect='excel')
	for row in string:
		muts.append(row[4])
	lenmuts = len(muts)
	A = muts.count('15')
	DecA = Decimal(A)
	DecLen = Decimal(lenmuts)
	P = DecA/DecLen
	Prob = float(P) 
	Probl.append(Prob)	
	n = n + 1 
	muts = []
print (Probl)
#plt.plot(Probl)
#plt.xlim((0,5))
#plt.xlabel('Fitness')
#plt.ylabel('Probability to Fixation')
#plt.title('Ring Star Probability to Fixation')
#plt.show()
