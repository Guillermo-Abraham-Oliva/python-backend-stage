import os
os.system('clear' if os.name=='posix' else 'cls')

# Lista 1 con 10 elementos
lista_1 = ['manzana', 'pera', 'uva', 'naranja', 'mango', 'cereza', 'banana', 'sandía', 'kiwi', 'limón']

# Lista 2 con 10 elementos, incluyendo 3 elementos coincidentes con lista_1
lista_2 = ['mango', 'naranja', 'kiwi', 'piña', 'melón', 'fresa', 'papaya', 'granada', 'durazno', 'ciruela']

print(f'\n\tLista 1: {lista_1}')
print(f'\tLista 2: {lista_2}')

##################################
# inicializaciones
coincidencias = []

# compilamos una lista de productos coincidentes
for item in lista_1:
    if item in lista_2:
        coincidencias.append(item)
print(f'\n\tFrutas coincidentes: {coincidencias}')

###################################
# inicializaciones
union = lista_1[:]   # OJO: si no colocamos al final [:] LINKEA LAS LISTAS y desastre!

# unimos las listas, y ordenamos.
for item in lista_1:
    if not item in lista_2:
        union.append(item)

print(f'\nFusión de las listas (ordenada y sin repeticiones):\n {set(sorted(union))}\n\n')

