import scipy as sy
from scipy.special import comb

def baye (x,r,n):
    
    b=(comb(n,x))*((r**x)*(((1-r)**(n-x))))*r
    return b

k=[]
mayor=[]
menor=[]
x=sy.arange(0,1.01,0.001)
for i in x:
    k.append(baye(18,i,33))
    if i>0.5:
        mayor.append(baye(18,i,33))
    if i<0.5:
        menor.append(baye(18,i,33))
        
suma=sy.sum(k)


large=mayor/suma
minor=menor/suma

print(sy.sum(large),sy.sum(minor))
print(sy.sum(large)+sy.sum(minor)) #suma de prob no es uno porque falta r=0.5
