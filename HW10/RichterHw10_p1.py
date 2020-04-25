'''
Rejection Method
Use the rejection method to generate a sequence of random
numbers distributed according to Py = a exp(-by) 
make a 10 bin histogram of the resulting distribution N = 1000
and a 100 bin for N = 1e6 

Plot the analytical curves over both. 


'''

import numpy as np 
import matplotlib.pyplot as plt 
def ProbFunction(x):
    return 2*np.exp(-3*x)
def Rejection(Npoints, DensityFunction, binNumber):
    i = 1 
    yl = []

    # Full Rejection method
    while i <= Npoints:
        x = np.random.uniform(low = 0, high = 10 )
        y = np.random.uniform(low = 0, high = 10 )
        # Rejecting the samples that don't meet the criteria
        if y <= DensityFunction(x):
            yl.append(y)
            i +=1
        else:
            continue
    # Creating the Histogram artist 
    width = 0.5
    histmin = np.floor(min(yl))
    histmax = np.ceil(max(yl))+width
    bins = np.linspace(histmin,histmax,binNumber)
    histArtist = plt.hist(yl,bins=bins)
    return histArtist

plt.figure()
Rejection(1000, ProbFunction, 10)
plt.show()

plt.figure()
Rejection(1000000, ProbFunction, 100)
plt.show()