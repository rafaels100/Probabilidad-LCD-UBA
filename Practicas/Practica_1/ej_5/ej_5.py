from itertools import chain, combinations, product
import numpy as np
import random

"""
5)
Este ejercicio nos plantea sacar n bolitas de un bolillero con bolitas numeradas de 1 a N.

a) Proba de que se extraiga la bolita numero m en la k-esima extraccion?

b) Proba de que se extraiga la bolilla m?
"""



def experimento(N, n, m, k):
    #Primero, calculo el espacio muestral con reposicion, y luego elimino los elementos que no son validos.
    #El espacio muestral S de los resultados de todas las n sacadas de bolillas de 1 a N (con reposicion, es como tirar un dado este S)
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

    #a) Proba de que se extraiga la bolita numero m en la k-esima extraccion?
    #teniendo una muestra, ya puedo hacer estadistica y comprobar si mis resultados teoricos se condicen con los experimentales
    #segun mis calculos, la probabilidad de que se extraiga la bolita m en la k-esima extraccion es de
    proba_m_k_teo = ((N-1)/N)**(k-1) * 1/N
    #compruebo, buscando cual es la proporcion de puntos muestrales que obtuve experimentalmente que cumplen con lo pedido, sobre el 
    #total de experimentos que corri
    evento_m_k = [elem for elem in RESULTADOS if elem[k-1] == m]
    card_evento_m_k = len(evento_m_k)
    proba_m_k_exp = card_evento_m_k / cant_exp
    
    print("a) Resultado teorico: ", proba_m_k_teo, " Resultado experimental: ", proba_m_k_exp)
    
    #b) Proba de que se extraiga la bolilla m?
    #n no inclusive, multiplico hasta n - 1. Saco factor como 1/N de la sumatoria
    proba_m_teo = sum([((N-1)/N)**i for i in range(0, n)]) * 1/N
    #compruebo buscando la proporcion de puntos muestrales que tienen a m sobre el total de experimentos realizados
    evento_m = [elem for elem in RESULTADOS if m in elem]
    card_evento_m = len(evento_m)
    proba_m_exp = card_evento_m / cant_exp
    print("\nb) Proba teorica de que ocurra el evento m: ", proba_m_teo, " Proba experimental: ", proba_m_exp)
    
    #compruebo calculando el complemento teoricamente, que es 1 - el resultado teorico obtenido
    proba_no_m_teo = 1 - proba_m_teo
    #Chequeo que el resultado teorico se condiga con el experimental para este calculo
    #evento_no_m = [elem for elem in RESULTADOS if m not in elem]
    #Como ya calcule el evento_m, podria calcular el cardinal del evento_no_m por su complemento, sin necesidad de buscar por esos puntos muestrales en mis experimentos
    card_evento_no_m = cant_exp - card_evento_m
    #print("Deberian coincidir: ", card_evento_no_m, len(evento_no_m))
    proba_no_m_exp = card_evento_no_m / cant_exp
    print("\nProba del complemente de m teorica: ", proba_no_m_teo, " Proba experimental: ", proba_no_m_exp)
    return

N = 6
n = 4
m = 3
k = 3
experimento(N, n, m, k)
