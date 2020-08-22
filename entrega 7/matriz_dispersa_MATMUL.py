# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 18:50:13 2020

@author: TOSHIBA 2IN1
"""

import numpy as np
from numpy import double, zeros, linspace
from time import perf_counter
from matplotlib import pyplot
from numpy import *
from scipy.sparse import lil_matrix
import numpy as np

def matriz_laplaciana_dispersa(N, t=np.float32):
    e = eye(N)-eye(N,N,1)
    return t(e+e.T)




i=1
while i<=5:
    Ns=[ 2, 5, 10, 12, 15, 20, 30, 40, 45, 50, 55, 60, 75, 100, 125, 160, 200, 250, 500, 600, 800, 1000,2000,5000,10000]
    dts1=[] 
    dts2=[]
    print (f"iteracion = {i}")
    for N in Ns:
        
        print (f"N = {N}")
        t1=perf_counter()
        
        A=matriz_laplaciana_dispersa(N)
        b=matriz_laplaciana_dispersa(N)
        
        t2=perf_counter()
        x=A@b
        
        t3=perf_counter()
        
        dts1.append(t2-t1)
        dts2.append(t3-t2)
        
       
        x = [10,20,50,100,200,500,1000,2000,5000,10000,20000]
        x1=["10","20","50","100","200","500","1000","2000","5000","10000","20000"]
        x2=["","","",""]
        y=[0.1e-3,1e-3,1e-2,0.1,1.,10,60,60*10,60*60]
        ejey=["0.1 ms","1 ms", "10 ms", "0.1 s", "1 s", "10 s", "1 min","10 min","1 h"]
      
    dtmax1=max(dts1)
    dtmax2=max(dts2)  
    dtcte1=[dtmax1,dtmax1,dtmax1,dtmax1,dtmax1,dtmax1,dtmax1,dtmax1,dtmax1,dtmax1,dtmax1,dtmax1,dtmax1,dtmax1,dtmax1,dtmax1,dtmax1,dtmax1,dtmax1,dtmax1,dtmax1,dtmax1,dtmax1,dtmax1,dtmax1]
    dtcte2=[dtmax2,dtmax2,dtmax2,dtmax2,dtmax2,dtmax2,dtmax2,dtmax2,dtmax2,dtmax2,dtmax2,dtmax2,dtmax2,dtmax2,dtmax2,dtmax2,dtmax2,dtmax2,dtmax2,dtmax2,dtmax2,dtmax2,dtmax2,dtmax2,dtmax2]
    N1=linspace(1,10000,100)
    pyplot.subplot(2,1,1)
    pyplot.loglog(Ns,dts1,"-o", color="0.5")
    pyplot.loglog(Ns,dtcte1, "b--")#cte
    pyplot.loglog(N1,N1*(dtmax1/N), "y--")#O(N)
    pyplot.loglog(N1,N1**2*(dtmax1/N**2), "g--")#O(N^2)
    pyplot.loglog(N1,N1**3*(dtmax1/N**3), "r--")#O(N^3)
    pyplot.loglog(N1,N1**4*(dtmax1/N**4), "m--")#O(N^4)
    pyplot.xticks(x,x2)
    pyplot.yticks(y,ejey) 
    pyplot.ylim(0.00001,600)
    pyplot.xlim(2,20000)
    pyplot.ylabel("Tiempo de ensamblado")
        
    pyplot.subplot(2,1,2)
    pyplot.loglog(Ns,dts2,"-o", color="0.4")
    pyplot.loglog(Ns,dtcte2, "b--")#cte
    pyplot.loglog(N1,N1*(dtmax2/N), "y--")#O(N)
    pyplot.loglog(N1,N1**2*(dtmax2/N**2), "g--")#O(N^2)
    pyplot.loglog(N1,N1**3*(dtmax2/N**3), "r--")#O(N^3)
    pyplot.loglog(N1,N1**4*(dtmax2/N**4), "m--")#O(N^4)
    pyplot.xticks(x,x1,rotation=45)
    pyplot.yticks(y,ejey) 
    pyplot.ylim(0.00001,600)
    pyplot.xlim(2,20000)
    pyplot.ylabel("Tiempo de solución")
    pyplot.xlabel("Tamaño matriz $N$")
    pyplot.legend(["constante","O(N)","O(N$^2$)","O(N$^3$)","O(N$^4$)"])
    i+=1       


    
pyplot.figure()   
pyplot.show()   