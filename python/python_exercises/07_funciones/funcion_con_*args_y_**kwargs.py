import os
os.system("clear")

# 📌 Explicación de  *args  y  **kwargs
#    *  1 asterisco  es para utilizar una cant variable de argumentos en una TUPLA
#   **  2 asteriscos es para utilizar una cant variable de pares 'clave-valor' en un DICT exclusivamente


# 1️⃣ Ejemplo de  *args (Argumentos posicionales variables) ✅ 90%
    # Cuando usas  *args, la función puede recibir 
    # cualquier cantidad de argumentos posicionales (*args)
    # que serán almacenados en una TUPLA

def sumar_numeros(*args):  # ejemplo choto básico (5%)
    total = sum(args)  # `args` es una tupla con todos los números pasados
    print(f"Suma total: {total}")

sumar_numeros(5, 10, 15, 20)  # Puedo pasar cualquier cantidad de números

        # Salida:
            # Suma total: 50

# 📌 **¿Qué pasa aquí?**  
# La función `sumar_numeros` acepta **cualquier cantidad de números**.
# `args` se convierte en la tupla `(5, 10, 15, 20)`.
# Se usa `sum(args)` para sumar todos los elementos que se reciban.

#########################################################################
# En backend profesional, el uso de `*args` no es tan frecuente como
# otros conceptos clave (como bases de datos, APIs o autenticación). 
# Sin embargo, sí hay escenarios donde `*args` es crucial en entornos reales. 
# Aquí tienes esos ejemplos:


## 1️⃣ **Middleware para procesamiento de datos dinámicos**  ✅ 90% 
# 🔹 En backend, los **middlewares** procesan datos antes de que lleguen a una función principal (ej., validaciones, logs, autenticación).

# Función middleware que recibe múltiples funciones y devuelve una nueva función
def middleware(*funciones):
    # Recibe varias funciones y DEVUELVE UNA NUEVA FUNCIÓN que aplicará todas esas funciones en orden sobre una entrada
    
    def procesar(datos):   # Toma datos de entrada y les aplica todas las funciones en secuencia.
        for funcion in funciones:  
            datos = funcion(datos)  # Se aplica cada función a los datos y se actualiza el resultado
        return datos  
    
    return procesar  # No ejecuta nada todavía, solo devuelve la función 'procesar'

# Definimos algunas funciones de transformación
def normalizar(texto):  # Convierte el texto a minúsculas y elimina espacios extra.
    return texto.lower().strip()

def agregar_prefijo(texto):  # Añade un prefijo 'LOG:' al texto.
    return f"LOG: {texto}"

# Creamos un "procesador" con las funciones 'normalizar' y 'agregar_prefijo'
procesador = middleware(normalizar, agregar_prefijo)

# Aplicamos el procesador a un texto
resultado = procesador("  ERROR en el sistema  ")
print(resultado)
            # Salida:
                # LOG: error en el sistema

### **Explicación paso a paso**

#### **1️⃣ ¿Qué hace el código?**
# Este script permite encadenar varias funciones y aplicarlas a un dato cuando sea necesario.  

# 1. `middleware` recibe varias funciones y **devuelve una nueva función** (`procesar`) que, cuando se ejecute, aplicará todas esas funciones a los datos de entrada.  
# 2. `procesador` es esa función devuelta, que aún **no ha procesado nada**, solo está lista para hacerlo.  
# 3. Cuando ejecutamos `procesador("  ERROR en el sistema  ")`, se aplican las transformaciones en orden:
#    - Se eliminan espacios y se convierte a minúsculas (`normalizar`).
#    - Se añade el prefijo "LOG:" (`agregar_prefijo`).
#    - El resultado final es `"LOG: error en el sistema"`.

# #### **2️⃣ ¿Por qué `procesar(datos)` está dentro de `middleware` y no directamente el `for`?**
# Si hubiéramos puesto el `for` dentro de `middleware` directamente, **las funciones se aplicarían inmediatamente en el momento de definir `procesador`**, en lugar de esperar a recibir datos.

# **Ejemplo incorrecto (lo que NO queremos):**

def middleware(*funciones):
    datos = "ALGO FIJO"  # No podemos procesar datos desconocidos todavía
    for funcion in funciones:
        datos = funcion(datos)  # Se ejecuta una sola vez, no cuando llamemos a la función
    return datos  # Devuelve el resultado de inmediato, sin flexibilidad

# ❌ **Problema**: Esto solo permitiría procesar un valor fijo y no podríamos reutilizar `procesador` con diferentes entradas.

# ✅ **Solución correcta (como está en nuestro código)**:  
# - `middleware` **solo devuelve una función** (`procesar`), sin ejecutarla.  
# - `procesar(datos)` **se ejecuta después**, cuando reciba un dato real.  
# - Así, podemos reutilizar `procesador` para múltiples valores.

# #### **3️⃣ ¿Cómo funciona el flujo de ejecución?**
# | Paso | Acción | Valor de `datos` |
# |------|--------|------------------|
# | 1 | Se llama `middleware(normalizar, agregar_prefijo)` | Nada todavía |
# | 2 | Se devuelve la función `procesar`, que aún no se ejecuta | Nada todavía |
# | 3 | Se ejecuta `procesador("  ERROR en el sistema  ")` | `"  ERROR en el sistema  "` |
# | 4 | Se aplica `normalizar(datos)` | `"error en el sistema"` |
# | 5 | Se aplica `agregar_prefijo(datos)` | `"LOG: error en el sistema"` |
# | 6 | Se devuelve el resultado final | `"LOG: error en el sistema"` |

# #### **4️⃣ Conclusión**
# 📌 **EL TRUCO ESTÁ EN DEVOLVER UNA FUNCIÓN EN LUGAR DE EJECUTAR EL CÓDIGO DE INMEDIATO**.  
# 📌 **El `for` debe estar dentro de `procesar`** para que la transformación ocurra cada vez que llamamos a `procesador(datos)`, y no antes.  
# 📌 **Este patrón permite aplicar múltiples funciones de forma flexible a cualquier entrada futura**.


# ### 🔥 **Regla de oro**
# 👉 **SI UNA FUNCIÓN NECESITA RECORDAR CONFIGURACIONES PERO EJECUTARSE DESPUÉS, HAY QUE DEVOLVER OTRA FUNCIÓN EN LUGAR DE EJECUTARLA DE INMEDIATO.**  


# Este codigo es Frecuente en:  
# - Filtrado y transformación de datos antes de entrar a la lógica del backend.  
# - Implementación de **pipelines de procesamiento** en APIs.  
# - Aplicaciones con **múltiples capas de validación**.  


#-----------------------------------------------------------------------------------------------------------------
## 2️⃣ **Sistema de eventos y callbacks dinámicos** ✅ 90%
# 🔹 Los sistemas backend suelen usar eventos o **callbacks** para ejecutar múltiples funciones de manera flexible.

def manejar_evento(evento, *callbacks):
    """Ejecuta múltiples funciones cuando ocurre un evento."""
    print(f"Evento recibido: {evento}")
    for callback in callbacks:
        callback(evento)

# Callbacks
def log_evento(evento): print(f"Registrado en log: {evento}")
def enviar_alerta(evento): print(f"ALERTA enviada: {evento}")

# Llamada al sistema de eventos
manejar_evento("Usuario conectado", log_evento, enviar_alerta)

        # Salida:
            # Evento recibido: Usuario conectado
            # Registrado en log: Usuario conectado
            # ALERTA enviada: Usuario conectado


# Frecuente en:  
# - **WebSockets** y sistemas de eventos en tiempo real.  
# - Registro de actividad de usuarios en **monitoreo de backend**.  
# - Mecanismos de **plugins y extensiones** en servidores.  



## 3️⃣ **Sistema de permisos y roles de usuario** ✅ 100%**  
# 🔹 En un backend real, **el control de acceso es fundamental** y `*args` ayuda a definir permisos de forma flexible.


def verificar_permisos(usuario, *permisos_requeridos):
    """Verifica si un usuario tiene los permisos que solicita."""
    permisos_usuario = usuario.get("permisos", []) # se ven los permisos que tiene (si "permisos" no existe, devuelve una lista vacia evitando que el programa se detenga por keyerror")
    if all(x in permisos_usuario for x in permisos_requeridos):  # VER OPCION A ESTO MAS ABAJO!!
        print(f"Acceso concedido a {usuario['nombre']} (eres {usuario['categoria']})")
    else:
        print(f"Acceso DENEGADO a {usuario['nombre']} (eres {usuario['categoria']})")

# Definir usuarios con permisos
usuario1 = {
    "nombre": "Juan", 
    "categoria": "Admin", 
    "permisos": ["leer", "escribir", "eliminar"]}
usuario2 = {
    "nombre": "Pedro", 
    "categoria": "Invitado", 
    "permisos": ["leer"]}

# Verificación dinámica de permisos
verificar_permisos(usuario1, "escribir", "eliminar") # ✅ Acceso concedido a Juan (eres Admin)
verificar_permisos(usuario2, "escribir")             # ❌ Acceso DENEGADO a Pedro (eres Invitado)

# OPCION  a if all()  de linea 158 :
#       for p in permisos_requeridos:
#            if p not in permisos_usuario:
#                 return False              # Acceso denegado
#       return True                         # Acceso concedido

# Frecuente en:  
# - **Autenticación y autorización** de usuarios en backend.  
# - Control de acceso basado en **roles y permisos**.  
# - Aplicaciones empresariales con múltiples niveles de usuarios.  



## 4️⃣ **Enrutamiento dinámico en servidores** ✅ 100%
# En un backend, definir rutas de API de manera dinámica es esencial, y `*args` permite flexibilidad total.

from pprint import pprint

rutas = {}

def registrar_ruta(url, *metodos):
    rutas[url] = metodos

registrar_ruta("/usuarios", "GET", "POST", "PUT", "DELETE")
registrar_ruta("/productos", "GET", "POST", "PUT", "DELETE")
registrar_ruta("/pedidos", "GET", "POST", "PUT")
registrar_ruta("/pagos", "POST", "GET")

pprint(rutas)
    # Salida:
            # {'/pagos': ('POST', 'GET'),
            #  '/pedidos': ('GET', 'POST', 'PUT'),
            #  '/productos': ('GET', 'POST', 'PUT', 'DELETE'),
            #  '/usuarios': ('GET', 'POST', 'PUT', 'DELETE')}


# Frecuente en:  
# - **Definición de rutas en APIs** (con frameworks como Flask, Django o FastAPI).  
# - Configuración de **microservicios** y puntos de entrada dinámicos.  
# - Control de acceso a **endpoints según métodos HTTP**.  


### **🔹 Conclusión**
# ⚠️ **Advertencia:** Si bien `*args` es útil en estos casos, en muchos frameworks modernos **se usan decoradores, clases o diccionarios** para lograr la misma flexibilidad. Pero si entiendes `*args`, dominarás mejor la lógica de backend y te ayudará a escribir código más eficiente.



################################################################################
# 2️⃣ Ejemplo de `**kwargs` (Argumentos con nombre variables) ✅ 85%
    # Cuando usas `**kwargs`, la función puede recibir
    # cualquier cantidad de ARGUMENTOS CON NOMBRE o KEYWORDS ARGUMENTS (**kwargs)
    # que serán almacenados en un DICCIONARIO

def mostrar_usuario(**kwargs):
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")

mostrar_usuario(nombre="Carlos", edad=30, ciudad="Madrid")

        # Salida:
            # nombre: Carlos
            # edad: 30
            # ciudad: Madrid

# 📌 **¿Qué pasa aquí?**  
# La función `mostrar_usuario` acepta **cualquier cantidad de argumentos con nombre**.
# `kwargs` se convierte en el diccionario 
#         {"nombre": "Carlos", "edad": 30, "ciudad": "Madrid"}
# Se usa un for para recorrer e imprimir cada clave y valor.


# 3️⃣ Ejemplo COMBINADO de *args y **kwargs  ✅ 95% en backend profesional
# Puedes usar ambos juntos para aceptar tanto
# argumentos posicionales como argumentos con nombre en la misma función.

def informacion(*args, **kwargs):
    print("Argumentos posicionales:", args)  # Tupla
    print("Argumentos con nombre:", kwargs)  # Diccionario

informacion(10, "Hola", True, nombre="Ana", edad=25, ciudad="Sevilla")

        # Salida:
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


################## 📌 más ejemplos para esclarecer la diferencia clave ########################

# **kwargs convierte los "argumentos con nombre" en un diccionario automáticamente. ✅ 85%
def mostrar_info(**kwargs):
    print(kwargs)

mostrar_info(nombre="Carlos", edad=30, ciudad="Madrid")

        # Salida:
            # {'nombre': 'Carlos', 'edad': 30, 'ciudad': 'Madrid'}


# En cambio, un diccionario normal (dict) debe pasarse explícitamente como un solo argumento. (✅ 80% en backend profesional)
def mostrar_info(diccionario):
    print(diccionario)

datos = {"nombre": "Carlos", "edad": 30, "ciudad": "Madrid"}
mostrar_info(datos)

        # Salida:
                # {'nombre': 'Carlos', 'edad': 30, 'ciudad': 'Madrid'}
