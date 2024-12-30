numeros = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]


numeros2 = sorted(numeros, reverse=True)
print(numeros)
print(numeros2)

usuarios = [["chanchito", 4],
            ['gatito', 3],
            ['perrito', 8]]


usuarios.sort(key=lambda el: el[1], reverse=True)

print(usuarios)
