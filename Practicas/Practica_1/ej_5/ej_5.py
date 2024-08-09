from itertools import chain, combinations
import numpy as np

"""
5)
Este ejercicio nos plantea sacar una bolita de un bolillero de N bolitas, unas n veces, sin reposicion.

Voy a hacer el caso en que si hay reposicion. En este caso es como tirar un dado de N caras y anotar el numero cada vez.
Voy con N = 3, un dado de 3 caras, y con n = 2, tiro dos veces el dado. 

Voy a usar python randint para generar un entero entre 1 y 3, con la misma probabilidad para cada uno. Luego armo tuplas para obtener
los puntos muestrales que salen de manera aleatoria.
"""
#El espacio muestral S de los resultados de todas las tiradas de dos dados posibles es
S = [(x, y) for x in range(1, 4) for y in range(1, 4)]
print("\nS con reposicion: ", S)
card_S = len(S) #es 9

#Puedo obtener todos los eventos posibles calculando el conjunto de partes del espacio muestral. Es mi sigma algebra, son las cosas 
#que puedo medir. Los eventos.
def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))


P_S = list(powerset(S))
#print(P_S)
card_P_S = len(P_S) #es 512

#Ahora, corro el experimento algunas veces
n = 100 #tiro dos veces el dado esta cantidad de veces
RESULTADOS = [(np.random.randint(1,4), np.random.randint(1, 4)) for i in range(0, n)]

#print(RESULTADOS)

#puedo calcular las probas para cada punto muestral con esta sample. Todas deberian parecerse mientras mas tiradas hago
#cada elemento tiene la misma probabilidad, y como 3*3 = 9 elementos, deberia ser 1/9 aprox
PROBAS_EXP = [RESULTADOS.count(i)/n for i in S]
print(f"Corriendo el experimento unas {n} veces, obtengo las siguientes probas")
print("Probas experimentales: ", PROBAS_EXP)
print(f"Que deberian aproximarse a {1/9} cuando n -> inf")
PROBAS_TEORICAS = [1/card_S for _ in range(0, card_S)]
print("Probas teoricas: ", PROBAS_TEORICAS)



#Ahora, si considero el espacio sin reposicion, no puedo permitir repetidos
S = [elem for elem in S if elem[0] != elem[1]]
print("\nS sin reposicion: ", S)
print(f"El espacio se redujo de {card_S} a {len(S)}")
card_S = len(S)
#de igual manera saco los que no son tiradas validas de mis tiradas experimentales
RESULTADOS = [elem for elem in RESULTADOS if elem[0] != elem[1]]
#y debo reducir las tiradas que supuestamente hice, pero recicle en realidad
n = len(RESULTADOS)
#las probas teoricas son
PROBAS_TEO = [1/card_S for _ in range(0, card_S)]
print("Las probas teoricas son: ", PROBAS_TEO)

#Las probas experimentales
PROBAS_EXP = [RESULTADOS.count(i)/n for i in S]
print("Las probas experimentales son: ", PROBAS_EXP)
