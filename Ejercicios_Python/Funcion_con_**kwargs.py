import os
os.system('clear')

"""Este script define una función `construir_perfil()` que crea un diccionario con la información de un usuario.

📌 Funcionamiento:
1. Recibe un nombre y un apellido como parámetros 'obligatorios'.
2. Puede recibir un número **variable** de pares 'clave-valor' adicionales
gracias a `**informacion_usuario`, los cuales se almacenan como un diccionario.
3. Crea un diccionario `perfil` donde almacena los datos.
4. Itera sobre los argumentos adicionales (`**informacion_usuario`)
y los añade al diccionario `perfil`.
5. Devuelve el diccionario con toda la información del usuario.

Este método es útil cuando se quiere almacenar información flexible sobre un usuario sin necesidad de definir un número fijo de parámetros."""

def construir_perfil(nombre, apellido, **informacion_usuario):
    """Construir un diccionario conteniendo todo lo que sabemos del usuario"""
    perfil = {}
    perfil["nombre"] = nombre
    perfil["apellido"] = apellido
    
    for clave, valor in informacion_usuario.items():
        perfil[clave] = valor
    
    return perfil

perfil_usuario = construir_perfil("alberto", "lopez",
                                  ubicacion="Madrid",
                                  trabajo="programador")

print(perfil_usuario)
# Salida:
# {'nombre': 'alberto', 'apellido': 'lopez', 'ubicacion': 'Madrid', 'trabajo': 'programador'}
