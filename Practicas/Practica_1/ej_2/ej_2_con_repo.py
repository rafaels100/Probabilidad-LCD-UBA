from itertools import chain, combinations, product
import numpy as np
import random
from math import factorial

"""
2)
Este ejercicio nos plantea sacar n bolitas de un bolillero con bolitas numeradas de 1 a N.

a) Proba de que se extraiga la bolita numero m en la k-esima extraccion?

?) Proba de que se extraiga la bolita numero m en la k-esima extraccion por primera vez?

b) Proba de que se extraiga la bolilla m?

c) Proba de que el maximo sea meor o igual a m?

d) Proba de que el maximo sea igual a m?

e) Proba de que el maximo este entra a y b inclusive? n <= a < b <= N
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
    print("\nTamaño del espacio muestral S (con reposicion): ", card_S)
    #cardinal teorico
    card_S_teo = N**n
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
    #NOTA: Aqui no importa si m aparecio antes de la kesima extraccion, lo importante es que este alli en la posicion k
    #busco los puntos muestrales en el espacio muestral donde aparece m en la kesima posicion (sin importar si m haya aparecido antes en la secuencia)
    evento_m_k = [elem for elem in S if elem[k-1] == m]
    card_evento_m_k = len(evento_m_k)
    proba_m_k = card_evento_m_k / card_S
    #segun mis calculos, la probabilidad de que se extraiga la bolita m en la k-esima extraccion es de
    proba_m_k_teo = 1/N
    #compruebo, buscando cual es la proporcion de puntos muestrales que obtuve experimentalmente que cumplen con lo pedido, sobre el 
    #total de experimentos que corri
    evento_m_k_exp = [elem for elem in RESULTADOS if elem[k-1] == m]
    card_evento_m_k_exp = len(evento_m_k_exp)
    proba_m_k_exp = card_evento_m_k_exp / cant_exp
    print(f"\na) Restulado exacto: {proba_m_k} \nResultado teorico: {proba_m_k_teo} \nResultado experimental: {proba_m_k_exp}")

    #?) Proba de que se extraiga la bolita numero m en la k-esima extraccion POR PRIMERA VEZ?
    #busco los puntos muestrales en los que aparece m por primera vez en la k esima posicion. Aqui si importa si m aparecio antes en la secuencia.
    evento_m_k_1 = [elem for elem in S if m not in elem[:k-1] and elem[k-1] == m]
    #print(evento_m_k)
    card_evento_m_k_1 = len(evento_m_k_1)
    proba_m_k_1 = card_evento_m_k_1 / card_S
    #segun mis calculos, la probabilidad de que se extraiga la bolita m en la k-esima extraccion por primera vez es de
    proba_m_k_1_teo = ((N-1)/N)**(k-1) * 1/N
    #compruebo, buscando cual es la proporcion de puntos muestrales que obtuve experimentalmente que cumplen con lo pedido, sobre el 
    #total de experimentos que corri
    evento_m_k_1_exp = [elem for elem in RESULTADOS if elem[k-1] == m]
    card_evento_m_k_1_exp = len(evento_m_k_1_exp)
    proba_m_k_1_exp = card_evento_m_k_1_exp / cant_exp
    
    print(f"\n?) Restulado exacto: {proba_m_k_1} \nResultado teorico: {proba_m_k_1_teo} \nResultado experimental: {proba_m_k_1_exp}")
    
    #b) Proba de que se extraiga la bolilla m?
    #busco los puntos muestrales donde ocurre el evento
    evento_m = [elem for elem in S if m in elem]
    card_evento_m = len(evento_m)
    proba_m = card_evento_m / card_S
    #teoricamente obtuve que
    #aqui chatgpt sugiere calcular por el complemento, calculando la proba de que m no aparezca, y se lo restamos a 1:
    proba_m_teo = 1 - ((N - 1)/ N)**n
    #por mi parte hice este approach con teorica de conjuntos que funciona bien
    proba_m_teo_conj = sum([((N-1)/N)**i for i in range(0, n)]) * 1/N    #Esto sirve para extraccion sin reposicion
    #compruebo buscando la proporcion de puntos muestrales que tienen a m sobre el total de experimentos realizados
    evento_m_exp = [elem for elem in RESULTADOS if m in elem]
    card_evento_m_exp = len(evento_m_exp)
    proba_m_exp = card_evento_m / cant_exp
    print(f"\nb) Restulado exacto: {proba_m} \nProba teorica de que ocurra el evento m con combinatoria y teoria de conjuntos: {proba_m_teo} {proba_m_teo_conj} \nProba experimental: {proba_m_exp}")
    
    #c) Proba de que el maximo sea meor o igual a m?
    #busco los puntos muestrales en los que aparece m por primera vez en la k esima posicion. Aqui si importa si m aparecio antes en la secuencia.
    evento_max_menig_m = [elem for elem in S if max(elem) <= m]
    card_evento_max_menig_m = len(evento_max_menig_m)
    proba_max_menig_m = card_evento_max_menig_m / card_S
    #segun mis calculos, la probabilidad de que se extraiga la bolita m en la k-esima extraccion por primera vez es de
    proba_max_menig_m_teo = (m/N)**n
    #compruebo, buscando cual es la proporcion de puntos muestrales que obtuve experimentalmente que cumplen con lo pedido, sobre el 
    #total de experimentos que corri
    evento_max_menig_m_exp = [elem for elem in RESULTADOS if max(elem) <= m]
    card_evento_max_menig_m_exp = len(evento_max_menig_m_exp)
    proba_max_menig_m_exp = card_evento_max_menig_m_exp / cant_exp
    
    print(f"\nc) Restulado exacto: {proba_max_menig_m} \nResultado teorico: {proba_max_menig_m_teo} \nResultado experimental: {proba_max_menig_m_exp}")
    
    #d) Proba de que el maximo sea igual a m?
    #busco los puntos muestrales en los que aparece m por primera vez en la k esima posicion. Aqui si importa si m aparecio antes en la secuencia.
    evento_max_m = [elem for elem in S if max(elem) == m]
    card_evento_max_m = len(evento_max_m)
    proba_max_m = card_evento_max_m / card_S
    #segun mis calculos, la probabilidad de que se extraiga la bolita m en la k-esima extraccion por primera vez es de
    proba_max_m_teo = ((m-1)/N)**(n-1) * 1/N
    #chatgpt propone
    proba_max_m_teo_1 = (m/N)**n * (1 - ((m-1)/N)**n)
    #compruebo, buscando cual es la proporcion de puntos muestrales que obtuve experimentalmente que cumplen con lo pedido, sobre el 
    #total de experimentos que corri
    evento_max_m_exp = [elem for elem in RESULTADOS if max(elem) == m]
    card_evento_max_m_exp = len(evento_max_m_exp)
    proba_max_m_exp = card_evento_max_m_exp / cant_exp
    
    print(f"\nd) Restulado exacto: {proba_max_m} \nResultado teorico: {proba_max_m_teo, proba_max_m_teo_1} \nResultado experimental: {proba_max_m_exp}")
    
    #e) Proba de que el maximo este entra a y b inclusive? n <= a < b <= N
    #busco los puntos muestrales en los que aparece m por primera vez en la k esima posicion. Aqui si importa si m aparecio antes en la secuencia.
    evento_max_a_b = [elem for elem in S if a <= max(elem) <= b]
    card_evento_max_a_b = len(evento_max_a_b)
    proba_max_a_b = card_evento_max_a_b / card_S
    #segun mis calculos, la probabilidad de que se extraiga la bolita m en la k-esima extraccion por primera vez es de
    proba_max_a_b_teo = (b/N)**n - ((a-1)/N)**n
    #compruebo, buscando cual es la proporcion de puntos muestrales que obtuve experimentalmente que cumplen con lo pedido, sobre el 
    #total de experimentos que corri
    evento_max_a_b_exp = [elem for elem in RESULTADOS if a <= max(elem) <= b]
    card_evento_max_a_b_exp = len(evento_max_a_b_exp)
    proba_max_a_b_exp = card_evento_max_a_b_exp / cant_exp
    
    print(f"\ne) Restulado exacto: {proba_max_a_b} \nResultado teorico: {proba_max_a_b_teo} \nResultado experimental: {proba_max_a_b_exp}")
    
    return

N = 9
n = 4
m = 3
k = 3
#a, b tales que n <= a < b <= N
a = 5
b = 7
experimento(N, n, m, k)
