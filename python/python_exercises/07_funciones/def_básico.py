import os
os.system('clear')

'''En una función puedo dejar un parámetro con un valor por defecto 
-como 'perro' en este caso- 
entonces cuando llamamos a la función en el script 
si NO aclaramos el tipo_animal, se asumirá que es un perro. 
El cambio si se asigna otro valor a tipo_animal 
obviamente tomará ese otro valor'''

def mascota(nombre_mascota, tipo_animal="perro"):  # valor por defecto -> "perro"
    print(f"Tengo un {tipo_animal}.")
    print(f"Mi {tipo_animal} se llama {nombre_mascota.title()}.\n")

mascota(nombre_mascota="pony")
mascota(nombre_mascota="roderic", tipo_animal="gato")

print(f'------------------------------------')


'''
Idéntico ejemplo con el rellenado de datos de una persona. 
Como parámetros obligatorios ponemos 'nombre' y 'apellido' 
pero ya dejamos como parámetros opcionales el segundo nombre y el segundo apellido 
entonces por las dudas que estos no existan 
debemos asignarle un valor por defecto vacío = ""

Se define una función llamada 'persona' con los parámetros obligatorios 'nombre' y 'apellido', 
y los parámetros opcionales 'segundo_nombre' y 'segundo_apellido'.

Esta función retorna un diccionario con 4 pares clave-valor, donde cada clave representa 
un dato personal y su respectivo valor se capitaliza utilizando el método .title().

En el script, la variable 'datos_persona' almacena el diccionario retornado tras llamar a la 
función 'persona' con los argumentos correspondientes.
'''

def persona(nombre, apellido, segundo_nombre="", segundo_apellido=""):
    """Retorna un diccionario con los datos personales formateados."""
    return {
        "nombre": nombre.title(),
        "segundo_nombre": segundo_nombre.title(),
        "apellido": apellido.title(),
        "segundo_apellido": segundo_apellido.title(),
    }

# Llamada a la función con argumentos
datos_persona = persona("juan", "gomez", segundo_apellido="perez")

# Imprimir el diccionario resultante
print(datos_persona)
