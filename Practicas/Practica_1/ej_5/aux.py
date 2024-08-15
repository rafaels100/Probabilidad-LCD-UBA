from itertools import product

A = [1,2,3,4]

S = product(A, A)
print(S)

print(list(S))

n = 4
listas = [A for _ in range(0, n)]
#uso * para unpack la lista y pasarsela como multiple argumentos a la funcion product
S = list(product(*listas))

print(S)

"""
N = {1,2,3,4,5,6,7,8,9}
n = 4
Dado un espacio muestral con permutaciones de N en n, contar todas las posibles sucesiones crecientes
"""
camino = [0] * 4
contador = 0
N = 9
def rec(i):
    if i == 4:
        print(camino)
        if camino[i-2] > camino[i-1]:
            contador += 1
        return
    for j in range(camino[i]+1, N+1):
        camino[i] = j
        return rec(i+1)
    return

rec(0)
print(contador)
#NO ME SALIO
