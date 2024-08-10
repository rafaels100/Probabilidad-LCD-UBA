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

