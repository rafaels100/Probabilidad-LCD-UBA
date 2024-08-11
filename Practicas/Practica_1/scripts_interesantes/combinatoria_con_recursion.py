"""
Se tira un dado de {1, 2, .., N} caras unas n veces, y se anota el resultado.

En este script formo todas las posibles permutaciones que me daran el espacio muestral S, que contiene todos los posibles resultados
del experimento, todos los puntos muestrales.

Lo hago con reposicion y sin reposicion.
"""
N = 4
n = 3
#creo la lista U con todos los resultados posibles del dado/ todas las bolillas enumeradas
U = [i for i in range(1, N+1)]

"""
rec_con_repo(i)
Argumentos: 
int i
Explicacion:
La idea es ir creando los n niveles del arbol recursivamente. En el primer nivel tendremos N hijos, en el segundo N**2, en el tercero N**3, y asi
hasta N**n, que son todas las permutaciones posibles con reposicion.
"""
#el espacio muestral S es
S = []
#creo una lista llena de 0s con n elementos. Aqui trackeo el camino que voy recorriendo en el arbol. Cuando hago backtracking
#ese camino hata ese punto era valido
camino = [0] * n
def rec_con_repo(i):
    if i == n:
        """
        Como python, cuando haces append, pasa por alias al objeto que estas anexando a la lista, eso es una complicacion si quiero
        manipular a la lista camino, pues va a ser la que este trackeando el camino en el arbol.
        Por eso, al llegar al final de la recursion, paso la lista por copia con lista[:] en vez de por referencia.
        """
        S.append(camino[:])
        return
    for elem in U:
        camino[i] = elem
        #NOTA: como no uso el metodo del append, sino que modifico el indice de la lista, no necesito hacer pop
        rec_con_repo(i + 1)
    return

#llamo a la funcion con el 0
rec_con_repo(0)

print(S, len(S))


S = []
def rec_sin_repo(i):
    if i == n:
        S.append(camino[:])
        return
    for elem in U:
        #como es extraccion sin reposicion, debo tener cuidado de no repetir elementos en mis puntos muestrales de S
        if elem not in camino[:i]:
            #Con este if me aseguro de que el camino que voy a seguir ahora no repite los elementos que use hasta este momento 
            #(el i-esimo indice de la lista)
            camino[i] = elem
            rec_sin_repo(i + 1)
    return
    
rec_sin_repo(0)
print(S, len(S))
