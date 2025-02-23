import os
os.system('clear' if os.name == 'posix' else 'cls')

# Pedir al usuario que ingrese un número y almacenarlo como cadena
numero_usuario = input(f'\n\tIntroduce un número: ')

# Inicializar variables
suma = 0
representacion = ''

# Iterar sobre cada dígito del número
for digito in numero_usuario:
    suma += int(digito)  # Convertir el dígito a entero y sumarlo
    # Crear la representación de la suma concatenando el digito (str) con la otra str ' + '
    representacion += digito + ' + '

# Eliminar el último " + " de la representación y añadir el resultado
representacion = representacion[:-3]  # Eliminar los últimos 3 caracteres
representacion += f' = {suma}'  # Añadir el resultado final

# Mostrar el resultado
print(f'\n\t{representacion}\n\n')



