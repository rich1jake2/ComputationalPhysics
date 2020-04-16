# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 22:38:38 2020

@author: jakri
"""

'''
Jake Richter 8.9 

Vibration in one d 
'''
import numpy as np
from numpy import pi, sin, sqrt, cos 
import matplotlib.pyplot as plt 

def fn(r,t):
    w = 2.0 
    k = 6.0 
    m = 1.0 # kg
    r = np.array(r, dtype = float)
    # print(r)
    
    
    F1 = cos(w*t)
    fs = np.empty(len(r)//2, dtype = float)
    ds = np.empty(len(r//2), dtype = float)
    ps = np.empty(len(r//2), dtype = float)
    
    ds = r[0:len(r)//2]
    ps = r[len(r)//2:len(r)]
    #print(ds)
    #print(ps)
    
    for i in range(len(ds)):
        if i == 0: 
            fs[i] = (k/m)*(ds[1] - ds[0]) + (F1/m)
        elif i == len(ds)- 1:
            fs[i] = (k/m)*(ds[-2] - ds[-1])
        else:
            fs[i] = (k/m)*(ds[i+1] - ds[i]) + (k/m)*(ds[i-1] - ds[i])
            
            
        
    #print(fs)
    final = np.append(ps,fs)
    #print(final)
    #print(final)
    return final

def Numerical_DE(oscN,t0,tf,N):
    
    
    h = (tf-t0)/N                               # creating the step size h
    half = .5 
    sixth = 1/6          

    time = np.arange(t0,tf,h)                       # creating the time steps
    r = np.zeros((len(time),2*oscN),dtype = float)   # Creating R-vector - initalizing all to 0 
    
    
    
    for c,t in enumerate(time):                 # to animate - go through this for loop to get the updated pos/velocity 
                                                                                            
        if c == N-1:
            break 
        else :
            k1 = h*fn(r[c,:],t)
            k2 = h*fn(r[c,:] + half*k1, t + half*h)
            k3 = h*fn(r[c,:] + half*k2, t + half*h)
            k4 = h*fn(r[c,:] + k3, t + h)
            r[c+1,:] = r[c,:] + sixth*(k1 + 2*k2 + 2*k3 + k4)
            
    plt.figure()
    for i in range(len(r[c,:])//2):
        plt.plot(time,r[:,i])
    plt.xlim(0,20)
    #plt.ylim(0,.4)
    plt.show()
    
    return r,time,oscN
rs, t, Nosc = Numerical_DE(5,0,20,1000)


from vpython import box,sphere, cylinder, color, vector,rate  


radi = .105

balls = np.empty(Nosc, sphere)

displ = rs[:,:Nosc]

print(len(displ[0,:]))
for k in range(5):

        balls[k] = sphere(pos = vector(.75*k,0,0), radius = radi, color = color.red)
while True:
    for x in range(len(displ[:,0])):
        rate(100)
        for i,b in enumerate(balls):
            b.pos = vector(.75*i - displ[x,i],0,0)
        