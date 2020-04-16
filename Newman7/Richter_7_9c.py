import numpy as np 
from numpy.fft import rfft2, irfft2
from numpy import sin, cos, exp   
from cmath import sin
import matplotlib.pyplot as plt 

# Blur Spread Function 
def fk(x,y):
    
    sigma = 25.0 
    z = np.empty([len(x),len(y)])
    for xk in x:
        for yk in y:
            
            z[xk,yk] =  exp(-(np.square(xk) + np.square(yk))/(2*sigma**2))
    return z

# Creating a 2D fourier transformation to map onto screen

    
def Full_Program(file):
    blur = open('blur.txt','r')
    k = np.array([],dtype = float)
    for x in blur:
        x1 = x.split(' ')
        for l in range(len(x1)):
            x1[l] = float(x1[l])
        k = np.append(k,x1)
    
    
    k = k.reshape(1024,1024)
    
    xc = np.arange(-512,512,1)
    yc = np.arange(-512,512)
    ym = np.arange(-256,256)

    xi, yi = np.meshgrid(xc,yc)
    z = fk(xc,yc)

    point_spreadFFT = rfft2(z)
    
    print(np.shape(point_spreadFFT))

    blurred_picFFT  = rfft2(k)

   
    print(np.shape(blurred_picFFT))
    
    div_fft = np.empty(np.shape(blurred_picFFT),complex)
    print(np.shape(div_fft))
    for i in xc:
        for j in ym:
            div_fft[i,j] = (blurred_picFFT[i,j])/(max(point_spreadFFT[i,j],10e-4))

    unblur = irfft2(div_fft)
    
    

    

    return xi,yi, unblur

xg, yg, u_pic = Full_Program('blur.txt')

plt.figure('Unblurred Pic')
plt.imshow(u_pic, cmap = 'gray')
plt.show()




