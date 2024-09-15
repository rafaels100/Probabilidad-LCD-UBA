import numpy as np

"""
El ejercicio consiste en un pajaro que puede poner 0, 1 o 2 huevos por vez. Cada uno de estos huevos puede desarrollarse o no.
Asi, el espacio muestral consta de duplas donde el primer elemento nos dice la cantidad de huevos puestos, y el segundo nos dice la cantidad de huevos
que se desarrollaron.
omega = {(2,1), (1,1), (0, 0), (2, 2), (1, 0), ...}

Tenemos dos variables aleatoria:
X = #huevos puestos
Y = #huevos desarrollados
Tenemos la probabilidad puntual de X y de Y:
f_X(x) = 0.3 si x = 0
         0.5 si x = 1
         0.2 si x = 2
         0   caso contrario (cc)
         
f_Y(y) = 0.532 si y = 0
         0.396 si y = 1
         0.072 si y = 2
         0     cc
"""
#Voy a crear el espacio muestral a partir de las funciones de probabilidad de X y de Y
#la variable aleatoria X nos dice la cantidad de huevos puestos
X = [0, 1, 2] #atomos de X
P_X = [0.3, 0.5, 0.2] #probabilidad de cada atomo de X
#la variable aleatoria Y nos dice la cantidad de huevos desarrollados
Y = [0, 1, 2] #atomos de Y
P_Y = [0.532, 0.396, 0.072] #probabilidad de cada atomo de Y

#cantidad de muestras, de puntos muestrales que quiero
n = 100
muestras_X = np.random.choice(X, n, P_X)
muestras_Y = np.random.choice(Y, n, P_Y)
#creo el espacio muestral omega
omega = list(zip(muestras_X, muestras_Y))
print(omega)

def f_X(x):
    return sum([1 for elem in omega if elem[0] == x])/len(omega)
    
def f_Y(y):
    return sum([1 for elem in omega if elem[1] == y])/len(omega)

def F_X(x):
    return sum([f_X(x_i) for x_i in range(0, x+1)])

def F_Y(y):
    return sum([f_Y(y_i) for y_i in range(0, y+1)])
    
#si los eventos son independientes, deberia ocurrir que 
#P(X <= x, Y <= y) = P(X <= x) * P(Y <= y)
#F_XY(x, y) = F_X(y) * F_Y(y)

#para ello creo a la funcion de probabilidad conjunta
def f_XY(x, y):
    print(f"({x}, {y})")
    return sum([1 for elem in omega if elem[0] == x and elem[1] == y])/len(omega)

#y la funcion acumulada conjunta
def F_XY(x, y):
    """
    Debo recorrer todas las combinaciones de X e Y para poder calcular todo lo anterior, y poder sumarlos.
    Para eso fijo un x_i, e itero con todos los y_i de 0 a y.
    Lo hago para todos los x_i de 0 a x.
    """
    return sum([sum([f_XY(x_i, y_i) for y_i in range(0, y+1)]) for x_i in range(0, x+1)])

    
print(F_XY(1,1), F_X(1) * F_Y(1))
#parece que more often than not esto se cumple para los eventos menores a 1. 

#veamos todo el espacio
print(F_XY(2,2), F_X(2) * F_Y(2))

#veamos asi
print(F_XY(2,1), F_X(2) * F_Y(1))

#Parece que fueran independientes... makes no sense to me, es claro que la cantidad de huevos puestos no es independiente de la cantidad de huevos
#que se desarrollan
