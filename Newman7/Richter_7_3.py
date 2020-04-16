'''
Fourier Transforms of Musical Instruments 
(a) Take the paino and trump txt files. Import them and get there FFT and map onto the first 10k frequencies
    then discuss wha the weights of the coefficients mean 
(b) They were recorded at the same rate and playing the same note. What note were they playing - Should be the note with 
    the highest coeficient value - but that seems too easy. I think I have this wrong ask grads on monday
'''
import numpy as np 
from numpy.fft import rfft as fft
import matplotlib.pyplot as plt 




piano = open('piano.txt', 'r')
trumpet = open('trumpet.txt', 'r')

waveform_p = []
waveform_t = []

for x in piano:
    waveform_p.append(float(x))
    
for y in trumpet:
    waveform_t.append(float(y))
piano.close()
trumpet.close()

piano_dft = fft(waveform_p)
trumpet_dft = fft(waveform_t)


x = np.arange(0,len(waveform_p))

xdft = np.linspace(0,10000,50001)

plt.figure('Piano Waveform')
plt.title('Piano Waveform')
plt.plot(x,waveform_p)

plt.figure('Piano Fourier Transform')
plt.plot(xdft,piano_dft)

plt.figure('Trumpet Waveform')
plt.plot(x,waveform_t)
plt.figure('Trumpet Fourier Transform')
plt.plot(xdft,trumpet_dft)


plt.show()

print('Note Piano was playing  is at',xdft[np.argmax(piano_dft)], 'Hz')
print('Note Trumpet was playing is at',xdft[np.argmax(trumpet_dft)],'Hz')
