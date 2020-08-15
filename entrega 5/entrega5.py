# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 13:25:20 2020

@author: TOSHIBA 2IN1
"""
import numpy as np
import scipy as sp
from numpy import float32
import scipy.linalg as spLinalg
from time import perf_counter
from matplotlib import pyplot

def matriz_laplaciana(N,dtype=float32):
    N-=1
    lista3=[]
    i=0
    while i<=N:
        lista3.append(2)
        i+=1
    C=np.array((lista3),dtype=dtype)
    Z= np.diag(C) 
    b=0
    while b<N:
        Z[b,(b+1)]=-1
        Z[b+1,b]=-1
        b+=1
    
    return Z

Ns = [ 2, 5, 10, 12, 15, 20, 30, 40, 45, 50, 55, 60, 75, 100, 125, 160, 200, 250, 500, 600, 800, 1000,2000,5000,10000]

corrida=10
names=["A_invB_inv.txt","A_invB_npSolve.txt"]

files=[open(name,"w") for name in names]

for N in Ns:
    dts=np.zeros((corrida,len(files)))
    print(f"N={N}")
    for i in range (corrida):
        print(f"i={i}")
        
        A=matriz_laplaciana(N)  #invirtiendo y multiplicando
        B=np.ones(N)
        t1 = perf_counter()
        A_inv=np.linalg.inv(A)
        A_invB=A_inv@B
        t2 = perf_counter()
        dt = t2 - t1
        dts[i,0]=dt
        
        A=matriz_laplaciana(N)  #solve
        B=np.ones(N)
        t1 = perf_counter()
        A_invB=np.linalg.solve(A,B)
        t2 = perf_counter()
        dt = t2 - t1
        dts[i][1]=dt
        
    print("dts:", dts)
    
    dts_mean=[np.mean(dts[:,j]) for j in range(len(files))]
    
    print("dts_mean:",dts_mean)
    
    for j in range(len(files)):
        files[j].write(f"{N} {dts_mean[j]} \n")
        files[j].flush()
    
[file.close() for file in files]

x=["","","10","","","20","","","","","","50","","","","","","100","","","200","","500","","","1000","2000","5000","10000"]
y=[0.1e-3,1e-3,1e-2,0.1,1.,10,60,60*10,60*60]
ejey=["0.1 ms","1 ms", "10 ms", "0.1 s", "1 s", "10 s", "1 min","10 min","1 h"]

pyplot.figure()

for name in names:
    data=np.loadtxt(name)
    Ns=data[:,0]
    dts=data[:,1]
    
    print("Ns:",Ns)
    print("dts:",dts)
    
    pyplot.loglog(Ns,dts.T,"-o", label=name)
    pyplot.xticks(Ns,x,rotation=45)
    pyplot.yticks(y,ejey) 
    pyplot.grid(True)
    pyplot.ylabel("Tiempo transcurrido")
    pyplot.xlabel("Tamaño matriz $N$")
    
pyplot.tight_layout()
pyplot.legend()
pyplot.show()

