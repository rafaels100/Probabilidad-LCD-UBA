import math

"""
5)
Este ejercicio nos plantea sacar n bolitas, sin reposicion, de un bolillero con bolitas numeradas de 1 a N.

a) Proba de que se extraiga la bolita numero m en la k-esima extraccion?

b) Proba de que se extraiga la bolilla m?

c) El maximo numero obtenido sea menor o igual a m?

d) El maximo numero obtenido sea m?

?) El maximo numero obtenido sea mayor o igual a m?

e) El maximo numero obtenido este entre a y b? Con n <= a < b <= N

f) Proba de que los numeros de las bolillas en el orden que fueron extraidas constituyan una sucesion estrictamente creciente?
"""

#b)
#La probabilidad de que la bolilla m este entre las extraidas
N = 9
n = 4
#p_m = n/N
card_evento_m = math.comb(N-1, n-1)
card_S = math.comb(N, n)
p_m = card_evento_m / card_S
print(card_evento_m, card_S, p_m)
print(card_evento_m * math.factorial(n), card_S * math.factorial(n))
