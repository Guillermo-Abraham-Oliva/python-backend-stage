import os
os.system('clear')

'''Diccionarios anidados (Uso en backend: 30%)
🔹 Uso futuro en backend: 30%
En backend, los datos anidados se manejan con bases de datos NoSQL (MongoDB) o JSON.
⚠️ Advertencia: Los diccionarios anidados son reemplazados por bases de datos NoSQL como MongoDB o JSON serializado.
✅ Solo aprende lo justo: Cómo acceder y recorrer datos en estructuras anidadas.'''

# Diccionarios anidados! OJO!   # ✅ 80%
diccionario_productos = {
    "001": {"nombre": "Laptop", "precio": 1200},
    "002": {"nombre": "Mouse", "precio": 25},
} 

# Recorriendo el Diccionario original
for clave, diccioAnidadoComoValor in diccionario_productos.items():                             # ✅ 80%
    print(f"{clave}_{diccioAnidadoComoValor['nombre']} - {diccioAnidadoComoValor['precio']}€")  # ✅ 80%

print() # espaciado

# Agregando un nuevo producto
diccionario_productos["003"] = {"nombre": "Teclado", "precio": 45}  # ✅ 80%

# Recorriendo el Diccionario original
for clave, diccioAnidadoComoValor in diccionario_productos.items():                             # ✅ 80%
    print(f"{clave}_{diccioAnidadoComoValor['nombre']} - {diccioAnidadoComoValor['precio']}€")  # ✅ 80%

