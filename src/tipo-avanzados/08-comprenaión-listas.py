usuarios = [["chanchito", 4],
            ['gatito', 3],
            ['perrito', 8]]

# transformar
nombres = [usuario[0] for usuario in usuarios]

print(nombres)


# filtrar
nombres = [usuario for usuario in usuarios if usuario[1] > 3]

# transformar y filtrar
nombres = [usuario for usuario in usuarios if usuario[1] > 3]

print(nombres)
