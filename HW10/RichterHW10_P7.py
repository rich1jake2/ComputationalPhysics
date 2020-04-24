'''
Problem #7 - make a Diffusion Limited Aggregation as discussed in class 
get the dimensionality of it

'''

import numpy as np 
import matplotlib.pyplot as plt 

gridPoints = 101

def draw_cricle(r):
    SurroundingCircle = plt.Circle((gridPoints/2,gridPoints/2), r, fill = False, color = 'b')
    return SurroundingCircle


def cluster_size(clust):
    x,y = np.nonzero(clust)
    r = np.sqrt((x - gridPoints/2)**2 + (y - gridPoints/2)**2)
    return np.max(r) + 4

def ctest(x,y,c):
    if c[x,y]==1:
        return True
    if c[x+1,y]==1 or c[x-1,y]==1 or c[x,y-1]==1 or c[x,y+1]==1:
        return True

# Initializing Cluster
cluster = np.zeros([gridPoints,gridPoints], dtype = int)
cluster[int(gridPoints/2),int(gridPoints/2)] = 1 

Attempts = 1500
WalkerSteps = 500000
# Initializing random walker 
rw = np.zeros([1,2])



for i in range(Attempts):
    r = cluster_size(cluster)
    # Initial random number on circle
    theta = np.random.uniform(low = -2*np.pi , high = 2*np.pi)
    xi = r*np.cos(theta) + 50
    yi = r*np.sin(theta) + 50 
    rw[0:,] = [xi,yi]

    for l in range(WalkerSteps):
        
        xstep = np.random.uniform(low = -1, high = 1)
        ystep = np.random.uniform(low = -1, high= 1)
        if xstep >= 0 :
            rw[0,0] += 1.0 
        else:
            rw[0,0] -= 1.0 


        if ystep >= 0 :
            rw[0,1] += 1.0
        else:
            rw[0,1] -= 1.0  
        rw[0,0] += xstep 
        rw[0,1] += ystep

        rw[0,0] = int(rw[0,0])
        rw[0,1] = int(rw[0,1])
        int(rw[0,1])

        dist = np.sqrt((rw[0,0] - (gridPoints/2))**2 + (rw[0,1]-(gridPoints/2))**2)
        if dist/r  > 1.5 :
            break
        if ctest(int(rw[0,0]), int(rw[0,1]), cluster) == True:
            cluster[int(rw[0,0]),int(rw[0,1])] = 1
            break
        

    if i%500 == 0.0:
        print(rw)
        print(theta)
        fig,ax = plt.subplots()
        xp, yp = np.nonzero(cluster)
        
        plt.scatter(xp, yp, color = 'b', s = 2.0)
        plt.scatter((r*np.cos(theta)+50), ((r*np.sin(theta)+50)))
        plt.axis([0,gridPoints,0,gridPoints])
        Circ = plt.Circle((gridPoints/2, gridPoints/2), r, fill = False)
        ax.add_artist(Circ)
    rw[0:,] = 0.0 
plt.show()
        