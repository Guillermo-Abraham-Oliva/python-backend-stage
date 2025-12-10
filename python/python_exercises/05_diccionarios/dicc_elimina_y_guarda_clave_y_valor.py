import os
os.system('clear' if os.name == 'posix' else 'cls')

####################################################################
### Script para guardar tanto la clave como el valor con pop() en dict ###
####################################################################

dicc = {'manzana': 1, 'platano': 4, 'pera': 9}
print(f'\nDiccionario original: {dicc}\n')

# En diccs, pop SOLO puede devolver el 'valor', entonces guardamos previamente la 'clave'
clave_a_eliminar = 'manzana'
valor_a_eliminar = dicc.pop(clave_a_eliminar)  # pop devuelve SOLO el valor
pares_eliminados = (clave_a_eliminar, valor_a_eliminar)# Guardamos clave y valor en una tupla

print(f'\nPares eliminados: {pares_eliminados}')  # ('manzana', 1)
print(f'\nDiccionario modificado: {dicc}\n\n')