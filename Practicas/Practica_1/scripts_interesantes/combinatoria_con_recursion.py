"""
Se tira un dado de {1, 2, .., N} caras unas n veces, y se anota el resultado.

En este script trato de formar todas las posibles permutaciones que me daran el espacio muestral S, que contiene todos los posibles resultados
del experimento, todos los puntos muestrales.
"""
N = 4
n = 3
U = [i for i in range(1, N+1)]


S = []
def rec(x):
    print("Entro")
    if len(x) == n:
        S.append(x)
        return
    for elem in U:
        rec(x.append(elem))
    return

#llamo a la funcion con el conjunto vacio []
rec([])

print(S, len([]))
