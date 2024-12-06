for numero in range(5):
    print(numero, numero * "hola mundo ")

buscar = 10
for numero in range(5):
    print(numero)
    if numero == buscar:
        print("Encontrado", buscar)
        break
else:
    print("\"No se encontró el valor buscado\"")

for char in "Ultimate python":
    print(char)
