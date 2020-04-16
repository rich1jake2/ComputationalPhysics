
import numpy as np 
import matplotlib.pyplot as plt 

def f3d(r,t):
    x = r[0]
    y = r[1]
    z = r[2]
    theta = 10.0 # intializing Constant values
    rp    = 28.0
    b     = 8/3

    # Evaluting the functions

    f1 = theta*(y - x)
    f2 = rp*x - y - x*z
    f3 = x*y - b*z

    return np.array([f1,f2,f3]) 

def Numerical_DE3d(t0,tf,N,x0,y0,z0):
    h = (tf-t0)/N            # creating the step size h
    half = .5 
    sixth = 1/6          

    time = np.arange(t0,tf,h) # creating the time steps
    r = np.empty((len(time),3),dtype = float)   # intializing x, y 
    
    r[0][0] = x0
    r[0][1] = y0 
    r[0][2] = z0


    for c,t in enumerate(time):
        if c == N-1:
            break 
        else :
            k1 = h*f3d(r[c,:],t)
            k2 = h*f3d(r[c,:] + half*k1, t + half*h)
            k3 = h*f3d(r[c,:] + half*k2, t + half*h)
            k4 = h*f3d(r[c,:] + k3, t + h)
            r[c+1,:] = r[c,:] + sixth*(k1 + 2*k2 + 2*k3 + k4)
    print(r)

    xl = r[:,0]
    yl = r[:,1]
    zl = r[:,2]

    plt.figure()
    
    plt.plot(time,yl)
    plt.figure()
    plt.plot(zl,xl)
    
    plt.show()

    return xl, yl, time

Numerical_DE3d(0,50,10000,0.0,1.0,0.0)