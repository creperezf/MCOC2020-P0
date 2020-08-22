
import numpy as np
from numpy import double, zeros,

def matriz_laplaciana_llena(N,dtype=double):
   Z = zeros((N,N),dtype=double)
   for i in range (N):
       for j in range(N):
          if i==j:
              Z[i,j]=2
          if i+1==j:
              Z[i,j]=-1
          if i-1==j:
              Z[i,j]=-1        
    
   return Z



def matriz_laplaciana_dispersa(N, t=np.float32):
    e = eye(N)-eye(N,N,1)
    return t(e+e.T)