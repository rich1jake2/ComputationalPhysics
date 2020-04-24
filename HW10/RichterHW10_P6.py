'''
Create a Random 3D walker 

'''
import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D 
plt.rcParams['animation.ffmpeg_path'] ='C:\\Users\\jakri\\Programs\\Python\\Python38\\Lib\\site-packages\\ffmpeg\\ffmpeg-20200403-52523b6-win64-static\\bin\\ffmpeg.exe'


# Initial Parameters 
Nwalkers = 100
Nsteps = 30000
x = np.zeros(Nwalkers)
y = np.zeros(Nwalkers)
z = np.zeros(Nwalkers)

r = np.array([x,y,z])
r = r.T

xmax = ymax = zmax = 100
xmin = ymin = zmin = -100


for t in range(Nsteps):
    
    
    for walker in range(Nwalkers):
        xrand = np.random.uniform(low = -1.0, high = 1.0, size = 1)
        yrand = np.random.uniform(low = -1.0, high = 1.0, size = 1)
        zrand = np.random.uniform(low = -1.0, high = 1.0, size = 1)
        
        
        if xrand >= 0 :
            dx = 1.0 
            
            
        else:
            dx = -1.0 

        
        if yrand >= 0 :
            dy = 1.0
        else:
            dy = -1.0

        if zrand >= 0 :
            dz = 1.0
        else:
            dz = -1.0
        
        # Creating the Displacement vector 
        displVec = np.array([dx, dy, dz], dtype = float)
        # Normalizing it 
        displVec *= np.sum(np.square(displVec))

        # adding the normalized displacement vector to our position coordinate
        r[walker,:] += displVec
    if np.max(r[:, 0]) >= xmax or np.min(r[:,0]) <= xmin or np.max(r[:, 1]) >= ymax or np.min(r[:,1]) <= ymin or np.max(r[:, 2]) >= xmax or np.min(r[:,2]) <= xmin :
                
    
                
        break  

fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')
ax.scatter(xs = r[:,0], ys = r[:,1], zs = r[:,2])

# creating the orthogonal grid

ax.plot(xs = (xmax, 0, 0), ys = (0,0,0), zs = (0,0,0))
ax.plot(xs = (0, 0, 0), ys = (ymax,0,0), zs = (0,0,0))
ax.plot(xs = (0, 0, 0), ys = (0,0,0), zs = (zmax,0,0))


ax.set_xlim(-100,100)
ax.set_xlabel('X')

ax.set_ylim(-100,100)
ax.set_ylabel('Y')

ax.set_zlim(-100,100)
ax.set_zlabel('Z')

plt.show()      


        
        