'''
Problem #7 - make a Diffusion Limited Aggregation as discussed in class 
get the dimensionality of it

'''

import numpy as np 
import matplotlib.pyplot as plt 

# The number of grid points we want to plot on 
gridPoints = 101

def draw_cricle(r):
    SurroundingCircle = plt.Circle((gridPoints/2,gridPoints/2), r, fill = False, color = 'b')
    return SurroundingCircle


def cluster_size(clust):
    x,y = np.nonzero(clust)
    r = np.sqrt((x - gridPoints/2)**2 + (y - gridPoints/2)**2)
    return np.max(r) + 3

def ctest(x,y,c):
    if c[x,y]==1:
        return True
    if c[x+1,y]==1 or c[x-1,y]==1 or c[x,y-1]==1 or c[x,y+1]==1:
        return True

# Initializing Cluster
cluster = np.zeros([gridPoints,gridPoints], dtype = int)
cluster[gridPoints//2,gridPoints//2] = 1 

# How many walkers and how many steps each walker takes
Attempts = 751
WalkerSteps = 500

# Initializing random walker 
rw = np.zeros([1,2])
# Creating/Intializing a temporary r and m value calculate the dimensions
nr = 0.0 
nm = 0.0 
r = 0.0 
Dimension = 1.0



# Main walker loop

for i in range(Attempts):
    
    # Calculating the radius 
    r = cluster_size(cluster)
    
    
    

    

    # Initial random number on circle
    theta = np.random.randint(low = 0, high = 360*3)*np.pi/180
    xi = r*np.cos(theta) + gridPoints//2
    yi = r*np.sin(theta) + gridPoints//2
    
    # Setting initial elements of the walker to be elements
    rw[0:,] = [int(xi),int(yi)]

    for l in range(WalkerSteps):
        # Creating a random step
        xstep = np.random.uniform(low = -1, high = 1)
        ystep = np.random.uniform(low = -1, high= 1)
        
        # Moving the random walker based on the value of the random steps
        if xstep > .5 :
            rw[0,0] += 1.0 
        elif xstep < -.5 :
            rw[0,0] -= 1.0 


        elif xstep > 0 :
            rw[0,1] += 1.0
        else:
            rw[0,1] -= 1.0  
        
        # Ensuring that the random walker is using integers
        rw[0,0] = int(rw[0,0])
        rw[0,1] = int(rw[0,1])
        
        # Creating a distance variable to test how far past the original radius it has gone 
        dist = np.sqrt((rw[0,0] - (gridPoints/2))**2 + (rw[0,1]-(gridPoints/2))**2)
        if dist/r  > 1.5 :
            break
        
        # Testing whether the random walker has 'ran' into the cluster 
        if ctest(int(rw[0,0]), int(rw[0,1]), cluster) == True:
            r = cluster_size(cluster)

            cluster[int(rw[0,0]),int(rw[0,1])] = 1
            
            nr = cluster_size(cluster) 
            deltaR = nr - r 
        
            
            # Temprorary array to calculate the mass
            xtempor, ytempor = np.nonzero(cluster)
    
            # Calculating mass and change in mass
            m = len(ytempor)
            deltaM = m - nm
            nm = m  
            Dimension = deltaR/deltaM
            
             
            break
        
    # Making a plots every 250 iterations
    if i%250 == 0.0:
        
        # Creating the figure -
        fig,ax = plt.subplots()
        xp, yp = np.nonzero(cluster)
        ax.set_aspect('equal')
        
        # making the artists - This one is for the cluster
        plt.scatter(xp, yp, color = 'b', s = 2.0)
        
        # Artist for the random walker's starting point on the circle 
        plt.scatter((r*np.cos(theta)+50), ((r*np.sin(theta)+50)), s = 2.0)
        
        # Artist for the (original) cener of the cluster 
        plt.scatter((50),(50), color = 'k')
        
        # Defining the axis to plot over
        plt.axis([0,gridPoints,0,gridPoints])
        
        # Annotating artists to indicate dimensionality 
        plt.annotate('Dimensionality =' + str(Dimension), xy = (90,90), xytext = (90,90))
        # Artist for the cirlcle - appending it to the axis
        Circ = plt.Circle((gridPoints/2, gridPoints/2), r, fill = False)
        ax.add_artist(Circ)


    rw[0:,] = 0.0 
    

   
plt.show()

# From Eden Cluster Code - getting the Dimensions

ry, rx = np.mgrid[0:gridPoints,0:gridPoints]

ry = ry-(gridPoints/2)
rx = rx-(gridPoints/2)


rp = np.sqrt(ry**2 + rx**2)


rc = rp*cluster


rad = np.arange(2,int(r*.7))
m_r = []
for i in range(2,int(r*.7)):
    a = rc[rc<i]
    m_r.append(len(a[a>0]))
print(rad,m_r)

logr = np.log10(rad)
logm = np.log10(m_r)
plt.plot(logr,logm,label='data')
m, b = np.polyfit(logr,logm,1)

xfit = np.linspace(min(logr),max(logr),100)
yfit = m*xfit + b

plt.plot(xfit,yfit,'r-',label='fit')

print("slope = ",m)

plt.legend(loc=2)
plt.show()