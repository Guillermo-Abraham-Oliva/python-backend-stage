'''
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

EJERCICIO MIO

Pedir por pantalla que se ingrese un número entero. 
Dicho número puede tener cualquier cantidad de dígitos. 
Sumar dígito a dígito. 
Mostrar el resultado.

|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
'''

import os
os.system('clear' if os.name == 'posix' else 'cls')

# incialización
suma = 0

# Solicitar al usuario que introduzca un número
numero_usuario = input("\n\tIntroduce un número de varias cifras: ")

# Iterar sobre cada dígito del número y mostrarlo en una línea diferente
for digito in numero_usuario:
    suma += int(digito)

# imprimir suma
print(f'\n\tLa suma de todos esos números da {suma}\n\n')









