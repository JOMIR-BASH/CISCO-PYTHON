punto = {"x": 56, "y": 25}

print(punto["x"])
print(punto["y"])

punto["z"] = 63

# print(punto, punto["lala"])

if "lala" in punto:
    print("encontré lala", punto["lala"])

print(punto.get("lala", 97))

del punto["x"]
del (punto["y"])

print(punto)

punto["x"] = 85

print(punto)

for valor in punto:
    print(valor, punto[valor])


for valor in punto.items():
    print(valor)


for llave, valor in punto.items():
    print(llave, valor)

usuarios = [
    {"id": 1, "nombre": "chanchito"},
    {"id": 2, "nombre": "puerco"},
    {"id": 3, "nombre": "Lola"},
    {"id": 4, "nombre": "Judas"},
]

for usuario in usuarios:
    print(usuario["nombre"])
