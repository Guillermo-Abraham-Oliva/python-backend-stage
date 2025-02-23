import os
os.system('clear' if os.name == 'posix' else 'cls')


# Diccionario con información de un usuario en una página web
user_0 = {
    'username': 'ef3rmi',
    'nombre': 'Enrique',
    'apellido': 'Gomez'
}

# imprime todo el diccio pero con una presentacion mediocre: una LISTA DE TUPLAS:
print(user_0.items())
print()

# Recorriendo el diccionario e imprimiendo clave y valor
for a, b in user_0.items():  # a, b representan la "clave y el valor"
    print(f'\tClave: {a}')
    print(f'\tValor: {b}')
    print(f'\t----------------')

### esto es muy usado: 80% (aunque será sobre bases de datos no en python)

for a, b in user_0.items():  # presentacion en 1 renglón con aclaratoria
    print(f'\tClave: {a}   Valor: {b}')
print(f'\t----------------')

for a, b in user_0.items():  # presentacion mas resumida
    print(f'\t{a}: {b}')
print(f'\t----------------')
