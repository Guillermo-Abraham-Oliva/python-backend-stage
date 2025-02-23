import os
os.system('clear' if os.name == 'posix' else 'cls')

'''Diccionarios con listas anidadas (Uso en backend: 30%)
🔹 Uso futuro en backend: 30%
Se usa más en sistemas con JSON, pero en backend profesional se maneja con bases de datos NoSQL.⚠️ Advertencia: En backend, esto se maneja con bases de datos NoSQL o JSON, no con diccionarios en memoria.
✅ Solo aprende lo justo: Cómo manejar datos estructurados dentro de diccionarios.'''

# Diccionario con equipos deportivos
equipos = {
    "Futbol": {"nombre": "Los Tigres", "jugadores": ["Carlos", "Pedro", "Luis"]},
    "Basket": {"nombre": "Águilas", "jugadores": ["Ana", "Marta", "Julia"]}
}

# Recorriendo el diccionario
for deporte, equipo in equipos.items():
    print(f"{equipo['nombre']}: {', '.join(equipo['jugadores'])}")

# Agregando un nuevo equipo
equipos["Voley"] = {"nombre": "Las Panteras", "jugadores": ["Gabriela", "Sofía", "Elena"]}

# Actualizando la lista de jugadores
equipos["Futbol"]["jugadores"].append("Miguel")
print(equipos)
