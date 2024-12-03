"""Uso de operadores lógicos"""
# and, or, not
gas = False
encendido = True
edad = 18

if not gas and encendido or edad > 17:
    print("Puedes avanzar")
else:
    print("No puedes avanzar")
