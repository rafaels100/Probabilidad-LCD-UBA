#!/bin/bash

#Para hallar los numeros con digitos sin repetir, y contar la cantidad que hay
#crunch 3 3 123456 -d 1 | grep '\(.\).*\1' | wc -l

#Para hallar los numeros que empiezan con 0 con digitos sin repetir que sean pares, y contarlos
crunch 3 3 123456 -d 1 | grep -v '\(.\).*\1' | grep '[246]$' | wc -l
#aqui dejo 'fijo' al 0, asi se inhabilita un digito y solo tengo 3 sillas. Ademas, el 0 se va de la poblacion. Luego, me deshago de los que tengan digitos repetidos
#con el primer grep.
#Con el segundo grep me quedo con los pares
#finalmente cuento la cantidad de numeros

#Explicacion:
#crunch 3 3 123456 -d 1
#Esto crea numeros de 3 digitos usando los numeros 123456. Ademas con el -d flag no permitimos digitos que tengan numeros repetidos CONSECUTIVOS, pues
#limitamos las repeticiones consecutivas a solo 1.
#Esto quiere decir que numeros como 331 o 522 no va a estar, pues tienen repeticiones consecutivas. 
#Sin embargo, -d no afecta las repeticiones no consecutivas, por lo que numeros como 131 o 262 si van a estar.

#Es aqui donde entra grep, y el regex loco. Lo que hace este regex es encontrar el primer caracter que se repite, y si encuentra un match, grep 
#devuelve toda la linea.
#Explicacion:
#grep -v '\(.\).*\1'
#Grep matchea patrones en strings, y si hay match devuelve toda la string/linea. Sin embargo, al usar el flag -v estamos tomando el COMPLEMENTO
#de los matcheos, es decir, grep nos va a devolver todo aquello que NO cumple con el regex que le estamos pasando.
#Esto es util cuando queres quedarte con los numeros que no tienen repetidos, como es en este caso. 
#Podemos separar este regex en 3 partes fundamentales:
#1)----- \(.\)
#Esto captura un caracter, cualquiera. En realidad es (.), pero necesitamos escapar los parentesis usando \ para que no los tome literal y sepa que son
#de grupo.
#2)----- .*
#Esto captura todo lo que este entre medio, cualquier caracter . y todo lo que le sigue *.
#3)----- \1
#Esto es igual al primer caracter que capturo en 1), aqui es donde esta el matcheo con caracter que se repite, pues se invoca al grupo que capture al ppio
#con cualquier caracter.

#para hallar todas las cuaternas pares con digitos distintos entre si que NO empiezan con cero, puedo hacerlo de una
crunch 4 4 0123456 -d 1 | grep -v '^0' | grep -v '\(.\).*\1' | grep '[0246]$'
A=$(crunch 4 4 0123456 -d 1 | grep -v '^0' | grep -v '\(.\).*\1' | grep '[0246]$' | wc -l)
echo $((4*4*5*6 - 4*5*3)) $A

#o puedo hacerlo calculando primero las cuaternas pares con digitos disintos
B=$(crunch 4 4 0123456 -d 1 | grep -v '\(.\).*\1' | grep '[0246]$' | wc -l)

#y luego las cuaternas pares con digitos distintos que SI empiezan con 0 (esto es equivalente a lo que hice al ppio)
C=$(crunch 4 4 0123456 -d 1 | grep '^0' | grep -v '\(.\).*\1' | grep '[0246]$' | wc -l)

#y luego las resto
echo $(($B - $C))

#ambos metodos funcionan :)
