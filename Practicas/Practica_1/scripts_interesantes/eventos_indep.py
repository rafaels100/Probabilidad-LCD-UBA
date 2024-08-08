from itertools import chain, combinations

"""
El experimento consiste en tirar dos veces seguidas un dado de 3 caras.
Asi, el espacio muestral S estara compuesto por duplas, y tendra un tamaño de card_S = 3x3 = 9 elementos.
A su vez, todos los eventos que puedo medir vienen dados por la mayor sigma algebra posible: El conjunto de partes del espacio muestral, Partes(S).
El tamaño de todos los eventos posibles sera entonces card_Partes(S) = 2**9 = 512 eventos posibles

El objetivo sera tomar un evento cualquiera de todos los posibles y buscar los eventos que sean independientes con este.
"""
#El espacio muestral S de los resultados de todas las tiradas de dos dados posibles es
S = [(x, y) for x in range(1, 4) for y in range(1, 4)]
#print(S)
card_S = len(S) #es 9

#Puedo obtener todos los eventos posibles calculando el conjunto de partes del espacio muestral. Es mi sigma algebra, son las cosas 
#que puedo medir. Los eventos.
def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))


P_S = list(powerset(S))
#print(P_S)
card_P_S = len(P_S) #es 512
#print(card_P_S)

"""
Voy a elegir un evento al azar, y voy a ver si alguno de los otros eventos es independiente de el
"""
#creo la funcion que toma un evento y busca los eventos independientes con este
def buscar_indep(A):
    #chequeo que A sea un evento, es decir que este en mi power set
    if not A in P_S:
        print("El conjunto no es un evento posible")
        return
    #si si lo es, calculo su cardinal
    card_A = len(A)
    #calculo el cardinal de cada evento
    card_B = [len(B) for B in P_S]
    #calculo la interseccion entre este evento y cada evento posible en mi powerset y calculo su cardinal
    card_A_B = [len(set(A) & set(B)) for B in P_S]
    #hago la prueba de independencia para cada evento que no sea el conjunto nulo ni todo el espacio muestral
    #el conjunto nulo me trae problemas en la division por 0 y todo el espacio muestral siempre es independiente de cualquier conjunto, no me aporta
    res = [card_A_B[i]/card_B[i] == card_A/card_S for i in range(1, len(card_B) - 1)]
    #si alguno de los eventos paso la prueba, devuelvo los resultados. Si no, devuelvo False
    #print(res)
    if not (True in res):
        return False, None, None
    else:
        #le agrego mas uno a los indices para hacer el shifteo de no haber considerado al conjunto nulo en la creacion de res, que esta en la posicion 0
        return [i+1 for i in range(0, len(res)) if res[i] == True], card_B, card_A_B

#El evento A es todos los elementos que su suma sea par
A = tuple(elem for elem in S if (elem[0] + elem[1]) % 2 == 0)
res, card_B, card_A_B = buscar_indep(A)
print(res)
#El evento B es todos los elementos que su suma de 3
B = tuple(elem for elem in S if (elem[0] + elem[1]) == 3)
res, card_B, card_A_B = buscar_indep(B)
print(res)
#El evento C son todos los elementos que el primer componente sea distinto al segundo
C = tuple(elem for elem in S if elem[0] != elem[1])
print("C", C)
res, card_B, card_A_B = buscar_indep(C)
eventos_indep = [P_S[i] for i in res]
print("Eventos independientes a C: ", eventos_indep)

#chequeo si estos eventos creados a ojo estan en el conjunto de eventos independientes
ev_1 = ((1, 2), (2, 1), (3, 3))
ev_2 = ((1, 1), (2, 1), (2, 3), (3, 1), (3, 2), (3, 3)) 
print(ev_1 in eventos_indep, ev_2 in eventos_indep)
#chequeo el largo de los eventos independientes
print([len(e) for e in eventos_indep])
