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
def Rejection(Npoints, DensityFunction):
    i = 1 
    yl = []

    # Full Rejection method
    while i <= Npoints:
        x = np.random.randn()
        y = np.random.randn()
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
    bins = np.arange(histmin,histmax,width)
    histArtist = plt.hist(yl,bins=bins)
    return histArtist

plt.figure()
Rejection(1000, ProbFunction)
plt.show()

