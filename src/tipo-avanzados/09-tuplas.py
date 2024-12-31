numeros = (1, 2, 3, 4, 5) + (6, 7, 9)

print(numeros)

punto = tuple([95, 85])

print(punto)


menosNumeros = numeros[:7]

print(menosNumeros)

primero, segundo, *otros = numeros

print(primero, segundo, otros)

for n in numeros:
    print(n)

listaNumeros = list(numeros)

listaNumeros[0] = "Chanchito puerco"

print(listaNumeros)
