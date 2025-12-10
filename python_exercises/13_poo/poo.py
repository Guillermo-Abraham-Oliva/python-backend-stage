class persona:
    def __init__(self, nombre: str, edad: int, profesion: str):
        self.nombre = nombre
        self.edad = edad
        self.profesion = profesion


persona1 = persona("Juan", 30, "Abogado")
persona2 = persona("Maria", 25, "Ingeniera")

print(persona1.nombre, persona1.edad, persona1.profesion)
print(persona2.nombre, persona2.edad, persona2.profesion)


class fruta:
    def __init__(self, nombre: str, color: str, precio: float):
        self.nombre = nombre
        self.color = color
        self.precio = precio


manzana = fruta("manzana", "rojo", 2.50)
kiwi = fruta("kiwi", "verde", 3.90)


#####################################################################
class Fruta:
    def __init__(self, nombre: str, color: str, precio: float):
        self.nombre = nombre
        self.color = color
        self.precio = precio

    def descripcion(self) -> str:  # este self hace ref al self anterior: CONECTA
        return f"{self.nombre.capitalize()} de color {self.color}, cuesta €{self.precio:.2f}"


manzana = Fruta("manzana", "rojo", 2.50)
kiwi = Fruta("kiwi", "verde", 3.90)

print(manzana.descripcion())
print(kiwi.descripcion())


########################################################################################
# Ejercicios Conquer  (solo los de cierta utilidad)
########################################################################################

from dataclasses import dataclass
import random  # Se reemplaza por secrets (lo más usado hoy en producción para claves, tokens, contraseñas).

# =========================
# PERSONA (modelo de datos)
# Uso pro estimado (con dataclass/Pydantic/ORM): ~90%
# =========================


@dataclass
class Persona:
    nombre: str
    edad: int
    profesion: str

    def info(self) -> str:
        return f"{self.nombre} ({self.edad}) – {self.profesion}"


# =========================
# LIBRO (modelo de datos)
# Uso pro estimado (con dataclass/Pydantic/ORM): ~90%
# =========================


class Libro:
    def __init__(self, titulo: str, autor: str, anio: int):
        self.titulo = titulo
        self.autor = autor
        self.anio = anio

    def info(self) -> str:
        return f"«{self.titulo}», {self.autor} ({self.anio})"


libro_1 = Libro("Hoy", "Guille", 2025)
tit = (
    libro_1.info()
)  # se accede al metodo 'info' (funcion interna) POR MEDIO DEL OBJETO CREADO ()libro_1)
print(tit)


# =========================
# COCHE (objeto con estado)
# Uso pro estimado: ~40%
# =========================


class Coche:
    def __init__(self, marca: str, modelo: str, anio: int):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.encendido = False  # estado interno

    def encender(self) -> str:
        if not self.encendido:
            self.encendido = True
            return "Coche encendido."
        return "El coche ya estaba encendido."

    def apagar(self) -> str:
        if self.encendido:
            self.encendido = False
            return "Coche apagado."
        return "El coche ya estaba apagado."

    def info(self) -> str:
        estado = "encendido" if self.encendido else "apagado"
        return f"{self.marca} {self.modelo} ({self.anio}) – {estado}"


# =========================
# DEMOSTRACIÓN RÁPIDA
# =========================
if (
    __name__ == "__main__"
):  # es un interruptor: el bloque debajo solo se ejecuta cuando corres el archivo directamente. Si el archivo se importa desde otro, no se ejecuta.

    # Persona
    personas = [  # aqui se arma una lista con 3 objetos de la clase persona
        Persona(
            "Guille", 40, "Guía espiritual"
        ),  # 1º objeto  se buscaría como Persona[0]
        Persona(
            "Ana", 35, "Desarrolladora Backend"
        ),  # 2º objeto  se buscaría como Persona[1]
        Persona("Luis", 29, "Diseñador"),  # 3º objeto  se buscaría como Persona[2]
    ]
    for (
        p
    ) in personas:  # se recorre la lista ejecutando el metodo (funcion) en cada objeto
        print(p.info())

        # Libro
    libros = [
        Libro("El hombre en busca de sentido", "Viktor Frankl", 1946),
        Libro("El arte de amar", "Erich Fromm", 1956),
    ]
    for l in libros:
        print(l.info())

        # Coche
    c = Coche("Toyota", "Corolla", 2020)
    print(c.info())
    print(c.encender())
    print(c.info())
    print(c.apagar())
    print(c.info())
