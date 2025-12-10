'''Utilizandose funciones utiles como:
sorted(), max(), min(), sum(), len() y round() 
se muestra en formato f.strings 
y como quedaría lo mismo con 
concatenación simple de argumentos (argumentos separados por coma)
'''

# Lista de números
lista_num = [1, 2, 3, 4]

# sorted()
print(f'\n\tLista en orden ascend: {sorted(lista_num)}')                 # formato f-strings
print('\n\tLista en orden ascend: ', sorted(lista_num))                  # concatenación simple de argumentos

print(f'\n\tLista en orden descen: {sorted(lista_num, reverse=True)}')   # formato f-strings
print('\n\tLista en orden descen: ', sorted(lista_num, reverse=True))    # concatenación simple de argumentos

# max()
print(f'\n\tMáximo valor de la lista: {max(lista_num)}')                 # formato f-strings
print('\n\tMáximo valor de la lista: ', max(lista_num))                  # concatenación simple de argumentos

# min()
print(f'\n\tMínimo valor de la lista: {min(lista_num)}')                 # formato f-strings
print('\n\tMínimo valor de la lista: ', min(lista_num))                  # concatenación simple de argumentos

# sum()
print(f'\n\tLa suma de todos los valores es: {sum(lista_num)}')          # formato f-strings
print('\n\tLa suma de todos los valores es: ', sum(lista_num))           # concatenación simple de argumentos

# len()
print(f'\n\tCantidad de valores ingresados: {len(lista_num)}')           # formato f-strings
print('\n\tCantidad de valores ingresados: ', len(lista_num))            # concatenación simple de argumentos

# round()
promedio = sum(lista_num) / len(lista_num)
print(f'\n\tPromedio redondeado a 2 decimales: {round(promedio, 2)}')    # formato f-strings
print('\n\tPromedio redondeado a 2 decimales: ', round(promedio, 2))     # concatenación simple de argumentos

