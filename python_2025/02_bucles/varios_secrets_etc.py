import os
os.system('clear')

#----------------------------------------------------------------------------------------------
#-------Script 1: Validaciones básicas y manipulación de strings ---------------------------
# Objetivo: Aprender a trabajar con strings y validaciones simples en Python.  
# Relevancia futura: 10%
# Uso de in y isdigit() sigue siendo útil para validaciones básicas.
# Construcción de condiciones (if) es esencial en cualquier lenguaje de programación.

def validar_datos(nombre, telefono):
    """ Verifica si los datos cumplen ciertas condiciones """
    if "@" in nombre:
        print(f"El nombre solo puede contener letras.")
    else:
        print(f"Nombre válido.")

    if not telefono.isdigit():
        print(f"El teléfono solo puede contener números.")
    else:
        print(f"Teléfono válido.")
    print(f"---------")

# Prueba
validar_datos("Juan@", "12345")  # Nombre inválido
validar_datos("Pedro", "ab123")  # Teléfono inválido

#----------------------------------------------------------------------------------------------
#-------Script 2: Generación aleatoria y seguridad de datos -------------------------------- 
# Relevancia futura en backend profesional: 80%
# secrets.token_hex() es criptográficamente seguro y se usa en backend, principalmente para:
# - Generar tokens temporales de seguridad (ej. enlaces de restablecimiento de contraseña).
# - Crear claves API o identificadores únicos.
# - Proteger datos sensibles en aplicaciones web.
# Pero NO reemplaza a JWT ni OAuth2 para autenticación
# Para autenticación segura, usarás JWT (JSON Web Tokens) en FastAPI, que es el estándar actual para manejar sesiones y permisos en backend.
# Conclusión: Sí vale la pena aprenderlo, pero más importante aún es aprender JWT y OAuth2 para autenticación en backend real.

import secrets

# Generar un token seguro con secrets (para seguridad real)
def token_seguro(longitud=16):
    return secrets.token_hex(longitud)

print("Token seguro:", token_seguro())

#----------------------------------------------------------------------------------------------
#-------Script 3: Modularización y uso de funciones en múltiples archivos ------------------
# Objetivo: Aprender a importar módulos y manejar funciones en archivos separados.  
# Conceptos incluidos:
# ✔ Cómo importar módulos en Python (`import validador, import generador`).  
# ✔ Modularización de código (`def function():` en un archivo y llamarlo desde otro).  
# ✔ Manejo de funciones (`def nombre_funcion(): ...`).  
# Relevancia futura: 90%
# ✔ Importar módulos y estructurar código es fundamental en backend.
# ✔ Separar funciones en archivos distintos es clave en el diseño de microservicios y APIs.
# Advertencia: En backend real, no usarás scripts sueltos, sino que estructurarás aplicaciones en FastAPI o Django.

#### **Estructura de archivos**
# /proyecto_modular/
# │── main.py  (Archivo principal)
# │── operaciones.py  (Funciones auxiliares)


# **Contenido de `operaciones.py`:**

# def sumar(a, b):
#     return a + b

# def restar(a, b):
#     return a - b

# **Contenido de `main.py`:**

import operaciones  # Importamos el módulo creado

print(f"\n --- Suma: {operaciones.sumar(5, 3)}")
print(f" --- Resta: {operaciones.restar(10, 4)}\n")


#----------------------------------------------------------------------------------------------
#-------Script 4: Listas y diccionarios para almacenar y manejar datos ---------------------
# Objetivo: Aprender a manejar listas y diccionarios, simular bases de datos pequeñas.  
# Relevancia futura: 10%
# Listas y diccionarios siguen siendo útiles para manejar estructuras de datos temporales en memoria.

ventas = []    # es una lista y tendra dentro tantos diccios como ventas se realicen -> agregar_venta()

def agregar_venta(producto, precio):
    venta = {"producto": producto, "precio": precio}
    ventas.append(venta)

def mostrar_ventas():
    for venta in ventas:
        print(f"Producto: {venta['producto']}, Precio: {venta['precio']}")
    print(f"---")

# Pruebas
agregar_venta("Camisa", 25.99)
agregar_venta("Pantalón", 39.95)
mostrar_ventas()


#----------------------------------------------------------------------------------------------
#-------🔹 Script 5: Condiciones avanzadas y lógica de negocio --------------------------------
# Objetivo: Aplicar `if` con múltiples criterios y mejorar la lógica de negocio en Python.  
# Relevancia futura: 80%
# Uso de if y lógica de negocio es esencial en cualquier backend.
# Estructurar decisiones en base a datos es clave en cualquier API.

def evaluar_descuento(cliente_vip, total_compra):
    """ Aplica descuentos según la condición del cliente """
    if cliente_vip and total_compra > 100:
        return "Descuento del 20%"
    elif total_compra > 50:
        return "Descuento del 10%"
    else:
        return "Sin descuento"

# Pruebas
print(evaluar_descuento(True, 120))  # 20%
print(evaluar_descuento(False, 60))  # 10%
print(evaluar_descuento(False, 30))  # Sin descuento
