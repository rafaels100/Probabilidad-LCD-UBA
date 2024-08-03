"""
iterador en python
En python uno define un iterador cuando define la clase, si quiere permitir que se itere por el objeto de la clase.
Una vez que moves el iterador, se queda alli.
La forma en que se hace es definiendo la funcion reservada __iter__().
El resultado de avanzar el iterador puede guardarse en una variable o no, pero el iterador avanza. Solo tiene ese metodo. Avanzar. NO retrocede, no se resetea. Avanza.

Para avanzar el iterador no se usa un metodo propio de la clase, sino que se usa la built in funcion next()
"""
a = [14,532,43,34]

b = a.__iter__()
print(next(b))


#otra forma de crear un iterador es usar la built in function iter(). No necesitas definir un iterador para la clase, si tiene una estructura iterable, iter() te 
#crea el iterador. Crazy stuff.
b = iter(a)
c = next(b)
next(b)
next(b)
print(next(b))


#Tambien se puede avanzar el iterador en un for loop. Debo reinicializar el iterador
b = iter(a)

for item in b:
    print(item)
    #incluso puedo recortar el loop avanzando el iterador adentro del propio loop
    next(b)


