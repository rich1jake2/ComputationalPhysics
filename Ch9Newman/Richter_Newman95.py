'''
Jake Richter
Newman 9.5 - FTCS Solution to the wave Equaion 

'''
import numpy as np
from numpy import exp 
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Defining Global Variables 
C = 1.0 
N = 200 
d = .1
L = 1 
sigma = .3 
h = 1e-6   # time step 
v = 100
a = L/N

x = np.linspace(0,L,N)
theta = np.zeros(N)
Phi = C * x * (L - x)/(L**2) * exp(-(x-d)**2/(2*sigma**2))
t = np.arange(0,20e-3,h)

ThetaList = []
fig = plt.figure()
ax = plt.axes(xlim = (0,1), ylim = (-.05,.05))
Lplot, = ax.plot([],[], lw = 2)

for time in t:
    for i in range(len(theta)-1):
        theta += h*Phi
        Phi[i] += h * v**2/(a**2) * (theta[i + 1] + theta[i - 1] - 2*theta[i])
    Lplot, = ax.plot(x, theta, color = 'b')
    
    
    ThetaList.append([Lplot,])

WaveAnimation = animation.ArtistAnimation(fig, ThetaList, interval = 5, blit = True)
plt.show()
   

