# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 20:06:56 2020

@author: TOSHIBA 2IN1
"""

import scipy as sp

N = 3

A = sp.matrix(sp.rand(N,N))
B = sp.matrix(sp.rand(N,N))

print(f"A = \n{A}")
print(f"B = \n{B}")

C = A*B     # Ojo numpy esto es multiplicacion de arreglos 




print(f"C = \n{C}")

print(f"C00 = \n{C[0,0]}")
print(f"A00 * B00 = \n{A[0,0]*B[0,0]}")