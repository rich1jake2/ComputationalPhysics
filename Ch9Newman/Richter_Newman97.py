'''
Jake Richter 
Newman 9.7 - The relaxation method for ordinary 
differential Equations 
'''
import numpy as np 
import matplotlib.pyplot as plt 


N = 100 # number of points
ti = 0 # starting time 
tf = 10 # final time 

x0 = 0.0 # Initial position 


error = 1e-6 # Relaxation goal 

times = np.linspace(ti,tf,N+1)
h = (tf - ti)/N
TestError = 1.0 # initializing the error to test and see if it is less than the goal error 

x = np.empty(N+1, dtype = float)
x[0] = 0 
UpdatedX = np.empty(N+1, dtype = float)
g = 9.8


while TestError > error :
    
    for  i in range(N): 
        if i == 0:
            UpdatedX[i] = x0
        else:
            UpdatedX[i] = (-g*h**2 + x[i + 1] + x[i - 1])/2 
    # As in book -
    TestError = np.max(np.abs(UpdatedX - x))

    # As in the book we swap the two values 
    x, UpdatedX = UpdatedX, x

plt.figure()
plt.plot(times,x)
plt.show()
    

    