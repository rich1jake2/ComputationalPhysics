import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
plt.rcParams['animation.ffmpeg_path'] ='C:\\Users\\jakri\\Programs\\Python\\Python38\\Lib\\site-packages\\ffmpeg\\ffmpeg-20200403-52523b6-win64-static\\bin\\ffmpeg.exe'

Nparticles = 100                                   

# Random Initial Positions 
xiniti = np.random.uniform(low = 1, high = 99.5, size = Nparticles)   # Initial x positions
yiniti = np.random.uniform(low = 1, high = 99.3, size = Nparticles)  # Initial y positions 


# Random Initial Velocities - Scaled to 1 
vmax = 1.0                                                              # Maximum velocity - in this case THE velcoity
vxin = np.random.uniform(size = Nparticles, low = -(vmax-.05), high = vmax - .05  )    # Intial vx velocities
vyin = np.sqrt(vmax**2 - np.square(vxin))                                  # initial vy velocities
vtotali = np.sqrt(np.square(vyin) + np.square(vxin))                    # total Vi - should be 1 in this case



rvec = np.array([xiniti,yiniti,vxin,vyin])
rvec = np.transpose(rvec)

radius = .5                                                             # Radius of all particles 


timestep = .005                                                         # Timestep to update positions
TotalTimesteps  = 400

VelList = [0,1,2,3,4]
VelLabels = [0.0, 1.0, 2.0, 3.0, 4.0]


fig = plt.figure()
gs = fig.add_gridspec(5, 4)

ax = fig.add_subplot(gs[1:5,:])
ax.set_xlim([0,100])
ax.set_ylim([0,100])
ax2 = fig.add_subplot(gs[0,:])

# bPlt  = ax2.bar(VelLabels, VelList)




# ax2 = fig.add_subplot(2,3,2)

# scatts = ax.scatter(rvec[:,0],rvec[:,1], color = infections)
# Functions to Update positions and velocities

def Update_Positions(rarray,timestep):
    xposes = rarray[0] 
    xposes += (rarray[2])*timestep
    
    yposes = rarray[1] 
    yposes += (rarray[3])*timestep
    return np.array([xposes, yposes], dtype = float)

def V(r):
    return 4 * ((1/r)**12 - (1/r)**6)
def Force(r):
    return 24 * (2*(5e-9/r)**13 - (5e-9/r)**7)


def Verlet_Velocities(r1,r2,h):                                             
   
    
    

    # Returning the proper values of V1 and V2 
    return np.array([vx1,vy1], dtype = float), np.array([vx2,vy2], dtype = float)

def BarUpdate(barPlots, DesiredHeights):
    for i, plot in enumerate(barPlots):
        plot.set_height(DesiredHeights[i])
    return barPlots


# Function to update all the positions - check for collisions and stuff

    
hstep = timestep
error = .5
radius = .5
ims = []
im2 = []
ts = []






# Initialize the half step for Verlet - 
vhalf = np.empty([Nparticles,2], dtype = float) # Half step with 2 columns - for each vel direction

for i in range(Nparticles ):
    for j in range(Nparticles):
        if i == j:
            continue
        else:
            # Because this Double counts the force we want to divide by 2 at the end  

            sepxi = rvec[i][0] - rvec[j][0]
            sepyi = rvec[i][1] - rvec[j][1]
            vhalf[i][0] = rvec[i,2] + Force(sepxi)
            vhalf[i][1] = rvec[i,3] + Force(sepyi)


# Initializing kp vector to update velocities in nested for loop

kp = np.empty(2, dtype = float)
kp2 = np.empty(2, dtype = float)

# Creating the Proper Frames 
for it in range(TotalTimesteps):
    cV0 = 0.0 
    cV1 = 0.0 
    cV2 = 0.0
    cV3 = 0.0 
    cV4 = 0.0 
    

    for i in range(Nparticles):
        
        
        

        x = rvec[i][0]
        y = rvec[i][1]
        vx = rvec[i][2]
        vy = rvec[i][3]

        rtest1 = [x,y,vx,vy] # Test positions- should not affect actual cacluations - input for update velocities
        
        


       # Testing Collision with Boundary - Reflective Boundaries for testing 
        if (y < 0 ) :
            rvec[i][1] += 100 

        if (y > 100 ):
            rvec[i][1] -= 100 

            
        if (x < 0 ): 
            rvec[i][0] += 100
        if (x > 100 ):
            rvec[i][0] -= 100
            
            
        
        
        
        
        
        # Then Checking for Interactions
        for j in range(Nparticles):
            if i == j:
                continue
            
            x2  = rvec[j][0]
            y2  = rvec[j][1]
            vx2 = rvec[j][2]
            vy2 = rvec[j][3]
            
            rtest2 = [x2,y2,vx2,vy2] # Test positions 2- should not affect actual cacluations - input for update velocities
            
            sepx = x - x2
            sepy = y - y2 
            
            # Continuing Verlet Integration 
            rvec[i,0:2] += timestep*vhalf[i,:]
            
            kp[0] = timestep* .5 *Force(sepx) # K along x - 
            kp[1] = timestep* .5 *Force(sepy) # k values along y 

            

            rvec[i,2:4] += vhalf[i,:] + .5 * kp
             
            
            vhalf[i,:] += kp 
            


            
            
            
    
    # Getting the Number of Particles in different velocities
    for ki,vel in enumerate(rvec[:,2]):
        mag = np.sqrt(vel**2 + (rvec[ki][3])**2 )
        if mag < VelLabels[0] + 1 :
            cV0 += 1 
        elif VelLabels[0] + 1 <= mag and mag < VelLabels[1] + 1.0:
            cV1 += 1
        elif VelLabels[1] + 1 <= mag and mag < VelLabels[2] + 1.0:
            cV2 += 1
        elif VelLabels[2] + 1 <= mag and mag < VelLabels[3] + 1.0:
            cV3 += 1
        elif mag >= VelLabels[4]:
            cV4 += 1
    VelList = [cV0, cV1, cV2, cV3, cV4] 
    
        


    
    # Creating the plots to be iterated through in ArtistAnimation
    totalTime = np.arange(0, it+1)

    
    scatts = ax.scatter(rvec[:,0], rvec[:,1], color = 'b')
    
  
    

    
    
    
    
    ims.append([scatts,])

    
    
        
            
            
            
FFwriter = animation.FFMpegWriter(fps = 1000/20)          


Animation = animation.ArtistAnimation(fig, ims, interval = 20, blit = True )

Animation.save('PT2_MD_Test.mp4', writer = FFwriter)


