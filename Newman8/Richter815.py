# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 21:03:17 2020

@author: jakri
"""

'''
Richter 8.15 - Double Pendulum 

'''
import numpy as np 
from numpy import sin, cos, sqrt
import matplotlib.pyplot as plt

def f(r,t):
    t1 = r[0]
    t2 = r[1]
    w1 = r[2]
    w2 = r[3]
    g = 9.81 # m/s^2
    l = .4   # m
    g_l = g/l
    
    f1 = w1
    f2 = w2
    f3 = -(w1**2*sin(2*t1 - 2*t2) + 2*w2**2*sin(t1 - t2) + g_l*(sin(t1 - 2*t2)+ 3*sin(t1)))/(3 - cos(2*t1 - 2*t2))
    f4 = (4*w1**2*sin(t1 - t2) + w2**2*sin(2*t1 - 2*t2) + 2*g_l*(sin(2*t1 - t2)- sin(t2)))/(3 - cos(2*t1 - 2*t2))

    return np.array([f1,f2,f3,f4]) 

def Numerical_DE(t0,tf,N,t10,t20,w10,w20):
    t10 *= np.pi/180
    t20 *= np.pi/180
    w10 = 0.0
    w20 = 0.0
    h = (tf-t0)/N                               # creating the step size h
    half = .5 
    sixth = 1/6          

    time = np.arange(t0,tf,h)                   # creating the time steps
    r = np.empty((len(time),4),dtype = float)   # intializing x, y 
    
    r[0][0] = t10
    r[0][1] = t20
    r[0][2] = w10
    r[0][3] = w20
    
    for c,t in enumerate(time):                 # to animate - go through this for loop to get the updated pos/velocity 
                                                                                            
        if c == N-1:
            break 
        else :
            k1 = h*f(r[c,:],t)
            k2 = h*f(r[c,:] + half*k1, t + half*h)
            k3 = h*f(r[c,:] + half*k2, t + half*h)
            k4 = h*f(r[c,:] + k3, t + h)
            r[c+1,:] = r[c,:] + sixth*(k1 + 2*k2 + 2*k3 + k4)

    
    t1l = r[:,0]
    t2l = r[:,1]
    w1l = r[:,2]
    w2l = r[:,3]
    m = 1
    l = .4
    g = 9.81
    
    te = -(m * g * l * (2 * cos(t1l) + cos(t2l))) +  (m * (l ** 2) * (w1l ** 2 + 0.5 * w2l ** 2 + w1l * w2l * cos(t1l - t2l)))
    
    plt.figure()

    plt.plot(time,te)

    plt.show()
    
    return time, te, t1l,t2l


t, totale,t1,t2 = Numerical_DE(0,100,100000,90,90,0,0)

from vpython import box,sphere, cylinder, color, vector,rate  

radi = .05
vlength = .4

b1 = sphere(pos = vector(vlength*cos(t1[0]),vlength*sin(t1[0]),0), radius = radi, color = color.red)
r1  = cylinder(pos = vector(0,0,0), axis = vector(vlength*cos(t1[0]),vlength*sin(t1[0]),0), radius = .25*radi )

b2 = sphere(pos = vector(vlength*cos(t2[0]),vlength*sin(t2[0]),0), radius = radi, color = color.red)
r2  = cylinder(pos = vector(0,0,0), axis = vector(vlength*cos(t2[0]),vlength*sin(t2[0]),0), radius = .25*radi )

# base = box( pos = vector(0,0,0), length = .01, height = .01, width = .01)
while True: 
    for tt1,tt2 in zip(t1,t2):
        rate(300)
        b1.pos = vector(vlength*sin(tt1),-vlength*cos(tt1),0)
        r1.axis = vector(vlength*sin(tt1),-vlength*cos(tt1 ),0)
        
        
        r2.pos = vector(vlength*sin(tt1),-vlength*cos(tt1 ),0)
        r2.axis = vector(vlength*sin(tt2),-vlength*cos(tt2 ),0)
        b2.pos = r2.pos + r2.axis
        