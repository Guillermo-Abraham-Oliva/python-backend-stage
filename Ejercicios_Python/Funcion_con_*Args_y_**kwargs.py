# 📌 Explicación de `*args` y `**kwargs`

# 1️⃣ Ejemplo de `*args` (Argumentos posicionales variables)
    # Cuando usas `*args`, la función puede recibir 
    # cualquier cantidad de argumentos posicionales (*args)
    # que serán almacenados en una TUPLA

def sumar_numeros(*args):
    total = sum(args)  # `args` es una tupla con todos los números pasados
    print(f"Suma total: {total}")

sumar_numeros(5, 10, 15, 20)  # Puedo pasar cualquier cantidad de números

    # 🔹 **Salida:**
    # Suma total: 50

# 📌 **¿Qué pasa aquí?**  
# La función `sumar_numeros` acepta **cualquier cantidad de números**.
# `args` se convierte en la tupla `(5, 10, 15, 20)`.
# Se usa `sum(args)` para sumar todos los elementos que se reciban.


# 2️⃣ Ejemplo de `**kwargs` (Argumentos con nombre variables)
    # Cuando usas `**kwargs`, la función puede recibir
    # cualquier cantidad de ARGUMENTOS CON NOMBRE o KEYWORDS ARGUMENTS (**kwargs)
    # que serán almacenados en un DICCIONARIO

def mostrar_usuario(**kwargs):
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")

mostrar_usuario(nombre="Carlos", edad=30, ciudad="Madrid")

    # 🔹 **Salida:**
    # nombre: Carlos
    # edad: 30
    # ciudad: Madrid

# 📌 **¿Qué pasa aquí?**  
# La función `mostrar_usuario` acepta **cualquier cantidad de argumentos con nombre**.
# `kwargs` se convierte en el diccionario 
#         {"nombre": "Carlos", "edad": 30, "ciudad": "Madrid"}
# Se usa un for para recorrer e imprimir cada clave y valor.


# 3️⃣ Ejemplo COMBINADO de *args y **kwargs
# Puedes usar ambos juntos para aceptar tanto
# argumentos posicionales como argumentos con nombre en la misma función.

def informacion(*args, **kwargs):
    print("Argumentos posicionales:", args)  # Tupla
    print("Argumentos con nombre:", kwargs)  # Diccionario

informacion(10, "Hola", True, nombre="Ana", edad=25, ciudad="Sevilla")

    # 🔹 **Salida:**
    # Argumentos posicionales: (10, 'Hola', True)
    # Argumentos con nombre: {'nombre': 'Ana', 'edad': 25, 'ciudad': 'Sevilla'}

# 📌 ¿Qué pasa aquí?
# `args` almacena `(10, "Hola", True)`, que son los valores sin clave.
# `kwargs` almacena `{"nombre": "Ana", "edad": 25, "ciudad": "Sevilla"}`.
# Así, podemos manejar datos de cualquier tipo SIN definir un número fijo de parámetros.


## *** 📌 Conclusión 📌 ***
# |   Uso    |   Se recibe como:       | Tipo de dato:        |
# | *args    | Argumentos posicionales | Tupla (`tuple`)      |
# | **kwargs | Argumentos con nombre   | Diccionario (`dict`) |

# ✅ `*args` es útil cuando no sabemos cuántos argumentos posicionales recibiremos.  
# ✅ `**kwargs` es ideal cuando queremos aceptar argumentos con nombre flexibles.  
# ✅ Ambos pueden combinarse para funciones súper flexibles.


################## 📌 mas ejemplos para esclarecer la Diferencia clave ########################

# **kwargs convierte los "argumentos con nombre" en un diccionario automáticamente.
def mostrar_info(**kwargs):
    print(kwargs)

mostrar_info(nombre="Carlos", edad=30, ciudad="Madrid")


# En cambio, un diccionario normal (dict) debe pasarse explícitamente como un solo argumento.
def mostrar_info(diccionario):
    print(diccionario)

datos = {"nombre": "Carlos", "edad": 30, "ciudad": "Madrid"}
mostrar_info(datos)