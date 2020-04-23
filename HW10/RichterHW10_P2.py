'''
Problem 2: Hypersphere volume 

Newman 10.7 - Give the volumes for sphere of 
radius = 1 and dimensionality 1-10

1D V = 2, 2D V = pi(area) 
'''
import numpy as np 

ListofVolumes = []
Npoints = 1000000

for n in np.arange(1, 11):
    count = 0.0 
    

    for i in range(Npoints):
        xs = np.random.uniform(low = -1.0, high = 1.0, size = n)
        SumToCheck = np.sum(np.square(xs))
        if SumToCheck <= 1 :
            count += 1
        else:
            continue
    Volume = (2**n)*count/(Npoints)
    ListofVolumes.append(Volume)

print(ListofVolumes)



        
        

