'''
Jake Richter - Newman 9.3 

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
    target = 1e-6
    scale = (1. + omega)/4.
    testmat = np.zeros([M+1,M+1], dtype = float)
    
    while delta > target:
        testmat = potVals
        for i in range(1,M):
            for j in range(1,M):
                if i == 0.0 or i == M or j == 0.0 or j == M:
                    potVals[i,j] = 0.0
                elif (i > 20 and i < 80) and (j == 19 or j == 79 ):
                    if j == 19: 
                        potVals[i,j] = Vbounds
                    elif j == 79:
                        potVals[i,j] = -Vbounds
                
                
                else:
                    # Here we can see this is just an averaging of the 4 neighboring points 
                    potVals[i,j] = scale*(potVals[i + 1,j] + potVals[i - 1, j] + potVals[i, j+1] + potVals[i,j-1]) - omega * potVals[i,j]
        
        # As in book - Updating delta vals 
        delta = np.max(np.abs(testmat - potVals))
        
            
            
            
    
    if plotQ == True:
        plt.figure()
        plt.imshow(potVals, cmap = 'gray')
        plt.colorbar()
        
        plt.show()
GausSidelPDE(100, 1, omega = .8,plotQ= True)