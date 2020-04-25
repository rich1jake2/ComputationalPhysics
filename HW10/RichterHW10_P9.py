'''
Problem 9 - Percolation
Dragly 

'''

import matplotlib.pyplot as plt
import numpy as np
from scipy.ndimage import measurements

L = 100
r = np.random.rand(L,L)
p = 0.60
z = r<p

plt.figure(figsize=(16,5))
plt.subplot(1,3,1)
plt.imshow(z, origin='lower', interpolation='nearest')
# plt.colorbar()
plt.title("Matrix")

# Show image of labeled clusters (shuffled)
lw, num = measurements.label(z)
plt.subplot(1,3,2)
b = np.arange(lw.max() + 1) # create an array of values from 0 to lw.max() + 1
np.random.shuffle(b) # shuffle this array
shuffledLw = b[lw] # replace all values with values from b
plt.imshow(shuffledLw, origin='lower', interpolation='nearest') # show image clusters as labeled by a shuffled lw
plt.colorbar()
plt.title("Labeled clusters")

# Calculate areas
plt.subplot(1,3,3)
area = measurements.sum(z, lw, index=np.arange(lw.max() + 1))
areaImg = area[lw]
im3 = plt.imshow(areaImg, origin='lower', interpolation='nearest')
plt.colorbar()
plt.title("Clusters by area")

# Bounding box
sliced = measurements.find_objects(areaImg == areaImg.max())
if(len(sliced) > 0):
    sliceX = sliced[0][1]
    sliceY = sliced[0][0]
    plotxlim = im3.axes.get_xlim()
    plotylim = im3.axes.get_ylim()
    plt.plot([sliceX.start, sliceX.start, sliceX.stop, sliceX.stop, sliceX.start],
                     [sliceY.start, sliceY.stop, sliceY.stop, sliceY.start, sliceY.start],
                     color="red")
    plt.xlim(plotxlim)
    plt.ylim(plotylim)

plt.show()


diameter = np.sqrt((sliceX.start - sliceX.stop)**2 + (sliceY.start - sliceY.stop)**2)
radius = (1/2)*diameter
ClusterArea = areaImg.max()

logB = np.log10(radius)
logA = np.log10(ClusterArea)
dimension = logA/logB
print(dimension)