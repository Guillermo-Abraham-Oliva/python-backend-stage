import os
os.system('clear' if os.name == 'posix' else 'cls')

###################################################################
# ✅Solo puedes acceder a 'claves' (dicc["clave"]). 
# ❌No puedes acceder directamente a un 'value' en un diccio
# Los diccionarios en Python están diseñados para buscar valores a través de claves, no al revés.
################################################################
### Métodos de diccios: items, keys, values, get, pop, clear ###
################################################################
### todo esto es muy utilizado, excepto lo marcado #############
################################################################

dicc = {'manzana': 1, 'platano': 4, 'pera': 9}
print(f'\nDiccionario original: {dicc}\n')

print(dicc.items())  # imprime todos los pares clave/valor
print(dicc.keys())   # imprime todas las claves
print(dicc.values()) # imprime todos los valores

### NO recomendado llamar directamente porque si no existe, ¡da error! :  ###################
print(dicc['pera']) # imprime el valor de la clave 'pera' / Salida: 9 / pero puede dar error!
#############################################################################################

### en su lugar, es mucho mas seguro y recomendado usar get()
# get() se usa para pedir el valor de una clave:
print(dicc.get('platano'))  # Salida: 4

# get() es bueno para gestionar las inexistencias y el error
print(dicc.get('uva'))   # si no hay 'uva' dará 'None' por defecto

# si no queremos 'None' podemos elegir que retornar:
print(dicc.get('uva',0)) # si no hay 'uva' dará un cero que puede usarse en un if (por ej)...
print(dicc.get('uva','Esa clave no existe')) # dar un mensaje si no existe la clave


eliminados = (dicc.pop('pera'))  # elimina la 'clave' 'pera' pero la guarda en eliminados
print(f'eliminados: {eliminados}')
print(f'nueva lista: {dicc}')

dicc.clear() # se borra todo el contenido del diccio

# Un detalle que puede resultar confuso:
# En los diccionarios de Python se usan corchetes []
# para acceder, modificar, agregar y eliminar elementos...
# PERO en los métodos como `.get()`  por ejemplo usa paréntesis ()
# Esto es porque son dos formas diferentes de interactuar con el diccionario.

### 🔹 **Uso de corchetes `[]`**
# Los corchetes se utilizan para acceder directamente a los valores de un diccionario,
# pero tienen un problema: 
# ---> si la clave no existe, genera un error `KeyError` !!!

mi_diccionario = {'manzana': 1, 'plátano': 2, 'naranja': 3}

print(mi_diccionario['manzana'])  # ✅ Imprime 1
print(mi_diccionario['pera'])  # ❌ Genera un KeyError porque 'pera' no existe

### 🔹 **Uso del método `.get()`**
# El método `.get()` es más seguro porque **evita errores si la clave no existe**
# devolviendo `None` o un valor que especifiquemos.

mi_diccionario = {'manzana': 1, 'plátano': 2, 'naranja': 3}

print(mi_diccionario.get('manzana'))  # ✅ Imprime 1
print(mi_diccionario.get('pera'))  # ✅ No genera error, imprime None
print(mi_diccionario.get('pera', 'No disponible'))  # ✅ Imprime "No disponible"

# ➡ 🔹Regla rápida🔹
#  Corchetes `[]`  = Acceso directo, pero puede generar error si la clave no existe.
#  .get() con `()` = Más seguro, evita errores y devuelve valor establecido.

# En backend profesional `.get()` es más recomendable cuando no estás seguro si la clave existe.


###############################################################################
# Definimos un diccionario inicial con algunas frutas y sus valores asociados #
mi_diccionario = {'manzana': 1, 'plátano': 2, 'naranja': 3}

# PARA TODO TIPO DE GESTIÓN EN DICCIOS USAREMOS CORCHETES []
# Acceder al valor de 'manzana'
print(mi_diccionario['manzana'])

# Agregar un nuevo par clave-valor al diccionario
mi_diccionario['pera'] = 4  # Agrega el par clave-valor ---> 'pera': 4

# Modificar un valor existente en el diccionario
mi_diccionario['manzana'] = 4  # Modifica el valor de la clave 'manzana'

# Eliminar un par clave-valor del diccionario
del mi_diccionario['plátano']  # Elimina 'platano'
