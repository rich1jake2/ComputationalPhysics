'''
The Lotka - Volterra equations
write a program to solve dx/dt = ax + by ; dy/dt = gxy - delta y 
then graph x, y as a function of t on the same axis

'''
import numpy as np 
import matplotlib.pyplot as plt 

# Goal to make a generic 4th order Runge Kutte DE Solver
# Fourth Order Runge Kutta method for two variables 

def f(r,t):
    x = r[0]
    y = r[1]
    a = 1.0
    b = .50
    g = .50
    d = 2.0 

    f1 = a*x - b*x*y
    f2 = g*x*y - d*y

    return np.array([f1,f2]) 

def Numerical_DE(t0,tf,N,x0,y0):
    h = (tf-t0)/N            # creating the step size h
    half = .5 
    sixth = 1/6          

    time = np.arange(t0,tf,h) # creating the time steps
    r = np.empty((len(time),2),dtype = float)   # intializing x, y 
    
    r[0][0] = x0
    r[0][1] = y0 


    for c,t in enumerate(time):
        if c == N-1:
            break 
        else :
            k1 = h*f(r[c,:],t)
            k2 = h*f(r[c,:] + half*k1, t + half*h)
            k3 = h*f(r[c,:] + half*k2, t + half*h)
            k4 = h*f(r[c,:] + k3, t + h)
            r[c+1,:] = r[c,:] + sixth*(k1 + 2*k2 + 2*k3 + k4)
    print(r)

    xl = r[:,0]
    yl = r[:,1]

    plt.figure()
    plt.plot(time,xl)
    plt.plot(time,yl)
    plt.show()

    return xl, yl, time

Numerical_DE(0,30,1000,2.0,2.0)


    

    
    
