import os
os.system('clear' if os.name == 'posix' else 'cls')

# Lista principal con 8 sublistas de 5 elementos
list1 = [  
    [0, 'Juan', 25, 3.85, 'juan@gmail.com'],
    [1, 'Ana', 30, 4.12, 'ana@yahoo.com'],
    [2, 'Luis', 27, 3.67, 'luis@outlook.com'],
    [3, 'Sofia', 22, 4.45, 'sofia@hotmail.com'],
    [4, 'Leo', 35, 3.98, 'leo@icloud.com'],
    [5, 'Emma', 28, 4.30, 'emma@aol.com'],
    [6, 'Raúl', 40, 3.75, 'raul@proton.me'],
    [7, 'Mia', 26, 4.20, 'mia@zoho.com']
]

print(list1[0], type(list1[0]))  # Imprime la 1º sublista y su tipo (list)
print(list1[3], type(list1[3]))  # Imprime la 4º sublista y su tipo (list)

print('\n1º sublista campo por campo y su clase:')
print(list1[0][0], type(list1[0][0]))  # Imprime el 1º elemento de la 1º sublista y su tipo (int)
print(list1[0][1], type(list1[0][1]))  # Imprime el 2º elemento de la 1º sublista y su tipo (str)
print(list1[0][2], type(list1[0][2]))  # Imprime el 3º elemento de la 1º sublista y su tipo (int)
print(list1[0][3], type(list1[0][3]))  # Imprime el 4º elemento de la 1º sublista y su tipo (float)
print(list1[0][4], type(list1[0][4]))  # Imprime el 5º elemento de la 1º sublista y su tipo (str)

print('---')

print(list1[4][2], type(list1[4][2]))  # Imprime el 3º elemento de la 5º sublista (35) y su tipo (int)
print(list1[7][4], type(list1[7][4]))  # Imprime el 5º elemento de la 8º sublista ('mia@zoho.com') y su tipo (str)
print(list1[5][3], type(list1[5][3]))  # Imprime el 4º elemento de la 6º sublista (4.30) y su tipo (float)

print('------------')

print(list1[3:4])  # Es una mala praxis! imprime la 3º sublista (equivale a print(list1[3])
print(list1[3:6])  # Imprime las sublistas 3º, 4º y 5º
print(list1[5:])   # Imprime todas las sublistas desde la 5º en adelante

print('---------------------------')

# Imprimir las sublistas (completas) correspondientes a Mia, Leo, Raúl y Ana (en este orden):
print([list1[i] for i in [7, 4, 6, 1]])

# Imprimir el elemento 1 (nombre) de las sublistas correspondientes a Mia, Leo, Raúl y Ana (en este orden):
print([list1[i][1] for i in [7, 4, 6, 1]])  # ['Mia', 'Leo', 'Raúl', 'Ana']

print('---------------------------')

print(list1[7:2:-1])  # Extraerá elementos en orden inverso: 7, 6, 5, 4, 3
