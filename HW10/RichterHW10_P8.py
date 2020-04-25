'''
Problem 8 - DLA 2.0 - making it work on a line 

'''

import numpy as np 
import matplotlib.pyplot as plt 

gridPoints = 101

def draw_line(r):
    line = plt.plot([0,gridPoints],[r,r], color = 'b')
    return line,


def cluster_size(clust):
    x,y = np.nonzero(clust)
    r = np.max(y)
    return r + 3

def ctest(x,y,c):
    if c[x,y]==1:
        return True
    if c[x+1,y]==1 or c[x-1,y]==1 or c[x,y-1]==1 or c[x,y+1]==1:
        return True

# Initializing Cluster
cluster = np.zeros([gridPoints,gridPoints], dtype = int)
cluster[:,0] = 1 

Attempts = 3001
WalkerSteps = 50
# Initializing random walker 
rw = np.zeros([1,2])


# Main walker loop

for i in range(Attempts):
    r = cluster_size(cluster)
    # Initial random number on circle
    
    xi = np.random.randint(low = 0.0, high = gridPoints-15)
    yi = r
    rw[0:,] = [int(xi),int(yi)]

    for l in range(WalkerSteps):
        
        xstep = np.random.uniform(low = -1, high = 1)
        ystep = np.random.uniform(low = -1, high = 1)
        if xstep >= 0 :
            rw[0,0] += 1.0 
        else:
            rw[0,0] -= 1.0 


        if ystep >= 0 :
            rw[0,1] += 1.0
        else:
            rw[0,1] -= 1.0  
        
        

        rw[0,0] = int(rw[0,0])
        rw[0,1] = int(rw[0,1])
        int(rw[0,1])

        
        if int(rw[0,0]) > 99:
            continue 
        if ctest(int(rw[0,0]), int(rw[0,1]), cluster) == True:
            cluster[int(rw[0,0]),int(rw[0,1])] = 1
            break
               
        

    if i%500 == 0.0:
        
        
        fig,ax = plt.subplots()
        xp, yp = np.nonzero(cluster)
        ax.set_aspect('equal')
        draw_line(r)
        plt.scatter(xp, yp, color = 'b', s = 2.0)
        
       
        plt.axis([0,gridPoints,0,gridPoints])

    rw[0:,] = 0.0 
plt.show()
        