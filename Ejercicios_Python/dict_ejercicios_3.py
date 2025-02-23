import os
os.system('clear' if os.name == 'posix' else 'cls')

'''Diccionarios anidados (Uso en backend: 30%)
🔹 Uso futuro en backend: 30%
En backend, los datos anidados se manejan con bases de datos NoSQL (MongoDB) o JSON.
⚠️ Advertencia: Los diccionarios anidados son reemplazados por bases de datos NoSQL como MongoDB o JSON serializado.
✅ Solo aprende lo justo: Cómo acceder y recorrer datos en estructuras anidadas.'''

# Diccionario con productos
productos = {
    "001": {"nombre": "Laptop", "precio": 1200},
    "002": {"nombre": "Mouse", "precio": 25}
}

# Recorriendo el diccionario
for clave, producto in productos.items():
    print(f"{producto['nombre']} - ${producto['precio']}")

# Agregando un nuevo producto
productos["003"] = {"nombre": "Teclado", "precio": 45}
print(productos)