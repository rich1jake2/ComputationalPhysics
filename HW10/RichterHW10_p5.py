import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.animation as animation
plt.rcParams['animation.ffmpeg_path'] ='C:\\Users\\jakri\\Programs\\Python\\Python38\\Lib\\site-packages\\ffmpeg\\ffmpeg-20200403-52523b6-win64-static\\bin\\ffmpeg.exe'


# Initial Parameters 
Nwalkers = 100
Nsteps = 50000
x = np.zeros(Nwalkers)
y = np.zeros(Nwalkers)
r = np.array([x,y])
r = r.T

# For cell creation
xmin = ymin = - 200
xmax = ymax = 200
nx = 7
ny = 7 
Cells = np.zeros(nx*ny)
# Intial Entropy 
Sentropy = np.zeros(Nsteps)
# Animation Set up 
fig = plt.figure()

ax = plt.axes(xlim = (xmin,xmax), ylim = (ymin,ymax))
ScatterArtists = [] # Lists for Scatter Artists 




# Main Walking Nested For loop
for t in range(Nsteps):
    Cells = np.zeros(nx*ny)
    
    for walker in range(Nwalkers):
        xrand = np.random.uniform(low = -1.0, high = 1.0, size = 1)
        yrand = np.random.uniform(low = -1.0, high = 1.0, size = 1)
        
        
        if xrand >= 0 :
            r[walker, 0] += 1.0 
            
            
        elif xrand < 0 :
            r[walker,0] -= 1.0 

        
        if yrand >= 0 :
            r[walker, 1] += 1.0
        elif yrand < 0:
            r[walker, 1] -= 1.0
        

        # Testing bounds and changing direction
        if r[walker,0] < xmin:
            r[walker,1] += 1
            r[walker,0] +=1
    
        if r[walker,0] >= xmax:
            r[walker,1] += 1
            r[walker,0] -=1
        
        if r[walker,1] <= ymin:
            r[walker,0] += 1
            r[walker,1] +=1
        
        if r[walker,1] >= ymax:
            r[walker,0] += 1
            r[walker,1] -= 1
        
        # Checking Corners
        if r[walker,1] >= ymax and r[walker,0] >= xmax:
            r[walker,0] -= 1
            r[walker,1]-=1
        if r[walker,1] >= ymax and r[walker,0] <= xmin:
            r[walker,1] -=1
            r[walker,0] +=1
        if r[walker,1] <=ymin and r[walker,0] >= xmax:
            r[walker,1] += 1
            r[walker,0] -= 1
        if r[walker,1] <= ymin and r[walker,0] <= xmin:
            r[walker,0] +=1
            r[walker,1] +=1 

        
        

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
    
   
    
    # Creating the Scatterplot artists every 2 time steps
    
    scatter = ax.scatter(r[:,0],r[:,1], marker = 's', c = 'b')
    annotatedEntropy = plt.annotate('Entropy = '+ str(np.around(Sentropy[t],5)), xy = (-150, 150), xytext = (-150,150))
    ScatterArtists.append([scatter, annotatedEntropy] )




FFwriter = animation.FFMpegWriter(fps = 30)


WalkerAnimation2 = animation.ArtistAnimation(fig, ScatterArtists, interval = 50, blit = True )
plt.show()
# WalkerAnimation2.save('HW10_Problem4.mp4', writer = FFwriter)

plt.figure()
plt.scatter(r[:,0],r[:,1], marker = 's', c = 'b')

plt.figure()
plt.plot(np.arange(t),Sentropy[0:t])
plt.show()