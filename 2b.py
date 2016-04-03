import scipy as sy

lista2=[]
c=0

for z in range(1000):
    lista=[]
    for i in range(33):
        x = sy.random.random_integers(2)
        lista.append(x)
    lista2.append(lista)
    if (sy.bincount(lista)[1])==18:
        c+=1
    
print(c)
print(float(c)/1000) #porcentaje de la observacion
