import os
os.system('clear' if os.name == 'posix' else 'cls')

lista_usuarios = ['Alice', 'Bob', 'Charlie'] # <--- LISTA !!!
nuevo_usuario = input(f'\nIntroduce tu nombre para registrarte: ').strip().title()

if nuevo_usuario == '':
    print('Error: El nombre no puede estar vacío. Inténtalo de nuevo.')
elif nuevo_usuario in lista_usuarios:
    print(f'El usuario \'{nuevo_usuario}\' ya está registrado.')
else:
    lista_usuarios.append(nuevo_usuario)
    print(f'¡Registro exitoso! Bienvenido, {nuevo_usuario}.')

print('\nUsuarios registrados actualmente:')
for usuario in lista_usuarios:
    print(f'- {usuario}')

buscar = input('\n¿Quieres buscar un usuario registrado? (y/n): ').strip().lower()

if buscar == 'y':

    usuario_a_buscar = input('Introduce el nombre del usuario que deseas buscar: ').strip().title()
    
    if usuario_a_buscar in lista_usuarios:
        print(f'ya está registrado!')
    else:
        print(f'El usuario \'{usuario_a_buscar}\' no está registrado.')
        
elif buscar == 'n':
    print('Gracias por usar nuestro sistema. ¡Hasta luego!')
else:
    print('Respuesta no válida. El programa se cerrará.')
 