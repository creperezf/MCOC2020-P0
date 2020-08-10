# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 12:29:09 2020

@author: TOSHIBA 2IN1
"""


from scipy import matrix, rand
from time import perf_counter
from matplotlib import pyplot
from mimatmul import mimatmul


i=1
while i<=10:
    lista=[]
    listamem=[]
    Ns = [1, 2, 3, 4, 6, 8, 10, 12, 14, 16, 18, 20, 25, 30, 35,40,45, 50, 60,70, 80, 90, 100,200,500,1000]
    for N in Ns:
        A = matrix(rand(N,N))
        B = matrix(rand(N,N))
            
        t1 = perf_counter()
        C = mimatmul(A,B,N)
        t2 = perf_counter()
            
        dt = t2 - t1
        size=3*(N**2)*8
        lista.append(dt)
        listamem.append(size)
        x=["","","","","","","10","","","","","20","","","","","","50","","","","","100","200","500","1000"]
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
    pyplot.ylabel("tiempo transcurrido")
    pyplot.title("Rendimiento A@B")
    pyplot.subplot(2,1,2)
    pyplot.loglog(Ns,listamem,"-o")
    pyplot.xticks(Ns,x,rotation=45)
    pyplot.yticks(Memy,Memy2)
    pyplot.grid(True)
    pyplot.xlabel("tamaño de la matriz")
    pyplot.ylabel("Uso de memoria")
    pyplot.axhline(y=10000000000, xmin=0.001, xmax=0.9999,color="black",ls="--")
    i+=1
pyplot.figure()
pyplot.show()