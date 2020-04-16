'''
Diffraction Gratings - Write a python program to calculate the diffractoin pattern for a grating with transmission
function q(u) = sin^2(a*u) with width at 20mu meters alpha = pi/20 and w = 200 micro meter W = 10w = 2mm
lambda = 500nm and f = 1 meter, screeen = 10cm 

check with 5.19 

I(xk) = (W/N)^2 * |ck|^2
xk    = (lamb*f)/W * k 

'''

import numpy as np 
from numpy.fft import rfft,ifft as fft,ifft
from numpy import sin,cos, pi
import matplotlib.pyplot as plt
from cmath import exp,pi 


def q(u):
    slit_w = 20e-6
    return (sin(u*pi/slit_w))**2

# We need to take the fourier transfrom of q(u)
# then I(xk) = (w/N)^2 * |ck|^2

def I(w):
    

    w = 200e-6
    f = 1
    lamb = 500e-9
    W = 10*w
    N = 500
    
    n = np.arange(0,N)
    n2 = np.arange(0,N//2)
    # x = np.linspace(-5e-5,5e-5,N)
    u = n*W/N - W/2
    space1 = -lamb*f*n/W
    space2 = lamb*f*n/W

    
    #x = np.arange(-5e-2,5e-2,space)
    

    

    y = np.sqrt(q(u))

    for l,l2 in enumerate(y): 
        if l > .1*(len(y)):
            y[l] = 0.0
    

    ck = fft(y)



    I = ((W/N)**2)*((abs(ck))**2)

    

    

    


   

    return space2, I

x, I1 = I(10)
plt.figure('Diffraction Grating')

plt.plot(x,I1,'b')
plt.plot(-x,I1,'b')
plt.xlim(-5e-2,5e-2)



plt.show()
