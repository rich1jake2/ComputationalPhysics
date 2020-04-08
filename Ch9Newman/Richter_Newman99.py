'''
Jake Richter HW 7 ch 9 

Newman 9.9 

'''

import numpy as np
from numpy import copy 

import matplotlib.pyplot as plt 
from numpy import empty,arange,exp,real,imag,pi, cos, sin
from numpy.fft import rfft,irfft
import matplotlib.animation as animation


def dst(y):
    N = len(y)
    y2 = empty(2*N,float)
    y2[0] = y2[N] = 0.0
    y2[1:N] = y[1:]
    y2[:N:-1] = -y[1:]
    a = -imag(rfft(y2))[:N]
    a[0] = 0.0

    return a
def idst(a):
    N = len(a)
    c = empty(N+1,complex)
    c[0] = c[N] = 0.0
    c[1:N] = -1j*a[1:]
    y = irfft(c)[:N]
    y[0] = 0.0

    return y


# Part A - The discrete sin fft 

N = 1000 # Spatial Slices
L = 1e-8 # Size of the Box 
a = L/N  # Spatial Distances 

x0 = L/2

sigma = 1e-10 # meters
s2 = sigma**2

kappa = 5e10 # inverse meters 



h = 1e-19 # Time steps/Slices 
hbar = 6.62e-34
m = 9.109e-31 

x = np.linspace(0,L,N+1)

# Initializing the wave function - with real and imaginary separated 
wave = np.empty(N+1, dtype = complex)
imaginaryWave = np.empty(N+1, dtype = float)
RealWave = np.empty(N+1, dtype = float)
for i,xi in enumerate(x) :
    wave[i] = exp(-(xi - x0)**2/(2*s2)) * exp(complex(0,kappa*xi))
    imaginaryWave[i] = np.imag(wave[i])
    RealWave[i] = np.real(wave[i])


# Taking the discrete Fourier Transforms 
Realbks = dst(RealWave)
Imagbks = dst(imaginaryWave)


# Part B - find the real part of the wave 
t0 = 1e-16
k = np.arange(1,N+2)
Coeffs = (Realbks*cos(pi**2 * hbar**2 / (2 * m * k**2 * L**2 )*t0) - Imagbks*sin(pi**2 *k **2 * hbar**2 / (2 * m * L**2)*t0))*(sin(pi  * k *x/N))
Wave = idst(Coeffs)*( sin(pi * k * x/N))

plt.figure()
plt.plot(x,Wave)
plt.show()

# Part C - Creating the animation
fig2 = plt.figure()
PlotListing= [] 
times = np.arange(0,1e-16,h)
real = np.empty(N+1, dtype = float)
Coeffs = np.empty(N+1, dtype = float)
for t in times:
    for i,xi in enumerate(x): 
    
        Coeffs[i] = (Realbks[i]*cos(pi**2 * k[i]**2 * hbar / (2 * m * L**2 )* t) - Imagbks[i]*sin(pi**2 * k[i]**2 * hbar / (2 * m * L**2)*t))
    
        
    Wave = idst(Coeffs)*( sin(pi * k * x/N))



    
    
    Plot, = plt.plot(x, Wave, color = 'b')
    PlotListing.append([Plot,])

Animate = animation.ArtistAnimation(fig2, PlotListing, interval = 10, blit = True, repeat_delay = 500 )
plt.show()


    

    



