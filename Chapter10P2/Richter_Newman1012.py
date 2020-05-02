'''
Newman Problem 10.12 

'''
import numpy as np 
import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D

# Part c 

theta = np.arccos(np.random.uniform(low = 0, high = np.pi))
phi = 2*np.pi * np.random.uniform(low = 0, high = 1)

# Part D 
thetaList = []
phiList = []

for i in range(500):
    theta = np.arccos(np.random.uniform(low = 0, high = np.pi))
    phi = 2*np.pi * np.random.uniform(low = 0, high = 2*np.pi)
    thetaList.append(theta)
    phiList.append(phi)

phiList = np.array(phiList)
thetaList = np.array(thetaList)

x = np.sin(phiList) * np.cos(thetaList)
y = np.sin(phiList) * np.sin(thetaList)
z = np.cos(phiList)

fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')
ax.scatter(xs = x, ys = y, zs = z)
plt.show()