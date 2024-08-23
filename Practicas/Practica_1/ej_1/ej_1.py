#El espacio muestral S es
S = [(x, y) for x in range(1, 7) for y in range(1, 7)]
print('S: ', S)
print(f"El cardinal de S es {len(S)} que coincide con 6**2 = {6**2}\n")

#El evento A es
A = [elem for elem in S if (elem[0] + elem[1]) % 2 == 0]
print('A: ', A)
print(f"El cardinal de A es {len(A)} que coincide con 6**2/2={6**2/2}\n")

#El evento B es 
B = [elem for elem in S if (elem[0] + elem[1]) == 8]
print("B: ", B)
print(f"El cardinal de B es {len(B)}\n")

#El evento C es
C = [elem for elem in S if elem[0] != elem[1]]
print("C: ", C)
print(f"El cardinal de C es {len(C)}\n")

AC = set(A) & set(C)
print("AC: ", AC)
print(f"El cardinal de A interseccion C es {len(AC)}\n")

#Puedo obtener todos los eventos posibles calculando el conjunto de partes del espacio muestral. Es mi sigma algebra, son las cosas 
#que puedo medir. Los eventos.
from itertools import chain, combinations

def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))

#P_S = list(powerset(S))
#print(len(P_S), 2**36)

#El objeto a crear tiene demasiadas cosas, tarda mucho en hacerlo. Es entendible, debe crear 2**36 conjuntos, y el mas grande de ellos tiene 36 elementos,
#que son todos los elementos de mi espacio muestral

#Para jugar con todos los eventos posibles, deberia reducir el tamaño del dado, digamos, a un dado de 3 caras.
#En la carpeta scripts_interesantes exploro esta posibilidad, en el script eventos_indep.py


