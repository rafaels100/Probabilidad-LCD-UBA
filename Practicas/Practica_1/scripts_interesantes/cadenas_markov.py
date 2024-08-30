import numpy as np

M = np.array([[0.7, 0.4],
              [0.3, 0.6]])
              
"""
f(i, j): Da la probabilidad de que, empezando desde un dia soleado, luego de i dias nos toque un dia j, donde j es una variable binaria que simboliza:
0 = soleado
1 = nublado
"""

def f(i, j):
    if i == 0:
        if j == 0:
            #si al llegar al final ocurre que estamos en un dia soleado, esta multiplicacion sobrevive para la sumatoria
            return 1
        else:
            #sino, toda la multiplicacion se anula y no suma en la sumatoria
            return 0
    elif i >= 0 and j == 0:
        return M[0][0] * f(i-1, 0) + M[0][1] * f(i-1, 1)
    else:
        return M[1][0] * f(i-1, 0) + M[1][1] * f(i-1, 1)
        
"""
HOW IT WORKS:
j funciona como la variable que nos dice que queremos que pase mañana. A partir de ahi, pensamos: Que puede pasar para que mañana ocurra j (por ej, j = 0 soleado)?
Bueno, puede que hoy sea soleado y mañana sea soleado, o que hoy sea nublado y mañana sea soleado. 
Y que tiene que ocurrir para que hoy sea soleado? Bueno, que el dia anterior haya pedido que mañana sea soleado (f(i-1, 0))
Y que tiene que ocurrir para que hoy sea nublado? BUeno, que el dia anterior haya pedido que mañana sea nublado (f(i-1, 1))
Asi se van acumulando las multiplicaciones, mirando hacia atras, a lo que necesito que pase con los dias anteriores para que ocurra la situacion que quiero mañana.
Si al llegar al ultimo dia i = 0 que puedo considerar, ocurre que el tipo de dia j NO ES el que necesito (en este caso soleado j = 0), entonces esa rama no me sirve,
no es un camino valido de sucesiones de dias que empiezan en soleado (por como defini f) y terminan en soleado (j = 0 inicial). Entonces, multiplico por 0 y se anula 
en la sumatoria. Si ocurre que si es un camino valido, multiplico por 1 y esas multiplicaciones de probas que acumule sobreviven y suman en la sumatoria.
"""

#empezando desde un dia soleado
i = np.array([1, 0])
print(f(1, 0), 0.7**2 + 0.4*0.3, M @ i)
print(f(2, 0), M @ M @ i)
print(f(3, 0), M @ M @ M @ i)
print(f(4, 0), M @ M @ M @ M @ i)

print(f(1, 1), 0.7**2 + 0.4*0.3, M @ i)
print(f(2, 1), M @ M @ i)
print(f(3, 1), M @ M @ M @ i)
print(f(4, 1), M @ M @ M @ M @ i)

"""
f se puede modificar ligeramente para que contemple los casos de inicio soleados o nublados. Agrego una variable k que no se modifica en toda la ejecucion,
y nos sirve para chequear en que situacion estamos cuando llegamos al final (i = 0). Si en ese punto llegamos al tipo de dia que queriamos, devolvemos 1 para
que contemple esas probabilidades, sino 0 y todo se anula
"""
def g(i, j, k):
    if i == 0:
        if j == k:
            #si llegamos al final de la recursion y el dia es del tipo que queremos, sobrevive para la sumatoria
            return 1
        else:
            #si el dia es del tipo contrario, se anula este sumando
            return 0
    elif i >= 0 and j == 0:
        return M[0][0] * g(i-1, 0, k) + M[0][1] * g(i-1, 1, k)
    else:
        return M[1][0] * g(i-1, 0, k) + M[1][1] * g(i-1, 1, k)

#ahora puedo empezar tanto desde un dia soleado (k = 0) como desde un dia nublado (k=1)
s = np.array([1, 0]) #dia soleado
n = np.array([0, 1]) #dia nublado
print(g(1, 0, 0), M @ s) #empezando desde un dia soleado (k=0), luego de un dia (i=1) cual es la proba de que el dia este soleado (j=0)?
print(g(1, 1, 0), M @ s) #empezando desde un dia soleado (k=0), luego de un dia (i=1) cual es la proba de que el dia este nublado (j=1)?

print(g(1, 0, 1), M @ n) #empezando desde un dia nublado (k=1), luego de un dia (i=1) cual es la proba de que el dia este soleado (j=0)?
print(g(1, 1, 1), M @ n) #empezando desde un dia nublado (k=1), luego de un dia (i=1) cual es la proba de que el dia este nublado (j=1)?

print(g(2, 0, 1), M @ M @ n) #empezando desde un dia nublado (k=1), luego de dos dias (i=2) cual es la proba de que el dia este soleado (j=0)?
print(g(2, 1, 1), M @ M @ n) #empezando desde un dia nublado (k=1), luego de dos dias (i=2) cual es la proba de que el dia este nublado (j=1)?
