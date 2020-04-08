'''
Jake Richter
Newman 9.8 

The Schrodinger equation and the crank Nicolson method:
'''
import numpy as np
from numpy import copy 

import matplotlib.pyplot as plt 
from cmath import exp 
import matplotlib.animation as animation

# Banded Matrix to use Later 
def banded(Aa,va,up,down):

    # Copy the inputs and determine the size of the system
    A = copy(Aa)
    v = copy(va)
    N = len(v)

    # Gaussian elimination
    for m in range(N):

        # Normalization factor
        div = A[up,m]

        # Update the vector first
        v[m] /= div
        for k in range(1,down+1):
            if m+k<N:
                v[m+k] -= A[up+k,m]*v[m]

        # Now normalize the pivot row of A and subtract from lower ones
        for i in range(up):
            j = m + up - i
            if j<N:
                A[i,j] /= div
                for k in range(1,down+1):
                    A[i+k,j] -= A[up+k,m]*A[i,j]

    # Backsubstitution
    for m in range(N-2,-1,-1):
        for i in range(up):
            j = m + up - i
            if j<N:
                v[m] -= A[i,j]*v[j]

    return v
# Part A - Program for One iteration - then iterating more 

N = 1000 # Spatial Slices
L = 1e-8 # Size of the Box 
a = L/N  # Spatial Distances 

x0 = L/2

sigma = 1e-10 # meters
s2 = sigma**2

kappa = 5e10 # inverse meters 



h = 1e-18 # Time steps/Slices 
hbar = 6.62e-34
m = 9.109e-31 

v = np.empty(N+1, dtype = complex)

b1 = complex(1.0 , - h * hbar/(2*m*a**2))
b2 = complex(0.0, hbar*h/(4*m*a**2))

a1 = complex(1.0 ,  h * hbar/(2*m*a**2))
a2 = complex(0.0, -hbar*h/(4*m*a**2))



A = np.empty([3,N+1], dtype = complex)
A[0,:], A[2,:] = a2,a2
A[1,:] = a1



times = np.arange(0,1e-15,h)



fig = plt.figure()
ax = fig.add_subplot(111)

x = np.linspace(0,L,N+1)
wave = np.empty(N+1, dtype = complex)
ListToPlot = []

for i,xi in enumerate(x) :
    wave[i] = exp(-(xi - x0)**2/(2*s2)) * exp(complex(0,kappa*xi))


for l in range(len(times)):
    for i,k in enumerate(x):
        if k == 0 or k == L:
            v[i] = 0
        else:
            v[i] = b1 * wave[i] + b2 * (wave[i + 1] + wave[i - 1])

    xfinal = banded(A, v,1,1)
    wave = xfinal
    xfinal = xfinal.real
    xfPlot, = ax.plot(x, xfinal, color = 'blue')

    ListToPlot.append([xfPlot,])







Animate = animation.ArtistAnimation(fig, ListToPlot, interval = 10, blit = True, repeat_delay = 500 )
plt.show()
