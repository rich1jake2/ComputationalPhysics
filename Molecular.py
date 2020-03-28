import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


Nparticles = 2                                                          # Number of Particles

r = np.empty([Nparticles, 4], dtype = float)                            # Setting up Array of particles pos and vel
xboundary = [0,100]                                                     # Establishing a boundary in x axis
yboundary = [0,100]                                                     # in the y axis

xiniti = np.random.uniform(low = .01, high = 99.5, size = Nparticles)   # Initial x positions
yintii = np.random.uniform(low = 0.01, high = 99.3, size = Nparticles)  # Initial y positions 

vmax = 1.0                                                              # Maximum velocity - in this case THE velcoity
vxin = np.random.uniform(size = 25, low = 0.01, high = vmax - .05  )    # Intial vx velocities
vyin = np.sqrt(vmax - np.square(vxin))                                  # initial vy velocities
vtotali = np.sqrt(np.square(vyin) + np.square(vxin))                    # total Vi - should be 1 in this case

radius = .5                                                             # Radius of all particles 


timestep = .001                                                         # Timestep to update positions


# Functions to Update positions and velocities

def Update_Positions(rarray,h):

    xposes = r[0,:] 
    xposes += r[2,:]*h
    
    yposes = r[1,:] 
    yposes += r[3,:]*h
    return np.array([xposes, yposes], dtype = float)
    

def Update_Velocities(rarray,h,a, boundary):                                             
    
    
    # Finding the slope to update the velocity to 


    a_x = 0.0 # This should be acceleration vector - x direction (From slope)
    a_y = 0.0 # This should be acceleration vector - y direction (From Slope)

    
    # Updating the change in direction
    
    vx = rarray[2,:] = h*a_x
    vy = rarray[3,:] = h*a_y 
    vmag = np.sqrt(vx) + np.square(vy)      # We should divide both resulting velocities by this

    # Normalize Velcocities back to one - divide by magnitued of v vector
    vx /= vmag
    vy /= vmag

    return np.array([vx,vy], dtype = float)

# Creating a graph of the Particles 
def NewGraph():
    plt.figure()

    plt.scatter(x , y)

    
'''
# Animation Function From matplotlib 
fig = plt.figure()


def f(r, y):
    
    return np.sin(x) + np.cos(y)

x = np.linspace(0, 2 * np.pi, 120)
y = np.linspace(0, 2 * np.pi, 100).reshape(-1, 1)
# ims is a list of lists, each row is a list of artists to draw in the
# current frame; here we are just animating one artist, the image, in
# each frame
ims = []
for i in range(60):
    x += np.pi / 15.
    y += np.pi / 20.
    scat = plt.scatter( )
    scat.append([im])

ani = animation.ArtistAnimation(fig, ims, interval=50, blit=True,
                                repeat_delay=1000)

# To save the animation, use e.g.
#
# ani.save("movie.mp4")
#
# or
#
# from matplotlib.animation import FFMpegWriter
# writer = FFMpegWriter(fps=15, metadata=dict(artist='Me'), bitrate=1800)
# ani.save("movie.mp4", writer=writer)

plt.show()

'''