# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 21:20:11 2020

@author: jakri
"""

'''
Jake Richter - HW6 Problem 4

correction for change in air density 

'''

import numpy as np
from numpy import pi, sin, sqrt, cos,exp 
import matplotlib.pyplot as plt 

def fun4b(r,t,m):
    r = np.array(r)
    x = r[0]
    y = r[1]
    vx = r[2]
    vy = r[3]
    
    b2 = 4e-5
    g = 9.81
    a = 6.5e-3
    t2 = sqrt(vx*vx + vy*vy)
    po = 1.275
    T0 = 300 #kelvin
    alpha = 2.5
    p = (1 - (a*y)/T0)**2.5
    
    f1 = vx
    f2 = vy
    f3 = - vx * b2*t2*p
    f4 = -g - vy*b2*t2*p
    return np.array([f1,f2,f3,f4])

def fun4a(r,t,m):
    r = np.array(r)
    x = r[0]
    y = r[1]
    vx = r[2]
    vy = r[3]
    b2 = 4e-5
    g = 9.81
    t2 = sqrt(vx*vx + vy*vy)
    po = 1.275
    T0 = 300 #kelvin
    alpha = 2.5
    y0 = 10**4
    p = po*exp(-y/y0)
    
    f1 = vx
    f2 = vy
    f3 = - vx * b2*t2*(p/po)
    f4 = -g - vy*b2*t2*(p/po)
    return np.array([f1,f2,f3,f4])

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

# Choosing the initial conditions to plug in
theta0s = np.array([ 35.0, 45.0, ])
npoints = 10000
vi = 700
tf = 1000

# Initializing x,y positions that will later be used to plot

xs = np.empty([npoints,1])
ys = np.empty([npoints,1])

xs2 = np.empty([npoints,1])
ys2 = np.empty([npoints,1])



# Creating a Color list to help clarify plot

color = ['r','b']



# Plotting the Figures  - for the Adibiatic Case
plt.figure()
for i,t0 in enumerate(theta0s):
    t0tit = str(t0)
    xs,ys = Numerical_DE(fun,0,tf,npoints,0,0,vi,t0,1)
    xs2, ys2 = Numerical_DE(fun4b,0,tf,npoints,0,0,vi,t0,1)
    plt.plot(xs/1000,ys/1000, label = 'No Density Correction: Theta0 = ' + t0tit+' degrees', color = color[i], linestyle = ':')
    plt.plot(xs2/1000,ys2/1000,label = 'Density Correction: Theta0 = ' + t0tit+' degrees', color = color[i] )
plt.title('Density Correction: Adibiatic Approx.')
plt.xlabel('x (Km)')
plt.ylabel('y (Km)')
plt.ylim(0,15)
plt.xlim(0,30)
plt.legend()
plt.show()


# Plotting figures - Constant Temperature

plt.figure()
for i,t0 in enumerate(theta0s):
    t0tit = str(t0)
    xs,ys = Numerical_DE(fun,0,tf,npoints,0,0,vi,t0,1)
    xs2, ys2 = Numerical_DE(fun4a,0,tf,npoints,0,0,vi,t0,1)
    plt.plot(xs/1000,ys/1000, label = 'No Density Correction: Theta0 = ' + t0tit+' degrees', color = color[i], linestyle = ':')
    plt.plot(xs2/1000,ys2/1000,label = 'Density Correction: Theta0 = ' + t0tit+' degrees', color = color[i] )
plt.title('Density Correction: Constant Temp Approx.')
plt.xlabel('x (Km)')
plt.ylabel('y (Km)')
plt.ylim(0,15)
plt.xlim(0,30)
plt.legend()
plt.show()

