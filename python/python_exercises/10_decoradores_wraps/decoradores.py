import os
os.system("clear")

'''
1️⃣ El decorador es 'decorador_1' → Es la función que recibe otra función → 'función_que_se_esta_decorando', en este caso 'saludar', y la modifica. En un entorno profesional USAR SIEMPRE EL MISMO NOMBRE DE → funcion_original
2️⃣ 'decoracion' es el decorador o envoltura → Es la que realmente se ejecuta cuando llamas a la función decorada 'saludar'.
3️⃣ función_que_se_esta_decorando → es en este caso, saludar.

Cuando aplicas @decorador_1, lo que realmente ocurre es:
saludar = decorador_1(saludar)
Es decir, 'saludar' se decora.'''


def decorador_1(función_que_se_esta_decorando):
    '''Siempre es mejor definir decoradores con (*args, **kwargs) por si acaso la función decorada necesita argumentos.
    Si no recibe, no pasa nada'''
    def decoracion(*args, **kwargs):
        '''aqui va el codigo que queremos se ejecute ANTES 
        de la funcion original (o decorada en cuestion)
        Esto sería la decoración previa'''
        resultado = función_que_se_esta_decorando(*args, **kwargs)  # Pasa los argumentos a la función original por las dudas que los haya...
        '''aqui va el codigo que queremos se ejecute DESPUES 
        de la funcion original (o decorada en cuestion)
        Esto sería la decoración posterior'''
        return resultado # usar siempre resultado para todos los decoradores pues son de uso interno, da igual.
    return decoracion  # Esto reemplaza la función original por la versión decorada.

@decorador_1
def saludar():
    print("Hola, esto es un saludo!")

@decorador_1
def presentar(nombre):
    print(f"Hola, soy {nombre}!")

saludar()               # Función simple sin *args ni **kwargs
presentar("Guillermo")  # Función con  *args y **kwargs

        # Salida:
            # ---Decoro antes de ejecutar la función---
            # Hola, esto es un saludo!
            # ---Decoro posterior a ejecutar la función---
            # ---Decoro antes de ejecutar la función---
            # Hola, soy Guillermo!
            # ---Decoro posterior a ejecutar la función---

'''Práctica'''

def decorador_1(funcion_original):
    def decoracion(*args, **kwargs):
        '''codigo/decorador previo'''
        resultado = funcion_original(*args, **kwargs)
        '''codigo/decorador posterior'''
        return resultado
    return decoracion

@decorador_1
def calculo(**kwargs):
    nuevo_diccionario = {}  # Crear un diccionario vacío

    for clave, valor in kwargs.items():  # Iterar sobre los pares clave-valor
        nuevo_diccionario[clave] = valor  # Agregar al nuevo diccionario

    return nuevo_diccionario  # Devolver el diccionario lleno

# Ejemplo de uso
resultado = calculo(a=1, b=2, c=3)
print(resultado)  # {'a': 1, 'b': 2, 'c': 3}


'''---------------------------------------------------------------------------------'''
'''--------------PASANDO A ALGO REAL Y MUY USADO------------------------------------'''
'''✅ Ejemplo real con el uso más alto de decoradores en backend profesional 📌 90%'''
'''---------------------------------------------------------------------------------'''

from functools import wraps

# Simulación de usuario autenticado (en un sistema real, se extrae de una base de datos o token)
USUARIO_ACTUAL = {"nombre": "Guillermo", "autenticado": True}

def requiere_autenticacion(func):
    """Decorador que verifica si el usuario está autenticado antes de ejecutar la función."""
    @wraps(func)  # Mantiene el nombre y la documentación de la función original
    def envoltura(*args, **kwargs):
        if not USUARIO_ACTUAL.get("autenticado", False): # VER EXPLICACION AL FINAL !
            print("Acceso denegado: usuario no autenticado.")
            return {"error": "No tienes permiso para acceder"} # Se devuelve un diccio como error en lugar de ejecutar la función (esto es super normal en JSON)
        print("Usuario autenticado. Ejecutando la función...")
        return func(*args, **kwargs) # aqui se devuelve la funcion orginal con sus argus y demas (para que se ejecute) porque paso la prueba de la autentificacion
    return envoltura # aqui no puede ir (*args, **kwargs) porque se estaria ejecutando la función inmediatamente, lo cual es un error porque el decorador solo debe "envolver" la función original, no ejecutarla en ese momento.

# Aplicando el decorador a una función que simula un endpoint protegido
@requiere_autenticacion
def obtener_datos_sensibles():
    return {"mensaje": "Estos son datos sensibles de la API"} # Normalmente se devuelve un diccio

# Llamando la función decorada
print(obtener_datos_sensibles())


''' Practica '''
'''Aqui esta todo mas simple y directo!'''
from functools import wraps

usuario = {"nombre": "guillermo",
           "autenticado": True}

def requiere_autenticacion(func):
    @wraps(func)
    def decorador(*args, **kwargs):
        if not usuario.get("autenticado", False):
            print(f"No tienes permisos")
            return {"error": "No tienes permisos"}
        print("ejecutando peticion...")
        return func(*args, **kwargs) # aqui se devuelve la funcion orginal con sus argus y demas (para que se ejecute) porque paso la prueba de la autentificacion
    return decorador

@requiere_autenticacion
def obtener_datos_sensibles():
    return {"datos_sensibles": "xxxxxxxxxx"}

print(obtener_datos_sensibles())


# EN LA LINEA DEL IF: no confundirse con todo esto!! se devuelve 'False' si no existe la clave "autenticado"
# (es solo una precaución muy recomendable para evitar el KeyError y que se detenga el programa)
# 📢 siempre que se pregunte 👉 X.get("clave") 👉 -por defecto- esta preguntando SI ES TRUE !!!
# entonces ---> if not USUARIO_ACTUAL.get("autenticado") esta preguntando si USUARIO_ACTUAL No es 'autenticado' true.

# Hacer preguntas tipo:
        # if USUARIO_ACTUAL["autenticado"] == True:  
        # son equivalnetes pero tienen el posible fallo de que si la clave "autenticado" no existe dara KeyError!
# por eso lo mejor es: 
        # if USUARIO_ACTUAL.get("autenticado", False)

# RECORDAR:
# todo 'return' actua como un break en bucles, haciendo salir inmendiatamente de la funcion!

#################################################################################

# El decorador más usado en backend profesional con Python es `@lru_cache` de `functools`,
# porque optimiza el rendimiento al **almacenar en caché** los resultados de funciones costosas,
# evitando cálculos repetidos. 
# Esto mejora la velocidad de las APIs y reduce la carga en los servidores.

## ✅ **Ejemplo real en backend: Caché de resultados de una API**
# Imagina que tienes una API que obtiene datos de una fuente externa (como el clima o una consulta a una API de terceros). Sin caché, cada petición repetiría la consulta, desperdiciando tiempo y recursos.

from functools import lru_cache
import time

# Simulamos una función costosa (como una consulta a una API externa)
@lru_cache(maxsize=100)  # Guarda en caché hasta 100 respuestas
def obtener_datos(id):
    print(f"Consultando API externa para ID: {id}...")
    time.sleep(2)  # Simula un retardo de API externa
    return {"id": id, "dato": f"Información de {id}"}

# Prueba de la caché
print(obtener_datos(1))  # Primera vez (consulta real)
print(obtener_datos(2))  # Primera vez (consulta real)
print(obtener_datos(1))  # Segunda vez (usa caché, más rápido)


### 🔹 **Explicación**
# 1. **`@lru_cache(maxsize=100)`** almacena las últimas 100 respuestas en caché.
# 2. **Primera llamada:** Llama a la API y guarda el resultado.
# 3. **Segunda vez con el mismo ID:** No consulta la API, usa el resultado guardado **al instante**.
# 4. **`time.sleep(2)`** simula el retardo de una API real, mostrando cómo la caché acelera respuestas posteriores.

# Uso real en backend profesional: 10-20%
# ✅ lru_cache es útil en casos específicos, pero no es la mejor opción para almacenamiento en caché en entornos de backend modernos.

# Este decorador lo seguirás usando **toda la vida** en backend, incluso cuando llegues a **FastAPI y bases de datos**. ¡Apréndelo bien! 🚀