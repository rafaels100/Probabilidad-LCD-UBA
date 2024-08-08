import math
import itertools
"""
4)a)
Cuantos anagramas de BIBLIOTECARIA pueden formarse?
"""
"""
Si pienso la palabra bilbiotecarios como cada letra fuera unica, con una numeracion con las que son iguales, puedo pensar en las permutaciones de 
las letras, y dividir por la cantidad de letras repetidas !. 
Eso es porque no me interesan las repeticiones que tienen a las letras iguales 'enumeradas' en distintas posiciones, pues I_1 = I_2 = I_3, es decir,
todas las Is que aparece son iguales para mi, aunque las trate como unicas en las permutaciones.
Por eso debo dividir por #sillas!, para quitar esos repetidos.
"""
A = list("BIBLIOTECARIA")
print(A)
permutaciones = itertools.permutations(A, len(A))
#for i in range(0,10):
 #   print(next(permutaciones))
    
#para contar la cantidad de permutaciones con repeticiones de letras uso generacion comprensiva
#cant_permut_con_rep = sum(1 for _ in permutaciones)
#TARDA DEMASIADO EN CONTAR TODOS LOS ELEMENTOS PORQUE SON DEMASIADOS

#para obtener la verdadera cantidad de permutaciones, divido por la cantidad de letras repetidas
repet_I = 3
repet_B = 2
repet_A = 2
#cant_permut = cant_permut_con_rep / math.factorial(repet_I + repet_B + repet_A)
#print(cant_permut)
#contar la cantidad de permutaciones lleva demasiado tiempo. Lo mejor es usar las formulas. 
#Para obtener la cantidad de permutaciones, simplemente uso la formula de las combinaciones y multiplico por el factorial de la cantidad de sillas
cant_permut_con_rep = math.comb(len(A), len(A)) * math.factorial(len(A))

#Ahora divido por el factorial de la cantidad de letras repetidas para obtener la verdadera cantidad de permutaciones
cant_permut = cant_permut_con_rep / math.factorial(repet_I + repet_B + repet_A)

print(cant_permut)
print(math.factorial(10)/math.factorial(math.factorial(repet_I) * math.factorial(repet_B) * math.factorial(repet_A)))
