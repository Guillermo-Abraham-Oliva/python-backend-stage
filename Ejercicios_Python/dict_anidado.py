import os
os.system('clear' if os.name == 'posix' else 'cls')

#######################################################
############# ANIDAMIENTO DE DICCIONARIOS #############
#######################################################

# Diccionario que almacena información de usuarios de una página web
users = {
    'lvene': {                 # Clave: nombre de usuario
        'nombre': 'lucas',     # Subclave: nombre real del usuario
        'apellido': 'vene',    # Subclave: apellido del usuario
        'ubicacion': 'paris',  # Subclave: ubicación del usuario
    },
    'crodriguez': {
        'nombre': 'carlos',
        'apellido': 'rodriguez',
        'ubicacion': 'madrid',
    },
    'tbauer': {
        'nombre': 'thomas',
        'apellido': 'bauer',
        'ubicacion': 'berlin',
    }
}

# Recorremos el diccionario users con un bucle for
for nombre_usuario, info_personal in users.items():
    print(f'\nNombre de usuario: {nombre_usuario}')  # Imprimimos el nombre de usuario (clave principal)

    # Extraemos el nombre y apellido del diccionario anidado y los concatenamos
    fullname = info_personal['nombre'] + " " + info_personal['apellido']

    # Extraemos la ubicación del usuario
    localizacion = info_personal['ubicacion']

    # Mostramos el nombre completo y la ubicación con formato adecuado
    print(f'   Nombre completo: {fullname.title()}')
    print(f'   Localización: {localizacion.title()}')


"""
EXPLICACIÓN:

1) Definimos un diccionario llamado 'users', donde cada clave representa un nombre de usuario.
2) Cada nombre de usuario almacena otro diccionario con tres claves:
   - 'nombre' (nombre real del usuario)
   - 'apellido' (apellido real del usuario)
   - 'ubicacion' (ciudad en la que vive el usuario)

3) Usamos un bucle for para recorrer el diccionario 'users'. 
   - 'nombre_usuario' toma el valor de cada clave principal (nombre de usuario).
   - 'info_personal' toma el valor del diccionario anidado que contiene los datos personales.

4) Dentro del bucle:
   - Se imprime el nombre de usuario.
   - Se extraen y concatenan el nombre y apellido en una variable 'fullname'.
   - Se extrae la ubicación en la variable 'localizacion'.
   - Se imprimen el nombre completo y la ubicación, aplicando el método .title() para formatear correctamente.

"""