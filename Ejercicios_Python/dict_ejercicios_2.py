import os
os.system('clear' if os.name == 'posix' else 'cls')

'''Listas de diccionarios (Uso en backend: 40%)
🔹 Uso futuro en backend: 40%
Las listas de diccionarios no se usan directamente en backend, ya que los datos se almacenan en bases de datos y se gestionan con ORM.
⚠️ Advertencia: En backend, los datos estructurados se guardan en bases de datos (SQL o NoSQL), no en listas de diccionarios.
✅ Solo aprende lo justo: Cómo acceder, recorrer y modificar listas de diccionarios.'''

# Lista de diccionarios de estudiantes
estudiantes = [{"nombre": "Carlos", "edad": 22}, {"nombre": "Laura", "edad": 24}]

# Recorriendo la lista
for estudiante in estudiantes:
    print(f"{estudiante['nombre']} - {estudiante['edad']} años")

# Agregando un nuevo estudiante
estudiantes.append({"nombre": "Mariana", "edad": 21}) # esta agregando un diccio a la lista

# Eliminando un estudiante
del estudiantes[1]

# Actualizando edad del primer estudiante
estudiantes[0]["edad"] = 23