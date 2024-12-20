saludo = "Esta es una variable global"


def saludar():
    global saludo
    saludo = "Hola mundo"
    print(saludo)


def saludarCahnchito():
    saludo = "Hola chanchito"
    print(saludo)


print(saludo)
saludar()
