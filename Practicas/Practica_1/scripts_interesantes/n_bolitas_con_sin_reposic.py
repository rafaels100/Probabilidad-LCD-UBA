from itertools import chain, combinations, product
import numpy as np
import random

"""
El experimento se basa en sacar n veces bolitas numeradas del 1 a N.
Abarco los dos casos, con reposicion y sin reposicion.
NOTA: Notar que el espacio es equiprobable, tengo la misma probabilidad de sacar cada bolita.
"""

def experimento_con_reposicion(N, n):
    #El espacio muestral S de los resultados de todas las tiradas de dos dados posibles es
    S = list(product(*[range(1, N + 1) for _ in range(0, n)]))
    card_S = len(S)
    print("Tamaño del espacio muestral con reposicion: ", card_S)
    """
    EXPLICACION de S:
    Lo que hago aqui es crear todos los espacios muestrales que voy a multiplicar en el producto cartesiano usando list comprehension: 
    Creo n listas de valores 1 a N inclusive, y tengo que hacer unpack de la lista con * adelante para pasarle todas las listas como argumento,
    no como una lista de listas.
    """

    #Ahora, corro el experimento algunas veces
    cant_exp = 1000 #corro cant_exp veces el experimento de sacar n veces las bolitas que van de 1 a N
    RESULTADOS = [S[np.random.randint(0, card_S)] for _ in range(0, cant_exp)]
    """
    EXPLICACION de RESULTADOS:
    La idea es ver todo el pool de puntos muestrales posibles, todo el espacio muestral, y sacar algunos al azar. randint me asegura que la 
    probabilidad con la que voy a elegir un numero de 0 a card_S va a ser la misma para cada numero, es decir, va a ser de 1/card_S para
    cada numero. Eso coincide con la probabilidad de ocurrir de cada uno de mis puntos muestrales.
    NOTA: ESTO SOLO LO PUEDO HACER PORQUE EL ESPACIO ES EQUIPROBABLE.
    """

    #puedo calcular las probas para cada punto muestral con esta sample. Todas deberian parecerse mientras mas tiradas hago
    #cada elemento tiene la misma probabilidad
    PROBAS_TEORICAS = [1/card_S for _ in range(0, card_S)]
    print(f"Las probas teoricas con reposicion son: ", PROBAS_TEORICAS)
    PROBAS_EXP = [RESULTADOS.count(i)/cant_exp for i in S]
    print(f"Las probas experimentales con reposicion obtenidas de correr el experimento unas {cant_exp} veces son: ", PROBAS_EXP)
    return



def experimento_sin_reposicion(N, n):
    #El espacio muestral S de los resultados de todas las tiradas de dos dados posibles es
    S = list(product(*[range(1, N + 1) for _ in range(0, n)]))
    card_S = len(S)
    """
    EXPLICACION de S:
    Lo que hago aqui es crear todos los espacios muestrales que voy a multiplicar en el producto cartesiano usando list comprehension: 
    Creo n listas de valores 1 a N inclusive, y tengo que hacer unpack de la lista con * adelante para pasarle todas las listas como argumento,
    no como una lista de listas.
    """
    #Ahora, si considero el espacio sin reposicion, no puedo permitir repetidos. Para eliminar las tiradas que no son validas,
    #es decir, aquellas en donde la lista no se achica al transformarla en un conjunto y calcular su tamanio
    S = [elem for elem in S if len(elem) == len(set(elem))]
    #print("\nS sin reposicion: ", S)
    print("\nTamaño del espacio muestral sin reposicion: ", len(S))
    print(f"El espacio se redujo de {card_S} a {len(S)}")
    #redefino el cardinal de S
    card_S = len(S)
    
    #corro cant_exp veces el experimento de sacar n veces las bolitas que van de 1 a N
    cant_exp = 1000
    RESULTADOS = [S[np.random.randint(0, card_S)] for _ in range(0, cant_exp)]
    """
    EXPLICACION de RESULTADOS:
    La idea es ver todo el pool de puntos muestrales posibles, todo el espacio muestral, y sacar algunos al azar. randint me asegura que la 
    probabilidad con la que voy a elegir un numero de 0 a card_S va a ser la misma para cada numero, es decir, va a ser de 1/card_S para
    cada numero. Eso coincide con la probabilidad de ocurrir de cada uno de mis puntos muestrales.
    NOTA: ESTO SOLO LO PUEDO HACER PORQUE EL ESPACIO ES EQUIPROBABLE.
    """
    
    #las probas teoricas son
    PROBAS_TEO = [1/card_S for _ in range(0, card_S)]
    print("Las probas teoricas sin reposicion son: ", PROBAS_TEO)

    #Las probas experimentales
    PROBAS_EXP = [RESULTADOS.count(i)/cant_exp for i in S]
    print(f"Las probas experimentales sin reposicion obtenidas de correr el experimento unas {cant_exp} veces son: ", PROBAS_EXP)
    return

N = 4
n = 3
experimento_con_reposicion(N, n)
experimento_sin_reposicion(N, n)
