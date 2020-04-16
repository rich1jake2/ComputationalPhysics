# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 15:15:22 2020

@author: jakri
"""

'''
Jake Richter HW 6 - P2
Radioactive decay 


'''
import numpy as np 
from numpy import sqrt, sin, cos
import matplotlib.pyplot as plt


def F2(r,t,taua,taub):
    r = np.array(r)
    
    Na = r[0]
    Nb = r[1]
    
    
    f1 = -Na/taua
    f2 = -f1 - Nb/taub
    
    
    return np.array([f1,f2])


def Numerical_DE(fs,t0,tf,N,x0,y0,taua,taub):
    
    
    h = (tf-t0)/N                               # creating the step size h
    half = .5 
    sixth = 1/6          

    time = np.arange(t0,tf,h)                   # creating the time steps
    r = np.empty((len(time),2),dtype = float)   # intializing x, y 
    
    r[0][0] = x0
    r[0][1] = y0
    # r[0][2] = v0*cos(theta0*pi/180)
    # r[0][3] = v0*sin(theta0*pi/180)
    
    for c,t in enumerate(time):                 # to animate - go through this for loop to get the updated pos/velocity 
                                                                                            
        if c == N-1:
            break 
        else :
            k1 = h*fs(r[c,:],t,taua,taub)
            k2 = h*fs(r[c,:] + half*k1, t + half*h, taua, taub)
            k3 = h*fs(r[c,:] + half*k2, t + half*h, taua, taub)
            k4 = h*fs(r[c,:] + k3, t + h, taua, taub)
            r[c+1,:] = r[c,:] + sixth*(k1 + 2*k2 + 2*k3 + k4)

    
    
    xl = r[:,0]
    yl = r[:,1]
    
    
    '''
    plt.figure()

    plt.plot(xl,yl)
    plt.xlim(0,250)
    plt.ylim(0,100)

    plt.show()
    '''
    return time,xl, yl
# Creating the proper intial tau values 
    
tauas = np.linspace(1,20,7)
taubs = np.linspace(1,20,7)

# Initial Conditions 
na0 = 100
nb0 = 100

# Number of iteration points per tau values
Npoints = 1000
# time conditions
t0 = 0.0 
tf = 35 # idk the unit on this 



# Iterating through the taus to teest their interatic

for i in range(1,len(tauas)):
    plt.figure()
    times, Na, Nb = Numerical_DE(F2,t0,tf,Npoints,na0,nb0,tauas[-i],taubs[0])
    plt.title('taua/taub = ' + str(np.around(tauas[-i]/taubs[0],3)))
    plt.plot(times, Na, label = 'Na')
    plt.plot(times,Nb, label = 'Nb ')
plt.show()
    

for tb in taubs:
    plt.figure()
    times, Na, Nb = Numerical_DE(F2,t0,tf,Npoints,na0,nb0,tauas[0],tb)
    plt.title('taua/taub = ' + str(np.around(tauas[0]/tb,3)))
    plt.plot(times, Na, label = 'Na')
    plt.plot(times,Nb, label = 'Nb ')


    plt.xlabel('Time')
    plt.legend()
plt.show()

'''
# Attempting to animate - from matplotlib documentation \
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
xdata, ydata = [], []
xd2, yd2 = [],[]
ln, = plt.plot([], [], 'ro')
ln2, = plt.plot([],[])

def init():
    ax.set_xlim(0, 35)
    ax.set_ylim(-1, 200)
    return ln,ln2

def update(frame):
    
    
    xdata.append(frame)
    ydata.append(
    ln.set_data(xdata, ydata)
    return ln,

ani = FuncAnimation(fig, update, frames=np.linspace(0, 2*np.pi, 128),
                    init_func=init, blit=True)
plt.show()
        
'''
        
