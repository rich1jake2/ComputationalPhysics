'''
Overrelaxation and the Gauss-Sidel Method

Newman 9.2 pg 417 

Use the gauss sidel method to solve laplace equation for two dimensional problem of 9.1 
Note - gauss sidel calculate the potential at a point from the potential values around the point, but it uses 
the newly updated values around that point to do this. Unlike the Relaxation method where it iterates through the 
entirety of the old matrix 

this problem wants us to use equation 9.17 on pg 417 in the book (go through the explanation in the book if that
isn't making sense )

'''

import numpy as np 
import matplotlib.pyplot as plt
def GausSidelPDE(M,Vbounds, plotQ, omega, plotq = True):
    #--------------------------------------------------------------#
    # Intial functions - Most real work is done for us by the book #
    #--------------------------------------------------------------#
    
   
    # Creating the grid of Potential values - in this case spacing will be in cm 
    potVals = np.zeros([M+1,M+1], dtype = float)

    
    # initialzing potential at boundaries 
    potVals[0,:] = Vbounds
    
    
    
    
    # Initializing the change that happens after a relaxation iteration - we will want it to be less than 10^-6

    delta = 1.0 
    target = 1e-3
    scale = (1. + omega)/4.
    
    while delta > target:
        for i in range(M+1):
            for j in range(M+1):
                if i == 0 or i == M or j == 0 or j == M:
                    potVals[i,j] = Vbounds
                
                else:
                    # Here we can see this is just an averaging of the 4 neighboring points 
                    potVals[i,j] = scale*(potVals[i + 1,j] + potVals[i - 1, j] + potVals[i, j+1] + potVals[i,j-1]) - omega * potVals[i,j]
        
        # As in book - Updating delta vals 
        delta = np.max(np.abs(potVals))
            
            
            
    
    if plotQ == True:
        plt.figure()
        plt.imshow(potVals, cmap = 'plasma')
        plt.show()

GausSidelPDE(M = 100, Vbounds = 1.0, plotQ = True, omega = .9 , plotq = True)
