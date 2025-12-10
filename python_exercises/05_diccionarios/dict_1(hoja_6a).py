import os
os.system('clear' if os.name == 'posix' else 'cls')

'''Diccionarios básicos (Uso en backend: 50%)
🔹 Uso futuro en backend: 50%
Los diccionarios son esenciales en Python, pero en backend los datos se manejan con bases de datos (SQL, NoSQL) y ORM. Se usará en casos puntuales para estructuras temporales.
⚠️ Advertencia: En backend, los diccionarios se reemplazan con bases de datos SQL/NoSQL y ORM.
✅ Solo aprende lo justo: Sintaxis básica y manipulación de datos en memoria.

🔹 Se crean con LLAVES pero se gestionan con CORCHETES !!! '''


# Creación de un diccionario vacío
mi_diccionario = {}  # ✅ 90%

# Agregando clave-valor
mi_diccionario["nombre"] = "Guillermo"  # ✅ 90%

# Accediendo/imprimiendo a un valor
print(mi_diccionario["nombre"])  # Salida: Guillermo  # ✅ 90%

# Verificando si una clave existe
print("edad" in mi_diccionario)  # Salida: False  (porque no existe la clave "edad")  # ✅ 90%

###### Creando un diccionario llamado 'estudiante' ######
estudiante = {"nombre": "Juan", "edad": 25, "materia": "Matemáticas"}  # ✅ 90%

# Actualizando un valor
estudiante["edad"] = 26  # ✅ 90%

# Eliminando la clave "materia" con del (si no existe, dará error!)
del estudiante["materia"]  # en este caso, existe, así que todo ok...  # ✅ 90%

# Intentando eliminarla nuevamente con pop
# el sentido de pop es USAR SIEMPRE un msj personalizado de error!!!!
# de esta forma no hay error! sino solo un msj !!!
print(estudiante.pop("trabajo", "No existe esa clave"))  # Salida: No existe esa clave  # ✅ 85%
# .pop(clave) sin valor por defecto → ❌ Dará error (KeyError) si la clave no existe.
# .pop(clave, valor_por_defecto) → ✅ Nunca da error, simplemente devuelve mensaje si la clave no está
# PERO ---> devuelve mensaje -SOLO- al imprimir o almacenar !
# Si no almacenas ni imprimes el resultado de .pop(), no sucede nada visible.

# Imprimiendo todas las claves
print(estudiante.keys())  # ✅ 85%

###### Creando un diccionario llamado 'agenda' ######
agenda = {"Juan": "1234567890", "Joana": "9876543210", "Jimena": "5555555555"}  # ✅ 80%

# Agregando una entrada
agenda["Julio"] = "9998887777"  # ✅ 80%

# Número de entradas
print(len(agenda))  # ✅ 80%

# Creando lista de claves y Lusta de valores
lista_claves = list(agenda.keys())     # ✅ 80%  🔹🔹🔹 ME CUESTA !!!!!!!!!!!
lista_valores = list(agenda.values())  # ✅ 80%  🔹🔹🔹 ME CUESTA !!!!!!!!!!!

# Verificando existencia de clave
print("Juan" in agenda)  # como sí existe la clave "Juan", devolverá 'True'  # ✅ 80%

# Eliminando una entrada
del agenda["Jimena"]  # ✅ 80%
print(agenda.pop("Pepe", "No existe esa clave")) # Salida: No existe esa clave # ✅ 80%

# Recorriendo diccionario con un bucle
for nombre, numero in agenda.items():  # ✅ 85%
    print(f"{nombre}: {numero}")       # ✅ 85%

# Usando .get() con manejo de excepciones
print(agenda.get("Peter", "Clave no encontrada"))  # ✅ 90%
# como no existe la clave "Peter", devolverá el msj: Clave no encontrada

# Borrando todas las entradas
agenda.clear()  # ❌ 40%