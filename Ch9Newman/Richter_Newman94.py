'''
Jake Richter
Newman 9.4 pg. 424 

Calculate the termperature profile of the crust as a function of depth up to 20 m and the time up to 10 years 
'''

import numpy as np 
import matplotlib.pyplot as plt

L = 20       # Thickness oof earth
D = .1       # Thermal diffusivity
N = 100       # Number of divisions in grid
a = L/N       # Grid spacing
h = .10       # Time-step
epsilon = h/N
x = np.arange(0,L+a,a)
A = 10 
B = 12 
tau = 365

Tlo = 10     # Low temperature in Celcius

Thi = 11    # Hi temperature in Celcius



# initialzing T array 
T = np.empty(N+1,dtype = float)
T[1:N-1] = 10
T[0] = A
T[N] = 11 

Tp = np.empty(N+1,float)




c = h*D/(a*a)
t = 0 
tend = 10*365 + 94
plt.figure()
while t < tend:

    # Calculate the new values of T
    Tp[0] = A + B * np.sin(2 * np.pi * t/tau)
    Tp[N] = 11
    Tp[1:N] = T[1:N] + c*(T[2:N+1] + T[0:N-1]- 2*T[1:N])

    
    T,Tp = Tp,T
    t += h
    if t >  (9*365) and t <  (9*365) + .1 :
        plt.plot(x,T , label = 'Year 10 - Day 1 ')
    if t > 92 + (9*365) and t < (92*1) + (9*365) + .1 : 
        plt.plot(x,T, label = 'Year 10 - Month 3 ')
    if t > (92*2) + (9*365) and t < (92*2) + (9*365) + .1:
        plt.plot(x,T, label = 'Year 10 - Month 6')
    if t > (92*3) + (9*365) and t < (92*3) + (9*365) + .1 :
        plt.plot(x,T, label = 'Year 10 - Month 9')
    if t > (92*4) + (9*365) and t < (92*4) + (9*365) + .1 :
        plt.plot(x,T, label = 'Year 10 - Month 12')


plt.legend()
plt.show()