'''
2D Random Walkers - 
Simulate the random walk in 2D for N walkers
and Nsteps. start all from the origin, 
plot the positions of all particles as 5 times
'''
import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.animation as animation 

Nwalkers = 10
Nsteps = 500
x = np.zeros(Nwalkers)
y = np.zeros(Nwalkers)
r = np.array([x,y])
r = r.T

fig = plt.figure()
ax = plt.axes(xlim = (-100,100), ylim = (-100,100))


ScatterArtists = []


for t in range(Nsteps):
    for walker in range(Nwalkers):
        xrand = np.random.uniform(low = 0.0, high = 1.0, size = 1)
        yrand = np.random.uniform(low = 0.0, high = 1.0, size = 1)
        
        if xrand <= .5 :
            r[walker, 0] += 1.0 
        else:
            r[walker,0] -= 1.0 


        if yrand <= .5 :
            r[walker, 1] += 1.0
        else:
            r[walker, 1] -= 1.0  
    # Creating the Scatterplot artists
    if t == 0.0 or t == 25 or t == 50 or t==75 or t== 99 :
        scatt = ax.scatter(r[:,0],r[:,1], marker = 's')
        ScatterArtists.append([scatt,] )

WalkerAnimation = animation.ArtistAnimation(fig, ScatterArtists, interval = 1000, blit = True )
plt.show()