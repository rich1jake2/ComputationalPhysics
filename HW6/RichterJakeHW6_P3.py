# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 20:34:20 2020

@author: jakri
"""

'''
Jake Richter - H6 P3 
Cannon Ball

'''

import numpy as np
from numpy import pi, sin, sqrt, cos 
import matplotlib.pyplot as plt 

def fun(r,t,m):
    r = np.array(r)
    x = r[0]
    y = r[1]
    vx = r[2]
    vy = r[3]
    b2 = 4e-5
    g = 9.81
    t2 = sqrt(vx*vx + vy*vy)
    
    f1 = vx
    f2 = vy
    f3 = - vx * b2*t2
    f4 = -g - vy*b2*t2
    return np.array([f1,f2,f3,f4])

def f(r,t,m):
    r = np.array(r)
    x = r[0]
    y = r[1]
    vx = r[2]
    vy = r[3]
    
    
    
    f1 = vx
    f2 = vy
    f3 = 0.0
    f4 = -g 
    return np.array([f1,f2,f3,f4])

def Numerical_DE(fs,t0,tf,N,x0,y0,v0,theta0,m):
    
    
    h = (tf-t0)/N                               # creating the step size h
    half = .5 
    sixth = 1/6          

    time = np.arange(t0,tf,h)                   # creating the time steps
    r = np.empty((len(time),4),dtype = float)   # intializing x, y 
    
    r[0][0] = x0
    r[0][1] = y0
    r[0][2] = v0*cos(theta0*pi/180)
    r[0][3] = v0*sin(theta0*pi/180)
    
    for c,t in enumerate(time):                 # to animate - go through this for loop to get the updated pos/velocity 
                                                                                            
        if c == N-1:
            break 
        else :
            k1 = h*fs(r[c,:],t,m)
            k2 = h*fs(r[c,:] + half*k1, t + half*h,m)
            k3 = h*fs(r[c,:] + half*k2, t + half*h,m)
            k4 = h*fs(r[c,:] + k3, t + h,m)
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
    return xl, yl
    
theta0s = np.array([30.0, 35.0, 40.0, 45.0, 50.0, 55.0])
npoints = 10000
vi = 700
tf = 1000

xs = np.empty([npoints,1])
ys = np.empty([npoints,1])



plt.figure()
for i,t0 in enumerate(theta0s):
    t0tit = str(t0)
    xs,ys = Numerical_DE(f,0,tf,npoints,0,0,vi,t0,1)
    plt.plot(xs,ys, label = 'Initial angle = ' + t0tit+' degrees')
plt.ylim(0,20000)
plt.xlim(0,80000)
plt.legend()
plt.show()


plt.figure()
for i,t0 in enumerate(theta0s):
    t0tit = str(t0)
    xs,ys = Numerical_DE(fun,0,tf,npoints,0,0,vi,t0,1)
    plt.plot(xs,ys, label = 'Initial angle = ' + t0tit+' degrees')
plt.ylim(0,10000)
plt.xlim(0,50000)
plt.legend()
plt.show()

