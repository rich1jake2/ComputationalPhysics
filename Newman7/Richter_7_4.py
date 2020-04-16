'''
Problem 7.4 Newman - 
Fourier Filtering 
read in the dow txt file and then filter out the bottom 90%, then take the inverse fourier transform 

'''
import numpy as np 
import matplotlib.pyplot as plt 
from numpy.fft import rfft as fft 
from numpy.fft import ifft as ifft

# Opening the dow data

dow = open('dow.txt','r')

# Creating a list that the dow data will be appended to 
dw  = []

# appending the dow data to the dw list
for l in dow: 
    dw.append(float(l))

# Making a list of x values to plot against the dow, and the associate fourier transform
x = np.arange(len(dw))
xfft = np.arange(len(dw)//2 + 1)


dow_fft = fft(dw) # taking the fourier tranform of the dow data

filt_fft10 = np.zeros(1024) # making a list for the filtering of the fourier transform 
filt_fft02 = np.zeros(1024) # making a list for filtering bottom 98% of fft

# Filtering though the fourier transform and appending to the filter list for the 10%
for q,x1 in enumerate(dow_fft):
    
    if q > (.1*len(dow_fft)):
        x1 = 0.0
    filt_fft10[q] = x1
for q,x1 in enumerate(dow_fft):
    
    if q > (.02*(len(dow_fft))):
        x1 = 0.0
    filt_fft02[q] = x1
inverse_fft10 = ifft(filt_fft10)
inverse_fft02 = ifft(filt_fft02)



# Plotting the original dow data and the inverse fourier transform of the filtered data
plt.figure('Original Dow')
plt.title('Original')
plt.plot(x,dw)
plt.figure('Inverse top10%')
plt.title('Top 10%')
plt.plot(x,dw)
plt.plot(x,inverse_fft10)
plt.figure('Inverse Top2%')
plt.title('Inverse Top2%')
plt.plot(x,dw)
plt.plot(x,inverse_fft02)
plt.figure('All')
plt.title('All')
plt.plot(x,dw)
plt.plot(x,inverse_fft02)
plt.plot(x,inverse_fft10)

plt.legend(['Original Data','Inverse of top 10','Inverse of top 2'])

# Plotting the Fourier Transform of the data
plt.figure('Fourier Tranform - Dow')
plt.plot(xfft,dow_fft)

plt.show()

