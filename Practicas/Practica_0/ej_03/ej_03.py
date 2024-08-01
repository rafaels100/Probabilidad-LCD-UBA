import math

"""
3)a)
Aqui tenemos que no nos importa el orden, y hay extraccion sin reposicion, es decir, es un numero combinatorio
"""
RTA = math.comb(123, 5)
print("RTA a):", RTA)

"""
b)
Aqui volvemos a meter la bolita al pool una vez elegimos una, asi que en cada eleccion tenemos 123 opciones.
Debemos deshacernos de los repetidos con un 5!
"""
RTA = 123**5 / (5*4*3*2*1)
print("RTA b):", RTA)

"""
c)
Estamos en la misma situacion que en a)
"""
RTA = math.comb(123, 5)
print("RTA c):", RTA)
