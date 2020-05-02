import numpy as np 
import matplotlib.pyplot as plt 
from matplotlib import collections  as mc
import matplotlib.animation as animation
plt.rcParams['animation.ffmpeg_path'] ='C:\\Users\\jakri\\Programs\\Python\\Python38\\Lib\\site-packages\\ffmpeg\\ffmpeg-20200403-52523b6-win64-static\\bin\\ffmpeg.exe'

'''
Nl = 50 

# Initialize random dimer as a list because it will make the collection easier 
# Nl - 1 so we don't have to worry about a boundary 
dimx1 = np.random.randint(Nl - 1)
dimy1 = np.random.randint(Nl - 1)

dimer = [[dimx1, 0.0 ],[dimy1, 0.0]]

randtester = np.random.random()
print(dimer)
'''






def dimerComplete():
    Nl = 50
    dimx1 = np.random.randint(Nl - 1)
    dimy1 = np.random.randint(Nl - 1)

    dimer = [[dimx1 , dimy1 ],[0.0, 0.0]]

    randtester = np.random.random()
    

    # Completing the random dimer 
    if randtester < .25: 
        dimer[1][0] = dimx1 + 1
        dimer[1][1] = dimy1
    elif randtester <.5 :
        dimer[1][0] = dimx1 - 1 
        dimer[1][1] = dimy1
    elif randtester <.75: 
        dimer[1][1] = dimy1 + 1
        dimer[1][0] = dimx1
    elif randtester <1:
        dimer[1][1] = dimy1 - 1 
        dimer[1][0] = dimx1 


    return dimer
def Energy_calculation(list_object):
    return -len(list_object)

def iteration(nsteps):

    # Intializing list for dimer objects, with the first dimer (di - dimer itial)
    di = dimerComplete()
    dList = [di]
    # Initializing temperature variables
    T = Tmax = 10 
    tmin = 1e-3
    tau = 1e3 
    t = 0.0 
    # Initializing the energy calculation 
    ei = Energy_calculation(dList)

    # Artists list 
    Artists = []

    # Main loop 

    while T > tmin:
        t += 1
        T = Tmax * np.exp(-t/tau)
        dtempor = dimerComplete()
        
        # Test to see if the new dimer will overlap 
        for index,ddex in enumerate(dList):
            
            # if it does overlap - then run a monte carlo random number and see if it should be removed
            
            if dtempor == ddex:
                # Testing the energy difference 
                testD = dList
                testD.pop(index)


                ej = Energy_calculation(testD)
                deltaE = ej - ei 


                if np.random.random() <= np.exp(-deltaE/T):
                    dList = testD
                    ei = ej 
                    break
                else:
                    break
            
                    
            # Checking for individual 
            if (dtempor[0] == ddex[0]) or (dtempor[0] == ddex[1]) or (dtempor[1] == ddex[1]) or (dtempor[1] == ddex[0]) :
                dList.pop(index)
                break
                
            
            # if gets to the end with no overlap then we add it to the list of dimers
            elif index == len(dList) - 1:
                dList.append(dtempor)
                ei = Energy_calculation(dList)
                break

        
        
        if t%2 == 0.0 :
            
            
            draw_Dimers = mc.LineCollection(dList)
            a = ax.add_collection(draw_Dimers)
            
            

            
        
            return a,



fig, ax = plt.subplots()
'''
draw_Dimers = mc.LineCollection(imgs)
ax.add_collection(draw_Dimers)

ax.add_collection(draw_Dimers)
'''
ax.set_xlim(0,50)
ax.set_ylim(0,50)
ax.set_aspect('equal')



Newman10_11Animation = animation.FuncAnimation(fig, iteration, interval = 10, frames = 60000, blit = True )
plt.show()

FFwriter = animation.FFMpegWriter(fps = 60) 
Newman10_11Animation.save('Newman10_11.mp4', writer = FFwriter)
