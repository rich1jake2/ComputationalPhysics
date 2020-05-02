'''

Ising Model - 
Use a markov - monte carlo simulation to calculate the physics of the ising model

'''

# Part A - Energy Calcualtion 
import numpy as np 
import matplotlib.pyplot as plt 

class Spins: 
    def __init__(self,size):
        self.size = size 
        self.Smatrix = np.ones([size,size], dtype = int)
        self.TotalE  = 0.0 
        
        # Randomizing the +1 and -1 spins
        for i in range(len(self.Smatrix)):
            for j in range(len(self.Smatrix)):
                if np.random.random()>.5:
                    self.Smatrix[i][j] = - 1 
    
    def Energy(self):
        self.TotalE = 0.0 
        for col in range(len(self.Smatrix )-1):
            self.TotalE += np.sum(self.Smatrix[:,col] * self.Smatrix[:,col+1]) 
            self.TotalE += np.sum(self.Smatrix[col,:] * self.Smatrix[col + 1,:])
        return -1 * self.TotalE

    
    def Mag(self):
         
        M = np.sum(self.Smatrix)
        

        return M 

    def SpinFlipping(self, Npoints, plot):
        M_list = []
        # Energy before spin flip
        ei = self.Energy()
        for N in range(Npoints):
            

            # Random Element in Array of spins
            si = np.random.randint(low = 0.0 ,high = self.size )
            sj = np.random.randint(low = 0.0, high = self.size)
            
            # Changing the Direction of that spin 
            self.Smatrix[si][sj] *= -1 

            # Energy After the each spin flip 
            Ej = self.Energy()

            # The probability value 
            Pa = np.exp(-1*(Ej - ei))

            if Pa > np.random.random() :
                M_list.append(self.Mag())
                ei = Ej
                continue
            elif Ej <= ei:
                M_list.append(self.Mag())
                ei = Ej
                continue 
            else:
                self.Smatrix[si][sj] *= -1
                M_list.append(self.Mag()) 

            
                
            
            
        if plot == True: 
            plt.figure()
            plt.plot(np.arange(Npoints), M_list)
            plt.show()
    
        

        




s = Spins(20)
s.SpinFlipping(1000000, plot = True)








