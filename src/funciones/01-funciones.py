def hola(nombre, apellido="Feliz"): #cuando definimos "parametros" en esta sección se podran usar más adelante
    print("Hola mundo")
    print(f"Bienvenido {nombre} {apellido}")


hola("Nicolas") #cuando se entregan valores a los argumento se llaman "parametro"
hola("Nicolas", "Rivera") #si se configuran parametros por defecto, sus "argumentos" se vuelven opcionales, si no se entrega un valor, toman el asignado por defecto

#argumentos nombrados
hola (apellido="Rivera", nombre="Nicolai")