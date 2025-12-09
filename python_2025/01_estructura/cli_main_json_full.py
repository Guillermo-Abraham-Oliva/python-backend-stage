# JSON (JavaScript Object Notation) es un formato de texto 
# para almacenar y transmitir datos en forma de diccionarios y listas

# ---BASICO----

import json

numeros = [2, 3, 5, 7, 11, 13]
filename = 'numeros.json'  # Aquí decido cómo se va a llamar el archivo
with open(filename, 'w') as f_obj:  # Abre (o crea) un archivo con ese nombre en modo escritura.
    json.dump(numeros, f_obj) # Convierte la lista de python a texto JSON


# ----- EJEMPLO NORMAL FULL -----

import json
from pathlib import Path

objeto = {
    "nombre": "Guillermo",
    "edad": 50,
    "ciudad": "Oropesa"}

OUT = Path("/home/guille/Mi_Repositorio_Git/Ejercicios_Python/PRUEBA/salida")
# OJO: "salida" es una carpeta por eso se usa parents=True, para crear todo el arbol de carpetas / si esto terminase con un archivo seria OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.mkdir(parents=True, exist_ok=True)

# Forma preferida en entornos Pro o con archivos grandes (80%):
with open(OUT / "datos.json", "w", encoding="utf-8") as archivo:
    json.dump(objeto, archivo, ensure_ascii=False, indent=2)

# Otra forma: SOLO para files pequeños, scripts simples, uso interno (20%):
# (OUT / "datos.json").write_text(json.dumps(objeto, ensure_ascii=False, indent=2), encoding="utf-8")


# ----Leer el archivo JSON ---------

# Leer el JSON desde el archivo
with open(OUT / "datos.json", "r") as archivo:
    datos_cargados = json.load(archivo)

print(datos_cargados)  # {'nombre': 'Guillermo', 'edad': 51, 'ciudad': 'Alicante'}
print(datos_cargados["nombre"])  # Guillermo



# ------------------MODELO FULL GLOBAL------------------------
👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇

# Path + manejo de errores específicos (except) 
# Fail fast: si los datos base están mal, no seguimos “como si nada”
# Es el caso más usado hoy para leer JSON en scripts/servicios backend serios. 
# Cubre 80% de situaciones reales

from __future__ import annotations
from pathlib import Path
import json
from typing import Any

BASE = Path(__file__).resolve().parent # carpeta donde está main.py
DATA = BASE / "data"                   # .../Ejerc_11/data
OUT = BASE / "salida"                  # .../Ejerc_11/salida

def cargar_json(ruta: Path) -> Any:
    try:
        with open(ruta, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError as e:
        raise SystemExit(f"[ERROR] JSON inválido en {ruta}: {e!r}")
    except FileNotFoundError:
        raise SystemExit(f"[ERROR] Archivo no encontrado: {ruta}")
    except PermissionError:
        raise SystemExit(f"[ERROR] Sin permisos para leer {ruta}")
    except Exception as e:
        raise SystemExit(f"[ERROR] Fallo inesperado al leer {ruta}: {e!r}")

    # opcion para cosas pequeñas (20%):
    #       return json.loads(ruta.read_text(encoding="utf-8")) -> jlrre (sigla para memorizar)


def guardar_json(ruta: Path, data: Any) -> None:
    # SI NO SABEMOS SI EXISTE UNA CARPETA EN LA QUE VAMOS A ESCRIBIR
    # ESTA LINEA ES UNA PREVIA A WRITE!:
    # ruta.parent -> directorio donde se guardará el archivo especificado en `ruta`
    # mkdir() -> crea el directorio 
    # parents=True: crea también directorios padres si no existen.
    # exist_ok=True: si la carpeta existe, no lanza error y continúa sin tocarla.
    # todo esto hace la linea siguiente:
    ruta.parent.mkdir(parents=True, exist_ok=True)

    # Sobre la ruta, escribir el json dumpeado de 'data', no asegurando ascii (para coservar tildes, ñ, etc.), indentando en 2 (para que se vea bonito), y codificando todo ello en utf-8
    # Síntesis: data -> json -> ruta
    with open(ruta, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    # Opcion solo usada 20%:
    ruta.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

def main() -> None:
    '''
        Estructura de éste main/CLI básico:

            1) Inicialización del Entorno (carpetas, configs)
            2) Cargar datos
            3) Pipeline
            4) Guardar resultados
    '''

    # 1) INICIALIZACIÓN DEL ENTORNO va al principio -> crear la carpeta de salida
    # mkdir -> Crear carpeta 'salida' 
    # parents=True -> y toda la cadena de directorios intermedios si no existen. Sin eso, solo intenta crear el último nivel y si falta un padre, crash    ¡¡¡¡¡¡¡¡¡¡ VER !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    # exist_ok=True -> si existe, no la crea y continúa sin error
    OUT.mkdir(parents=True, exist_ok=True)

    # 2) CARGAR DATOS (fail fast con mensajes claros)
    inv_lista = cargar_json(DATA / "inventario.json")
    upd_lista = cargar_json(DATA / "actualizacion.json")

    # Aquí iría el PIPELINE (indexar → actualizar → normalizar → filtrar → ordenar)
    # ...
    catalogo_final = []  # placeholder del resultado final
    reporte = {}         # placeholder del reporte


    # GUARDAR RESULTADOS
    guardar_json(OUT / "catalogo_final.json", catalogo_final)
    # se le pasan 2 argumentos: 
    # 1) la ruta: carpeta OUT y fichero "catalogo_final.json"
    # 2) la 'data' (el catalogo_final)  

    guardar_json(OUT / "reporte.json", reporte)
    # idem al anterior


if __name__ == "__main__":
    main()


'''
    Estructura main/CLI completa:

    1) Parseo
    2) Logging 
    3) Entorno env (crear solo OUT)
    4) Validar entradas (rutas/objeto)
    5) Cargar datos
    6) Pipeline (lógica pura de negocio)
    7) Guardar resultados

'''

# ¿ruta.mkdir o ruta.parent.mkdir?

# Si Path apunta a un archivo siempre HAY QUE CREAR SU CARPETA CONTENEDORA
# -> agregar parent al inicio -> path.parent.mkdir(...) 
# de lo contrario intentaría crear una carpeta con el nombre del archivo!:

# Si Path apunta a un archivo ➡️ path.parent 👇
path.parent.mkdir(parents=True, exist_ok=True) # agregar parent tras la ruta/archivo
# luego guardar con with open....

# Si Path apunta a una carpeta 📁 -> no colocamos ese 1º parent 👇
path.mkdir(parents=True, exist_ok=True)
# ¡Y NADA DE path.write_text() -> ¡NO escribir texto a una carpeta!

# y OJO... si tenemos:
path = Path("salida/catalogo.json") # "salida" es la carpeta... pero no la crea!
# por eso se necesita path.parent para crear LA CARPETA "salida"
path.parent.mkdir(parents=True, exist_ok=True)
path.write_text(json.dumps(x, ensure_ascii=False, indent=2))
# aqui si va write_text porque apunto a fichero


# parents=True -> crea todas las necesarias por arriba si no existen
# exist_ok=True -> Si al crear carpeta ya existe -> no fallo ni stop 

 

#   Definiciones:

#       path.parent -> Devuelve la ruta del directorio padre (no crea nada)

#       mkdir(parents=True) -> Crea la carpeta y todas las necesarias para llegar a ella

#       exist_ok=True -> No falla si ya existen


| Ejemplo                          | Qué es  | mkdir correcto           |
| -------------------------------- | ------- | ------------------------ |
| `Path("salida/catalogo.json")`   | archivo | `path.parent.mkdir(...)` |
| `Path("salida/reportes")`        | carpeta | `path.mkdir(...)`        |
| `Path("output/data/final.xlsx")` | archivo | `path.parent.mkdir(...)` |
| `Path("tmp/logs")`               | carpeta | `path.mkdir(...)`        |

