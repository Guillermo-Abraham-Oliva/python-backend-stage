import os
os.system('clear' if os.name == 'posix' else 'cls')

'''Diccionarios con listas anidadas (Uso en backend: 30%)
🔹 Uso futuro en backend: 30%
Se usa más en sistemas con JSON, pero en backend profesional se maneja con bases de datos NoSQL.⚠️ Advertencia: En backend, esto se maneja con bases de datos NoSQL o JSON, no con diccionarios en memoria.
✅ Solo aprende lo justo: Cómo manejar datos estructurados dentro de diccionarios.'''

# SINTESIS: 'equipos' es un diccionario anidado con listas anidadas dentro.  ✅ 85%
# DESCRIPCIÓN PASO A PASO: El diccionario principal 'equipos'
# contiene claves que son 'deportes' y diccionarios como valores. 
# Dentro de esos diccionarios, hay 2 claves:
# el nombre del 'equipo' y los 'jugadores' cuyo valor es una lista anidada
# con el nombre de todos los jugadores.

equipos = {
    "Futbol": {"nombre": "Los Tigres", "jugadores": ["Carlos", "Pedro", "Luis"]},
    "Basket": {"nombre": "Águilas", "jugadores": ["Ana", "Marta", "Julia"]},
}  

# Recorriendo el diccionario (clave=deporte, valor=equipo)
for deporte, equipo in equipos.items():                             # ✅ 85%
    print(f"{equipo['nombre']}: {', '.join(equipo['jugadores'])}")  # ✅ 85%

print(f'\n-----------------------------\n')

# Agregando un nuevo equipo
equipos["Voley"] = {"nombre": "Las Panteras", "jugadores": ["Gabriela", "Sofía", "Elena"]} 
# como valor se ha agregado un diccionario tal como ya se venía haciendo   ✅ 80%

# Agregar el jugador Miguel a Futbol
equipos["Futbol"]["jugadores"].append("Miguel")  # ✅ 85%

# Recorriendo el diccionario con las actualizaciones (clave=deporte, valor=equipo)
for deporte, equipo in equipos.items():                             # ✅ 85%
    print(f"{equipo['nombre']}: {', '.join(equipo['jugadores'])}")  # ✅ 85%

print(f'\n-----------------------\n')

##########################################################################################
# SI HAY VARIOS EQUIPOS DENTRO DE FUTBOL Y VARIOS TAMBIEN DENTRO DE BASQUET, etc:
# 
# SOLUCIÓN: Un diccio ('equipos') que para cada clave ("futbol" y "tenis") tiene como valor una lista con 3 diccios.
# Cada diccio es 1 equipo. Tiene 2 claves: 
# "equipo" con un valor de cadena de caracteres ("RIVER" por ej.) 
# y la otra clave es "jugadores" que como valor tiene una Lista de 3 jugadores

equipos = {                                                                  # ✅ 85%
    "futbol": [
        {"equipo": "RIVER", "jugadores": ["pepe", "jose", "anto"]},
        {"equipo": "BOCA", "jugadores": ["tito", "titi", "tati"]},
        {"equipo": "NEWELS", "jugadores": ["mario", "juan", "luis"]},
    ],
    "tenis": [
        {"equipo": "A", "jugadores": ["pepe", "jose", "anto"]},
        {"equipo": "B", "jugadores": ["carlos", "pedro", "miguel"]},
    ]
}  

# SUPLANTAR "luis" POR "guille" en la lista de jugadores del tercer equipo de fútbol.
equipos["futbol"][2]["jugadores"][2] = "guille"
# EXPLICACIÓN: 
#             se cita la clave 'textual' si es Diccio, ej ["futbol"]
#             se cita la clave numerada si es Lista, ej [2]



# Recorrer todo este diccionario   ✅ 85%
for deporte, lista_equipos in equipos.items(): 
    print(f"Deporte: {deporte}")
    for equipo in lista_equipos:  # 'equipo' guarda el diccio con toda la info del equipo (nombre+jug)
        print(f"  Equipo: {equipo['equipo']}, Jugadores: {', '.join(equipo['jugadores'])}") 
    print() 


'''🔹 Conclusión final
📌 Lo que debes aprender: ✅ Sintaxis de diccionarios y listas.
✅ Métodos útiles como .get(), .keys(), .values(), .items().
✅ Cómo recorrer estructuras de datos anidadas.

⚠️ Lo que NO debes profundizar demasiado: 
❌ No pierdas tiempo en manipulación manual de diccionarios.
❌ No almacenes datos en listas de diccionarios en memoria.

🛠️ Herramientas modernas que reemplazan estos ejercicios en backend:

Bases de datos SQL (PostgreSQL, MySQL) y NoSQL (MongoDB) en lugar de diccionarios manuales.
ORM como SQLAlchemy o Django ORM en lugar de listas de diccionarios.
Pandas para manipulación de datos en lugar de estructuras en memoria.
⏩ Resumen final:
🔹 Aprende solo lo justo sobre diccionarios porque su uso en backend es limitado.
🔹 En backend real usarás bases de datos y no estructuras en memoria.

🚀 Prioriza aprender bases de datos y ORM cuanto antes para no perder tiempo en código que no te servirá en backend profesional.
'''