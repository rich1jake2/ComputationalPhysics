# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 19:15:25 2020

@author: jakri
"""

'''
Jake Richter - HW 6 P7 

Golf ball trajectory 

'''
from numpy import exp , sqrt, pi, sin, cos 
import numpy as np
import matplotlib.pyplot as plt

def f(v,t):
    vx = v[0]
    vy = v[1]
    vmag = sqrt(vx**2 + vy**2)
    
    # Finding the value to use for C in drage force 
    Cx = 0.9
    if vx <= 14 :
        Cx = .5 
    else :
        Cx = 7./vx
    
    Cy = .5
    if vy <= 14:
        Cy = .5
    else:
        Cy = 7./vy
        
        
    # Listing the constants
                   
    p0 = 1.275                  # Air density 
    A = .00562287  # Cross-Section Area
    m = (.04593)              # mass of ball in kg
    g = 9.81                    # gravity 
    
    # Equations of motion 
    
    f1 = -Cx * p0 * A * vx * (vmag)/m - .25 * vy 
    f2 = -Cy * p0 * A * vy * (vmag)/m - .25 * vx   - g
    
    # Returning the values of the equations of motions
    return np.array([f1,f2])

def f2(v,r,t):
    x = r[0]
    y = r[1]
    
    vx = v[0]
    vy = v[1]
    
    f1 = vx
    f2 = vy
    
    # Returning the values of the equations of motions
    return np.array([f1,f2])


def Euler_Method(function1,function2,N,t0, tf,v0, theta0):
    
    h = (tf - t0)/N
    time = np.arange(t0,tf,h)
    vp = np.zeros([len(time),2])
    xp = np.zeros([len(time),2])
    
    
    vx0 = v0*cos(theta0*pi/180)
    vy0 = v0*sin(theta0*pi/180)
    
    x0, y0 = 0.0, 0.0
    
    v = np.array([vx0, vy0])
    x = np.array([x0 , y0])
    
    for i, t in enumerate(time): 
        
        
        
        vp[i,:] = v
        v += h*function1(v,t)
        
        
        xp[i,:] = x 
        
        x +=  (h*v)
        
        
        
        
        
        
            
    '''
    vtit = str(v0)
    plt.figure()
    plt.title('Velocity vs Time, v0 = '+vtit)
    plt.plot(time,vp)
    plt.show()
    '''
    return time, vp, xp

# Argument values 
ti = 0.000 
tf = 5

v0 = 70
npoints = 1000


t , vps, pos = Euler_Method(f,f2,npoints, ti,tf, v0,9)
t, vps2, pos2 = Euler_Method(f,f2, npoints,ti,tf,v0,9)
vxs = vps[:,0]
vys = vps[:,1]

xs = pos[:,0]
ys = pos[:,1]
#print(vys)
#print(vxs)

plt.figure()
plt.plot(xs, ys)
plt.xlim(0,300)
plt.ylim(0,80)

# plt.plot(t, vys)

plt.figure()
plt.plot(vys,vxs)
plt.show()





