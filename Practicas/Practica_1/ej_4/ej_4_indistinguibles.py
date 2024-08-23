from itertools import chain, combinations, product
import numpy as np
from math import factorial, comb
"""
4)
Tenemos 6 bolillas y 4 urnas

a) Probabilidad de que todas las urnas esten ocupadas?

b) Probabilidad de que al menos 3 urnas esten ocupadas?

Podemos representar el espacio muestral como 9-uplas de 0's y 1's, donde los 1's son las barras internas entre las urnas, y los 0's son las bolillas en cada urna
"""
#creo todo el espacio de 9-uplas de 0's y 1's
n = 9
S = list(product(*[[0, 1] for _ in range(0, n)]))
#card_S = len(S)
#print(S, card_S)

#pero debo quedarme con las secuencias de 0's y 1's que sumen 3
S = [elem for elem in S if sum(elem) == 3]
card_S = len(S)
#el cardinal teorico calculado es
card_S_teo = comb(9, 3)
#print(S)
print(f"El cardinal de S computado es {card_S} y el calculado teoricamente es {card_S_teo}")

#a) Probabilidad de que todas las urnas esten ocupadas?
#puedo crear por cada elemento una sucesion con los indices donde aparecen los 1's
indices = [[i for i in range(0, len(elem)) if elem[i] == 1] for elem in S]
print(indices)
#ahora debo quedarme con los elementos en donde los 1's no esten en ninguno de los extremos, y donde el 1 del medio este separado de los 1's de los extremos
buscados = [elem for elem in indices if (elem[0] != 0) and (elem[-1] != n-1) and abs(elem[1] - elem[0]) > 1 and abs(elem[1] - elem[-1]) > 1]
print(buscados, len(buscados))

#b) Probabilidad de que al menos 3 urnas esten ocupadas?
print(S)
#creo una lista que me indique si la primera urna esta ocupada
primera_urna_ocup = [1 if elem[0] != 0 else 0 for elem in indices]
print(primera_urna_ocup)
#otra para la segunda urna
segunda_urna_ocup = [1 if abs(elem[0]-elem[1]) > 1 else 0 for elem in indices]
print(segunda_urna_ocup)
#otra para la tercera urna
tercera_urna_ocup = [1 if abs(elem[1]-elem[2]) > 1 else 0 for elem in indices]
print(tercera_urna_ocup)
#otra para la cuarta
cuarta_urna_ocup = [1 if elem[-1] != n-1 else 0 for elem in indices]
print(cuarta_urna_ocup)

#para saber cuantas urnas estan ocupadas en cada punto muestral del espacio muestral, solo queda sumar estas listas
cant_urnas_ocup = [primera_urna_ocup[i] + segunda_urna_ocup[i] + tercera_urna_ocup[i] + cuarta_urna_ocup[i] for i in range(0, card_S)]
print(cant_urnas_ocup)
#para saber cuantos elementos del espacio muestral tienen al menos 3 de sus 4 urnas ocupadas
al_menos_3_ocup = [1 if elem >= 3 else 0 for elem in cant_urnas_ocup]
print(al_menos_3_ocup)
card_al_menos_3_ocup = sum(al_menos_3_ocup)
print(card_al_menos_3_ocup, comb(6, 3))

print(sum(primera_urna_ocup), comb(8, 5))
print(sum(segunda_urna_ocup), comb(8, 5))
print(sum(tercera_urna_ocup), comb(8, 5))
print(sum(cuarta_urna_ocup), comb(8, 5))

print(sum([1 if elem == 2 else 0 for elem in cant_urnas_ocup]), comb(7, 3))
