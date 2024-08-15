from itertools import chain, combinations, product
import numpy as np
import random
from math import factorial, comb

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



def experimento(N, n, m, k, a, b):
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
    #deberia coincidir con las permutaciones de {1,..,N} en n lugares
    card_S_teo = factorial(N)/factorial(N-n)
    print("Cardinal teorico: ", card_S_teo, "Cardinal computado: ", card_S)
    
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
    #proba_m_k_teo = ((N-1)/N)**(k-1) * 1/(N-k+1) Esta sirve para extraccion con reposicion
    proba_m_k_teo = np.prod([(N-j)/(N-j+1) for j in range(1, k)]) * 1/(N-k+1)
    proba_m_k_teo = 1/N
    #compruebo, buscando cual es la proporcion de puntos muestrales que obtuve experimentalmente que cumplen con lo pedido, sobre el 
    #total de experimentos que corri
    evento_m_k = [elem for elem in RESULTADOS if elem[k-1] == m]
    card_evento_m_k = len(evento_m_k)
    proba_m_k_exp = card_evento_m_k / cant_exp
    
    print("a) Resultado teorico: ", proba_m_k_teo, " Resultado experimental: ", proba_m_k_exp)
    
    #b) Proba de que se extraiga la bolilla m?
    #n no inclusive, multiplico hasta n - 1. Saco factor como 1/N de la sumatoria
    #proba_m_teo = sum([((N-1)/N)**i for i in range(0, n)]) * 1/N    Esto sirve para extraccion sin reposicion
    
    proba_m_teo = sum([np.prod([(N-j)/(N-j+1) for j in range(1, i)]) * 1/(N-i+1) for i in range(1, n+1)])
    #compruebo buscando la proporcion de puntos muestrales que tienen a m sobre el total de experimentos realizados
    evento_m = [elem for elem in RESULTADOS if m in elem]
    card_evento_m = len(evento_m)
    evento_m_teo = [elem for elem in S if m in elem]
    card_evento_m_teo = len(evento_m_teo)
    print("\nCardinal de evento m: ", card_evento_m_teo, "Tamaño del espacio muestral: ", card_S, "Proba de m: ", card_evento_m_teo / card_S)
    proba_m_exp = card_evento_m / cant_exp
    print("b) Proba teorica de que ocurra el evento m: ", proba_m_teo, " Proba experimental: ", proba_m_exp)
    
    #compruebo calculando el complemento teoricamente, que es 1 - el resultado teorico obtenido
    proba_no_m_teo = 1 - proba_m_teo
    #Chequeo que el resultado teorico se condiga con el experimental para este calculo
    #evento_no_m = [elem for elem in RESULTADOS if m not in elem]
    #Como ya calcule el evento_m, podria calcular el cardinal del evento_no_m por su complemento, sin necesidad de buscar por esos puntos muestrales en mis experimentos
    card_evento_no_m = cant_exp - card_evento_m
    #print("Deberian coincidir: ", card_evento_no_m, len(evento_no_m))
    proba_no_m_exp = card_evento_no_m / cant_exp
    print("\nProba del complemente de m teorica: ", proba_no_m_teo, " Proba experimental: ", proba_no_m_exp)
    
    #c) El maximo numero obtenido sea menor o gual a m
    #La proba obtenida de la teoria es
    proba_max_menig_m_teo =  ((factorial(m) * factorial(N-n))/(factorial(N) * factorial(m-n)))
    evento_max_menig_m = [elem for elem in RESULTADOS if max(elem) <= m]
    #print(evento_menig_m)
    card_evento_max_menig_m = len(evento_max_menig_m)
    #la probabilidad experimental es
    proba_max_menig_m_exp = card_evento_max_menig_m / cant_exp
    print("\nc) Proba maximo elemento sea menor o igual a m teorica: ", proba_max_menig_m_teo, " Proba experimental: ", proba_max_menig_m_exp)
    
    #d) El maximo numero obtenido sea m?
    proba_max_m_teo = n * ((factorial(m-1) * factorial(N-n))/(factorial(N) * factorial(m-n)))
    evento_max_m = [elem for elem in RESULTADOS if max(elem) == m]
    #print(evento_max_m)
    card_evento_max_m = len(evento_max_m)
    proba_max_m_exp = card_evento_max_m / cant_exp
    print("\nd) Proba maximo elemento sea m teorica: ", proba_max_m_teo, " Proba experimental: ", proba_max_m_exp)
    
    #?) El maximo numero obtenido sea mayor o igual a m
    #Aqui puedo obtener una formula mediante hacer ejemplos como hice en a,b,c,d, o puedo usar lo obtenido previamente
    #para calcular esta probabilidad. Hago ambos:
    #proba_max_mayig_m_teo_1 = (factorial(N-m+1) * factorial(N-n)) / (factorial(N) * factorial(N-m+1-n)) NO FUNCIONA, SE ROMPE EL DENOMINADOR para ciertos m
    #de los calculos anteriores deberiamos obtener que
    proba_max_mayig_m_teo = 1 - proba_max_menig_m_teo + proba_max_m_teo
    #compruebo
    #print(f"Estas dos probas deberian ser iguales {proba_max_mayig_m_teo} {proba_max_mayig_m_teo_1}") La proba de formula no funciono, pero la otra si
    evento_max_mayig_m = [elem for elem in RESULTADOS if max(elem) >= m]
    #print(evento_menig_m)
    card_evento_max_mayig_m = len(evento_max_mayig_m)
    #la probabilidad experimental es
    proba_max_mayig_m_exp = card_evento_max_mayig_m / cant_exp
    print("\n?) Proba maximo elemento sea mayor o igual a m teorica: ", proba_max_mayig_m_teo, " Proba experimental: ", proba_max_mayig_m_exp)
    
    #e)  El maximo numero obtenido este entre a y b? Con n <= a < b <= N
    #resultado teorico
    proba_max_a_b_teo = (factorial(b) * factorial(N-n)) / (factorial(N) * factorial(b-n)) - \
                        (factorial(a)*factorial(N-n)) / (factorial(N)*factorial(a-n)) + \
                        (n * factorial(a-1) * factorial(N-n)) / (factorial(N) * factorial(a-n)) 
    #resultado experimental
    evento_max_a_b = [elem for elem in RESULTADOS if a <= max(elem) <= b]
    #print(evento_max_a_b)
    card_evento_max_a_b = len(evento_max_a_b)
    proba_max_a_b_exp = card_evento_max_a_b / cant_exp
    print("\ne) Proba maximo elemento este entre a y b teorica: ", proba_max_a_b_teo, " Proba experimental: ", proba_max_a_b_exp)
    
    #f) Proba de que los numeros de las bolillas en el orden que fueron extraidas constituyan una sucesion estrictamente creciente?
    #No se me ocurre aun una respuesta teorica para este, pero puedo obtenerla experimentalmente al menos
    
    #Puedo obtener una especie de pseudoproba teorica si busco en todo el espacio muestral
    evento_suc_crec_teo = [elem for elem in S if np.all(np.diff(elem) > 0)]
    #print(evento_suc_crec_teo, len(evento_suc_crec_teo))
    proba_suc_crec_pseudoteo = len(evento_suc_crec_teo) / card_S
    #puedo incluso hacerlo recursivamente
    evento_suc_crec_rec = sucesiones_crecientes(n, N)
    print(evento_suc_crec_rec, len(evento_suc_crec_rec))
    #busco las sucesiones crecientes que salieron en los experimentos
    evento_suc_crec = [elem for elem in RESULTADOS if np.all(np.diff(elem) > 0)]
    #print(evento_suc_crec)
    proba_suc_crec_exp = len(evento_suc_crec) / cant_exp
    print(f"\nf) Proba de sucesion creciente resultado pseudoteorico: {proba_suc_crec_pseudoteo} Resultado experimental: {proba_suc_crec_exp}")
    print(1/factorial(n))
    return
    

#para el ejericio f
def rec_suc_crec(i, S, U, camino):
    if i == n:
        S.append(camino[:])
        return
    for elem in U:
        #como es extraccion sin reposicion, debo tener cuidado de no repetir elementos en mis puntos muestrales de S
        if elem not in camino[:i]:
            #Con este if me aseguro de que el camino que voy a seguir ahora no repite los elementos que use hasta este momento 
            #(el i-esimo indice de la lista)
            if i > 0:
                #con este if me aseguro de no seguir ramas que no sean crecientes
                if elem > camino[i-1]:
                    camino[i] = elem
                    rec_suc_crec(i + 1, S, U, camino)
            else:
                #si estoy en el primero me interesan seguir todas las ramas
                camino[i] = elem
                rec_suc_crec(i + 1, S, U, camino)
    return


def sucesiones_crecientes(n, N):
    #variables necesarias para el ej5f
    S = [] #donde guardare las sucesiones crecientes
    camino = [0] * n
    U = [i for i in range(1, N+1)]
    rec_suc_crec(0, S, U, camino)
    return S


    

N = 9
n = 4
m = 7
k = 3
#a, b tales que n <= a < b <= N
a = 5
b = 8
experimento(N, n, m, k, a, b)
