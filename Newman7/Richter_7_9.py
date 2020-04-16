'''
7.9 - Image Deconvolution 
brightness b(x,y) = a(x',y')f(x-x',y-y')dx'dy'
(a) blur text file with a white black phot, spread with sigma = 25 

(b) Write another program that creates an array of the same size as the photo make a density plot 

(c) read in the blurred photo
calc the point spread function
fourier transforms both 
divides one by the other 
performs an inverse transform 
displays the unblurred photo on the screen 

'''

import numpy as np 
from numpy.fft import rfft,fft2,irfft,irfft2 
from numpy import sin, cos 
from cmath import exp, sin, pi
import matplotlib.pyplot as plt 

blur = open('blur.txt','r')
k = np.array([],dtype = float)


for n,x in enumerate(blur):
    x1 = x.split(' ')
    for l in range(len(x1)):
        x1[l] = float(x1[l])
    k = np.append(k,x1)
print(np.shape(k))
k = k.reshape(1024,1024)
xc = np.arange(512,-512,-1)
yc = np.arange(512,-512,-1)
print(np.shape(k))

plt.figure('Original Pic')

plt.imshow(k, cmap = 'gray')

plt.show()