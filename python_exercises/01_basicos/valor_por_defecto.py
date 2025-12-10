def generar_mensaje(nombre: str = "visitante") -> str:
    mensaje = f"Hola, {nombre}!"
    return mensaje

p = generar_mensaje("Guille")
print(p)

p = generar_mensaje()
print(p)
