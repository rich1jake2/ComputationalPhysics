'''
Find the value of the integeral 

x^(-1/2)/(exp(x) + 1) from 0 to 1 by using the correct distribution of random numbers for your sampling 
because this integarl will diverge. 

'''


import numpy as np 
import matplotlib.pyplot as plt 


def MonteIntegrated(Npoints):
    I = 0.0 
    for i in range(Npoints):

        x = np.random.random()
        I += 2/(np.exp(x**2) + 1)
    I *=(1/Npoints)

    print(I)
MonteIntegrated(10000000)