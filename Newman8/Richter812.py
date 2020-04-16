# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 17:28:15 2020

@author: jakri
"""

'''
Richter 8.12 - The verlet Method 

'''
import numpy as np 
from numpy import sin, cos, sqrt
import matplotlib.pyplot as plt


def F(r,t):
    x = r[0]
    y = r[1]
    vx = r[2]
    vy = r[3]
    
    G = 6.6738e-11*(8760*60**2)**2
    M = 1.9891e30
    gm = G*M
    
    rmag = sqrt(x**2 + y**2)
    
    f1 = vx
    f2 = vy 
    f3 = -gm*x/(rmag**3)
    f4 = -gm*y/(rmag**3)
    
    final = np.array([f1,f2,f3,f4], dtype = float)
    
    return final 

def Verlet_Meth():
    h = 1/8760.           # Step size 1 hour
    yr = 3       # Hours in a year 
    
    
    time = np.arange(0,yr+h,h) 
    
    r = np.zeros([len(time),4], dtype = float)
    r[0,:] = np.array([1.47e11, 0, 0, 3.0287e4*3600*8760.])
    
    v = np.array([r[:,2],r[:,3]])
    v = v.T
    
    v[1,:] = v[0,:] + [ .5*h*F(r[0,:],0)[0], .5*h*F(r[0,:],0)[1] ] 
    
    vm =  r[0 , 2:4] + .5*h*(F(r[0,:],0)[2:4])
    
    for i,t in enumerate(time):
        if i == len(time) - 1:
            break
        else:
            r[i + 1, 0:2] = r[i, 0:2] + h*vm
        
        
        
            k = h*F(r[i + 1,:],0)
        
        
            v[i + 1,:] = vm + [k[2]*.5, k[3]*.5]
            vm += [k[2],k[3]]
        
        
        
        

        
    
   
    # v[1,:] = v[0,:] + [.5*h*F(r[0,:],0)[0], .5*h*F(r[0,:],0)[1]] 
    
    
    return v,r,time


    
   
vi, xi, times = Verlet_Meth()

plt.figure()
plt.plot(xi[:,0],xi[:,1])
#plt.xlim(-1.48e11,-1.44e11)
plt.show()

# Plotting energy#
m = 5.9722e24
G = 6.6738e-11
M = 1.9891e30

kenergy = .5*m*((vi[:,0]/(3600*8760))**2 + (vi[:,1]/(3600*8760))**2)
penergy = -G*M*m/sqrt((xi[:,0]**2 + (xi[:,1]**2)))
tenergy = kenergy + penergy

plt.figure()
a = plt.plot(times,kenergy, label = 'kinetic energy')

b = plt.plot(times,penergy, label = 'Potential Energy')

c = plt.plot(times,tenergy, label = 'Total Energy')
plt.legend()
plt.show()

plt.figure()
plt.title('Total Energy')
plt.plot(times,tenergy)
plt.show()
