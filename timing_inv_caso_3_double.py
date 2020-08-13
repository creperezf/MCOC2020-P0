# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 20:15:53 2020

@author: TOSHIBA 2IN1
"""
from scipy import linalg
from time import perf_counter
from matplotlib import pyplot
from numpy.linalg import inv
from funcionlaplace import matriz_laplaciana1


lista=[]
listamem=[]
lista2=[]
lista3=[]
Ns = [1, 2, 3, 4, 6, 8, 10, 12, 14, 16, 18, 20, 25, 30, 35,40,45, 50, 60,70, 80, 90, 100,200,500,1000,2000,5000]
for N in Ns:
    Z = matriz_laplaciana1(N)
    t1 = perf_counter()
    C = inv(Z)
    t2 = perf_counter()
        
    t3 = perf_counter()
    D = linalg.inv(Z)
    t4 = perf_counter()
    
    t5 = perf_counter()
    E = linalg.inv(Z,overwrite_a=True, check_finite=True)
    t6 = perf_counter()
        
    dt = t2 - t1
    ds = t4 - t3
    dr = t6 - t5
    size=3*(N**2)*8 
        
    lista.append(dt)
    listamem.append(ds)
    lista2.append(dr)
    lista3.append(size)    
    x=["","","","","","","10","","","","","20","","","","","","50","","","","","100","200","500","1000","2000","5000"]
    x1=["","","","","","","","","","","","",""]
    y=[0.1e-3,1e-3,1e-2,0.1,1.,10,60,60*10,60*60]
    ejey=["0.1 ms","1 ms", "10 ms", "0.1 s", "1 s", "10 s", "1 min","10 min","1 h"]
    Memy=[10**3,10**4,10**5,10**6,10**7,10**8,10**9,10**10]
    Memy2=["1 KB","10 KB","100 KB","1 MB","10 MB","100 MB","1 GB","10 GB"]

pyplot.subplot(2,1,1)
pyplot.loglog(Ns,lista,"-o")
pyplot.xticks(Ns,x1)
pyplot.yticks(y,ejey) 
pyplot.grid(True)

pyplot.loglog(Ns,listamem,"-o")
pyplot.xticks(Ns,x1)
pyplot.yticks(y,ejey)
pyplot.grid(True)

pyplot.loglog(Ns,lista2,"-o")
pyplot.yticks(y,ejey) 
pyplot.grid(True)
pyplot.xticks(Ns,x1)
pyplot.ylabel("tiempo transcurrido")
pyplot.title("Rendimiento matriz inversa A (double)")
pyplot.legend(["Numpylinalg","scipylinalg","scipylinalg overwrite"])
pyplot.subplot(2,1,2)
pyplot.loglog(Ns,lista3,"-o")
pyplot.xticks(Ns,x,rotation=45)
pyplot.yticks(Memy,Memy2)
pyplot.xlabel("tamaño de la matriz")
pyplot.ylabel("Uso de memoria")
pyplot.grid(True)

pyplot.show()
