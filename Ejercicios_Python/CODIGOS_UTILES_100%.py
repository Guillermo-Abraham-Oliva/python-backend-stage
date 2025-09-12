numeros = [17, 24, 7, 39, 8, 51, 92]
numeros_pares = [num for num in numeros if num % 2 == 0]
print(numeros_pares)

def generar_resumen_usuario(nombre: str, edad: int, activo: bool) -> dict:
    return {
        "usuario": nombre.title(),
        "edad": edad,
        "estado": "activo" if activo else "inactivo",
        "mayor de edad": edad >= 18
    }

# Prueba
print(generar_resumen_usuario("juan", 20, True))

# asigna "activo" si activo es True, de lo contrario, asigna "inactivo".


