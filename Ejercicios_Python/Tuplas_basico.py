import os
os.system('clear' if os.name == 'posix' else 'cls')
#############################################################################

# Comprobar a existencia de un elemento
mi_tupla = ('manzana', 45, True)

print('manzana' in mi_tupla) # Salida: True   / porque existe
print('pera' in mi_tupla)    # Salida: False  / porque no existe

print(mi_tupla[0:3])  # Salida: ('manzana', 45, True)

print(mi_tupla.count('manzana')) # Salida: 1 / porque 'manzana' aparece 1 vez 
print(len(mi_tupla))   # Salida: 3 / porque la tupla tiene 3 elementos

# pasar de una lista a una tupla
mi_lista = [1, 2, 3, 4, 5,]
mi_tupla = tuple(mi_lista)
print(f'mi_lista = {mi_lista}')  # Salida: mi_lista = [1, 2, 3, 4, 5]
print(f'mi_tupla = {mi_tupla}')  # Salida: mi_tupla = (1, 2, 3, 4, 5)

# pasar de una tupla a una lista
mi_tupla = (1, 2, 3, 4, 5,)
mi_lista = list(mi_tupla)
print(f'mi_tupla = {mi_tupla}')  # Salida: mi_tupla = (1, 2, 3, 4, 5)
print(f'mi_lista = {mi_lista}')  # Salida: mi_lista = [1, 2, 3, 4, 5]

# combinar tuplas formando una tupla de tuplas
tupla1 = (1, 2, 3)
tupla2 = ('a', 'b', 'c')
tupla_combinada = tuple(zip(tupla1, tupla2))
print(tupla_combinada)  # Salida: ((1, 'a'), (2, 'b'), (3, 'c'))

# acceder a los elementos de una tupla de tuplas
tupla_combinada = ((1, 'a'), (2, 'b'), (3, 'c'))
print(mi_tupla[0][0])
print(mi_tupla[1][1])
print(mi_tupla[2][0])

# "Empaquetamiento" y "Desempaquetamiento" de tuplas
# El concepto de empaquetamiento y desempaquetamiento en Python se refiere a cómo se pueden agrupar múltiples valores en una sola variable (empaquetamiento) y luego extraerlos de manera sencilla en múltiples variables (desempaquetamiento).

mi_tupla = ("fruta", 45, True)       # Empaquetamiento
cadenas, numeros, booleanos = mi_tupla # Desempaquetamiento
# El Desempaquetamiento es la asignación de variables a cada elemento..
print(cadenas)
print(numeros)
print(booleanos)
