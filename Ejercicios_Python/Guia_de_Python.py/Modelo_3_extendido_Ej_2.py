import os
os.system('clear')

'''✅ Modelo 3 extendido – Ejemplo 2: 
Uso de .append() para construir listas dinámicas

Función real que acumula elementos según condición y devuelve la lista final

Este patrón es clave cuando necesitas:
•	Recorrer datos recibidos
•	Filtrar o seleccionar algunos
•	Acumularlos dinámicamente en una lista
•	Devolver esa lista limpia y filtrada al frontend o para otro uso

Este tipo de función se utiliza para construir listas de elementos válidos, disponibles, aprobados, encontrados, etc.
'''

def controlador (numeros: str):
    lista_numeros_enteros = [int(n) for n in numeros.split(",")]  # "7,8,9,10,11,12"
    numeros_pares = solo_pares(lista_numeros_enteros)
    return {"pares": numeros_pares}

def solo_pares (numeros: list) -> list:
    pares = []
    for n in numeros:
        if n % 2 == 0:
            pares.append(n)
    return pares   # devuelve lista 


numeros = "7,8,9,10,11,12"

controlador(numeros)
print(controlador)
