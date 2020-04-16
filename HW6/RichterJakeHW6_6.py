# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 11:58:46 2020

@author: jakri
"""

'''
Jake Richter - HW6 P6

'''
import numpy as np
from numpy import pi, sin, sqrt, cos,exp 
import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D

def fun6(r,t,m):
    r = np.array(r)
    x = r[0]
    y = r[1]
    z = r[2]
    vx = r[3]
    vy = r[4]
    vz = r[5]
    
    vd = 35
    delv = 5
    
    p0 = 1.275
    a = 6.5e-3
    alpha = 2.5
    T0 = 300
    
    p = p0*(1 - (a*y)/T0)**alpha
    
    vwind = 4.470 # in y direction
    
    b2x = .0039 + .0058/(1 + exp((vx - vd)/delv))
    b2y = .0039 + .0058/(1 + exp((vy - vd)/delv))
    b2z = .0039 + .0058/(1 + exp((vz - vd)/delv))
    
    
    g = 9.81
    
    t2 = sqrt(vx**2 + vy**2 + vz**2)
    
    
    
    f1 = vx
    f2 = vy
    f3 = vz
    f4 = - vx * b2x * t2
    f5 = - vy  * b2y * t2
    f6 = -g - vz * b2z * t2 
    
    return np.array([f1,f2,f3,f4,f5,f6])
def fun6_air(r,t,m):
    r = np.array(r)
    x = r[0]
    y = r[1]
    z = r[2]
    vx = r[3]
    vy = r[4]
    vz = r[5]
    
    vd = 35
    delv = 5
    
    p0 = 1.275
    a = 6.5e-3
    alpha = 2.5
    T0 = 300
    
    p = p0*(1 - (a*y)/T0)**alpha
    
    vwind = 4.470 # in y direction
    
    b2x = .0039 + .0058/(1 + exp((vx - vd)/delv))
    b2y = .0039 + .0058/(1 + exp(((vy - vwind) - vd)/delv))
    b2z = .0039 + .0058/(1 + exp((vz - vd)/delv))
    
    
    g = 9.81
    
    t2 = sqrt(vx**2 + (vy - vwind)**2 + vz**2)
    
    
    
    f1 = vx
    f2 = vy
    f3 = vz
    f4 = - vx * b2x * t2
    f5 = - (vy - vwind) * b2y * t2
    f6 = -g - vz * b2z * t2 
    
    return np.array([f1,f2,f3,f4,f5,f6])

def Numerical_DEz(fs,t0,tf,N,x0,y0,z0,v0,theta0,m):
    
    
    h = (tf-t0)/N                               # creating the step size h
    half = .5 
    sixth = 1/6          

    time = np.arange(t0,tf,h)                   # creating the time steps
    r = np.empty((len(time),6),dtype = float)   # intializing x, y 
    
    r[0][0] = x0
    r[0][1] = y0
    r[0][2] = z0
    r[0][3] = v0*cos(theta0*pi/180)
    r[0][4] = 0.0
    r[0][5] = v0*sin(theta0*pi/180)
    
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
    zl = r[:,2]
    
    
    '''
    plt.figure()

    plt.plot(xl,yl)
    plt.xlim(0,250)
    plt.ylim(0,100)

    plt.show()
    '''
    return xl, yl, zl 

tf = 10 
Npoints = 10000
x0 = y0 = z0 = 0
theta0 = 70
v0 = 49 

x, y, z = Numerical_DEz(fun6_air,0,tf,Npoints,x0,y0,z0,v0,theta0,0.0)
xx, yy, zz = Numerical_DEz(fun6,0,tf,Npoints,x0,y0,z0,v0,theta0,0.0)

#Cutting of Specific values
xn = []
yn = []
zn = []
xn2 = []
yn2 =[] 
zn2 = []
for i,zk in enumerate(z):
    xn.append(x[i])
    yn.append(y[i])
    zn.append(zk)
    if zk < 1e-2 and zk > -1e-2 and x[i] > 30:
        xn = np.array(xn)
        yn = np.array(yn)
        zn = np.array(zn)
        break

for j, zt in enumerate(zz):
    xn2.append(xx[j])
    yn2.append(yy[j])
    zn2.append(zt)
    if zt< 1e-2 and zt > -1e-2 and xx[j] > 20:
        xn2 = np.array(xn2)
        yn2 = np.array(yn2)
        zn2 = np.array(zn2)
        break
    

x, y, z = xn, yn, zn
xx, yy, zz = xn2, yn2, zn2
        
        
        

fig = plt.figure()

ax = Axes3D(fig)
ax.plot(xs = x,ys = y,zs = z)
ax.plot(xs = xx, ys = yy, zs = zz )
ax.set_zlim(0,50)

plt.xlim(-4,150)
plt.ylim(-4,20)
# ax.zlim(0,150)
plt.show()

print('Magnitude Difference between trajectory with no wind and with wind:')
print(sqrt((xx[-1] - x[-1])**2 + (yy[-1] -y[-1] )**2))
