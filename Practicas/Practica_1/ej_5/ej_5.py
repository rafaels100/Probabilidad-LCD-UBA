from itertools import chain, combinations, product
import numpy as np
import random
from math import factorial, comb

"""
5)
Este ejercicio nos plantea sacar n bolillas, sin reposicion, de un bolillero con bolitas numeradas de 1 a N.

a) Proba de que se extraiga la bolilla m en la k-esima extraccion?

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
    print(f"\nTamaño del espacio muestral S sin reposicion: {len(S)}")
    print(f"El espacio se redujo de {card_S} a {len(S)}")
    #redefino el cardinal de S
    card_S = len(S)
    #deberia coincidir con las permutaciones de {1,..,N} en n lugares
    card_S_teo = comb(N, n) * factorial(n)
    print(f"Cardinal exacto de S: {card_S} Cardinal teorico: {card_S_teo}")
    
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
    #con el approach de teoria de conjuntos
    """ Calculando la probabilidad exacta """
    #Puedo calcular la probabilidad buscada si capturo todos los puntos muestrales del espacio muestral S que cumplen la condicion pedida, y los divido
    #por todos los puntos muestrales que hay en S
    evento_m_k = [elem for elem in S if elem[k-1] == m]
    card_evento_m_k = len(evento_m_k)
    proba_m_k = card_evento_m_k / card_S
    """ Resultados teoricos """
    #con combinatoria, puedo contador todos los puntos muestrales que cumplen la condicion en S, es decir, calcular el cardinal del evento m en la posicion kesima
    card_evento_m_k_teo = comb(N-1, k-1) * factorial(k-1) * comb(N-k, n-k) * factorial(n-k)
    #para calcular la proba teorica, basta dividir por el cardinal de S
    #proba_m_k_teo = card_evento_m_k_teo / card_S
    #de hecho, si simplificamos esto resulta
    proba_m_k_teo = 1/N
    #tambien pude hallar una formula mas complicada para la probabilidad utilizando teoria de conjuntos y probabilidad condicional
    proba_m_k_teo_conj = np.prod([(N-j)/(N-j+1) for j in range(1, k)]) * 1/(N-k+1)
    """ Probabilidad experimental """
    #compruebo, buscando cual es la proporcion de puntos muestrales que obtuve experimentalmente que cumplen con lo pedido, sobre el 
    #total de experimentos que corri
    evento_m_k_exp = [elem for elem in RESULTADOS if elem[k-1] == m]
    card_evento_m_k_exp = len(evento_m_k_exp)
    proba_m_k_exp = card_evento_m_k_exp / cant_exp
    print("\na) Proba de que se extraiga la bolilla m en la k-esima extraccion?")
    print(f"   Cardinal exacto del evento bolilla m en la k-esima extraccion: {card_evento_m_k} Cardinal teorico: {card_evento_m_k_teo} ")
    print(f"   Probabilidad exacta de sacar la bolilla m en la k-exima tirada: {proba_m_k} \n   Probabilidad teorica con combinatoria y teoria de conjuntos: {proba_m_k_teo} {proba_m_k_teo_conj} \n   Probabilidad experimental:  {proba_m_k_exp}")
    
    #b) Proba de que se extraiga la bolilla m?
    """ Calculando la probabilidad exacta """
    #busco en S todos los puntos muestrales que cumplan con la condicion impuesta por el evento de que m este presente en dicho punto muestral
    #divido por el total de puntos muestrales para calcular la probabilidad exacta
    evento_m = [elem for elem in S if m in elem]
    card_evento_m = len(evento_m)
    proba_m = card_evento_m / card_S
    """ Resultados teoricos """
    #usando combinatoria puedo contar la cantidad de puntos muestrales que cumplen la condicion, es decir, el cardinal del evento m pertenece al punto muestral
    card_evento_m_teo = comb(N-1, n-1) * factorial(n)
    #divido por la cantidad total de puntos muestrales para calcular la proba teorica
    #proba_m_teo = card_evento_m_teo / card_S
    #simplificando se llega a 
    proba_m_teo = n/N
    #usando teoria de conjuntos llegue a una forma de calcular la probabilidad un poco mas rebuscada
    proba_m_teo_conj = sum([np.prod([(N-j)/(N-j+1) for j in range(1, i)]) * 1/(N-i+1) for i in range(1, n+1)]) #n no inclusive, multiplico hasta n - 1. Saco factor como 1/N de la sumatoria
    """ Probabilidad experimental """
    #compruebo buscando la proporcion de puntos muestrales que tienen a m sobre el total de experimentos realizados
    evento_m_exp = [elem for elem in RESULTADOS if m in elem]
    card_evento_m_exp = len(evento_m_exp)
    proba_m_exp = card_evento_m_exp / cant_exp
    print("\nb) Proba de que se extraiga la bolilla m?")
    print(f"   Cardinal exacto del evento bolilla m: {card_evento_m} Cardinal teorico: {card_evento_m_teo} ")
    print(f"   Probabilidad exacta de sacar la bolilla m: {proba_m} \n   Probabilidad teorica con combinatoria y teoria de conjuntos: {proba_m_teo} {proba_m_teo_conj} \n   Probabilidad experimental:  {proba_m_exp}")
    
    #c) El maximo numero obtenido sea menor o gual a m
    """ Calculando la probabilidad exacta """
    #busco todos los puntos muestrales en el espacio muestral S que cumplen la condicion de que el maximo es menor o igual a m
    evento_max_menig_m = [elem for elem in S if max(elem) <= m]
    card_evento_max_menig_m = len(evento_max_menig_m)
    proba_max_menig_m = card_evento_max_menig_m / card_S
    """ Resultados teoricos """
    #con combinatoria puedo contar la cantidad de puntos muestrales que cumplen esto, es decir, el cardinal del evento maximo menor o igual a m
    card_evento_max_menig_m_teo = comb(m, n) * factorial(n)
    #divido por el total de puntos muestrales para hallar la probabilidad teorica
    proba_max_menig_m_teo = card_evento_max_menig_m_teo / card_S
    #con teoria de conjuntos llegue a la siguiente formula 
    proba_max_menig_m_teo_conj =  ((factorial(m) * factorial(N-n))/(factorial(N) * factorial(m-n)))
    """ Probabilidad experimental """
    evento_max_menig_m_exp = [elem for elem in RESULTADOS if max(elem) <= m]
    card_evento_max_menig_m_exp = len(evento_max_menig_m_exp)
    proba_max_menig_m_exp = card_evento_max_menig_m_exp / cant_exp
    print("\nc) El maximo numero obtenido sea menor o igual a m?")
    print(f"   Cardinal exacto del evento maximo menor o igual a m: {card_evento_max_menig_m} Cardinal teorico: {card_evento_max_menig_m_teo} ")
    print(f"   Probabilidad exacta de sacar maximo menor o igual a m: {proba_max_menig_m} \n   Probabilidad teorica con combinatoria y teoria de conjuntos: {proba_max_menig_m_teo} {proba_max_menig_m_teo_conj} \n   Probabilidad experimental:  {proba_max_menig_m_exp}")
    
    #d) El maximo numero obtenido sea m?
    """ Calculando la probabilidad exacta """
    #busco todos los puntos muestrales en el espacio muestral S que cumplen la condicion de que el maximo sea m
    evento_max_m = [elem for elem in S if max(elem) == m]
    card_evento_max_m = len(evento_max_m)
    #calculo la proba exacta
    proba_max_m = card_evento_max_m / card_S
    """ Resultados teoricos """
    #usando combinatoria puedo contar la cantidad de puntos muestrales que cumplen la condicion
    card_evento_max_m_teo = comb(m-1, n-1) * factorial(n)
    #divido por el total de puntos muestrales para dar la proba teorica
    proba_max_m_teo = card_evento_max_m_teo / card_S
    #usando teoria de conjuntos pude llegar a 
    proba_max_m_teo_conj = n * ((factorial(m-1) * factorial(N-n))/(factorial(N) * factorial(m-n)))
    """ Probabilidad experimental """
    evento_max_m_exp = [elem for elem in RESULTADOS if max(elem) == m]
    card_evento_max_m_exp = len(evento_max_m_exp)
    proba_max_m_exp = card_evento_max_m_exp / cant_exp
    print("\nd) El maximo numero obtenido sea m?")
    print(f"   Cardinal exacto del evento maximo igual a m: {card_evento_max_m} Cardinal teorico: {card_evento_max_m_teo} ")
    print(f"   Probabilidad exacta de sacar maximo igual a m: {proba_max_m} \n   Probabilidad teorica con combinatoria y teoria de conjuntos: {proba_max_m_teo} {proba_max_m_teo_conj} \n   Probabilidad experimental:  {proba_max_m_exp}")
    
    #?) El maximo numero obtenido sea mayor o igual a m
    """ Calculando la probabilidad exacta """
    #busco todos los puntos muestrales que cumplan la condicion
    evento_max_mayig_m = [elem for elem in S if max(elem) >= m]
    card_evento_max_mayig_m = len(evento_max_mayig_m)
    #calculo la probabilidad exacta
    proba_max_mayig_m = card_evento_max_mayig_m / card_S
    """ Resultados teoricos """
    #Aqui puedo obtener una formula mediante combinatoria o usar los calculos anteriores y calcularlo por el complemento
    #de combinatoria tenemos que la cantidad de puntos muestrales que cumplen la condicion impuesta por el evento son
    card_evento_max_mayig_m_teo = (comb(N, n) - comb(m-1, n)) * factorial(n)
    proba_max_mayig_m_teo = card_evento_max_mayig_m_teo / card_S
    #de los calculos anteriores podemos obtener esta proba por el complemento
    proba_max_mayig_m_teo_comp = 1 - proba_max_menig_m_teo + proba_max_m_teo
    """ Probabilidad experimental """
    evento_max_mayig_m_exp = [elem for elem in RESULTADOS if max(elem) >= m]
    card_evento_max_mayig_m_exp = len(evento_max_mayig_m_exp)
    proba_max_mayig_m_exp = card_evento_max_mayig_m_exp / cant_exp
    print("\n?) El maximo numero obtenido sea mayor o igual a m?")
    print(f"   Cardinal exacto del evento maximo mayor o igual a m: {card_evento_max_mayig_m} Cardinal teorico: {card_evento_max_mayig_m_teo} ")
    print(f"   Probabilidad exacta de sacar maximo mayor o igual a m: {proba_max_mayig_m} \n   Probabilidad teorica con combinatoria y por el complemento: {proba_max_mayig_m_teo} {proba_max_mayig_m_teo_comp} \n   Probabilidad experimental:  {proba_max_mayig_m_exp}")
    
    #e)  El maximo numero obtenido este entre a y b? Con n <= a < b <= N
    """ Calculando la probabilidad exacta """
    #busco los puntos muestrales que cumplan la condicion
    evento_max_a_b = [elem for elem in S if a <= max(elem) <= b]
    card_evento_max_a_b = len(evento_max_a_b)
    #calculo la proba exacta
    proba_max_a_b = card_evento_max_a_b / card_S
    """ Resultados teoricos """
    #por combinatoria puedo contar la cantidad de puntos muestrales que cumplen
    card_evento_max_a_b_teo = (comb(b, n) - comb(a-1, n)) * factorial(n)
    #divido por el total de puntos muestrales para hallar la proba
    proba_max_a_b_teo = card_evento_max_a_b_teo / card_S
    #por teoria de conjuntos llegue a una forma muy complicada, calculando por el complemento. Basicamente lo que hice en combinatoria pero mas verboso
    proba_max_a_b_teo_conj = (factorial(b) * factorial(N-n)) / (factorial(N) * factorial(b-n)) - \
                             (factorial(a)*factorial(N-n)) / (factorial(N)*factorial(a-n)) + \
                             (n * factorial(a-1) * factorial(N-n)) / (factorial(N) * factorial(a-n)) 
    """ Probabilidad experimental """
    evento_max_a_b_exp = [elem for elem in RESULTADOS if a <= max(elem) <= b]
    card_evento_max_a_b_exp = len(evento_max_a_b_exp)
    proba_max_a_b_exp = card_evento_max_a_b_exp / cant_exp
    print(f"\ne) El maximo numero obtenido este entre a y b? Con n={n} <= a={a} < b={b} <= N={N}")
    print(f"   Cardinal exacto del evento maximo entre a y b: {card_evento_max_a_b} Cardinal teorico: {card_evento_max_a_b_teo} ")
    print(f"   Probabilidad exacta de sacar maximo entre a y b: {proba_max_a_b} \n   Probabilidad teorica con combinatoria y por teoria de conjuntos: {proba_max_a_b_teo} {proba_max_a_b_teo_conj} \n   Probabilidad experimental:  {proba_max_a_b_exp}")
    
    #f) Proba de que los numeros de las bolillas en el orden que fueron extraidas constituyan una sucesion estrictamente creciente?
    """ Calculando la probabilidad exacta """
    #Puedo obtener todos los puntos muestrales crecientes de mi espacio muestral con numpy
    evento_suc_crec = [elem for elem in S if np.all(np.diff(elem) > 0)]
    card_evento_suc_crec = len(evento_suc_crec)
    proba_suc_crec = card_evento_suc_crec / card_S
    """ Resultados teoricos """
    #no pude obtener una formula para contar la cantidad de puntos muestrales con combinatoria
    #segun chatGPT, por combinatoria se obtiene que la proba de obtener una sucesion creciente es de
    proba_suc_crec_teo = 1 / factorial(n) #still dunno why though
    #sin embargo, si puedo hacer una recursion que cuente las ramas crecientes del arbol recursivo
    evento_suc_crec_teo_rec = sucesiones_crecientes(n, N)
    card_evento_suc_crec_teo_rec = len(evento_suc_crec_teo_rec)
    proba_suc_crec_teo_rec = card_evento_suc_crec_teo_rec / card_S
    """ Probabilidad experimental """
    #busco las sucesiones crecientes que salieron en los experimentos
    evento_suc_crec_exp = [elem for elem in RESULTADOS if np.all(np.diff(elem) > 0)]
    card_evento_suc_crec_exp = len(evento_suc_crec_exp)
    proba_suc_crec_exp = card_evento_suc_crec_exp / cant_exp
    print("\nf) Proba de que los numeros de las bolillas en el orden que fueron extraidas constituyan una sucesion estrictamente creciente?")
    print(f"   Cardinal exacto del evento sucesion creciente: {card_evento_suc_crec} Cardinal teorico por recursion: {card_evento_suc_crec_teo_rec} ")
    print(f"   Probabilidad exacta de sacar una sucesion creciente: {proba_suc_crec} \n   Probabilidad teorica con combinatoria y por recursion: {proba_suc_crec_teo} {proba_suc_crec_teo_rec} \n   Probabilidad experimental:  {proba_suc_crec_exp}")
    
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
k = 4
#a, b tales que n <= a < b <= N
a = 6
b = 9
experimento(N, n, m, k, a, b)
