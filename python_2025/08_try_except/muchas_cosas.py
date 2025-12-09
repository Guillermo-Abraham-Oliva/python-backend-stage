'''Este programa gestiona un sistema de socios a través de una interfaz de línea de comandos. Permite visualizar la lista completa de socios, buscar un socio específico por su identificador, obtener su correo electrónico, agregar nuevos socios con validaciones, y leer información de un archivo externo. Además, maneja múltiples excepciones para garantizar un funcionamiento estable y proporciona una opción para salir del programa cuando el usuario lo desee.
Utiliza algunos de los princiales except: 
Exception, ValueError, TypeError, KeyError, IndexError, AttributeError, FileNotFoundError y PermissionError'''

import os  # Importamos el módulo 'os' para ejecutar comandos del sistema

# Limpiamos la pantalla dependiendo del sistema operativo
os.system('clear' if os.name == 'posix' else 'cls')  # 'clear' para Linux/macOS, 'cls' para Windows

# Lista de socios con estructura: [ID, Nombre, Edad, Coeficiente, Correo]
lista_socios = [  
    [0, 'Tomas', 25, 3.85, 'tomas@gmail.com'],
    [1, 'Anabel', 30, 4.12, 'anabel@yahoo.com'],
    [2, 'Maximo', 27, 3.67, 'maximo@outlook.com'],
    [3, 'Susana', 22, 4.45, 'susana@hotmail.com'],
    [4, 'Leandro', 35, 3.98, 'leandro@icloud.com'],
    [5, 'Eva', 28, 4.30, 'eva@aol.com'],
    [6, 'Roberto', 40, 3.75, 'roberto@proton.me'],
    [7, 'Miriam', 26, 4.20, 'miriam@zoho.com']
]

def imprimir_lista_socios():
    # Imprime la lista de socios en un formato tabulado
    print('\nListado de Socios:')
    print('=' * 50)  # Línea decorativa para separar
    print(f'{'ID':<5}{'Nombre':<10}{'Edad':<5}{'Coef.':<10}{'Correo':<20}')  # Encabezado con alineación
    print('-' * 50)  # Separador visual
    for socio in lista_socios:  # Iteramos sobre cada campo de c/u de los socios de la lista
        print(f'{socio[0]:<5}{socio[1]:<10}{socio[2]:<5}{socio[3]:<10}{socio[4]:<20}')  # Impresión formateada
    print('=' * 50)  # Línea decorativa final

def buscar_socio(id_socio):
    # Busca un socio por su ID y lo devuelve si existe
    try:
        if not isinstance(id_socio, int):  # Validamos que el ID sea un número entero
            raise TypeError('El ID del socio debe ser un número entero.')
        return next(socio for socio in lista_socios if socio[0] == id_socio)  # Busca el socio por ID
    except StopIteration:  # Si no encuentra el ID
        raise KeyError('El socio con el ID especificado no existe.')

def obtener_correo(id_socio):
    # Devuelve el correo electrónico de un socio según su ID
    try:
        socio = buscar_socio(id_socio)  # Llama a la función de búsqueda
        return socio[4]  # Retorna el correo del socio encontrado
    except KeyError as e:  # Manejo de error si el socio no existe
        print(f'Error: {e}')
        return None
    except IndexError:  # Manejo de error si la estructura de datos está mal
        print('Error: La estructura del socio no es válida.')
        return None

def agregar_socio():
    # Permite agregar un nuevo socio con validaciones
    try:
        nuevo_id = len(lista_socios)  # El ID será el tamaño actual de la lista
        nombre = input('Ingrese el nombre del nuevo socio: ')
        edad = int(input('Ingrese la edad del socio: '))  # Convertimos la entrada a entero
        calificacion = float(input('Ingrese coeficiente del socio: '))  # Convertimos a flotante
        correo = input('Ingrese el correo electrónico del socio: ')
        
        # Validación de tipos de datos
        if not isinstance(nombre, str) or not isinstance(edad, int) or not isinstance(calificacion, float) or not isinstance(correo, str):
            raise TypeError('Los datos ingresados no tienen el tipo correcto.')
        
        lista_socios.append([nuevo_id, nombre, edad, calificacion, correo])  # Agregamos el nuevo socio
        print(f'Socio {nombre} agregado correctamente.')
    except ValueError:  # Si hay error en la conversión de datos
        print('Error: Ingrese valores numéricos para edad y calificación.')
    except TypeError as e:
        print(f'Error de tipo: {e}')
    except Exception as e:
        print(f'Error inesperado: {e}')
    finally:
        print('Operación finalizada.')

def leer_archivo_socios(nombre_archivo):
    # Intenta leer un archivo con datos de socios
    try:
        with open(nombre_archivo, 'r') as archivo:  # Abre el archivo en modo lectura
            datos = archivo.readlines()  # Lee todas las líneas del archivo
            print('Contenido del archivo:')
            for linea in datos:
                print(linea.strip())  # Imprime cada línea eliminando espacios en blanco
    except FileNotFoundError:  # Si el archivo no existe
        print('Error: El archivo especificado no existe.')
    except PermissionError:  # Si no hay permisos de lectura
        print('Error: No tienes permisos para leer este archivo.')
    except Exception as e:  # Para cualquier otro error
        print(f'Error inesperado: {e}')
    finally:
        print('Intento de lectura finalizado.')

############### Menú interactivo ######################################################
while True:
    print('\nOpciones:')
    print('1. Imprimir listado de socios')
    print('2. Buscar socio por ID')
    print('3. Obtener correo de socio')
    print('4. Agregar nuevo socio')
    print('5. Leer archivo de socios')
    print('6. Salir')
    
    opcion = input('Seleccione una opción: ')  # Entrada de usuario
    
    if opcion == '1':  # Imprimir lista de socios
        imprimir_lista_socios()  # Ejecutar función
    elif opcion == '2':  # Buscar socio por ID
        try:
            id_socio = int(input('Ingrese el ID del socio: ')) # Conversión a entero
            print('Socio encontrado:', buscar_socio(id_socio)) # Ejecutar función
        except KeyError as e:
            print(f'Error: {e}')
        except ValueError:
            print('Error: Debe ingresar un número entero.')
    elif opcion == '3':  # Obtener correo del socio
        try:
            id_socio = int(input('Ingrese el ID del socio: '))
            correo = obtener_correo(id_socio) # Ejecutar función
            if correo:
                print('Correo del socio:', correo)
        except ValueError:
            print('Error: Debe ingresar un número entero.')
    elif opcion == '4':  # Agregar nuevo socio
        agregar_socio()  # Ejecutar función
    elif opcion == '5':  # Leer archivo de socios
        nombre_archivo = input('Ingrese el nombre del archivo: ')
        leer_archivo_socios(nombre_archivo) # Ejecutar función
    elif opcion == '6':  # Salir del programa
        print('Saliendo del programa...')
        break
    else:
        print('Opción no válida. Intente de nuevo.')