print("""
Bienvenidos a la calculadora
Para salir escribe \"salir\"
Las operaciones disponibles son:
+ suma
- resta
* multi
/ div

""")

resultado = None  # Se crea la variable "resultado" y se le asigna el valor de None
# Los valores "Falsy" son aquellos que tiene el valor de None, un string vacio ", un cero y el valor de False
while True:
    if not resultado:  # Dados los requerimientos del ejercicio que piden solicitar un primer ingreso de datos por parte del usuario, para asegurar que esta parte se ejecute solo durante el inicio del loop,
        # se puede utilizar esta técnica donde se inicializa la variable que capturará el valor del usuario, a None y luego se coloca la instrucción "if not variable" ya que permitira devolver un "true"
        # que viene de negar el estado inicial de la variable declarada e inicializada a None, en otras palabras al tener un valor de None se convierte un "falsy" o "false" y al negarlo con el "not"
        # nos aseguramos que esa sección del código solo se corra mientras el usuario no ha ingresado ningún valor
        resultado = input("Ingrese número:  ")
        if resultado.lower() == "salir":  # no se convierte a entero la entrada del usuario, ya que se está validando si ha ingresado la palabra "salir" que detiene la ejecución
            break  # Se agrega e¡un break para detener la ejecución en caso de que el usuario ingrese la palabra "salir"
        resultado = int(resultado)
    op = input("Ingresa operación: ")
    if op.lower() == "salir":
        break
    n2 = input("Ingresa siguiente número: ")
    if n2.lower() == "salir":
        break
    n2 = int(n2)
    if op.lower() == "suma":
        resultado += n2
    elif op.lower() == "resta":
        resultado -= n2
    elif op.lower() == "multi":
        resultado *= n2
    elif op.lower() == "div":
        resultado /= n2
    else:
        print("Operación no válida")
        break

    print(f"El resultado de la operación {
          op} entre ambos número es {resultado}")
