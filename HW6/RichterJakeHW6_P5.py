# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 22:07:37 2020

@author: jakri
"""

'''
Jake Richter HW6 - P5

'''

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
    
    
    '''
    plt.figure()

    plt.plot(xl,yl)
    plt.xlim(0,250)
    plt.ylim(0,100)

    plt.show()
    '''
    return xl, yl

# Choosing the initial conditions to plug in
theta0s = np.linspace(1,90,180)
npoints = 1000
vi = 49
tf = 8

xdistances1 = np.empty([len(theta0s),2]) # first column will be range, second will be angle
r = 0.0    
r2 = 0.0
r3 = 0.0                             # Initializing r, range - these will be elments of column 1

xdistances2 = np.empty([len(theta0s),2])
xdistances3 = np.empty([len(theta0s),2])

# Initializing x,y positions that will later be used to plot

xs = np.empty([npoints,1])
ys = np.empty([npoints,1])

xs2 = np.empty([npoints,1])
ys2 = np.empty([npoints,1])


xs3 = np.empty([npoints,1])
ys3 = np.empty([npoints,1])



# Finding theta0 that gives maximum range - With no Change head/tail wind
plt.figure()
for i, t0 in enumerate(theta0s):
    xs,ys = Numerical_DE(fun5a,0,tf,npoints,0,0,vi,t0,1)
    plt.plot(xs,ys)
    
    for k,y in enumerate(ys):
        if y > -1e-1 and y < 1e-1 and xs[k] > 0.0:
            r = xs[k]
    xdistances1[i,:] = np.array([r,t0])
    
plt.ylim(0,100)
plt.xlim(0,150)
plt.show()

print('Angle of Farthest distance is',xdistances1[np.argmax(xdistances1[:,0]),1], 'Max distance is',xdistances1[np.argmax(xdistances1[:,0]),0])
    

# Finding Theta0 that gives max range with Head/Tail wind

plt.figure()
for i2, t02 in enumerate(theta0s):
    
    
    xs2,ys2 = Numerical_DE(fun5bh,0,tf,npoints,0,0,vi,t02,1)
    
    xs3, ys3 = Numerical_DE(fun5bt,0,tf,npoints,0,0,vi,t02,1)
    
    
    plt.plot(xs2,ys2)
    plt.plot(xs3,ys3)
    
    
    for k2,y2 in enumerate(ys2):
        if y2 > -1.0 and y2 < 1.0 and xs2[k2] > 0.0:
            r2 = xs2[k2]
    xdistances2[i2,:] = np.array([r2,t02])
    
    
    for k3,y3 in enumerate(ys2):
        if y3 > -1.0 and y3 < 1.0 and xs3[k3] > 0.0:
            r3 = xs3[k3]
    
    xdistances3[i2,:] = np.array([r3,t02])
        
    
    
plt.ylim(0,100)
plt.xlim(0,150)
plt.show()


print('Angle of Farthest distance is - Head wind',xdistances2[np.argmax(xdistances2[:,0]),1], 'Max Distance',xdistances2[np.argmax(xdistances2[:,0]),0])
print('Angle of Farthest distance is - tail wind',xdistances3[np.argmax(xdistances3[:,0]),1],'Max Distance',xdistances3[np.argmax(xdistances3[:,0]),0])





# Finding the speeed of Baseball as it crosses homeplate

# Assume launch at an angle of -7 degrees, y0 = 2m , xf = 18.44meters


'''

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

'''
