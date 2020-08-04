from scipy import matrix, rand
from time import perf_counter

N = 3

A = matrix(rand(N,N))
B = matrix(rand(N,N))

t1 = perf_counter()
C = A*B
t2 = perf_counter()

dt = t2 - t1

print(f"Tiempo transcurrido = {dt} s")



