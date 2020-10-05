import numpy as np
import matplotlib.pyplot as plt
import math

a = [[1,2,3,1,2,3,1,2,3],
     [4,5,6,4,5,6,4,5,6],
     [1,2,2,1,2,2,1,2,2]]

def avg(x):
    sum = 0.0
    for i in x:
        sum += i
    return sum / len(x)

moyenn_ligne1 = avg(a[0])
print(moyenn_ligne1)

def deviation(x):
    sumv = 0.0
    for i in x:
        sumv += (i - avg(x))**2
    return math.sqrt(sumv/len(x)-1)

deviation_Ligne1 = deviation(a[0])
print(deviation_Ligne1)

def pearson(x,y):
    coefx = []
    coefy = []
    
    for i in x:
        coefx.append((i - avg(x))/deviation(x))

    for j in y:
        coefy.append((j - avg(y))/deviation(y))
        
    return (sum([i*j for i,j in zip(coefx,coefy)]))/(len(x)-1)

