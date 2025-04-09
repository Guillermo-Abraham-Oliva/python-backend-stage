'''
Análisis de precios de productos: Escribir un programa en Python que analice una lista de precios (l_p)de productos y determine el precio más alto, el precio más bajo y el precio promedio de todos los productos. Soluciona el ejercicio sin usar las funciones max() o min().
'''

import os
os.system('clear' if os.name == 'posix' else 'cls')

precio_maximo = float('-inf')  # atento a esto! se da infinito
precio_minimo = float('inf')   # para que se guarde el valor la 1º vez el los if !
suma = 0.0

l_p = [25.99, 49.50, 78.25, 12.75, 99.99, 65.40, 33.80, 85.20, 18.95, 59.30]
print('\n\nLista precios:', l_p, '\n')

for precio in l_p:
    if precio > precio_maximo:
        precio_maximo = precio
    if precio < precio_minimo:
        precio_minimo = precio
    suma += precio

# Calcular promedio
promedio = suma / len(l_p)

# Mostrar resultados
print('precio maximo: ', precio_maximo, '\n')
print('precio minimo: ', precio_minimo, '\n')
print('suma total de precios: ', suma, '\n')
print('promedio: ', round(promedio, 2), '\n')
print('ultimos 3 valores: ', l_p[-3:], '\n\n')




















