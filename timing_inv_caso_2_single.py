# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 20:13:33 2020

@author: TOSHIBA 2IN1
"""
from scipy import linalg
from time import perf_counter
from matplotlib import pyplot
from numpy.linalg import inv
from funcionlaplace import matriz_laplaciana2


lista=[]
listamem=[]
lista2=[]
Ns = [1, 2, 3, 4, 6, 8, 10, 12, 14, 16, 18, 20, 25, 30, 35,40,45, 50, 60,70, 80, 90, 100,200,500,1000]
for N in Ns:
    Z = matriz_laplaciana2(N)
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
        
    lista.append(dt)
    listamem.append(ds)
    lista2.append(dr)
        
    x=["","","","","","","10","","","","","20","","","","","","50","","","","","100","200","500","1000"]
    x1=["","","","","","","","","","","","",""]
    y=[0.1e-3,1e-3,1e-2,0.1,1.,10,60,60*10,60*60]
    ejey=["0.1 ms","1 ms", "10 ms", "0.1 s", "1 s", "10 s", "1 min","10 min","1 h"]
    Memy=[0.1e-3,1e-3,1e-2,0.1,1.,10,60,60*10,60*60]
    Memy2=["0.1 ms","1 ms", "10 ms", "0.1 s", "1 s", "10 s", "1 min","10 min","1 h"]

pyplot.subplot(2,1,1)
pyplot.loglog(Ns,lista,"-o")
pyplot.xticks(Ns,x1)
pyplot.yticks(y,ejey) 
pyplot.grid(True)

pyplot.loglog(Ns,listamem,"-o")
pyplot.xticks(Ns,x1)
pyplot.yticks(Memy,Memy2)
pyplot.grid(True)

pyplot.loglog(Ns,lista2,"-o")
pyplot.xticks(Ns,x,rotation=45)
pyplot.yticks(y,ejey) 
pyplot.grid(True)

pyplot.ylabel("tiempo transcurrido")
pyplot.title("Rendimiento matriz inversa A (single)")
pyplot.legend(["Numpylinalg","scipylinalg","scipylinalg overwrite"])
pyplot.subplot(2,1,2)
pyplot.loglog(Ns,listamem,"-o")
pyplot.xticks(Ns,x,rotation=45)
pyplot.yticks(Memy,Memy2)
pyplot.xlabel("tamaño de la matriz")
pyplot.ylabel("Uso de memoria")
pyplot.grid(True)

pyplot.show()

