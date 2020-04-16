import numpy as np 
from numpy.fft import rfft,fft2,irfft,irfft2 
from numpy import sin, cos, exp   
from cmath import sin
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
xc = np.arange(-512,512)
yc = np.arange(-512,512)
print(np.shape(k))


# Blur Spread Function 
def fk(x,y):
    sigma = 25.0 
    z = np.empty([len(x),len(y)])
    for xk in x:
        for yk in y:
            z[xk,yk] =  exp(-(np.square(xk) + np.square(yk))/(2*sigma**2))
    return z

    
xi, yi = np.meshgrid(xc,yc)
z = fk(xi,yi)

# MDfourier(k)

plt.figure('Original Pic')

plt.imshow(z, cmap = 'gray')

plt.show()