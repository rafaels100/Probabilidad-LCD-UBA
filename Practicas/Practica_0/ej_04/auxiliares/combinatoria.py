import itertools

"""
itertools es la libreria para iterar sobre cosas
"""
"""
Puedo obtener todas las combinaciones en grupos de a n
"""
a = [32,12,53,11]

combinaciones = itertools.combinations(a, 3)
print(combinaciones) #vemos que es un objeto llamado combinations
b = next(combinaciones) #es un objeto iterable, compuesto por 
print(type(b)) #tuplas
print(b)
#como ya avance el iterador, ahora va a empezar por el segundo elemento
for item in combinaciones:
    print(item)

#si quisiera conocer la cantidad de elementos que tiene el iterador, debo necesariamente iterar por todos los elementos
#para iterar efectivamente sobre el obejto, creo una funcion generadora. Esto lo puedo hacer mediante la comprension de generadores
#Esa funcion devuelve 1 cada vez que encuentra un elemento. Luego uso sum para obtener la suma de todos esos 1's, y asi encontrar
#la cantidad de elementos en las combinaciones.
combinaciones = itertools.combinations(a, 3)
cant_comb = sum(1 for _ in combinaciones)
print("Cantidad de combinaciones de a 3 posibles: ", cant_comb)

"""
Puedo obtener las permutaciones de manera similar
"""
permutaciones = itertools.permutations(a, 3)
#for item in permutaciones:
 #   print(item)

#y el numero de permutaciones de a 3 de la lista es
cant_perm = sum(1 for _ in permutaciones)
print("Cantidad de permutaciones de a 3 posibles: ", cant_perm)
print("Lo cual deberia ser igual a la cantidad de combinaciones por el factorial de numero de sillas, 3: ", cant_comb * 3 * 2 * 1)
