# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 19:32:05 2020

@author: jakri
"""

import numpy as np 
from numpy import sin,pi, cos, arctan
import matplotlib.pyplot as plt

def f(r,t):
    theta = r[0]
    omega = r[1]
    g = 9.81 # m/s^2
    l = .1   # m
    g_l = g/l
    f1 = omega
    f2 = -g_l*sin(theta)

    return np.array([f1,f2]) 

def Numerical_DE(t0,tf,N,theta0):
    theta0 *= np.pi/180
    omega0 = 0.0
    
    h = (tf-t0)/N                               # creating the step size h
    half = .5 
    sixth = 1/6          

    time = np.arange(t0,tf,h)                   # creating the time steps
    r = np.empty((len(time),2),dtype = float)   # intializing x, y 
    
    r[0][0] = theta0
    r[0][1] = omega0
    for c,t in enumerate(time):                 # to animate - go through this for loop to get the updated pos/velocity 
                                                                                            
        if c == N-1:
            break 
        else :
            k1 = h*f(r[c,:],t)
            k2 = h*f(r[c,:] + half*k1, t + half*h)
            k3 = h*f(r[c,:] + half*k2, t + half*h)
            k4 = h*f(r[c,:] + k3, t + h)
            r[c+1,:] = r[c,:] + sixth*(k1 + 2*k2 + 2*k3 + k4)

    
    thetal = r[:,0]
    omegal = r[:,1]

    
    plt.figure()

    plt.plot(time,thetal)

    plt.show()
    
    return thetal, omegal, time 


theta, omega, time = Numerical_DE(0,15,1000,179)

''' 
Part B: Creating the animation 
'''
from vpython import box,sphere, cylinder, color, vector,rate  

radi = .5
vlength = .1

ball = sphere(pos = vector(vlength*cos(theta[0]),vlength*sin(theta[0]),0), radius = radi, color = color.red)
rod  = cylinder(pos = vector(0,0,0), axis = vector(vlength*cos(theta[0]),vlength*sin(theta[0]),0), radius = radi )
xhat = cylinder(pos = vector(0,0,0), axis = vector(vlength,0,0), radius = .1*radi) # Basis vectors for easy viewing
yhat = cylinder(pos = vector(0,0,0), axis = vector(0,vlength,0), radius = .1*radi, color = color.blue)
zhat = cylinder(pos = vector(0,0,0), axis = vector(0,0,vlength), radius = .1*radi, color = color.red)
# base = box( pos = vector(0,0,0), length = .01, height = .01, width = .01)
while True: 
    for degree in theta:
        rate(30)
        ball.pos = vector(vlength*sin(degree),-vlength*cos(degree ),0)
        rod.axis = vector(vlength*sin(degree),-vlength*cos(degree ),0)
    
        





