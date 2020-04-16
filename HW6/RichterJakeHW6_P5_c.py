# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 01:30:47 2020

@author: jakri
"""

import numpy as np
from numpy import pi, sin, sqrt, cos,exp 
import matplotlib.pyplot as plt 

def fun5a(r,t,m):
    r = np.array(r)
    x = r[0]
    y = r[1]
    vx = r[2]
    vy = r[3]
    
    vd = 35
    delv = 5
    
    p0 = 1.275
    a = 6.5e-3
    alpha = 2.5
    T0 = 300
    
    p = p0*(1 - (a*y)/T0)**alpha
    
    b2x = .0039 + .0058/(1 + exp((vx - vd)/delv))
    b2y = .0039 + .0058/(1 + exp((vy - vd)/delv))
    
    
    g = 9.81
    t2 = sqrt(vx*vx + vy*vy)
    
    
    
    f1 = vx
    f2 = vy
    f3 = - vx * b2x*t2
    f4 = -g - vy* b2y * t2 
    return np.array([f1,f2,f3,f4])

def fun5bt(r,t,m):
    r = np.array(r)
    x = r[0]
    y = r[1]
    vx = r[2]
    vy = r[3]
    
    vwind = 24*.447
    
    g = 9.81
   
    t2 = sqrt(((vx-vwind)**2 + vy*vy))
    
    p0 = 1.275
    a = 6.5e-3
    alpha = 2.5
    T0 = 300
    
    p = p0*(1 - (a*y)/T0)**alpha
    
    vd = 35
    delv = 5
    
    
    
    
    b2x = (.0039 + .0058/(1 + exp(((vx -vwind) - vd)/delv)))
    b2y = (.0039 + .0058/(1 + exp((vy - vd)/delv)))
    
    
    f1 = vx
    f2 = vy
    f3 = - (vx-vwind) * b2x * t2 
    f4 = -g - vy * b2y * t2
    
    return np.array([f1,f2,f3,f4])


def fun5bh(r,t,m):
    r = np.array(r)
    x = r[0]
    y = r[1]
    vx = r[2]
    vy = r[3]
    
    
    g = 9.81
    vwind = 25*.447
    
    p0 = 1.275
    a = 6.5e-3
    alpha = 2.5
    T0 = 300
    
    p = p0*(1 - (a*y)/T0)**alpha
    t2 = sqrt(((vx + vwind)**2 + vy*vy))
    vd = 35
    delv = 5
    
    
    
    
    b2x = (.0039 + .0058/(1 + exp(((vx + vwind) - vd)/delv)))
    b2y = (.0039 + .0058/(1 + exp((vy - vd)/delv)))
    
    
    
    
    f1 = vx
    f2 = vy
    f3 = - (vx + vwind) * b2x * t2
    f4 = -g - vy * b2y * t2 
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
    
    vx = r[:,2]
    vy = r[:,3]
    
    
    
    '''
    plt.figure()

    plt.plot(xl,yl)
    plt.xlim(0,250)
    plt.ylim(0,100)

    plt.show()
    '''
    return xl, yl, vx, vy

# Find final velocity 
npoints = 10000
y0 = 2
theta0 = 0
v0 = 44.704

    
x1, y1, vx1, vy1 = Numerical_DE(fun5a,0,5,npoints,0,y0,v0,theta0,0)
x2, y2, vx2, vy2 = Numerical_DE(fun5bt,0,5,npoints,0,y0,v0,theta0,0)
x3, y3, vx3, vy3 = Numerical_DE(fun5bh,0,5,npoints,0,y0,v0,theta0,0)

plt.figure()
plt.plot(x1,y1, c = 'r')
plt.plot(x2,y2, c = 'b')
plt.plot(x3,y3, c = 'k')
plt.ylim(0,20)
plt.xlim(0,20)
plt.show()

for k,x in enumerate(x1):
    if x >=  18.44:
        print('End Velocity - No wind',sqrt(vx1[k]**2 + vy1[k]**2))
        break
for i,xx in enumerate(x2):
    if xx >=  18.44:
        print('End Velocity - Tail Wind',sqrt(vx2[i]**2 + vy2[i]**2))
        break
for j, xxx in enumerate(x3):
    if xxx >= 18.44:
        print('End Velocity - Head Wind', sqrt(vx3[j]**2 + vy3[j]**2))
        break
        
        

