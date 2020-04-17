import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.patches as patches
import matplotlib.path as path
plt.rcParams['animation.ffmpeg_path'] ='C:\\Users\\jakri\\Programs\\Python\\Python38\\Lib\\site-packages\\ffmpeg\\ffmpeg-20200403-52523b6-win64-static\\bin\\ffmpeg.exe'


# Initializing a global list of initial values for the system of particles we have_______________________
np.random.seed(223497)
Nparticles = 75                                   

# Random Initial Positions 
xiniti = np.random.uniform(low = 1, high = 99.5, size = Nparticles)   # Initial x positions
yiniti = np.random.uniform(low = 1, high = 99.3, size = Nparticles)  # Initial y positions 


# Random Initial Velocities - Scaled to 1 
vmax = 1.0                                                      # Maximum velocity - in this case THE velcoity
vxin = np.random.uniform(size = Nparticles, low = -(vmax-.05e-1), high = vmax - .05e-1  )    # Intial vx velocities
vyin = np.sqrt(vmax**2 - np.square(vxin))                                  # initial vy velocities
vtotali = np.sqrt(np.square(vyin) + np.square(vxin))                    # total Vi - should be 1 in this case



rvec = np.array([xiniti,yiniti,vxin,vyin])
rvec = np.transpose(rvec)

radius = .5                                                             # Radius of all particles 


timestep = 5e-3                                                         # Timestep to update positions
TotalTimesteps  = 750 # total number of timesteps to iterate through

#####_______________________________________________________________________________________________________


# Velocities and velocity titles for the bar graph
VelList = [0,1,2,3,4]
VelLabels = [0.0, 1.0, 2.0, 3.0, 4.0]

# Initializng the figure and its subplot - look to matplotlib documentation to understand add_gridspec 
fig = plt.figure()
gs = fig.add_gridspec(5, 4)

ax = fig.add_subplot(gs[1:5,:])
ax.set_xlim([0,100])
ax.set_ylim([0,100])

# Initializing  the Second subplot for the histogram 
vmagi = np.sqrt(vxin**2 + vyin**2)
vels, bins = np.histogram(vmagi, 10)

left = bins[:-1]
right = np.array(bins[1:])
bottom = np.zeros(len(left))
top = bottom + vels 
nrects = len(left)
nverts = nrects * (1 + 3 + 1)


verts = np.zeros([nverts, 2])
codes = np.ones(nverts, int) * path.Path.LINETO
codes[0::5] = path.Path.MOVETO
codes[4::5] = path.Path.CLOSEPOLY
verts[0::5, 0] = left
verts[0::5, 1] = bottom
verts[1::5, 0] = left
verts[1::5, 1] = top
verts[2::5, 0] = right
verts[2::5, 1] = top
verts[3::5, 0] = right
verts[3::5, 1] = bottom


barpath = path.Path(verts, codes )
patch = patches.PathPatch(barpath )

ax2 = fig.add_subplot(gs[0,:])
ax2.add_patch(patch)
ax2.set_xlim(left[0], right[-1])
ax2.set_ylim(bottom.min(), 20)




# Uesful Functions fo Calculations ----------------


# The Lennared Jones 6-12 formula 

def V(r):
    return 4 * ((1/r)**12 - (1/r)**6)
# Force that the particles exert on each other 
def Force(r):
    return 24 * (2*(1/r)**13 - (1/r)**7)

#########-------------------------------------------


# Timestep initialization to the one above - except applying to global variable h-step -----

hstep = timestep
#-------------------------------------------------------------------------------------------


# Useful lists for animations #-----------------------------------------

ims = [] # list to append images/artists to for animation 
im2 = [] #
ts = []  # empty list of times that will be useful for animation purposes 
#------------------------------------------------------------------------





# This nested for loop will Initialize the half step for Verlet ------------------------------

# Initializing the vhalf vector that will be updated later in the verlet integration 
vhalf = np.zeros([Nparticles,2], dtype = float ) 

for i in range(Nparticles ):
    for j in range(i+1, Nparticles):
        
            

        sepxi = rvec[i][0] - rvec[j][0]
        sepyi = rvec[i][1] - rvec[j][1]

        disti = np.sqrt(sepxi**2 + sepyi**2)

        # Assigning the initial 1/2 step velocity Values in the x direction
        vhalf[i][0] = rvec[i,2] + Force(disti)* (sepxi/disti)
        vhalf[j][0] = rvec[j,2] - Force(disti)* (sepxi/disti)
        
        # Now in doing the same thing above in the y direction
        vhalf[i][1] = rvec[i,3] + Force(disti)* (sepyi/disti)
        vhalf[j][1] = rvec[j, 3] - Force(disti)* (sepyi/disti)

#---------------------------------------------------------------------------------------------
# Initializing kp vector to update velocities in nested for loop-----------------------------

kp = np.empty([Nparticles, 2], dtype = float)
kp2 = np.empty(2, dtype = float)
#----------------------------------------------------------------------------------------------

# For loop to iterate through each frame. It changes the value of the artists 'scatts' then appends to a list to be animated ---
for it in range(TotalTimesteps):
    # Creating bin counter to know how many particles are moving in a specific range of velocities ----------
    cV0 = 0.0 
    cV1 = 0.0 
    cV2 = 0.0
    cV3 = 0.0 
    cV4 = 0.0 

    # Initalizing the kp values to 0 on each iteration so I do  not overcount the force from the last iteration
    kp = np.zeros([Nparticles,2], dtype = float )
    #---------------------------------------------------------------------------------------------------------#

    
    # For loops to iterate through each particle and update their position -----------------------------------
    for i in range(Nparticles):
        
        
        
        # Creating a temprary array of values to test the separations between particles ----------------------#
        x = rvec[i][0]
        y = rvec[i][1]
        vx = rvec[i][2]
        vy = rvec[i][3]

        rtest1 = [x,y,vx,vy] 
        #-----------------------------------------------------------------------------------------------------#
        


       # Testing Boundary - Periodic Boundary ----------------------------------------------------------------#
       
        # First in the y direction - 
        if (y < 0 ) :
            rvec[i][1] += 100 

        if (y > 100 ):
            rvec[i][1] -= 100

        # Then in the x direction
        if (x < 0 ): 
            rvec[i][0] += 100
        if (x > 100 ):
            rvec[i][0] -= 100
        #------------------------------------------------------------------------------------------------------#
            
        
        
        
        
        
        # Calculating the lennard Jones Force interactions between the particle of rvec[i] and rvec[j]--------
        for j in range(i+1,Nparticles):
            # Creating the temporary array for the second particle to test the separation and force---- 
            x2  = rvec[j][0]
            y2  = rvec[j][1]
            vx2 = rvec[j][2]
            vy2 = rvec[j][3]
            
            rtest2 = [x2,y2,vx2,vy2] 
            # -------------------------------------------------------------------------------------------

            # Calculating the Separations in either direction---------
            sepx = x - x2
            sepy = y - y2 
            dist = np.sqrt(sepx**2 + sepy**2)
            if dist < 1.50:
                dist = 1.0 
            # --------------------------------------------------------
            
            # Continuing Verlet Integration with half-time step calculations --------------------------
            
            #using formulas from Newman chapter 8 pg 373
            rvec[i, 0:2] += timestep * vhalf[i,:]
            rvec[j, 0:2] += timestep * vhalf[j,:]
            
            kp[i,0] = timestep *Force(dist) * (sepx/dist)
            kp[i,1] = timestep *Force(dist) * (sepy/dist)
            
            
            kp[j,0] = (- kp[i,0])
            kp[j,1] = (- kp[i,1])

            

            rvec[i, 2:4] = (vhalf[i,:] + .5 * kp[i])
            rvec[j, 2:4] = (vhalf[j,:] + .5 * kp[j])
            
            
            
        
            vhalf[i,:] += kp[i,:]
            vhalf[j,:] += kp[j,:]
    
            
    scatts = ax.scatter(rvec[:,0], rvec[:,1], color = 'b')
    
  
    

    
    velocity_mags = np.sqrt(rvec[:,2]**2 + rvec[:,3]**2)
    
    
    vels, bins = np.histogram(velocity_mags, 25)
    left = np.array(bins[:-1])
    right = np.array(bins[1:])
    bottom = np.zeros(len(left))
    top = bottom + vels 
    nrects = len(left)
    nverts = nrects * (1 + 3 + 1)


    verts = np.zeros((nverts, 2))
    codes = np.ones(nverts, int) * path.Path.LINETO
    codes[0::5] = path.Path.MOVETO
    codes[4::5] = path.Path.CLOSEPOLY
    verts[0::5, 0] = left
    verts[0::5, 1] = bottom
    verts[1::5, 0] = left
    verts[1::5, 1] = top
    verts[2::5, 0] = right
    verts[2::5, 1] = top
    verts[3::5, 0] = right
    verts[3::5, 1] = bottom


    barpath = path.Path(verts, codes )
   
    
    patch = patches.PathPatch(barpath, facecolor = 'blue', alpha = .5 )
    ax2.add_patch(patch)
    ax2.set_xlim(left[0], right[-1])
    ax2.set_ylim(bottom.min(), 20)

    
    

    


    ims.append([scatts, patch,])

    
    
        
            
            
# Basic Animation writer given by matplotlib --------------------------------------------
FFwriter = animation.FFMpegWriter(fps = 1000/20)          


Animation = animation.ArtistAnimation(fig, ims, interval = 20, blit = True )

Animation.save('PT2_MD_Test.mp4', writer = FFwriter)

# ----------------------------------------------------------------------------------------

### CODE DONE ####
