import os
os.system('clear' if os.name == 'posix' else 'cls')

'''Listas de diccionarios (Uso en backend: 40%)
🔹 Uso futuro en backend: 40%
Las listas de diccionarios no se usan directamente en backend, ya que los datos se almacenan en bases de datos y se gestionan con ORM.
⚠️ Advertencia: En backend, los datos estructurados se guardan en bases de datos (SQL o NoSQL), no en listas de diccionarios.
✅ Solo aprende lo justo: Cómo acceder, recorrer y modificar listas de diccionarios.'''

# LISTA de diccionarios de estudiantes
lista_estudiantes = [{"nombre": "Carlos", "edad": 22}, {"nombre": "Laura", "edad": 24}]  # ✅ 85%

# Recorriendo la lista
for estudiante in lista_estudiantes:                              # ✅ 85%
    print(f"{estudiante['nombre']} - {estudiante['edad']} años")  # ✅ 85%

# Agregando un nuevo estudiante
lista_estudiantes.append({"nombre": "Mariana", "edad": 21})  # esta agregando un diccio a la lista  # ✅ 80%

# Eliminando un estudiante
del lista_estudiantes[1]  # Elimina "Laura"  ✅ 80%

# Actualizando edad del primer estudiante
lista_estudiantes[0]["edad"] = 23  # es con '[][]' porque es una Lista  ✅ 85%

print(lista_estudiantes)