''' 
Conversión de tipos en Python
✅ Muy usado en Backend (90%)

Estas conversiones son fundamentales cuando se trabaja con datos en APIs, JSON, bases de datos, procesamiento de datos en frameworks como FastAPI, Django y Flask y estructuras dinámicas.

¡Apréndelas bien! 🚀
'''

### 🔹 Convertir una lista a una tupla → 20% ⚠️ (La inmutabilidad se maneja con bases de datos)
lista = [1, 2, 3, 4]
mi_tupla = tuple(lista)
print(mi_tupla)  # (1, 2, 3, 4)
# 📌 Se usa cuando los datos deben ser inmutables (no modificables)  

### 🔹 Convertir una lista a un set → 30%⚠️ (Se maneja con DISTINCT en SQL)
lista = [1, 2, 3, 3, 4, 5, 5]
mi_set = set(lista)  
print(mi_set)  # {1, 2, 3, 4, 5} (elimina duplicados)
# 📌 **Útil cuando se necesita eliminar duplicados rápidamente.**  


### 🔹 Convertir dos listas a una sola lista → 40%⚠️ (En bases de datos, se hace con JOIN)
from itertools import chain
lista_1 = ['matemáticas', 'historia', 'ciencias']
lista_2 = [8.5, 7.0, 9.0]
lista_unificada = list(chain(*zip(lista_1, lista_2)))
# Salida: ['matemáticas', 8.5, 'historia', 7.0, 'ciencias', 9.0]

# Si la lista tiene un numero impar de elementos, dara error. Prevenir asi:
if len(lista) % 2 == 0:
    mi_diccionario = dict(zip(lista[::2], lista[1::2]))
else:
    print("Error: La lista tiene un número impar de elementos")


### 🔹 Convertir una tupla a un diccionario 📌 Uso futuro en backend profesional: 50%
tupla = (('nombre', 'Guillermo'), ('edad', 51))
mi_diccionario = dict(tupla)
print(mi_diccionario)  # {'nombre': 'Guillermo', 'edad': 51}
# 📌 **Muy común en la conversión de datos de bases de datos a estructuras de Python.**

# Se usa mucho extraer solo las claves, o solo los valores:
dicc = {'a': 1, 'b': 2, 'c': 3}
lista_claves = list(dicc.keys())     # ['a', 'b', 'c']
lista_valores = list(dicc.values())  # [1, 2, 3]

### 🔹 Lista de tuplas a diccionario 📌 Uso futuro en backend profesional: 65%
lista_tuplas = [('id', 1), ('nombre', 'Paola')]
mi_diccionario = dict(lista_tuplas)
# 📌 **Común al recibir datos de bases de datos.**

### 🔹 Convertir una lista a un diccionario 📌 Uso futuro en backend profesional: 85%
### 🔹🔹🔹 LAS LISTAS SE ZIPEAN !!!! 🔹🔹🔹
lista = ['clave1', 'valor1', 'clave2', 'valor2']    # la lista puede ser infinita...
mi_diccionario = dict(zip(lista[::2], lista[1::2])) # y esto funcionará igual.......
print(mi_diccionario)  # {'clave1': 'valor1', 'clave2': 'valor2'}
# 📌 ** útil en APIs y JSON **

### 🔹 Diccionario a lista (claves o valores) 📌 Uso futuro en backend profesional: 80%
dicc = {'a': 1, 'b': 2, 'c': 3}
lista_pares = list(dicc.items())  # [('a', 1), ('b', 2), ('c', 3)]
# 📌 **MUY usado cuando se necesita extraer datos de JSON o bases de datos.**

### 🔹 Diccionario a JSON (para APIs) 📌 Uso futuro en backend profesional: 95%
import json
dicc = {'nombre': 'Guillermo', 'edad': 51}
json_data = json.dumps(dicc)
print(json_data)  # '{"nombre": "Guillermo", "edad": 51}'
# 📌 **Esencial en APIs y comunicación entre sistemas.**


""" ✅ Aprende bien:
Convertir diccionarios a JSON (json.dumps()) → 95%
Convertir diccionario a lista (dict.items(), dict.keys(), dict.values()) → 80%
Convertir lista a diccionario (dict(zip(...))) → 70%
Convertir lista de tuplas a diccionario → 65%

📉 Aprende solo lo justo (se hace mejor con bases de datos u otras herramientas):
Convertir lista a set → 30% ⚠️ (Se maneja con DISTINCT en SQL)
Convertir lista a tupla → 20% ⚠️ (La inmutabilidad se maneja con bases de datos)
Convertir dos listas en una (itertools.chain) → 40% ⚠️ (En bases de datos, se hace con JOIN)
 """