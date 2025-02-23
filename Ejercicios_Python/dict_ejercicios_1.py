import os
os.system('clear' if os.name == 'posix' else 'cls')

'''Diccionarios básicos (Uso en backend: 50%)
🔹 Uso futuro en backend: 50%
Los diccionarios son esenciales en Python, pero en backend los datos se manejan con bases de datos (SQL, NoSQL) y ORM. Se usará en casos puntuales para estructuras temporales.
⚠️ Advertencia: En backend, los diccionarios se reemplazan con bases de datos SQL/NoSQL y ORM.
✅ Solo aprende lo justo: Sintaxis básica y manipulación de datos en memoria.'''

# Creación de un diccionario vacío
mi_diccionario = {}

# Agregando clave-valor
mi_diccionario["nombre"] = "Guillermo"

# Accediendo a un valor
print(mi_diccionario["nombre"])

# Verificando si una clave existe
print("edad" in mi_diccionario) # como no existe la clave "edad", devolverá 'false'

###### Creando un diccionario ######
estudiante = {"nombre": "Juan", "edad": 25, "materia": "Matemáticas"}

# Actualizando un valor
estudiante["edad"] = 26

# Eliminando una clave
del estudiante["materia"]

# Imprimiendo todas las claves
print(estudiante.keys())

###### Creando otro diccionario ######
agenda = {"Juan": "1234567890", "Joana": "9876543210", "Jimena": "5555555555"}

# Agregando una entrada
agenda["Julio"] = "9998887777"

# Número de entradas
print(len(agenda))

# Creando lista de claves
claves = list(agenda.keys())

# Verificando existencia de clave
print("Juan" in agenda) # como sí existe la clave "Juan", devolverá 'true'

# Eliminando una entrada
del agenda["Jimena"]

# Recorriendo diccionario con un bucle
for nombre, numero in agenda.items():
    print(f"{nombre}: {numero}")

# Usando .get() con manejo de excepciones
print(agenda.get("Peter", "Clave no encontrada"))
# como no existe la clave "Peter", devolverá el msj: Clave no encontrada

# Borrando todas las entradas
agenda.clear()