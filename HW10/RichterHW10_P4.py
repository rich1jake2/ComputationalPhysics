'''
Calculating the Entropy from problem 10.3

'''

import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.animation as animation
plt.rcParams['animation.ffmpeg_path'] ='C:\\Users\\jakri\\Programs\\Python\\Python38\\Lib\\site-packages\\ffmpeg\\ffmpeg-20200403-52523b6-win64-static\\bin\\ffmpeg.exe'


# Initial Parameters 
Nwalkers = 10
Nsteps = 500
x = np.zeros(Nwalkers)
y = np.zeros(Nwalkers)
r = np.array([x,y])
r = r.T

# For cell creation
xmin = ymin = -100
xmax = ymax = 100
nx = 5
ny = 5 
Cells = np.zeros(nx*ny)
# Intial Entropy 
Sentropy = np.zeros(Nsteps)
# Animation Set up 
fig = plt.figure()
ax = plt.axes(xlim = (xmin,xmax), ylim = (ymin,ymax))
ScatterArtists = [] # Lists for Scatter Artists 





for t in range(Nsteps):
    Cells = np.zeros(nx*ny)
    
    for walker in range(Nwalkers):
        xrand = np.random.uniform(low = 0.0, high = 1.0, size = 1)
        yrand = np.random.uniform(low = 0.0, high = 1.0, size = 1)
        
        if xrand <= .45 :
            r[walker, 0] += 1.0 
            
        else:
            r[walker,0] -= 1.0 


        if yrand <= .45 :
            r[walker, 1] += 1.0
        else:
            r[walker, 1] -= 1.0

        
        

        # Determining cell counts 
        ix = int(r[walker,0]/(xmax - xmin)*nx)
        iy = int(r[walker,1]/(ymax - ymin)*ny)
        cell = ix + iy*ny
        Cells[cell] += 1.0 

    # Calculating Entropy 
    for k in range(len(Cells)):
        Pk = Cells[k]/Nwalkers
        if Pk > 0 :
            Sentropy[t] += -Pk * np.log2(Pk)
    
    # Breaking when the first one makes it to a bound
    if np.max(r[:, 0]) >= xmax or np.min(r[:,0]) <= xmin or np.max(r[:, 1]) >= ymax or np.min(r[:,1]) <= ymin:
                
        break  
    
    # Creating the Scatterplot artists every 2 time steps
    if t%2 == 0:
        scatter = ax.scatter(r[:,0],r[:,1], marker = 's', c = 'b')
        annotatedEntropy = plt.annotate('Entropy = '+ str(np.around(Sentropy[t],5)), xy = (0, 0), xytext = (0,0))
        ScatterArtists.append([scatter, annotatedEntropy] )
FFwriter = animation.FFMpegWriter(fps = 10)
WalkerAnimation2 = animation.ArtistAnimation(fig, ScatterArtists, interval = 50, blit = True )

WalkerAnimation2.save('HW10_Problem4.mp4', writer = FFwriter)