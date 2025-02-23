"""
Este programa permite al usuario eliminar todas las ocurrencias de una letra específica 
de una lista predefinida de letras. La lista conserva sus modificaciones a lo largo 
de la ejecución del programa, permitiendo que el usuario continúe trabajando con la 
lista actualizada en cada iteración. Utiliza validaciones robustas y manejo de excepciones 
para prevenir errores y permite al usuario decidir si quiere seguir interactuando.
"""

import os
os.system('clear' if os.name == 'posix' else 'cls')

# Inicializar la lista una vez al inicio
lista = ['a', 'b', 'c', 'd', 'a', 'b', 'c', 'd', 'a', 'b', 'c', 'd']

# Función principal para eliminar letras de la lista
def borrar_letras():
    global lista  # Permitir acceso a la lista global
    print(f'\n\tLista actual: {" | ".join(lista)}\n')  # Muestra la lista actual

    while True:  # Bucle para validar la entrada del usuario
        
        try:
            # Solicitar al usuario la letra a borrar
            letra_a_borrar = input('\tLetra a borrar?: ').lower().strip()
            # Validar que la entrada sea exactamente 1 letra alfabética
            if len(letra_a_borrar) != 1 or not letra_a_borrar.isalpha():
                # Genera un error si la entrada no es válida
                raise ValueError('\t\tDebes ingresar una sola letra válida.')  
        
        except ValueError as e:
            print(e, '\n')  # Muestra el error y permite volver a intentar
        
        else:
            # Siendo la entrada válida: verificar y eliminar la letra de la lista
            if letra_a_borrar in lista:
                # Crear una nueva lista excluyendo las ocurrencias de la letra
                lista = [letra for letra in lista if letra != letra_a_borrar]
                print(f'\n\t--- Lista actualizada: {" | ".join(lista)}\n')
            else:
                # Informar si la letra no se encuentra en la lista
                print(f'\t\tLa letra \'{letra_a_borrar}\' no está en la lista.\n')
            break  # Salir del bucle si todo se realizó correctamente

# Bucle principal para repetir el programa
while True:
    borrar_letras()  # Ejecutar la función principal
    
    while True:  # Repetir hasta obtener una respuesta válida
        try:  # luego busca siempre un bloque except (o finally)
            continuar = input('¿Deseas borrar más letras? (s/n): ').lower().strip()
            if continuar not in ('s', 'n'): # Validar que la respuesta sea 's' o 'n'
                # raise dice 'guardar el error y el texto en ValueError'
                raise ValueError('\t\tPor favor, responde con "s" o "n".')
        # except asigna ValueError al objeto 'e' (puede ser cualquier cosa)
        except ValueError as e:
            print(e, '\n')  # Mostrar el msj de error y volver a pedir la entrada
        else:      # si lo anterior no es asi, entonces la respuesta es válida,
            break  # y hay que salir de éste bucle de validación
                
    # Verificar si el usuario quiere salir del programa
    if continuar == 'n':  # Si elige no continuar, salir del programa
        print('\n\t¡Hasta luego!\n')
        break  # Termina el bucle principal


'''
Cuando el programa comienza a ejecutarse:
def (definir función):
    Todo lo que está dentro de def "borrar_letras()" no se ejecuta inmediatamente.
    Solo se "guarda" la función en memoria para usarla más adelante.
Bucle principal while True: 
    El programa empieza aquí, fuera de la función. 
    Este bucle llama a la función "borrar_letras()"
Ejecución de la función: Cuando se llama a borrar_letras(), 
    el código dentro de la función se ejecuta, pero solo en ese momento.
    Esto permite que la función se ejecute cada vez
    que la llames desde el bucle.
    Así, el flujo del programa es controlado y modular.

'''
