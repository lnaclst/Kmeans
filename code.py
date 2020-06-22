#Implementation of k-means clustering

### HOW DO I GENERALIZE THIS TO HANDLE DIFFERENT SETS OF
### DATA WITH DIFFERENT DIMENSIONALITY?


import numpy as np
import random as rnd
import math

def euclid(p1, p2):
    """P1 and P2 are vectors of the same length."""
    a = (p1[0]-p2[0])**2
    b = (p1[1]-p2[1])**2
    return math.sqrt(a+b)

#Find mean of each cluster
    def cluster_mean(c1):
        #c1 is a list of points of variable length
        x = 0
        y = 0
        l = len(c1)
        for i in c1:
            x += i[0]/l
            y += i[1]/l
        return (x,y)

#Sample data
X = np.array([[1,2],[1.5,1],[5,8],[8,8],[1,0.6],[9,11]])

def kmeans(data, start_means=None,iter=0):
    """Data is an array of points in some space."""
    if start_means==None:
        m1, m2 = rnd.choices(data, k=2)
    else:
        m1,m2 = start_means

    #Calculate difference between each m and all points in X
    #Add each point to the cluster it is closest to
    cluster1 = []
    cluster2 = []

    for i in X:
        d1 = euclid(m1,i)
        d2 = euclid(m2,i)
        if d1 < d2:
            if d1 != 0:
                cluster1.append(i)
        else:
            if d2 != 0:
                cluster2.append(i)

    mean1 = cluster_mean(cluster1)
    mean2 = cluster_mean(cluster2)

    if iter !=0:
        print('Medial means.')
        print(mean1)
        print(mean2)

    return mean1, mean2

mean1, mean2 = kmeans(X)

print('Starting means.')
print(mean1)
print(mean2)

#Optimize means by iteratively applying the algorithm
#Stop after 10 iterations or if the means converge for 3 cycles
it = 0
iter = 0
for i in range(10):
    m1,m2 = mean1, mean2
    mean1,mean2 = kmeans(X, start_means=(mean1,mean2),iter=iter)
    iter += 1
    #Stop at convergence after no change for 3 cycles
    if m1 == mean1:
        if m2 == mean2:
            it += 1
            if it == 3:
                break

print('Final means.')
print(mean1)
print(mean2)
