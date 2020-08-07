# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 14:56:20 2020

@author: TOSHIBA 2IN1
"""

from scipy import matrix, rand
from time import perf_counter
from matplotlib import pyplot

lista=[]
listamem=[]
Ns = [2, 4, 8, 10, 20, 50, 100, 200, 500, 1000,2000,5000,10000]
for N in Ns:
    A = matrix(rand(N,N))
    B = matrix(rand(N,N))
        
    t1 = perf_counter()
    C = A*B
    t2 = perf_counter()
        
    dt = t2 - t1
    size=3*(N**2)*8
    lista.append(dt)
    listamem.append(size)
    y=[0.1e-3,1e-3,1e-2,0.1,1.,10,60,60*10]
    ejey=["0.1 ms","1 ms", "10 ms", "0.1 s", "1 s", "10 s", "1 min","10min"]
    Memy=[10**3,10**4,10**5,10**6,10**7,10**8,10**9,10**10]
    Memy2=["1 KB","10 KB","100 KB","1 MB","10 MB","100 MB","1 GB","10 GB"]

pyplot.figure()
pyplot.subplot(2,1,1)
pyplot.loglog(Ns,lista,"-s")
pyplot.xticks(Ns,Ns)
pyplot.yticks(y,ejey) 
pyplot.xlabel("tamaño de la matriz")
pyplot.ylabel("tiempo transcurrido")
pyplot.title("Rendimiento A@B")
pyplot.grid()
pyplot.subplot(2,1,2)
pyplot.loglog(Ns,listamem,"-s")
pyplot.xticks(Ns,Ns)
pyplot.yticks(Memy,Memy2)
pyplot.xlabel("tamaño de la matriz")
pyplot.ylabel("Uso de memoria")
pyplot.grid()

pyplot.show()