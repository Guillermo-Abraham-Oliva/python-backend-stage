'''
Este programa genera 100 números aleatorios de 6 dígitos, 
los muestra en una lista numerada,
los clasifica como pares o impares 
y muestra el número menor y mayor,
manteniendo el formato de seis dígitos.
'''
import os
os.system('clear' if os.name == 'posix' else 'cls')

list_num = []
num_pares = 0
num_impares = 0
i = 0

import random

list_num = random.sample(range(1000000), k = 100)

# Variables para el mínimo y máximo
num_menor = min(list_num)  # Encuentra el menor
num_mayor = max(list_num)  # Encuentra el mayor

for num in list_num:
    if num % 2 == 0:
        num_pares += 1
        i += 1
        print(f'\t {i:03d}) {num:06d} (Par)')
    else:
        num_impares += 1
        i += 1
        print(f'\t {i:03d}) {num:06d} (Impar)')

print(f'\n\tCantidad total de números pares: {num_pares}')
print(f'\tCantidad total de números impares: {num_impares}')

# Mostrar el número menor y mayor con formato de 6 dígitos
print(f'\n\tNúmero menor: {num_menor:06d}')
print(f'\tNúmero mayor: {num_mayor:06d}\n')