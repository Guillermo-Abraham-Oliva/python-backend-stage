'''Utilizandose funciones utiles como:
sorted(), max(), min(), sum(), len() y round() 
se muestra en formato f.strings 
y como quedaría lo mismo con 
concatenación simple de argumentos
'''

lista_num = [1, 2, 3, 4]

print(f'\n\tLista en orden ascend: {sorted(lista_num)}')                # formato f-strings
print(f'\n\tLista en orden ascend: ', sorted(lista_num))                # concatenación simple de argumentos

print(f'\n\tLista en orden descen: {sorted(lista_num, reverse=True)}')  # formato f-strings
print(f'\n\tLista en orden descen: ', sorted(lista_num, reverse=True))  # concatenación simple de argumentos

print(f'\n\tmaximo valor de la lista: {max(lista_num)}')                # formato f-strings
print('\n\tmaximo valor de la lista: ', max(lista_num))                 # concatenación simple de argumentos

print(f'\n\tminimo valor de la lista: {min(lista_num)}')                # formato f-strings
print('\n\tminimo valor de la lista: ', min(lista_num))                 # concatenación simple de argumentos

print(f'\n\tLa suma de todos los valores es: {sum(lista_num)}')         # formato f-strings
print('\n\tLa suma de todos los valores es: ', sum(lista_num))          # concatenación simple de argumentos

print(f'\n\tcantidad de valores ingresados: {len(lista_num)}')          # formato f-strings
print('\n\tcantidad de valores ingresados: ', len(lista_num))           # concatenación simple de argumentos

promedio = sum(lista_num) / len(lista_num)  # calculo del promedio
print('\n\tPromedio redondeado a 2 decimales: ', round(promedio, 2))    # formato f-strings
print('\n\tPromedio redondeado a 2 decimales: ', round(promedio, 2))    # concatenación simple de argumentos

# estudiar el caso de round(variable, numero de decimales deseados) !!!
