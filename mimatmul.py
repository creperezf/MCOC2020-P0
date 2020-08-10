import numpy as np
def mimatmul(A,B,N):   
    C=np.zeros((N,N))
    a=0
    while a<(N):
        b=0
        while b<(N):
            cuenta=0
            c=0
            while c<(N):
                cuenta+= A[a,c]*B[c,b]
                C[a,b]=cuenta
                c+=1
            b+=1
        a+=1
    return C
