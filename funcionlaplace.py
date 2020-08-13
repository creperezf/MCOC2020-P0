# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 16:15:38 2020

@author: TOSHIBA 2IN1
"""

import numpy as np
from numpy import half, double, single, longdouble



def matriz_laplaciana(N,dtype=half):
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

def matriz_laplaciana1(N,dtype=double):
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

def matriz_laplaciana2(N,dtype=single):
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

def matriz_laplaciana3(N,dtype=longdouble):
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