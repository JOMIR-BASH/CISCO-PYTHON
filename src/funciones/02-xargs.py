def suma(*numeros):
    resultado = 0
    for numero in numeros:
        resultado += numero
    print(resultado)


suma(7, 1,)
suma(7, 1, 10)
suma(7, 1, 10, 20)
suma(5, 10, 3, 14, 20)
