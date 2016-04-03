import scipy as sy
from scipy.special import comb
import matplotlib.pyplot as plt
import numpy as np

def baye (x,r,n):
    
    b=(comb(n,x))*((r**x)*(((1-r)**(n-x))))*r
    return b

k=[]
x=sy.arange(0,1.01,0.001)
for i in x:
    k.append(baye(18,i,33))

suma=sy.sum(k)


l=k/suma

print(sy.amax(l)) #maximo valor

print(np.trapz(l,x)) #integral bajo la curva es 1

plt.figure(0)
plt.plot(x,l)
plt.xlabel("Probabilidad r")
plt.ylabel(r"$P(r_i|X)$")

CDF=[]
cum=0.0
for z in l:
    cum+=z
    CDF.append(cum)
    
plt.figure(1)
plt.plot(x,CDF)
plt.xlabel("Probabilidad r")
plt.ylabel(r"$\sum P(r_i|X)$")


plt.show()




