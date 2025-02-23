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


'''🔹 Conclusión final
📌 Lo que debes aprender: ✅ Sintaxis de diccionarios y listas.
✅ Métodos útiles como .get(), .keys(), .values(), .items().
✅ Cómo recorrer estructuras de datos anidadas.

⚠️ Lo que NO debes profundizar demasiado: ❌ No pierdas tiempo en manipulación manual de diccionarios.
❌ No almacenes datos en listas de diccionarios en memoria.

🛠️ Herramientas modernas que reemplazan estos ejercicios en backend:

Bases de datos SQL (PostgreSQL, MySQL) y NoSQL (MongoDB) en lugar de diccionarios manuales.
ORM como SQLAlchemy o Django ORM en lugar de listas de diccionarios.
Pandas para manipulación de datos en lugar de estructuras en memoria.
⏩ Resumen final:
🔹 Aprende solo lo justo sobre diccionarios porque su uso en backend es limitado.
🔹 En backend real usarás bases de datos y no estructuras en memoria.

🚀 Prioriza aprender bases de datos y ORM cuanto antes para no perder tiempo en código que no te servirá en backend profesional.'''