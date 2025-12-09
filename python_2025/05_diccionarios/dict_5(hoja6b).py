import os
os.system('clear')

import sys # para interrumpir eventualmente el flujo con ---> sys.exit()

################################
###### REGISTRO DE VENTAS ######
################################

'''Tienes una tienda y deseas realizar un seguimiento de las ventas diarias
de tus productos. Cada producto tiene un nombre y una cantidad
vendida. Implementa un programa en Python que utilice un diccionario
para almacenar la información de las ventas. El programa debe permitir
registrar las ventas de productos, actualizar la cantidad vendida de un
producto existente y calcular el total de ventas diarias.
(Pista: puedes comenzar con un diccionario vacío e ir añadiendo cada
producto)'''

# Diccionario de ventas (Uso futuro en backend: 90%)
ventas = {} # otra opcion de inicializar un diccio ---> ventas = dict()

# Registrar las ventas (Uso futuro: 90%)
ventas["Producto1"] = 10
ventas["Producto2"] = 5
ventas["Producto3"] = 3

# Actualizar cantidad vendida de un producto existente (Uso futuro: 95%)
ventas["Producto2"] += 2  # Es más eficiente y profesional

# Imprimir el registro de ventas (Uso futuro: 60%)
print("Registro de ventas:\n")
for producto, cantidad in ventas.items():
    print(f"{producto}: {cantidad}")

# Calcular el total de ventas diarias (Uso futuro: 100%)
total_ventas = sum(ventas.values())     # 😲MEMORIZAR😲
print(f"\nTotal de ventas diarias: {total_ventas}\n")

'''
✅ Esta técnica es MUY ÚTIL en backend para recorrer diccionarios con datos clave-valor.
✅ La usarás bastante en procesamiento de datos, APIs y reportes.
⚠️ En backend real, si los datos vienen de una base de datos o API, recorrerás JSON o usarás SQL directamente.
'''

###############################################################################################
###############################################################################################
'''VERSION COMPLICADA pero ojo ---> NO SIRVE!!! :
Análisis de uso futuro en backend:
🔹 Estructuras de control (while, if, elif, else) → 10%
🔹 Manejo de diccionarios (ventas_diarias[producto] = cantidad) → 15%
🔹 Manejo de listas y diccionarios (for cantidad in ventas_diarias.values()) → 10%
🔹 Entrada de usuario con input() → ⚠️ (5% o menos en backend profesional, reemplazado por API y bases de datos)
🔹 Salida de datos con print() → ⚠️ (0% en backend profesional, reemplazado por logs y respuestas de API)
🔹 Manejo de variables (total = 0, continuar = True) → 5%
🔹 Operaciones matemáticas (total += cantidad) → 10%

Conclusión:
⚠️ Advertencia: Este código es más propio de un script básico que de un backend profesional.
✅ Para backend real: Deberás usar bases de datos (SQL, NoSQL) en lugar de diccionarios en memoria y sustituir la entrada de usuario por solicitudes HTTP a una API.'''

ventas_diarias = {}  # (10%)
continuar = True     # (5%)

while continuar:  # (10%)
    opcion = input("1. Registrar venta\n2. Actualizar cantidad vendida\n3. Calcular total de ventas\n4. Salir\nElige una opción: ")  # (5%)

    # Registrar ventas
    if opcion == "1":  # (10%)
        # Ingresar producto y cantidad vendida
        producto = input("Ingrese el nombre del producto: ")  # (5%)
        cantidad = int(input("Ingrese la cantidad vendida: "))  # (5%)
        # Si el producto ya está registrado
        if producto in ventas_diarias:  # (10%)
            # Sumamos la cantidad vendida a las cantidades anteriores
            ventas_diarias[producto] += cantidad  # (15%)
        # Si el producto no está registrado, añadimos el producto 
        else:
            ventas_diarias[producto] = cantidad  # (15%)

    # Actualizar la cantidad vendida
    elif opcion == "2":  # (10%)
        # Ingresar producto
        producto = input("Ingrese el nombre del producto a actualizar: ")  # (5%)
        # Comprobamos que el producto existe en nuestro registro
        if producto in ventas_diarias:  # (10%)
            # Pedimos la cantidad vendida de ese producto
            nueva_cantidad = int(input("Ingrese la nueva cantidad vendida: "))  # (5%)
            # Actualizamos la cantidad total de unidades vendidas
            ventas_diarias[producto] = nueva_cantidad  # (15%)
        # En el caso de que el producto no exista en la base de datos lo indicamos
        else:
            print("El producto no existe en las ventas diarias.")  # (0%)

    # Calcular el total de las ventas
    elif opcion == "3":  # (10%)
        total = 0  # (5%)
        # Recorremos los valores del diccionario
        for cantidad in ventas_diarias.values():  # (10%)
            # Los sumamos al valor total de ventas
            total += cantidad  # (10%)
        # Imprimimos el valor total de las ventas
        print("El total de ventas diarias es:", total)  # (0%)

    # Salir del programa
    elif opcion == "4":  # (5%)
        print("Saliendo del programa...")  # (0%)
        continuar = False  # (5%)

    # Si el número introducido no es 1,2,3,4 pedimos que se elija
    # una opción válida
    else:
        print("Opción inválida. Por favor, elija una opción válida.")  # (0%)
