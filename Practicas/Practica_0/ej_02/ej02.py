import math
"""
2)a)
Martin tiene pintura de 7 colores, va a pintar una mesa y una silla. De cuantas maneras puede hacerlo?
"""
"""
Aqui asumo que la pintura no se le acaba luego de usarla en la mesa, por lo que hay 7**2 formas de hacerlo.
El orden en que pinta importa, por lo que son las permutaciones, no las combinaciones
(azul, rojo) != (rojo, azul)
Pues simboliza pintar el objeto
"""
RTA = 7**2
print(f"\n2)a) RTA: La cantidad de formas en que puede pintar la mesa y la silla son {RTA}")

#-------------------------------------------------
"""
2)b)
Charly tiene que ubicar 7 pares de medias iguales en dos cajones distintos. De cuantas maneras puede hacerlo?
"""
"""
Aqui no hay distincion entre los pares de medias. Sin embargo, los enumeramos para crear esa distincion. 
Una vez que usa cierta cantidad de pares de medias, debe colocar el resto en el otro cajon.
Entonces estas son las posibles configuraciones:
0 pares de media primer cajon => 7 pares de media en el segundo
1 pares de media primer cajon => 6 pares de media en el segundo
                                .
                                .
                                .
7 pares de media primer cajon => 0 pares de media en el segundo

Son 8 posibles formas de ordenar los pares de media
"""
contador = 0
for i in range(0, 8):
    #print(f"{i} pares de media primer cajon y {7 - i} pares de media en el segundo")
    contador += 1

print(f"\n2)b) RTA: Hay {contador} posibles formas de ordenar los pares de medias")

"""
2)c)
La nona tiene muchos caramelos de naranja y de limon. Quiere regalarle uno a cada uno de sus 7 nietos. De cuantas maneras puede hacerlo?
"""
#Si enumeramos todos los n + m caramelos, es ordenamiento sin reposicion. Me interesan las combinaciones, pues es lo mismo:
#n4 l1 n5 l2 n6 l3 n7 que
#n2 l3 n6 l4 n7 l8 n10
n = 10
m = 3
#Calculo el numero combinatorio, la cantidad de subconjuntos que puedo extraer de a 7 del conjunto de caramelos enumerados
RTA = math.comb(n + m, 7)
print(f"\n2)c) RTA (con combinatoria): La cantidad de formas en que puede repartir los caramelos entre los 7 nietos es {RTA}")

"""
No me convence, mas que nada porque hay dos opciones para cada nieto: O le doy un caramelo de naranja o le doy uno de limon.
Me suena a que es una recursion de este estilo:
"""

def rec(n, m, nietos):
    if nietos == 0:
        #si ya reparti caramelos a todos los nietos y aun me quedan caramelos por repartir, esta es una forma valida de hacerlo. Sumo 1 a la recursion
        #considero la variable nietos como la cantidad de nietos, no el indice del nieto en el array de nietos. Por eso empiezo desde el total de nietos
        #y no desde el total - 1. Cuando ya me quedan 0 nietos por repartir caramelos, ahi termina mi recursion.
        return 1
    elif n == 0 or m == 0:
        #ya me quede sin alguno de los caramelos, debo repartirle al resto de mis nietos todos los que me quedan del mismo sabor
        #es el fin de un camino, de una forma de repartir caramelos
        #(esto asumiendo que me quedan suficientes caramelos del otro sabor para darle al resto de mis nietos. Puede que algunos se queden 
        #sin caramelos si no tengo esta consideracion).
        #si me quede sin caramelos de naranja, debo ver que me alcanzan con los que me quedan de limon para todos los nietos que faltan
        if n == 0 and (m - nietos) >= 0:
            return 1
        #si en cambio me quede sin caramelos de limon, deben ser los de naranja los que deben alcanzar para el resto de nietos
        elif (n - nietos) >= 0:
            return 1
        else:
            #en caso de que los caramelos de uno u otro sabor no me alcanzen para los nietos restantes, esta no es una forma valida de repartir los caramelos
            #no sumo nada en la recursion
            return 0
    else:
        nietos -= 1
        return rec(n - 1, m, nietos) + rec(n, m - 1, nietos)

n = 5 #caramelos de naranja
m = 3 #caramelos de limon
nietos = 7
#llamo a la funcion con cierta cantidad de caramelos iniciales y cierta cantidad de nietos iniciales
#NOTA: A diferencia de otros ejercicios de recursion en donde las variables se asocian al indice de un array, aqui son cantidades, no indices,
#por eso llamo a la funcion con las cantidades y no con las cantidades - 1, para arreglar el tema de los indices en arrays.
RTA = rec(n, m, nietos)
print(f"2)c) RTA ALTERNATIVA (con recursion): La cantidad de formas en que puede repartir los {n} caramelos de naranja y los {m} caramelos de limon entre los 7 nietos es {RTA}")
print("Si, quite a difference, me inclino por la recursion")

"""
CHATGPT 1:
Como nos dicen que la nona tiene muchos caramelos de naranja y de limon, podemos asumir que n y m son mucho mayores que la cantidad de nietos, es decir,
n, m >> nietos.
Esto da lugar a que cada nieto siempre tenga 2 opciones para recibir caramelos: o de naranja o de limon.
Entonces tenemos 2**7 = 128 posibilidades de darles caramelos
"""
RTA_chatgpt_1 = 2**7
print(f"2)c) RTA (con combinatoria CHATGPT 1): La cantidad de formas en que puede repartir los caramelos entre los 7 nietos es {RTA_chatgpt_1}")
"""
CHATGPT 2:
Otra forma de calcularlo es usar el truco de pensar al numero combinatorio a lo The Bright Side of Mathematics, pensarlo desde las sillas:
Si tengo r = #nietos sillas y tengo k caramelos de limon (el resto seran de naranjas, no me tengo que preocupar)... Cuantas formas tengo de 
distribuir esos k caramelos entre los r nietos?

Pero el tema es que tengo bastantes caramelos de limon para repartir, tantos como nietos, asi que debo considerar todos los casos.
Reparto 1 de limon y luego todos de naranja, luego reparto 2 de limon y el resto de naranja, luego 3 de limon y otros naranja, y asi...
Al final sumo todos los resultados de estas posibles configuraciones, y tengo la cantidad total de formas en que puedo distribuir
caramelos de naranja y limon entre mis 7 nietos.

Se juega con el hecho de que hay dos posibilidades: repartir k caramelos de limon implica que r - k caramelos de naranja van a llegar a los otros nietos.

Hay dos formas de ver al numero combinatorio (n, k):
1- Forma clasica
Cuantas formas hay de generar subconjuntos de k elementos de un conjunto de n elementos?
Esto es, cuantos grupos (sin repeticiones) de a k elementos puedo formar del grupo mas grande.
Es como mirar desde el grupo a las sillas, de arriba hacia abajo.

2- Forma tomar k elementos y repartirlos entre n lugares
Aqui tenemos k 'objetos' y queremos repartirlos entre n lugares/guiones.
Es como mirar desde las sillas hacia las personas, de abajo hacia arriba.

CONEXION ENTRE LAS DOS FORMAS DE VERLO:
Pero si pienso que ese objeto que quiero repartir en realidad se lo doy a una persona del grupo grande, es como si ese grupo que se crea 
de k personas definiera no solo lo que le pasa a el, sino lo que le pasa los demas en las posiciones restantes de las sillas. Porque no le queda otra
al resto de las sillas de ordenarse de la otra forma, ya que hay dos posibilidades. Como no es una, debe ser la otra. 
"""
RTA_chatgpt_2 = sum([math.comb(7, k) for k in range(0, 8)])
print(f"2)c) RTA (con combinatoria CHATGPT 2): La cantidad de formas en que puede repartir los caramelos entre los 7 nietos es {RTA_chatgpt_2}")

#veo que si dejo que los numeros n y m sean mas grandes que la cantidad de nietos, mi recursion funciona :)
n = m = 10
RTA = rec(n, m, nietos)
print(f"2)c) RTA ALTERNATIVA (con recursion): La cantidad de formas en que puede repartir los {n} caramelos de naranja y los {m} caramelos de limon entre los 7 nietos es {RTA}")
#entonces mi recursion es mas abarcativa, pues contempla los casos en que n y m son menores a la cantidad de nietos

"""
REFLEXION:
En mi primer approach tenia todo al reves: RTA = math.comb(n + m, 7)
Aqui consideraba a cada caramelo como una 'persona', estaba tageado, cuando en realidad los caramelos son indistinguibles uno del otro, lo unico que los
diferencia es el sabor, y lo hace en tan solo dos clases, no en n + m clases individuales.

Cuando tenemos estos temas de dos clases de objetos indistinguibles entre si, conviene pensarlo desde las sillas, de abajo hacia arriba:
Las personas son las sillas, y elijo a k personas para ser los portadores de los caramelos/objetos que quiero repartir. El resto de n - k
personas van a tener que portar los otros objetos indefectiblemente (si alcanzan).
"""

"""
2)d)
Beto tiene que decidir los resultados de un consurso en que participan 7 personas y hay premio para el primero y el segundo.
De cuantas formas puede hacerlo?
"""
"""
Este combiene pensarlo desde las sillas: Son las permutaciones.
"""
RTA = 7 * 6 #pues me interesan las permutaciones entre el primer y segundo lugar
print(f"\n2)d) RTA : Hay {RTA} formas de hacerlo")

"""
2)e)
Ana tiene 7 libros distintos y debe elegir 2 para llevarse al viaje. De cuantas maneras puede hacerlo?
"""
"""
Aqui no importa el orden. Es el numero combinatorio
"""
RTA = math.comb(7, 2)
print(f"\n2)e) RTA : Tiene {RTA} formas de hacerlo")
