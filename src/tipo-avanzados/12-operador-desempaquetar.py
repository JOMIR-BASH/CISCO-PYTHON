lista1 = (1, 2, 3, 4)

# print(lista)

# print(*lista)

lista2 = (1, 8, 9, 10)

combinada = [*lista1, *lista2]

print(combinada)


punto1 = {"x": 10, "y": 15}
punto2 = {"z": 60, "w": 45}

join = {**punto1, "h": True, **punto2, "z": "mundo"}

print(join)
