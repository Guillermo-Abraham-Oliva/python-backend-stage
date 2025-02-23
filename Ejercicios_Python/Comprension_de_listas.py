import os
os.system('clear' if os.name == 'posix' else 'cls')

lista_números = [7, 3, 1, 7, 5, 9, 7, 2, 8, 4]
nueva_lista = [num for num in lista_números if num != 7]
# Salida: [3, 1, 5, 9, 2, 8, 4]

#############################################################
numeros = [1, 2, 3, 4, 5]
cuadrados = [numero ** 2 for numero in numeros]
print(cuadrados)  # Salida: [1, 4, 9, 16, 25]

#############################################################
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = [numero for numero in numeros if numero % 2 == 0]
print(pares)  # Salida: [2, 4, 6, 8, 10]

numeros = range(1, 6)
clasificacion = ["Par" if numero % 2 == 0 else "Impar" for numero in numeros]

#############################################################
# range no se puede imprimir directamente ::: hay que usar list
Par = 0
Impar = 0
numeros = range(1, 5)
print(numeros)       # Salida: range(1, 6)   ¡NO DESEADO!
print(list(numeros)) # Salida: [1, 2, 3, 4]  ¡ OK !
clasificacion = ["Par" if numero % 2 == 0 else "Impar" for numero in numeros]
print(clasificacion)  # Salida: ['Impar', 'Par', 'Impar', 'Par', 'Impar']
for item in clasificacion:
    if item == 'Par':
        Par += 1
    else:
        Impar += 1
print(f'\n\tPares totales: {Par}')
print(f'\tImpares totales: {Impar}\n')











