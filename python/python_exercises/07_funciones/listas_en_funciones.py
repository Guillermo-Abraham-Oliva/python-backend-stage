import os
os.system('clear' if os.name == 'posix' else 'cls')

"""
Este script simula un sistema de impresión de modelos 3D.

Funciona de la siguiente manera:
1. Toma una lista de modelos pendientes de impresión.
2. Simula la impresión de cada modelo, moviéndolo a una lista de modelos completados.
3. Muestra los modelos que han sido impresos.
4. Hace que la lista original de encargos no se modifique porque usa una copia.

Este código es útil para entender la manipulación de listas y el paso de parámetros por referencia o copia en Python.
"""
# ✅ Porcentaje de uso futuro en backend profesional: 20%
def imprimir_modelos(encargos, finalizados):
    """Simula la impresión de cada diseño hasta que todos han sido completados.
    Mueve cada diseño a la lista de finalizados tras imprimirlo."""
    while encargos:
        diseño_actual = encargos.pop() # Extrae el último modelo de la lista de encargos
        print("Imprimiendo modelo: " + diseño_actual) # Simula la impresión del modelo
        finalizados.append(diseño_actual) # Agrega el modelo impreso a la lista de finalizados

def muestra_modelos_completados(finalizados):
    """ Muestra los modelos impresos. """
    print("\nLos siguientes modelos han sido impresos:")
    
    # Recorre la lista de modelos finalizados y los muestra
    for modelo_finalizado in finalizados:
        print(modelo_finalizado)

# Lista de modelos pendientes de impresión
modelos_encargados = ['iphone case', 'robot pendant', 'dodecahedron']
modelos_completados = [] # Lista vacía para almacenar los modelos completados

# Llama a la función de impresión, pasando una copia de la lista de encargos
imprimir_modelos(modelos_encargados[:], modelos_completados)

muestra_modelos_completados(modelos_completados) # Muestra los modelos que han sido impresos
# Cuando 'modelos_completados' se pasa como argumento a la función imprimir_modelos(), 
# dentro de la función es referenciado como 'finalizados'. 
# Como finalizados es solo un ALIAS dentro de la función, cualquier cambio hecho dentro de la función
# afecta DIRECTAMENTE a la lista original 'modelos_completados' 
# porque es un objeto mutable pasado por referencia.

print(modelos_encargados) # Muestra la lista original de modelos encargados
