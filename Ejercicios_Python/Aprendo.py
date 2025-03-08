import os
os.system('clear')


usuarios = [
    {"nombre": "Carlos", "edad": 30},
    {"nombre": "Ana", "edad": 11},
    {"nombre": "Luis", "edad": 25}
]

usuarios_ordenados = sorted(usuarios, key=lambda x: x["edad"])
print(usuarios_ordenados)

usuarios = [
    {"nombre": "Carlos", "edad": 30},
    {"nombre": "Ana", "edad": None},
    {"nombre": "Luis", "edad": 25}
]

usuarios_ordenados = sorted(usuarios, key=lambda x: (x["edad"] is None, x["edad"]))
print(usuarios_ordenados)