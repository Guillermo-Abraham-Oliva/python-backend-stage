import os
os.system('clear')

"""
Este script simula un sistema de pedidos de pizza con diferentes tamaños e ingredientes.

Funciona de la siguiente manera:
1. Recibe un tamaño de pizza en centímetros.
2. Puede recibir un número VARIABLE de ingredientes gracias al parámetro `*ingredientes`.
3. Muestra un resumen del pedido, incluyendo la dimensión y los ingredientes seleccionados.

📌 Uso del parámetro ---> *ingredientes:
El `*` en `*ingredientes` permite a la función aceptar un número **variable** de argumentos.
Esto significa que puedes llamar a la función con uno o más ingredientes sin necesidad de definir un número fijo de parámetros.
Los ingredientes se almacenan internamente como una **tupla**, lo que permite iterarlos dentro de la función.

Ejemplo:
- `hacer_pizza(16, "pepperoni")` → Recibe un solo ingrediente.
- `hacer_pizza(12, "champignons", "pimiento verde", "aceitunas")` → Recibe varios ingredientes.

Este enfoque es útil cuando no sabemos cuántos argumentos se van a pasar a la función.
"""

def hacer_pizza(dimension, *ingredientes):
    """Resumen del pedido"""
    print(f"Has pedido una pizza de {dimension} cm.")
    print("La pizza contiene los siguientes ingredientes:")
    for ingrediente in ingredientes:
        print(f"- {ingrediente}")
    print("\n")

hacer_pizza(12, "champignons", "pimiento verde", "aceitunas")
    # Salida:
    #   Has pedido una pizza de 12 cm.
    #   La pizza contiene los siguientes ingredientes:
    #   - champignons
    #   - pimiento verde
    #   - aceitunas

hacer_pizza(16, "pepperoni")
    # Salida:
    #   Has pedido una pizza de 16 cm.
    #   La pizza contiene los siguientes ingredientes:
    #   - pepperoni