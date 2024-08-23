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
n = 6
S = list(product(*[[1, 2, 3, 4] for _ in range(0, n)]))
#card_S = len(S)
#print(S, card_S)

card_S = len(S)
#el cardinal teorico calculado es
card_S_teo = 4**6
#print(S)
print(f"El cardinal de S computado es {card_S} y el calculado teoricamente es {card_S_teo}")

#a) Probabilidad de que todas las urnas esten ocupadas?
#cuento la cantidad de elementos que tienen todas las urnas ocupadas
ocup = [elem for elem in S if set([1,2,3,4]).issubset(set(elem))]
card_ocup = len(ocup)
print(card_ocup, 4**6 - (4*3**6 - 3*2**7 - 4))
