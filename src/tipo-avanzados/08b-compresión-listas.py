usuarios = [["chanchito", 4],
            ['gatito', 3],
            ['perrito', 8]]

# map
nombres = list(map(lambda usuario: usuario[0], usuarios))

print(nombres)

# filter
menosUsuarios = list(filter(lambda usuario: usuario[1] > 3, usuarios))

print(menosUsuarios)
