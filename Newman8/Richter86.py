# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 19:02:32 2020

@author: jakri

HW 5 8.6 - Harmonic and anharmonic oscilators 

(a) Turn second order equation into two coupled first order 
equations then write a program to solve them for the case 
omega = 1 in the range from t = 0 to t = 50 

use x = 1 and dx/dt = 0 as the initial conditions 
Make a graph showing x vs time 


(b) Increase the amplitude of the oscillations by making the 
initial value of x = 2 confirm that the period is about the same


(c) modify to solve the motion of the anharmonic oscillator 
d2x/dt2 = -w^2 * x^3 
and take w = 1 with x = 1 dx/dt = 0 as the initial conditions

(d) Modify so that it plots dx/dt against x - phase space

(e) the vander pol oscilator in optical physics 
modify the program to solve the equation from t = 0 to t = 20 
make a phase space plot with
"""
import numpy as np
from numpy import sin, cos
import matplotlib.pyplot as plt 

# Part A #

def f(r,t,w):
    x = r[0]
    row = r[1]
    
    w = 1.0 
    f1 = row
    f2 =-w**2 * x

    return np.array([f1,f2]) 

def Numerical_DE(t0,tf,N,row0,x0):
    
    
    h = (tf-t0)/N                               # creating the step size h
    half = .5 
    sixth = 1/6          

    time = np.arange(t0,tf,h)                   # creating the time steps
    r = np.empty((len(time),2),dtype = float)   # intializing x, y 
    
    r[0][0] = row0
    r[0][1] = x0
    for c,t in enumerate(time):                 # to animate - go through this for loop to get the updated pos/velocity 
                                                                                            
        if c == N-1:
            break 
        else :
            k1 = h*f(r[c,:],t,1)
            k2 = h*f(r[c,:] + half*k1, t + half*h,1)
            k3 = h*f(r[c,:] + half*k2, t + half*h,1)
            k4 = h*f(r[c,:] + k3, t + h,1)
            r[c+1,:] = r[c,:] + sixth*(k1 + 2*k2 + 2*k3 + k4)

    
    rowl = r[:,0]
    xl = r[:,1]

    
    plt.figure()

    plt.plot(time,xl)

    plt.show()
    
    # return thetal, omegal, time 
Numerical_DE(0,50,10000,0,1)


# Part B # 

Numerical_DE(0,50,10000,0,2)

# Part C/D Phase spaces # 
def f2(r,t,w):
    x = r[0]
    row = r[1]
    
    w = 1.0 
    f1 = row
    f2 =-w**2 * x**3

    return np.array([f1,f2]) 
def Numerical_DE2(t0,tf,N,row0,x0):
    
    
    h = (tf-t0)/N                               # creating the step size h
    half = .5 
    sixth = 1/6          

    time = np.arange(t0,tf,h)                   # creating the time steps
    r = np.empty((len(time),2),dtype = float)   # intializing x, y 
    
    r[0][0] = row0
    r[0][1] = x0
    for c,t in enumerate(time):                 # to animate - go through this for loop to get the updated pos/velocity 
                                                                                            
        if c == N-1:
            break 
        else :
            k1 = h*f2(r[c,:],t,1)
            k2 = h*f2(r[c,:] + half*k1, t + half*h,1)
            k3 = h*f2(r[c,:] + half*k2, t + half*h,1)
            k4 = h*f2(r[c,:] + k3, t + h,1)
            r[c+1,:] = r[c,:] + sixth*(k1 + 2*k2 + 2*k3 + k4)

    
    rowl = r[:,0]
    xl = r[:,1]

    
    plt.figure()

    plt.plot(time,xl)
    plt.figure()
    plt.title('Phase Space')
    plt.plot(xl,rowl)

    plt.show()
    
Numerical_DE2(0,50,10000,0,1)
Numerical_DE2(0,50,10000,0,2)

# Part E # 
def fe(r,t,w,u):
    x = r[0]
    row = r[1]
    
    w = 1.0 
    f1 = row
    f2 = u*(1 - x**2)*row - w**2 *x

    return np.array([f1,f2])

def Numerical_DEE(t0,tf,N,row0,x0, w, u):
    
    
    h = (tf-t0)/N                               # creating the step size h
    half = .5 
    sixth = 1/6          

    time = np.arange(t0,tf,h)                   # creating the time steps
    r = np.empty((len(time),2),dtype = float)   # intializing x, y 
    
    r[0][0] = row0
    r[0][1] = x0
    for c,t in enumerate(time):                 # to animate - go through this for loop to get the updated pos/velocity 
                                                                                            
        if c == N-1:
            break 
        else :
            k1 = h*fe(r[c,:],t,w,u)
            k2 = h*fe(r[c,:] + half*k1, t + half*h,w,u)
            k3 = h*fe(r[c,:] + half*k2, t + half*h,w,u)
            k4 = h*fe(r[c,:] + k3, t + h,w,u)
            r[c+1,:] = r[c,:] + sixth*(k1 + 2*k2 + 2*k3 + k4)

    
    rowl = r[:,0]
    xl = r[:,1]

    
    plt.figure()

    plt.plot(time,xl)
    plt.figure()
    plt.title('Phase Space')
    plt.plot(xl,rowl)

    plt.show()

Numerical_DEE( 0 , 20 ,10000, 0, 1,  1,  1)
    
Numerical_DEE(0,20,10000,  0,  1,  1, 2)
Numerical_DEE(0,20,10000, 0,  1, 1, 4)