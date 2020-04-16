# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 20:11:11 2020

@author: jakri
"""

'''
Jake Richter 8.7 - Trajectory with air resistance 

(a) Starting with Newton's second law f = ma show that the x, y equaitons with air resistacne

(b) make the set of second order equations into four first order 
solve them with a computer 

plot the trajectory y vs x 

(c) Figure out how a change in mass effects the range of the cannon ball 

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
    p = 1.22
    R = .08
    c = .47
    g = 9.81
    
    t1 = pi*R**2*p*c*(1/2)
    t2 = sqrt(vx*vx + vy*vy)
    
    
    f1 = vx
    f2 = vy
    f3 = - (t1 * vx * t2)/m
    f4 = -g - (t1*vy*t2)/m
    return np.array([f1,f2,f3,f4])

def Numerical_DE(t0,tf,N,x0,y0,v0,theta0,m):
    
    
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
            k1 = h*fun(r[c,:],t,m)
            k2 = h*fun(r[c,:] + half*k1, t + half*h,m)
            k3 = h*fun(r[c,:] + half*k2, t + half*h,m)
            k4 = h*fun(r[c,:] + k3, t + h,m)
            r[c+1,:] = r[c,:] + sixth*(k1 + 2*k2 + 2*k3 + k4)

    
    
    xl = r[:,0]
    yl = r[:,1]
    

    
    plt.figure()

    plt.plot(xl,yl)
    plt.xlim(0,250)
    plt.ylim(0,100)

    plt.show()
    
    # return thetal, omegal, time 
Numerical_DE(0,10,10000,0,0,100,30,1)



# Part C - Plotting Range vs Mass #

def Numerical_DE2(t0,tf,N,x0,y0,v0,theta0,m):
    
    
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
            k1 = h*fun(r[c,:],t,m)
            k2 = h*fun(r[c,:] + half*k1, t + half*h,m)
            k3 = h*fun(r[c,:] + half*k2, t + half*h,m)
            k4 = h*fun(r[c,:] + k3, t + h,m)
            r[c+1,:] = r[c,:] + sixth*(k1 + 2*k2 + 2*k3 + k4)

    
    
    xl = r[:,0]
    yl = r[:,1]
    
    for c,l in enumerate(yl):
        if  l < 1 and l > -1: 
            distance = xl[c]
    #print(distance)
    
    
    return distance, xl,yl
            
mass = np.arange(.5, 5, .05)
r    = np.empty(len(mass))
plt.figure()
for i,m in enumerate(mass):
    r[i],x,y = Numerical_DE2(0,10,1000,0,0,100,30,m)
    plt.plot(x,y)
plt.xlim(0,1000)
plt.ylim(0,125)
plt.show()
plt.figure()
plt.title('Range Vs Mass')
plt.plot(mass,r)
plt.show()
    

    
    