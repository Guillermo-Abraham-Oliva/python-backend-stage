'''Este programa permite al usuario ingresar una serie de números enteros positivos 
y realizar diversas operaciones matemáticas con ellos. 
Inicialmente, limpia la pantalla de la terminal para ofrecer una visualización ordenada. 
Luego, solicita al usuario que ingrese números, indicando que puede 
continuar ingresando valores con la tecla Enter o finalizar la entrada escribiendo 0. 
Cada número ingresado es validado para asegurar que sea un entero positivo, 
mostrando un mensaje de error si el valor ingresado no es válido. 
Una vez finalizada la captura de datos, el programa muestra 
la lista ordenada en orden ascendente y descendente, el valor máximo y mínimo, 
la suma total, la cantidad de valores ingresados, el promedio redondeado a dos decimales 
y una lista con los valores elevados al cuadrado. 
De esta manera, el programa permite realizar un análisis numérico básico 
de los valores ingresados de forma clara y estructurada.'''

# Borro la pantalla de la terminal
import os
os.system('clear' if os.name == 'posix' else 'cls')

# Inicializo
lista_num = []
num = ''

print('\n' + '=' * 50)
print('\tIngresa números enteros positivos')
print('\t(Enter -> seguir ingresando)')
print('\t(0 -> salir)')
print('=' * 50 + '\n')

# Bucle para pedir números
while True:
    try:
        num = input('Número? : ').strip()  # Pido número (str por defecto)

        # Si el input es 'falsy' continúo el bucle
        if not num:
            continue

        # Si no es un número, lanzo un error
        if not num.isdigit():
            raise ValueError('--- Debe ser un número entero positivo (0 -> salir)')

        num = int(num)  # Convierto a entero

        if num == 0:
            break  # Salgo del bucle principal

        lista_num.append(num)  # Agrego a la lista

    except ValueError as e:  # Manejo de errores
        print(f'ERROR: {e}')

# Verifico si la lista está vacía
if not lista_num:
    print('\n\tNo se ingresaron valores. Adiós!')
else:
    print('\n\t Lista ordenada ascendentemente:', sorted(lista_num))
    print('\n\t Lista ordenada y sin repetidos:', sorted(set(lista_num)), '\n')
    print('\n\t Lista ordenada descendentemente:', sorted(lista_num, reverse=True))
    print('\n\t Máximo valor de la lista:', max(lista_num))
    print('\n\t Mínimo valor de la lista:', min(lista_num))
    print('\n\t Suma de todos los valores:', sum(lista_num))
    print('\n\t Cantidad de valores ingresados:', len(lista_num))

    promedio = sum(lista_num) / len(lista_num)  # Cálculo del promedio
    print('\n\t Promedio redondeado a 2 decimales:', round(promedio, 2), '\n')

    print('\n\t Lista al cuadrado:', [cada_numero ** 2 for cada_numero in lista_num], '\n')

    print('\n\t el último número de la lista es el', lista_num[-1], '\n\n')
