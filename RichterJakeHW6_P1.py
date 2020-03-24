# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 19:31:50 2020

@author: jakri
"""

'''
Jake Richter - HW6 P1 - Terminal Velocity  
via Euler Method 

'''
import numpy as np 
import matplotlib.pyplot as plt 
from numpy import sin, cos 


def f(v,t, b):
    a = 10.0 
    b= 1
    return (a - b*v)

def Euler_Method(function,N,t0, tf,v0,b):
    h = (tf - t0)/N
    time = np.arange(t0,tf,h)
    v = v0
    vp = np.empty(len(time))
    
    for i, t in enumerate(time): 
        vp[i] = v
        v += h*function(v,t,b)
    
    vtit = str(v0)
    plt.figure()
    plt.title('Velocity vs Time, v0 = '+vtit)
    plt.plot(time,vp)
    plt.show()
    
    return time, vp, h, vtit
    

t1, v1, h, vtit1 = Euler_Method(f,10000,0,120,1,1)
t2, v2, h2, vtit2 = Euler_Method(f,10000,60,120,50,1)
t3, v3, h3, vtit3 = Euler_Method(f,10000,0,120,50,1)

plt.figure()
plt.title('Two Divers - deploying parachute at different times ')
plt.plot(t1,v1, label = 'V0 = '+vtit1 )
plt.plot(t2,v2, label = 'V0 = '+vtit2)
plt.legend()
plt.show()

plt.figure()
plt.title('Two divers- w/ same starting time but different v0')
plt.plot(t1,v1, label = 'V0 = '+vtit1 )
plt.plot(t3,v3, label = 'V0 = '+vtit3)
plt.legend()
plt.show()

    