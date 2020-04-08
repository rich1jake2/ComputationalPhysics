import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
plt.rcParams['animation.ffmpeg_path'] ='C:\\Users\\jakri\\Programs\\Python\\Python38\\Lib\\site-packages\\ffmpeg\\ffmpeg-20200403-52523b6-win64-static\\bin\\ffmpeg.exe'

Nparticles = 10                                   

# Random Initial Positions 
xiniti = np.random.uniform(low = 1, high = 49.5, size = Nparticles)   # Initial x positions
yiniti = np.random.uniform(low = 1, high = 49.3, size = Nparticles)  # Initial y positions 


# Random Initial Velocities 
vmax = 1.0                                                              # Maximum velocity - in this case THE velcoity
vxin = np.random.uniform(size = Nparticles, low = -.955, high = vmax - .05  )    # Intial vx velocities
vyin = np.sqrt(vmax - np.square(vxin))                                  # initial vy velocities
vtotali = np.sqrt(np.square(vyin) + np.square(vxin))                    # total Vi - should be 1 in this case

infections = np.array(['b']*( Nparticles - 1) + ['r'] ) 

rvec = np.array([xiniti,yiniti,vxin,vyin])
rvec = np.transpose(rvec)

radius = .5                                                             # Radius of all particles 


timestep = .25                                                         # Timestep to update positions
TotalTimesteps  = 1000



fig = plt.figure()
gs = fig.add_gridspec(5, 4)
ax = fig.add_subplot(gs[1:5,:])
ax2 = fig.add_subplot(gs[0,:])
ax2.set_ylim(0,Nparticles+10)
ax2.set_xlim(0,TotalTimesteps+500)



# ax2 = fig.add_subplot(2,3,2)

# scatts = ax.scatter(rvec[:,0],rvec[:,1], color = infections)
# Functions to Update positions and velocities

def Update_Positions(rarray,timestep):
    vmag = np.sqrt(np.square(rarray[2]) + np.square(rarray[3]))
    xposes = rarray[0] 
    xposes += (rarray[2]/vmag)*timestep
    
    yposes = rarray[1] 
    yposes += (rarray[3]/vmag)*timestep
    return np.array([xposes, yposes], dtype = float)


def Update_Velocities(r1,r2,h):                                             
   
    # Finding the slope to update the velocity to 
    # slope = (r2[1] - r1[1])/(r2[0] - r1[0])

    a_x = r2[0] - r1[0] # This should be acceleration vector - x direction (From slope)
    a_y = r2[1] - r1[1] # This should be acceleration vector - y direction (From Slope)

    testing_vxdirection = r2[2]*r1[2] # If both positive or both negative you get a positive number- same direction
    testing_vydirection = r2[3]*r1[3]
    
   
    '''
    if testing_vydirection > 0 and testing_vxdirection > 0:
        # Keeping same x dirction velocity - because they are moving in same direction
        vx1 = r1[2] = r1[2] 
        vx2 = r2[2] =  r2[2] 
        # Reversing Y directions
        vy1 = r1[3] = r1[3] 
        vy2 = r2[3] =  r2[3] 
        # Normalize Velcocities back to one - divide by magnitued of v vector
        vmag1 = np.sqrt(np.square(vx1) + np.square(vy1))
        vmag2 = np.sqrt(np.square(vx2) + np.square(vy2))
        vx1 /= vmag1
        vy1 /= vmag1

        vx2 /= vmag2
        vy2 /= vmag2
    
    
        
    if testing_vxdirection > 0 and testing_vydirection < 0:
        # Keeping same x dirction velocity - because they are moving in same direction
        vx1 = r1[2] = r1[2] + h*a_x
        vx2 = r2[2] =  r2[2] + h*a_x
        # Reversing Y directions
        vy1 = r1[3] = r1[3] - h*a_y 
        vy2 = r2[3] =  r2[3] + h*a_y
        # Normalize Velcocities back to one - divide by magnitued of v vector
        vmag1 = np.sqrt(np.square(vx1) + np.square(vy1))
        vmag2 = np.sqrt(np.square(vx2) + np.square(vy2))
        vx1 /= vmag1
        vy1 /= vmag1

        vx2 /= vmag2
        vy2 /= vmag2

     
    if testing_vydirection > 0 and testing_vxdirection < 0 :
        # Keeping same Y direction velocity 
        vy1 = r1[3] = r1[3] + h*a_y 
        vy2 = r2[3] = r2[3] + h*a_y 
        # Changing x direction Velocity 
        vx2 = r2[2] = r2[2] + h*100*a_x  
        vx1 = r1[2] = r2[2] - h*100*a_x 
        # Normalize Velcocities back to one - divide by magnitued of v vector
        vmag1 = np.sqrt(np.square(vx1) + np.square(vy1))
        vmag2 = np.sqrt(np.square(vx2) + np.square(vy2))

        vx1 /= vmag1
        vy1 /= vmag1

        vx2 /= vmag2
        vy2 /= vmag2
        
     '''
                             
    
    vx1 = r1[2] = r1[2] - 2*h*a_x # Use negative because we define the positive direction as that from particle 2
    vy1 = r1[3] = r1[3] - 2*h*a_y 
    vmag1 = np.sqrt(np.square(vx1) + np.square(vy1))      # We should divide both resulting velocities by this

    vx2 = r2[2] = r2[2] + 2*h*a_x
    vy2 = r2[3] = r2[3] +  2*h*a_y
    vmag2 = np.sqrt(np.square(vx2) + np.square(vy2))
    # Normalize Velcocities back to one - divide by magnitued of v vector
    vx1 /= vmag1
    vy1 /= vmag1

    vx2 /= vmag2
    vy2 /= vmag2

    # Returning the proper values of V1 and V2 
    return np.array([vx1,vy1], dtype = float), np.array([vx2,vy2], dtype = float)

def InfectionCounting(infectionList):
    InfectedCount = 0.0
    RecoveredCount = 0.0 
    UninfectedCount = 0.0 
    
    for state in infectionList:
        if state == 'r':
            InfectedCount += 1
        if state == 'k':
            RecoveredCount += 1
        if state == 'b':
            UninfectedCount += 1
    return [InfectedCount,UninfectedCount,RecoveredCount] 



# Function to update all the positions - check for collisions and stuff

    
hstep = timestep
error = .5
radius = .5
ims = []
im2 = []
ts = []

ccount = np.zeros([Nparticles])
InfectedPeople = []
NonInfected = []
RecoveredPeople = []


for it in range(TotalTimesteps):
    
    

    for i in range(Nparticles):
        
        if infections[i] == 'r':
            ccount[i] += 1
            if ccount[i] > 300:
                infections[i] = 'k'
        

        x = rvec[i][0]
        y = rvec[i][1]
        vx = rvec[i][2]
        vy = rvec[i][3]

        rtest1 = [x,y,vx,vy] # Test positions- should not affect actual cacluations - input for update velocities
        vmag = np.sqrt(np.square(vx) + np.square(vy))
        
        # Testing Collision with Boundary 
        if (y < 0 ) or (y > 50 ):
            rvec[i][0] +=  vx*hstep
            rvec[i][1] += - vy*2*hstep
            
            rvec[i][2] =  vx/vmag
            rvec[i][3] = - vy/vmag
        if (x < 0 ) or (x > 50 ):
            rvec[i][0] +=  - vx*2*hstep
            rvec[i][1] +=   vy*2*hstep
            
            rvec[i][2] = -vx/vmag
            rvec[i][3] = vy/vmag
        else:
            # Updating Individual Position
            rvec[i][0] += vx*hstep 
            rvec[i][1] += vy*hstep
        
        
        # Then Checking for collisions
        for j in range(Nparticles):
            if i == j:
                continue
            x2 = rvec[j][0]
            y2 = rvec[j][1]
            vx2 = rvec[j][2]
            vy2 = rvec[j][3]
            
            rtest2 = [x2,y2,vx2,vy2] # Test positions 2- should not affect actual cacluations - input for update velocities
            
            separation = np.sqrt(np.square(x2 - x) + np.square(y2 - y))

            # Loop for Collisions between particles 
            if (separation < 2*radius + .75  ) :
                v1, v2 = Update_Velocities(rtest1,rtest2,hstep)
                
                vx,vy = rvec[i][2],rvec[i][3] = v1[0], v1[1] # this is to update rarray - so we can update the positions of both particles at once
                vx2,vy2 = rvec[j][2],rvec[j][3] = v2[0], v2[1] # Note - r[i][2] = vx , r[i][3] = vy
                
                xupdated,yupdated = Update_Positions(rvec[i,:],hstep)
                x2updated, y2updated = Update_Positions(rvec[j,:],hstep)

                # Most of this is just for readability 

                rvec[i][0], rvec[i][1] = xupdated, yupdated
                rvec[j][0], rvec[j][1] = x2updated,y2updated
                
                if infections[i] == 'r' and infections[j] == 'b':
                    infections[j] = 'r'
                if infections[j] == 'r' and infections[i] == 'b':
                    infections[i] = 'r'
                
                
                

            else:
                
                

                continue
    
    # Getting the Number of people in each state - Infected, Uninfected, Recovered 
    states = InfectionCounting(infections)
    # Adding the respective numbers to their proper lists 
    InfectedPeople.append(states[0])
    CurrentInfected = str(InfectedPeople[-1])

    NonInfected.append(states[1])
    CurrentNon = str(NonInfected[-1])

    RecoveredPeople.append(states[2])
    CurrentRecovered = str(RecoveredPeople[-1])
    # Creat
    totalTime = np.arange(0, it+1)

    
    scatts = ax.scatter(rvec[:,0], rvec[:,1], color = infections)
    
    # Plotting and Annotating each line 
    linePlot, = ax2.plot(totalTime,InfectedPeople, marker = '_',color = 'r', linewidth = .5)
    annotatedl1 = ax2.annotate('Infected People' + CurrentInfected, xy =(totalTime[0], InfectedPeople[0]) , xytext = (totalTime[-1]+.25, InfectedPeople[-1]+.25), annotation_clip = False, fontsize = 'xx-small')
    
    linePlot2, = ax2.plot(totalTime,NonInfected, color = 'b', linewidth = .5, marker = '_')
    annotatedl2 = ax2.annotate('Non Infected People' + CurrentNon, xy =(totalTime[0], NonInfected[0]) , xytext = (totalTime[-1]+.25, NonInfected[-1]+.25), annotation_clip = False, fontsize = 'xx-small')
    
    
    linePlot3, = ax2.plot(totalTime, RecoveredPeople, color = 'k', linewidth = .5, marker = '_')
    annotatedl3 = ax2.annotate('Recovered People' + CurrentRecovered, xy =(totalTime[0], RecoveredPeople[0]) , xytext = (totalTime[-1]+.25, RecoveredPeople[-1]+.25), annotation_clip = False, fontsize = 'xx-small')
    
    
    ims.append([scatts,])
    ims.append([linePlot,annotatedl1,linePlot2,annotatedl2,linePlot3,annotatedl3,])
    
        
        
            
            
            
FFwriter = animation.FFMpegWriter(fps = 150)          


Animation = animation.ArtistAnimation(fig, ims, interval = 10, blit = True )

Animation.save('MD_Test.mp4', writer = FFwriter)


plt.show()