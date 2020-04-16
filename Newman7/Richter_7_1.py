'''
Fourier Transforms of Simple Functions
Calculate the coefficients of the sample periodic functions at N = 1000 evenly spaced points.
plot their amplitueds 

(a) A single cycle of a square wave with amplitude 1

(b) The sawtooth wave yn = n 

(c) The modulated wave yn = sin(pin/N)sin(20pin/N)
'''
import numpy as np
from numpy import sin
import matplotlib.pyplot as plt
from cmath import exp, pi 
from math import floor
# Making x inputs for waves
x_sqtest = np.linspace(0,3,1000)
x_stest = np.linspace(0,10,1000)
x_sin_t = np.linspace(0,1000,1000)


# Making the data points for input into the DFT
def Square_Wave(x):
    y = np.empty(len(x))
    for x,l in enumerate(x):
        if l <= 1:
            y[x] = 1
        if l > 1 and l <= 2:
            y[x] = 0 
        if l > 2 and l <=3:
            y[x] =  1
    return y 
def SawTooth(x):
    y = np.empty(len(x))
    for l in range(len(x)):
        y[l] = x[l] - floor(x[l])
    return y
    
def ModSinWave(x):
    N = len(x)
    return sin(pi*x/N)*sin(20*pi*x/N)

# Making the Discrete transform function   
    
def Discrete_Transform(y_data):
    N = len(y_data)
    ck = 0.0 
    it_thru = N//2 + 1
    c = np.empty(it_thru, complex)

    for k in range(it_thru):
        for n in range(N):
            c[k] += y_data[n]*exp(-2j*pi*k*n/N)
    return c


# Assigning the y values for each function
ysquare = Square_Wave(x_sqtest)
ysaw = SawTooth(x_stest)
ymod = ModSinWave(x_sin_t)
# Assinging the variables for the coefficients
ysqT = np.real(Discrete_Transform(ysquare))
ysT  = np.real(Discrete_Transform(ysaw))
ymT  = np.real(Discrete_Transform(ymod))
# Assigning the plotting of f spaces - [THIS IS A PROBLEM - I'M mapping onto the same spaces as before not the Frequency] 
xsqDFT = np.linspace(0,100,501)
xsDFT  = np.linspace(0,100,501)
xmDFT  = np.linspace(0,100,501)

# Plotting the Functions with their appropriate DFTs
plt.figure('Square Wave')
plt.plot(x_sqtest,ysquare)
plt.figure('Square Wave - Fouier Tranform Coef')
plt.plot(xsqDFT,abs(ysqT))

plt.figure('Saw Wave')
plt.plot(x_stest,np.real(ysaw))
plt.figure('Saw Wave - Fourier Transform Coef')
plt.plot(xsqDFT,abs(ysT))

plt.figure('Mod Wave ')
plt.plot(x_sin_t,ymod)
plt.figure('Mod Wave - Fourier Transform Coef')
plt.plot(xmDFT,abs(ymT))

plt.show()