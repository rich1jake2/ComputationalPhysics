'''
Write a program or modify from 9.1 to solve Poisson's Equation for the system described in example 9.2. 
work in units where e0 = 1 and continue the iteration until your solution for the electric potential changes
by less than 10^-6V per step at every grid point 
'''
import numpy as np
import matplotlib.pyplot as plt

# We want to relax a set of Grid points to solve Poison's equation
# in this case the boundaries all have 0 potential and we have a charge density from two charges inside 


def Relaxation_PDE_Solver(M,Vbounds, plotQ = True):
    #--------------------------------------------------------------#
    # Intial functions - Most real work is done for us by the book #
    #--------------------------------------------------------------#
    
   
    # Creating the grid of Potential values - in this case spacing will be in cm 
    potVals = np.zeros([M+1,M+1], dtype = float)
    UpdatedPotVals = np.zeros([M+1,M+1], dtype = float)
    
    # initialzing potential at boundaries 
    potVals[0,:] = Vbounds
    
    # initializing grid of the charges 
    rowPlus = np.zeros([M+1,M+1], dtype = float)
    rowMinus = np.zeros([M+1,M+1], dtype = float)

    rowPlus[20:41,60:81] = 1.0 
    rowMinus[60:81,20:41] = -1.0 

    row = rowPlus + rowMinus
    
    # Initializing the change that happens after a relaxation iteration - we will want it to be less than 10^-6

    delta = 1.0 
    target = 1e-6
    OneFourth = 1./4. # For calculation zoom zoom 
    
    while delta > target:
        for i in range(M+1):
            for j in range(M+1):
                if i == 0 or i == M or j == 0 or j == M:
                    UpdatedPotVals[i,j] = potVals[i,j]
                # Else statment will differ from laplace because we have charge density - eq 9.12 in book 
                else:
                    # Here we can see this is just an averaging of the 4 neighboring points 
                    UpdatedPotVals[i,j] = OneFourth*(potVals[i + 1,j] + potVals[i - 1, j] + potVals[i,j+1] + potVals[i,j-1])\
                                        + 1/4 * row[i,j]
            # As in book - Updating delta vals 
            delta = np.max(np.abs(potVals - UpdatedPotVals))
            
            # As in book - updating potVals to be the UpdatedPotVals - essentially throwing away old values 
            potVals,UpdatedPotVals = UpdatedPotVals, potVals 
            
    
    if plotQ == True:
        plt.figure()
        plt.imshow(potVals, cmap = 'plasma')
        plt.show()

Relaxation_PDE_Solver(M = 100,Vbounds = 0.0 , plotQ = True)