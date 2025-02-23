import os
os.system('clear' if os.name == 'posix' else 'cls')

lista_ultimos = []
lista_mensajes = []
lista_numeros = [1, 2, 3, 4]
lista_eliminados = []
eliminados = [1, 2, 3, 4]
i = 0

pila = [10, 20, 30, 40]
print(f'\nLista original: {pila}')

lista_ultimos.append(pila.pop())  # Elimina y agrega el último elemento (40)


lista_mensajes.append(f'Resultado: {str(abs(round(lista_numeros.pop() ** 2) + 100)).zfill(5)}')

lista_eliminados.append(f'Eliminado Nº {i + 1}: {str(round(eliminados.pop() ** 2) + 100).zfill(8).replace('0', '*')}')

lista_mensajes.append(f'Resultado: {str(round(lista_numeros.pop() ** 2) + 100).zfill(5).replace("0", "*").rjust(10)}'.upper().strip())
