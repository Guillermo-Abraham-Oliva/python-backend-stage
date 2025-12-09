# Ejercicio: MENSAJE DE BIENVENIDA

num_consigna = int(1)

# -1- inicial y basico
print('\nConsigna: ' + str(num_consigna))
num_consigna = num_consigna + 1

msj = str('estás usando "Python"')
print(msj)

# -2- pide nombre de usuario por 1º vez
print('\nConsigna Nº ' + str(num_consigna))
num_consigna = num_consigna + 1

hol = 'hola '
Nomb_Us = input('nombre de usuario? ')
print(hol.title() + Nomb_Us + " " + msj)

# -3- mayuscula
print('\nConsigna Nº ' + str(num_consigna))
num_consigna = num_consigna + 1

Nomb_Us = input('Nombre de usuario? ')
print(hol.upper() + Nomb_Us.upper() + " " + msj.upper())

# -4- minuscula
print('\nConsigna Nº ' + str(num_consigna))
num_consigna = num_consigna + 1

Nomb_Us = input('Nombre de usuario? ')
print(hol.lower() + Nomb_Us.lower() + " " + msj.lower())

# -5- titulo
print('\nConsigna Nº ' + str(num_consigna))
num_consigna = num_consigna + 1

Nomb_Us = input('Nombre de usuario? ')
print(hol.title() + Nomb_Us.title() + " " + msj)

# -6- final (elimina puntos y title)
print('\nConsigna Nº ' + str(num_consigna))
num_consigna = num_consigna + 1

Nomb_Us = input('Nombre de usuario? ')
print(hol.title() + Nomb_Us.replace('.', " ").title() + " " + msj)




