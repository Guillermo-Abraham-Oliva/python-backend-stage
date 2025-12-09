#######################################################
# ✅ Ejemplo 1 – Lógica interna en un microservicio
# ________________________________________
# 1️ - Archivo: main.py
from fastapi import FastAPI
from routes import archivo_de_routes
app = FastAPI()
app.include_router(archivo_de_routes.router)
# ________________________________________
# 2️ - Carpeta routes / Archivo: archivo_de_routes.py
from fastapi import APIRouter
from services.archivo_de_services import función_lógica_pura
router = APIRouter()
@router.get("/ServicioQueTuAPIOfrece")
def funcion_deseada(parametro1: float, parametro2: bool):
    resultado = función_lógica_pura(parametro1, parametro2)
    return {"resultado": resultado}
# ________________________________________
# 3️ - Carpeta services / Archivo: archivo_de_services.py
def función_lógica_pura(parametro1: float, parametro2: bool) -> dict:
    return (aqui se efectúa el cálculo)


#######################################################
# ✅ Ejemplo 2 – Validación simple (sin errores aún)
# ________________________________________
1️ - Archivo: main.py
from fastapi import FastAPI   
from routes import validaciones       
app = FastAPI()              
app.include_router(validaciones.router)         
# ________________________________________
# 2️ - Archivo: routes/validaciones.py
from fastapi import APIRouter                   
from services.validaciones import es_mayor_de_edad  
router = APIRouter()                            
@router.get("/mayor")                           
def verificar_edad(edad: int):                     
    resultado = es_mayor_de_edad(edad)          
    return {"es_mayor": resultado}              
# ________________________________________
# 3️ - Archivo: services/validaciones.py
def es_mayor_de_edad(edad: int) -> bool:
    return edad >= 18                           

#######################################################
# ✅ Ejemplo 3 – Normalización de texto (limpieza de nombres)
# ________________________________________
# 1️ - Archivo: main.py
from fastapi import FastAPI
from routes import usuarios
app = FastAPI()
app.include_router(usuarios.router)
# ________________________________________
# 2️ - Archivo: routes/usuarios.py
from fastapi import APIRouter
from services.usuarios import limpiar_nombre
router = APIRouter()
@router.post("/usuarios")
def crear_usuario(nombre: str):
    nombre_limpio = limpiar_nombre(nombre)
    return {"nombre_guardado": nombre_limpio}
# ________________________________________
# 3️ - Archivo: services/usuarios.py
def limpiar_nombre(nombre: str) -> str:
    return nombre.strip().title()

#######################################################
# ✅ Ejemplo 4 – Construcción de respuesta estructurada
# ________________________________________
# 1️ - Archivo: main.py
from fastapi import FastAPI
from routes import respuestas
app = FastAPI()
app.include_router(respuestas.router)
# ________________________________________
# 2️ - Archivo: routes/respuestas.py
from fastapi import APIRouter
from services.respuestas import construir_respuesta
router = APIRouter()
@router.get("/respuesta")
def respuesta(dato: str):
    return construir_respuesta(dato)  # Devolvemos directamente el diccionario generado
# ________________________________________
# 3️ - Archivo: services/respuestas.py
def construir_respuesta(dato: str) -> dict:
    return {"estado": "ok", "resultado": dato}


# ________________________________________
# 2)	Modelo 2 – Funciones con manejo de errores (try, except, raise, else y finally)
# ________________________________________
def dividir(a: float, b: float) -> float:
    try:
        return a / b
    except ZeroDivisionError:
        raise ValueError("No se puede dividir por cero.")

# ________________________________________
# ✅ Modelo 2 – Ejemplo 1 – Manejo de errores en una división segura
# ________________________________________
# 1️ - Archivo: main.py
from fastapi import FastAPI
from routes import operaciones
app = FastAPI()
app.include_router(operaciones.router)
# ________________________________________
# 2️ - Archivo: routes/operaciones.py
from fastapi import APIRouter
from services.operaciones import dividir
router = APIRouter()
@router.get("/dividir")
def dividir_endpoint(a: float, b: float):
    resultado = dividir(a, b)
    return {"resultado": resultado}
# ________________________________________
# 3️ - Archivo: services/operaciones.py
def dividir(a: float, b: float) -> float:
    try:
        return a / b
    except ZeroDivisionError:
        # En vez de crashear, lanzamos un error claro y controlado
        raise ValueError("No se puede dividir por cero.")

# ✅ Modelo 2 – Ejemplo 2: Conversión de texto a número con control de error
# ________________________________________
# 1️ - Archivo: main.py
from fastapi import FastAPI
from routes import conversiones
app = FastAPI()
app.include_router(conversiones.router)
# ________________________________________
# 2️ - Archivo: routes/conversiones.py
from fastapi import APIRouter
from services.conversiones import convertir_a_entero
router = APIRouter()
@router.get("/convertir")
def convertir(texto: str):
    numero = convertir_a_entero(texto)  # Si no es válido, la función lanzará un error
    return {"numero": numero}
# ________________________________________
# 3️ - Archivo: services/conversiones.py
def convertir_a_entero(texto: str) -> int:
    try:
        return int(texto)
    except ValueError:
        raise ValueError("El valor debe ser un número entero válido.")

# ✅ Modelo 2 – Ejemplo 3: Validación manual con raise
# ________________________________________
# 1️ - Archivo: main.py
from fastapi import FastAPI
from routes import registros
app = FastAPI()
app.include_router(registros.router)
# ________________________________________
# 2️ - Archivo: routes/registros.py
from fastapi import APIRouter
from services.registros import validar_edad
router = APIRouter()
@router.get("/registrar")
def registrar_usuario(nombre: str, edad: int):
    validar_edad(edad)  # Si no tiene edad suficiente, se lanza un error
    return {"mensaje": f"Usuario {nombre} registrado correctamente"}
# ________________________________________
# 3️ - Archivo: services/registros.py
def validar_edad(edad: int) -> None:
    if edad < 18:
        raise ValueError("Debes ser mayor de edad para registrarte.")


# ✅ Modelo 2 – Ejemplo 4: Uso de else y finally en operaciones delicadas
# ________________________________________
# 1️ - Archivo: main.py
from fastapi import FastAPI
from routes import usuarios
app = FastAPI()
app.include_router(usuarios.router)
# ________________________________________
# 2️ - Archivo: routes/usuarios.py
from fastapi import APIRouter
from services.usuarios import obtener_usuario
router = APIRouter()
@router.get("/usuario")
def ver_usuario(id: int):
    usuario = obtener_usuario(id)
    return {"usuario": usuario}
# ________________________________________
# 3️ - Archivo: services/usuarios.py
class ConexionSimulada:
    def buscar_por_id(self, id: int) -> dict:
        if id == 1:
            return {"id": 1, "nombre": "Guillermo"}
        else:
            raise Exception("Usuario no encontrado")

    def cerrar(self):
        print("Conexión cerrada")

def obtener_usuario(id: int) -> dict:
    conexion = ConexionSimulada()
    try:
        usuario = conexion.buscar_por_id(id)
    except Exception:
        raise ValueError("No se pudo acceder a los datos del usuario.")
    else:
        return usuario
    finally:
        conexion.cerrar()

# ✅ Modelo 2 – Ejemplo 5: Uso combinado con validación de negocio
# ________________________________________
1️ - Archivo: main.py
from fastapi import FastAPI
from routes import pagos
app = FastAPI()
app.include_router(pagos.router)
# ________________________________________
# 2️ - Archivo: routes/pagos.py
from fastapi import APIRouter
from services.pagos import calcular_pago
router = APIRouter()
@router.get("/pago")
def obtener_pago(horas: float, tarifa: float):
    total = calcular_pago(horas, tarifa)
    return {"total": total}
# ________________________________________
# 3️ - Archivo: services/pagos.py
def calcular_pago(horas: float, tarifa: float) -> float:
    if horas < 0 or tarifa < 0:
        raise ValueError("Las horas y la tarifa deben ser valores positivos.")
    try:
        return horas * tarifa  # Cálculo principal
    except Exception:
        raise ValueError("Error inesperado al calcular el pago.")

# ________________________________________
# ✅ Modelo 3 – Ejemplo 1: Función que devuelve un dict estructurado
# ________________________________________
# 1️ - Archivo: main.py
from fastapi import FastAPI
from routes import resumen
app = FastAPI()
app.include_router(resumen.router)
# ________________________________________
# 2️ - Archivo: routes/resumen.py
from fastapi import APIRouter
generar_resumen_usuario
from services.resumen import generar_resumen_usuario
router = APIRouter()
@router.get("/resumen")
def ver_resumen(nombre: str, edad: int, activo: bool):
    resumen = generar_resumen_usuario(nombre, edad, activo)
    return resumen  
# ________________________________________
# 3️ - Archivo: services/resumen.py
def generar_resumen_usuario(nombre: str, edad: int, activo: bool) -> dict:
    return {
        "usuario": nombre.title(),
        "edad": edad,
        "estado": "activo" if activo else "inactivo",  # Ver abajo
        "mayor_de_edad": edad >= 18
        }

# ________________________________________
# ✅ Modelo 3 – Ejemplo 2: Uso de tuple para devolver múltiples valores
1️ - Archivo: main.py
from fastapi import FastAPI
from routes import estadisticas
app = FastAPI()
app.include_router(estadisticas.router)
# ________________________________________
# 2️ - Archivo: routes/estadisticas.py
from fastapi import APIRouter
from services.estadisticas import calcular_promedio_y_maximo
router = APIRouter()
@router.get("/estadisticas")
def ver_estadisticas(a: float, b: float, c: float):
    promedio, maximo = calcular_promedio_y_maximo(a, b, c) # DESEMPAQUETAMOS la tupla en dos variables
    return {"promedio": promedio, "maximo": maximo}
# ________________________________________
# 3️ - Archivo: services/estadisticas.py
def calcular_promedio_y_maximo(a: float, b: float, c: float) -> tuple:
    promedio = (a + b + c) / 3
    maximo = max(a, b, c)
    return promedio, maximo  # Esto devuelve una tupla automáticamente

# ________________________________________
# ✅ Modelo 3 – Ejemplo 3: Uso de set para eliminar duplicados
# ________________________________________
from fastapi import FastAPI
from routes import limpieza
app = FastAPI()
app.include_router(limpieza.router)
# ________________________________________
# 2️ - Archivo: routes/limpieza.py
from fastapi import APIRouter
from services.limpieza import eliminar_duplicados
router = APIRouter()
@router.get("/limpiar")
def limpiar(datos: str):
    lista = datos.split(",")
    resultado = eliminar_duplicados(lista)  # Limpiamos duplicados usando set
    return {"resultado": resultado}
# ________________________________________
# 3️ - Archivo: services/limpieza.py
def eliminar_duplicados(lista: list) -> list:
    return list(set(lista)) 

# ________________________________________
# ✅ Modelo 3 extendido – Ejemplo 1: Uso de .split() y .join() para limpiar y normalizar texto
# ________________________________________
# 1️ - Archivo: main.py
from fastapi import FastAPI
from routes import texto
app = FastAPI()
app.include_router(texto.router)
# ________________________________________
# 2️ - Archivo: routes/texto.py
from fastapi import APIRouter
from services.texto import normalizar_cadena
router = APIRouter()
@router.get("/normalizar")
def procesar_cadena(cadena: str):
    resultado = normalizar_cadena(cadena)
    return {"resultado": resultado}
# ________________________________________
# 3️ - Archivo: services/texto.py
def normalizar_cadena(cadena: str) -> str:
    partes = cadena.split(",")  # Separar en partes por coma
    partes_limpias = [p.strip().title() for p in partes] 
    return ", ".join(partes_limpias) 

________________________________________
✅ Modelo 3 extendido – Ejemplo 2: Uso de .append() para construir listas dinámicas
Función real que acumula elementos según condición y devuelve la lista final
Este patrón es clave cuando necesitas:
•	Recorrer datos recibidos
•	Filtrar o seleccionar algunos
•	Acumularlos dinámicamente en una lista
•	Devolver esa lista limpia y filtrada al frontend o para otro uso
Este tipo de función se utiliza para construir listas de elementos válidos, disponibles, aprobados, encontrados, etc.
Estructura completa real (simplificada para entenderla)
________________________________________
1️ - Archivo: main.py
from fastapi import FastAPI

# De la carpeta routes, importamos el fichero 'seleccion'
from routes import seleccion

# Creamos la instancia principal del backend
app = FastAPI()

# Conectamos el router externo (seleccion) a la app principal
app.include_router(seleccion.router)

________________________________________
2️ - Archivo: routes/seleccion.py
from fastapi import APIRouter

# Desde carpeta services, archivo 'seleccion.py' importamos la función de lógica pura: seleccionar_pares
from services.seleccion import seleccionar_pares

# Creamos un router específico para rutas relacionadas con selección y filtros
router = APIRouter()

# Definimos el endpoint /pares con método GET
@router.get("/pares")
# Esta función recibe una cadena con números separados por comas, los transforma en enteros
# y los pasa a la función que selecciona los pares
def ver_pares(numeros: str):
    lista = [int(n) for n in numeros.split(",")]  # Convertimos string a lista de enteros
    resultado = seleccionar_pares(lista)
    return {"pares": resultado}

________________________________________
3️ - Archivo: services/seleccion.py
# Función lógica que selecciona solo los números pares de una lista
def seleccionar_pares(numeros: list) -> list:
    pares = []  # Lista vacía donde iremos acumulando
    for n in numeros:
        if n % 2 == 0:
            pares.append(n)  # Añadimos solo si es par
    return pares  # Devolvemos la lista final

________________________________________
🌐 ¿Cómo se prueba esto?
Estructura de carpetas:
mi_backend/
│
├── main.py
├── routes/
│   └── seleccion.py
└── services/
    └── seleccion.py
Ejecutar el backend:
uvicorn main:app --reload
Probar desde el navegador:
http://localhost:8000/pares?numeros=1,2,3,4,5,6,7,8,9
Resultado esperado:
{"pares": [2, 4, 6, 8]}
________________________________________
✅ Modelo 3 extendido – Ejemplo 3: Uso de .replace() para corrección y limpieza de texto
Función real que corrige términos comunes antes de guardar un string en base de datos
El método .replace() es esencial cuando:
•	Quieres reemplazar palabras, símbolos o errores en una cadena.
•	Necesitas normalizar datos que vienen con variaciones (por ejemplo, "ñ" por "n", quitar tildes, limpiar caracteres raros, corregir errores de tipeo, etc.).
Estructura completa real (simplificada para entenderla)
________________________________________
1️ - Archivo: main.py
from fastapi import FastAPI

# De la carpeta routes, importamos el fichero 'correccion'
from routes import correccion

# Creamos la instancia principal de la aplicación backend
app = FastAPI()

# Conectamos el router externo (correccion) a la app principal
app.include_router(correccion.router)

________________________________________
2️ - Archivo: routes/correccion.py
from fastapi import APIRouter

# Desde carpeta services, archivo 'correccion.py' importamos la función de lógica pura: corregir_texto
from services.correccion import corregir_texto

# Creamos un router específico para rutas relacionadas con correcciones o limpieza de cadenas
router = APIRouter()

# Definimos el endpoint /corregir con método GET
@router.get("/corregir")
# Esta función recibe un texto por URL y lo pasa a la función de corrección
def ver_correccion(texto: str):
    resultado = corregir_texto(texto)
    return {"corregido": resultado}

________________________________________
3️ - Archivo: services/correccion.py
# Función lógica que corrige palabras mal escritas o inconsistentes
def corregir_texto(texto: str) -> str:
    texto = texto.replace("qeu", "que")          # Corrige errores comunes
    texto = texto.replace("xq", "porque")        # Cambia abreviaturas por versión completa
    texto = texto.replace("bn", "bien")          # Corrige lenguaje informal
    return texto

________________________________________
🌐 ¿Cómo se prueba esto?
Estructura de carpetas:
mi_backend/
│
├── main.py
├── routes/
│   └── correccion.py
└── services/
    └── correccion.py
Ejecutar el backend:
uvicorn main:app --reload
Probar desde el navegador:
http://localhost:8000/corregir?texto=hola qeu tal estas bn? xq no viniste
Resultado esperado:
{"corregido": "hola que tal estas bien? porque no viniste"}
________________________________________
✅ Modelo 3 extendido – Ejemplo 4: Uso de .items() para recorrer diccionarios
Función real que analiza un diccionario recibido y genera un resumen basado en sus claves y valores
En backend, muchas veces recibes diccionarios dinámicos (por ejemplo, de configuraciones, preferencias, filtros, etc.) y necesitas:
•	Recorrer todas sus claves y valores
•	Tomar decisiones en función de su contenido
•	Devolver algún resumen o validación
.items() es la herramienta que te permite recorrer clave y valor a la vez, sin complicarte.
Estructura completa real (simplificada para entenderla)
________________________________________
1️ - Archivo: main.py
from fastapi import FastAPI

# De la carpeta routes, importamos el fichero 'analisis'
from routes import analisis

# Creamos la instancia principal del backend
app = FastAPI()

# Conectamos el router externo (analisis) a la app principal
app.include_router(analisis.router)

________________________________________
2️ - Archivo: routes/analisis.py
from fastapi import APIRouter
from typing import Dict

# Desde carpeta services, archivo 'analisis.py' importamos la función de lógica pura: analizar_configuracion
from services.analisis import analizar_configuracion

# Creamos un router específico para rutas relacionadas con análisis de datos
router = APIRouter()

# Definimos el endpoint /analizar con método GET (aunque en la práctica esto suele ser POST)
@router.get("/analizar")
# Esta función recibe parámetros dinámicos como diccionario desde la URL (simulado aquí)
def ver_analisis(usuario: str, activo: bool = True, admin: bool = False):
    config = {
        "usuario": usuario,
        "activo": activo,
        "admin": admin
    }
    resultado = analizar_configuracion(config)
    return {"resumen": resultado}

________________________________________
3️ - Archivo: services/analisis.py
# Función lógica que recorre un diccionario y construye frases sobre cada clave-valor
def analizar_configuracion(config: dict) -> list:
    resumen = []  # Lista de frases resumen
    for clave, valor in config.items():  # Recorremos clave y valor a la vez
        frase = f"La opción '{clave}' tiene el valor: {valor}"
        resumen.append(frase)
    return resumen

________________________________________
🌐 ¿Cómo se prueba esto?
Estructura de carpetas:
mi_backend/
│
├── main.py
├── routes/
│   └── analisis.py
└── services/
    └── analisis.py
Ejecutar el backend:
uvicorn main:app --reload
Probar desde el navegador:
http://localhost:8000/analizar?usuario=guillermo&activo=true&admin=false
Resultado esperado:
{
  "resumen": [
    "La opción 'usuario' tiene el valor: guillermo",
    "La opción 'activo' tiene el valor: True",
    "La opción 'admin' tiene el valor: False"
  ]
}

________________________________________
✅ Modelo 3 extendido – Ejemplo 5: Función compacta que limpia, corrige y selecciona términos (retorna a ejemplos 1, 2 y 3)
Procesa una cadena separada por comas: la divide, corrige errores comunes, filtra lo deseado y devuelve una lista limpia
Escenario típico: recibes una lista de palabras separadas por comas, donde:
•	Algunas están mal escritas
•	Hay duplicados
•	Y solo te interesa guardar las que estén permitidas
Estructura completa real (simplificada para entenderla)
________________________________________
1️ - Archivo: main.py
from fastapi import FastAPI

# De la carpeta routes, importamos el fichero 'palabras'
from routes import palabras

# Creamos la instancia principal de la aplicación backend
app = FastAPI()

# Conectamos el router externo (palabras) a la app principal
app.include_router(palabras.router)

________________________________________
2️ - Archivo: routes/palabras.py
from fastapi import APIRouter

# Desde carpeta services, archivo 'palabras.py' importamos la función de lógica pura: procesar_palabras
from services.palabras import procesar_palabras

# Creamos un router para trabajar con listas de palabras o etiquetas
router = APIRouter()

# Definimos el endpoint /procesar con método GET
@router.get("/procesar")
# Esta función recibe una cadena desde la URL y la pasa a la función de procesamiento completo
def ver_palabras(cadena: str):
    resultado = procesar_palabras(cadena)
    return {"resultado": resultado}

________________________________________
3️ - Archivo: services/palabras.py
# Función lógica que procesa una lista de palabras separadas por comas:
# - las limpia de espacios
# - corrige errores comunes
# - filtra solo las palabras permitidas
# - y elimina duplicados
def procesar_palabras(cadena: str) -> list:
    permitidas = {"python", "backend", "api", "fastapi"}  # Palabras que sí aceptamos
    resultado = []

    for palabra in cadena.split(","):  # Dividimos en partes
        palabra = palabra.strip().lower() # Quitamos espacios y pasamos a minúscula
        palabra = palabra.replace("pyton", "python") # Corregimos errores comunes
        palabra = palabra.replace("fast apy", "fastapi")

        if palabra in permitidas and palabra not in resultado:
            resultado.append(palabra)  # Añadimos solo si es válida y no está repetida

    return resultado

________________________________________
🌐 ¿Cómo se prueba esto?
Estructura de carpetas:
mi_backend/
│
├── main.py
├── routes/
│   └── palabras.py
└── services/
    └── palabras.py
Ejecutar el backend:
uvicorn main:app --reload
Probar desde el navegador:
http://localhost:8000/procesar?cadena=pyton,  api ,fast apy, backend, api,   api
Resultado esperado:
{"resultado": ["python", "api", "fastapi", "backend"]}
________________________________________
✅ ¿Qué aprendes con este ejemplo?
Método	Qué hace en backend real
.split()	Divide texto recibido desde el frontend
.replace()	Corrige errores típicos o inconsistencias
.strip()	Elimina espacios que generan errores o desprolijidad
.append()	Acumula elementos válidos según una regla
if in ...	Filtra valores deseados (control de calidad o seguridad)
not in ...	Evita duplicados sin necesidad de usar set

________________________________________
✅ Modelo 4 – Función con parámetros opcionales (Optional)
Ejemplo 1: Función que adapta su comportamiento según reciba o no un parámetro
Tienes una función que puede saludar a un usuario.
•	Si se le pasa un nombre, lo usa.
•	Si no se le pasa nada, devuelve un saludo genérico.
Esto es muy común en APIs, formularios y configuraciones donde los valores pueden o no estar presentes.
Este patrón es altamente usado en endpoints donde:
•	No todos los parámetros son obligatorios
•	Se devuelven respuestas adaptadas
•	Se simplifica la lógica sin errores
________________________________________
📁 Archivo: services/saludo.py
from typing import Optional

# Función que devuelve un saludo adaptado, usando un parámetro opcional
def saludar(nombre: Optional[str] = None) -> str:
    if nombre:
        return f"Hola, {nombre.capitalize()} 👋"
    else:
        return "Hola, visitante 👋"

________________________________________
Prueba directa desde consola o script
📁 Archivo: pruebas_saludo.py
from services.saludo import saludar

print(saludar("guillermo"))  # Hola, Guillermo 👋
print(saludar())             # Hola, visitante 👋

________________________________________
🖨️ Resultado esperado
Hola, Guillermo 👋
Hola, visitante 👋
________________________________________
✅ ¿Qué aprendiste aquí?
Elemento	Función real en backend moderno
Optional[str]	Indica que el parámetro puede ser str o None
nombre: Optional[str] = None	Parámetro opcional, con valor por defecto si no se pasa
if nombre:	Verificación de presencia del valor
Comportamiento adaptable	Función responde diferente si se pasa o no se pasa el argumento

________________________________________
✅ Modelo 4 – Ejemplo 2: Función que recibe múltiples parámetros, algunos opcionales
Función profesional que permite lógica flexible según la cantidad de datos disponibles
Imagina una función que calcula el precio total de un producto:
•	Siempre requiere precio_base.
•	Puede sumar el IVA si se proporciona.
•	Y puede aplicar un descuento si también se proporciona.
Esto es típico de funciones reales en lógica de negocios, donde no siempre se reciben todos los datos.
Este patrón es altamente usado en APIs financieras, precios dinámicos, configuraciones opcionales y reglas de negocio adaptables.
________________________________________
📁 Archivo: services/facturacion.py
from typing import Optional

# Función que calcula el total, con IVA y descuento como opcionales
def calcular_total(precio_base: float, iva: Optional[float] = None, descuento: Optional[float] = None) -> float:
    total = precio_base

    if iva is not None:
        total += precio_base * (iva / 100)

    if descuento is not None:
        total -= total * (descuento / 100)

    return round(total, 2)

________________________________________
Prueba desde script
📁 Archivo: pruebas_facturacion.py
from services.facturacion import calcular_total

print(calcular_total(100))                    # Solo precio base → 100.0
print(calcular_total(100, iva=21))            # Con IVA → 121.0
print(calcular_total(100, descuento=10))      # Con descuento → 90.0
print(calcular_total(100, iva=21, descuento=10))  # Con ambos → 108.9

________________________________________
🖨️ Resultado esperado
100.0
121.0
90.0
108.9
________________________________________
✅ ¿Qué aprendes aquí?
Elemento	Aplicación real
Varios parámetros opcionales	Permite adaptarse a la lógica del negocio según los datos recibidos
Optional[float] = None	Señala que ese parámetro puede no estar presente
if descuento is not None	Es mejor que if descuento: cuando puede ser 0
round(total, 2)	Devolvemos un valor limpio para respuestas financieras
________________________________________

________________________________________
✅ Modelo 4 – Ejemplo 3: Función que recibe un dict opcional con configuración extra
Función profesional que usa un diccionario opcional para aplicar configuraciones extendidas
Imagina que tienes una función para generar un mensaje personalizado.
•	El nombre del usuario siempre se recibe.
•	Pero puedes pasarle un diccionario opcional con “configuraciones extra” como:
o	si se quiere usar mayúsculas
o	si se quiere añadir un emoji
o	si se quiere mostrar el saludo en versión “formal”
Este patrón es muy común en funciones reutilizables y con comportamiento flexible.
Este patrón es muy usado en backend para configuración de filtros, opciones, banderas, permisos o ajustes extra en funciones.
________________________________________
📁 Archivo: services/mensaje.py
from typing import Optional

# Función que devuelve un saludo personalizado con configuración extra opcional
def generar_mensaje(nombre: str, config: Optional[dict] = None) -> str:
    mensaje = f"Hola, {nombre}"

    if config:
        if config.get("mayusculas"):
            mensaje = mensaje.upper()

        if config.get("formal"):
            mensaje = f"Estimado/a {nombre}"

        if config.get("emoji"):
            mensaje += " 😊"

    return mensaje

________________________________________
Prueba desde script
📁 Archivo: pruebas_mensaje.py
from services.mensaje import generar_mensaje

print(generar_mensaje("Guillermo"))  # Sin config → Hola, Guillermo

print(generar_mensaje("Paola", config={
    "emoji": True
}))  # → Hola, Paola 😊

print(generar_mensaje("Sofía", config={
    "mayusculas": True,
    "emoji": True
}))  # → HOLA, SOFÍA 😊

print(generar_mensaje("Luis", config={
    "formal": True
}))  # → Estimado/a Luis

________________________________________
🖨️ Resultado esperado
Hola, Guillermo
Hola, Paola 😊
HOLA, SOFÍA 😊
Estimado/a Luis

________________________________________
✅ ¿Qué aprendes con este ejemplo?
Elemento	Aplicación en backend real
Optional[dict] = None	Se puede pasar o no una config adicional
config.get("clave")	Accede a cada opción sin lanzar error si no está
Diccionario como parámetro	Permite pasar muchas configuraciones sin usar muchos argumentos
Lógica condicional interna	La función se adapta elegantemente según los valores del dict
________________________________________
________________________________________
✅ Modelo 5 – Función como servicio lógico (capa intermedia)
Función que no es el controlador final ni la función pura, sino una capa que organiza y conecta pasos intermedios
¿Qué es una “capa intermedia”?
Es una función que:
•	Coordina varios pasos o funciones internas.
•	Organiza la lógica antes de llegar al controlador o endpoint.
•	Se usa para orquestar, validar o transformar datos sin mostrar nada al usuario directamente.
Este tipo de funciones se suele ubicar en carpetas como services/, logic/ o usecases/.
Este patrón se usa a diario en la lógica de negocio de servicios web. No muestra nada en pantalla, pero organiza y decide lo que el backend debe hacer.
________________________________________
✅ Ejemplo 1 – Función intermedia que procesa datos de usuario y calcula su acceso
________________________________________
📁 Archivo: services/autorizacion.py
# Función que decide si un usuario puede acceder, combinando dos funciones internas

def verificar_autorizacion(usuario: dict) -> dict:
    nombre = normalizar_nombre(usuario.get("nombre"))
    acceso = tiene_acceso(usuario.get("rol"))

    return {
        "nombre_normalizado": nombre,
        "puede_acceder": acceso
    }

# Función lógica interna 1
def normalizar_nombre(nombre: str) -> str:
    return nombre.strip().capitalize()

# Función lógica interna 2
def tiene_acceso(rol: str) -> bool:
    return rol in ["admin", "editor"]

________________________________________
Prueba desde script
📁 Archivo: pruebas_autorizacion.py
from services.autorizacion import verificar_autorizacion

usuario1 = {"nombre": " guillermo ", "rol": "admin"}
usuario2 = {"nombre": "paola", "rol": "invitado"}

print(verificar_autorizacion(usuario1))
print(verificar_autorizacion(usuario2))

________________________________________
🖨️ Resultado esperado:
{'nombre_normalizado': 'Guillermo', 'puede_acceder': True}
{'nombre_normalizado': 'Paola', 'puede_acceder': False}

________________________________________
✅ ¿Qué aprendes con este ejemplo?
Elemento	Aplicación real
Función intermedia (verificar_...)	Orquesta varias funciones internas (limpieza + decisión lógica)
Funciones internas pequeñas	Delegan responsabilidades concretas (SRP – principio de responsabilidad única)
Dict de entrada + dict de salida	Forma estándar de pasar y devolver datos entre capas del backend
________________________________________
¡Vamos, Guillermo! Este ejemplo te va a mostrar cómo una función intermedia prepara datos antes de guardarlos — algo que verás TODO el tiempo en backend.
________________________________________
✅ Modelo 5 – Ejemplo 2: Función intermedia que limpia y transforma datos antes de guardar
Ideal para preparar datos antes de pasarlos a una función de guardado o acceso a base de datos
Recibes datos crudos desde un formulario, un frontend o una API externa.
👉 Antes de guardarlos en una base de datos, necesitas:
•	Limpiar los campos
•	Validar la edad
•	Transformar el nombre
•	Estandarizar el email
•	Y devolver un dict listo para guardar
Este tipo de función intermedia es usada TODO EL TIEMPO en servicios (services/), y evita que el código de base de datos o el endpoint se ensucie con lógica dispersa.
________________________________________
📁 Archivo: services/preparador.py
from typing import Optional

# Función intermedia que transforma un diccionario de datos crudos en datos listos para guardar
def preparar_usuario(datos: dict) -> dict:
    nombre = limpiar_nombre(datos.get("nombre"))
    email = estandarizar_email(datos.get("email"))
    edad = validar_edad(datos.get("edad"))

    return {
        "nombre": nombre,
        "email": email,
        "edad": edad
    }

# Función interna: capitaliza y quita espacios
def limpiar_nombre(nombre: str) -> str:
    return nombre.strip().title()

# Función interna: pasa todo a minúsculas
def estandarizar_email(email: str) -> str:
    return email.strip().lower()

# Función interna: si la edad no está, se pone en None, si está, se convierte en int
def validar_edad(edad: Optional[str]) -> Optional[int]:
    if edad is None:
        return None
    return int(edad)

________________________________________
Prueba desde script
📁 Archivo: pruebas_preparador.py
from services.preparador import preparar_usuario

datos_crudos = {
    "nombre": "  guillermo   ",
    "email": "Guillermo@GMAIL.com  ",
    "edad": "51"
}

print(preparar_usuario(datos_crudos))

________________________________________
🖨️ Resultado esperado:
{
  "nombre": "Guillermo",
  "email": "guillermo@gmail.com",
  "edad": 51
}

________________________________________
✅ ¿Qué aprendes con este ejemplo?
Elemento	Aplicación real
Función intermedia (preparar_...)	Orquesta limpieza, validación y transformación antes de guardar
Entrada tipo dict	Representa datos recibidos sin procesar (lo más común en formularios)
Salida tipo dict	Datos listos para pasar a repositorios, ORMs, o queries
Separación por funciones internas	Limpieza, validación y lógica están claramente separadas
________________________________________

¡Perfecto, Guillermo! Este tercer ejemplo te muestra una función intermedia muy profesional: actúa como "traductor" entre formatos, algo súper común cuando tu backend:
•	Recibe datos en un formato
•	Debe transformarlos antes de enviarlos a otro sistema, microservicio, API o base de datos
________________________________________
✅ Modelo 5 – Ejemplo 3: Función intermedia que traduce formatos entre dos sistemas
Ideal para APIs, integraciones externas y microservicios que necesitan convertir estructuras
Escenario real
Supón que tu backend recibe un usuario con este formato:
{
  "nombre_completo": "Guillermo Abraham",
  "pais": "ES",
  "es_activo": true
}

Pero el sistema de terceros (o tu propia base de datos) espera este formato:
{
  "nombre": "Guillermo",
  "apellido": "Abraham",
  "codigo_pais": "+34",
  "estado": "activo"
}

👉 Tu función intermedia se encarga de hacer esa conversión limpia y ordenada.
Este patrón es muy usado en proyectos reales con microservicios, integración de terceros, APIs REST o cambios entre modelos internos y externos.
________________________________________
📁 Archivo: services/traductor.py
# Diccionario de países para convertir códigos a prefijos internacionales
PREFIJOS = {
    "ES": "+34",
    "AR": "+54",
    "MX": "+52",
    "CO": "+57"
}

# Función intermedia que traduce el formato de usuario
def traducir_usuario(origen: dict) -> dict:
    nombre, apellido = origen["nombre_completo"].split(" ", 1)  # Separamos en 2 partes
    codigo_pais = PREFIJOS.get(origen["pais"], "+00")  # Prefijo por país, o +00 por defecto
    estado = "activo" if origen["es_activo"] else "inactivo"  # Traducción de booleano

    return {
        "nombre": nombre,
        "apellido": apellido,
        "codigo_pais": codigo_pais,
        "estado": estado
    }

________________________________________
Prueba desde script
📁 Archivo: pruebas_traductor.py
from services.traductor import traducir_usuario

entrada = {
    "nombre_completo": "Guillermo Abraham",
    "pais": "ES",
    "es_activo": True
}

print(traducir_usuario(entrada))

________________________________________
🖨️ Resultado esperado:
{
  "nombre": "Guillermo",
  "apellido": "Abraham",
  "codigo_pais": "+34",
  "estado": "activo"
}

________________________________________
✅ ¿Qué aprendes aquí?
Elemento	Aplicación real
Función intermedia de traducción	Convierte estructura A en estructura B
.split(" ", 1)	Separa nombre completo en dos partes
.get(clave, valor_por_defecto)	Evita errores al acceder a claves que pueden no estar
if bool: valor1 else valor2	Traducción directa de booleanos
________________________________________

________________________________________
✅ Modelo 6 – Ejemplo 1: Función que valida campos y lanza ValueError si no se cumplen condiciones
Este patrón se usa todo el tiempo para proteger tu backend de datos erróneos, malformados o peligrosos
Escenario real
Estás validando datos antes de guardarlos, procesarlos o enviarlos a otro sistema.
Si los datos no cumplen una regla mínima, debes:
•	Cortar la ejecución
•	Lanzar un error claro
•	Evitar que el backend trabaje con información errónea
Este tipo de función se coloca antes de cualquier proceso sensible: creación de usuarios, validación de inputs, confirmación de datos, etc.
________________________________________
📁 Archivo: services/validador.py
# Función que valida datos obligatorios y lanza errores si hay problemas
def validar_usuario(nombre: str, edad: int):
    if not nombre.strip():
        raise ValueError("El nombre no puede estar vacío")
    
    if edad < 0 or edad > 120:
        raise ValueError("La edad debe estar entre 0 y 120")

    return f"Usuario válido: {nombre} ({edad} años)"

________________________________________
Prueba desde script
📁 Archivo: pruebas_validador.py
from services.validador import validar_usuario

# ✅ Caso válido
print(validar_usuario("Guillermo", 51))

# ❌ Casos con error
print(validar_usuario("   ", 25))       # Nombre vacío
print(validar_usuario("Paola", 140))    # Edad fuera de rango

________________________________________
🖨️ Resultado esperado:
Usuario válido: Guillermo (51 años)
Traceback (most recent call last):
...
ValueError: El nombre no puede estar vacío
...
ValueError: La edad debe estar entre 0 y 120

________________________________________
✅ ¿Qué aprendes aquí?
Técnica	Uso real en backend
raise ValueError(...)	Lanza un error cuando algo está mal
Validación mínima de campos	Se usa antes de guardar, calcular, o pasar datos
Cortar el flujo con error claro	Impide que el sistema continúe con datos corruptos o inválidos
Mensajes personalizados	Sirven para mostrar en logs o respuestas de API


________________________________________
✅ Modelo 6 – Ejemplo 2: Validación combinada de múltiples campos con múltiples raise
Usado en formularios, registros de usuario, configuración y cualquier lógica que exija condiciones mínimas
Escenario real
Estás recibiendo un dict con datos de registro de un usuario, y quieres asegurarte de:
•	Que todos los campos obligatorios estén presentes
•	Que tengan valores aceptables
•	Y que los errores sean claros y específicos
Este patrón es el más usado para validaciones previas a crear registros, enviar datos a otros sistemas, o controlar inputs en APIs REST.
________________________________________
📁 Archivo: services/validacion_registro.py
# Función que valida un dict con datos y lanza errores si hay problemas
def validar_registro(data: dict) -> None:
    if "nombre" not in data or not data["nombre"].strip():
        raise ValueError("El campo 'nombre' es obligatorio y no puede estar vacío")

    if "email" not in data or "@" not in data["email"]:
        raise ValueError("El campo 'email' es obligatorio y debe contener un '@'")

    if "edad" not in data:
        raise ValueError("El campo 'edad' es obligatorio")
    
    edad = data["edad"]
    if not isinstance(edad, int):
        raise ValueError("El campo 'edad' debe ser un número entero")
    
    if edad < 18:
        raise ValueError("Debes ser mayor de edad para registrarte")

________________________________________
Prueba desde script
📁 Archivo: pruebas_validacion.py
from services.validacion_registro import validar_registro

# ✅ Usuario correcto
usuario_valido = {
    "nombre": "Guillermo",
    "email": "guille@gmail.com",
    "edad": 51
}

# ❌ Usuario con errores
usuario_con_errores = {
    "nombre": "  ",
    "email": "correo_invalido",
    "edad": "dieciocho"
}

# Validación correcta
validar_registro(usuario_valido)

# Validación con errores múltiples (se detendrá en el primero que encuentre)
validar_registro(usuario_con_errores)

________________________________________
🖨️ Resultado esperado:
Traceback (most recent call last):
...
ValueError: El campo 'nombre' es obligatorio y no puede estar vacío
(Se detiene en el primer error. Si arreglas ese y vuelves a probar, verás los demás)
________________________________________
✅ ¿Qué aprendes aquí?
Técnica	Aplicación real
raise ValueError(...) múltiples	Permite validar cada campo por separado y dar errores personalizados
Validación exhaustiva de dict	Muy común en endpoints que reciben JSON
isinstance(valor, tipo)	Útil para confirmar tipos esperados (como int, str, etc.)
Cortar el flujo en validaciones	Evita errores en cascada más costosos
________________________________________

________________________________________
7) ✅ Funciones con *args y **kwargs

¿Para qué sirve cada uno?
Elemento	¿Qué permite hacer?	Uso real en backend
*args	Recibe múltiples valores posicionales en forma de tupla	Muy poco usado salvo en wrappers
**kwargs	Recibe múltiples valores nombrados en forma de diccionario	Sí se usa para pasar parámetros flexibles, sobre todo en validaciones, construcción dinámica o reenvío de datos

✅ ¿Cuál se usa realmente en backend?
En backend profesional moderno:
•	*args se usa rara vez (casi siempre reemplazado por listas bien estructuradas).
•	**kwargs sí se usa, especialmente en funciones que reciben muchos parámetros opcionales, configuraciones o argumentos dinámicos.
________________________________________
✅ Ejemplo 1: uso de **kwargs para validación dinámica y flexible
Este patrón se usa en validadores internos, adaptadores, parsers, construcción de objetos y funciones con configuraciones variables.

📁 Archivo: services/validacion_dinamica.py
# Función que recibe cualquier cantidad de campos y valida que no haya valores vacíos
def validar_campos_obligatorios(**kwargs):
    for campo, valor in kwargs.items():
        if not valor:
            raise ValueError(f"El campo '{campo}' es obligatorio y no puede estar vacío")

    return "Todos los campos están correctamente completos"

________________________________________
Prueba desde script
📁 Archivo: pruebas_kwargs.py
from services.validacion_dinamica import validar_campos_obligatorios

# ✅ Todos los campos correctos
print(validar_campos_obligatorios(nombre="Guillermo", email="guille@gmail.com", rol="admin"))

# ❌ Falta un campo
print(validar_campos_obligatorios(nombre="", email="paola@gmail.com", rol=""))

________________________________________
🖨️ Resultado esperado:
Todos los campos están correctamente completos

Traceback (most recent call last):
...
ValueError: El campo 'nombre' es obligatorio y no puede estar vacío

________________________________________
✅ ¿Qué aprendiste aquí?
Técnica	Aplicación real
**kwargs	Acepta cualquier cantidad de argumentos nombrados
.items() en kwargs	Recorre campo y valor dinámicamente
raise personalizado por campo	Permite validar sin repetir código para cada parámetro
Uso flexible	Función adaptable a distintos contextos o inputs dinámicos
________________________________________

________________________________________
✅ Ejemplo 2: *args, **kwargs aplicados uso más habitual en decoradores personalizados o funciones utilitarias
________________________________________
📁 Archivo: services/wrappers.py
# Decorador que imprime información sobre la llamada a una función
def loggear_llamada(func):
    def wrapper(*args, **kwargs):
        print(f"🔍 Llamando a: {func.__name__} con args={args}, kwargs={kwargs}")
        return func(*args, **kwargs)
    return wrapper

________________________________________
📁 Archivo: services/usuarios.py
from services.wrappers import loggear_llamada

@loggear_llamada
def registrar_usuario(nombre: str, edad: int):
    return {"status": "ok", "usuario": nombre}

________________________________________
Prueba rápida
from services.usuarios import registrar_usuario

registrar_usuario("Guillermo", 51)

________________________________________
🖨️ Resultado esperado:
🔍 Llamando a: registrar_usuario con args=('Guillermo', 51), kwargs={}
{'status': 'ok', 'usuario': 'Guillermo'}


________________________________________
✅ Modelo 8 – Ejemplo 1: Decorador personalizado para autorización con token
Este patrón se usa en backends que necesitan añadir filtros de seguridad, logging o condiciones antes de ejecutar funciones
Este patrón es una base profesional para crear middlewares caseros, validaciones transversales o protecciones antes de ejecutar lógica sensible.
Este es el único patrón de decorador personalizado que necesitás dominar al 100% en backend moderno si no estás usando un framework con middleware avanzado.
Escenario real
Tienes funciones que acceden a recursos sensibles (como datos, archivos o acciones internas).
👉 Solo deben ejecutarse si el usuario tiene un token válido.
Para no repetir la misma verificación en todas las funciones, se crea un decorador que:
•	Verifica si el token recibido es correcto
•	Corta el flujo con un error si no lo es
•	Permite la ejecución si el token es válido
________________________________________
📁 Archivo: services/autenticacion.py
# Decorador personalizado que verifica si se pasa un token válido
def requiere_token(func):
    def wrapper(*args, **kwargs):
        if not kwargs.get("token") == "secreto123":
            raise PermissionError("❌ Token inválido")
        return func(*args, **kwargs)
    return wrapper

________________________________________
📁 Archivo: services/recursos.py
from services.autenticacion import requiere_token

# Aplicamos el decorador a una función que solo debe ejecutarse con token correcto
@requiere_token
def acceder_recurso(data: str, token: str):
    return f"✅ Acceso concedido al recurso: {data}"

________________________________________
Prueba directa desde script
📁 Archivo: pruebas_token.py
from services.recursos import acceder_recurso

# ✅ Llamada con token válido
print(acceder_recurso("información_confidencial", token="secreto123"))

# ❌ Llamada con token inválido
print(acceder_recurso("información_confidencial", token="otro_token"))

________________________________________
🖨️ Resultado esperado:
✅ Acceso concedido al recurso: información_confidencial

Traceback (most recent call last):
...
PermissionError: ❌ Token inválido

________________________________________
✅ ¿Qué aprendiste aquí?
Técnica	Aplicación real
@requiere_token	Aplica una capa de autorización antes de ejecutar funciones sensibles
kwargs.get("token")	Revisa parámetros sin forzar su presencia
raise PermissionError(...)	Lanza un error si no se cumple la condición de acceso
wrapper(*args, **kwargs)	Reenvía todos los argumentos originales a la función decorada
________________________________________



