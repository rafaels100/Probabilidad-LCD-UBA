#El espacio muestral S es
S = [(x, y) for x in range(1, 7) for y in range(1, 7)]
print(S)
print(len(S), 6**2)

#El evento A es
A = [elem for elem in S if (elem[0] + elem[1]) % 2 == 0]
print(A, len(A), 6**2/2)
