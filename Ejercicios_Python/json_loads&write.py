# aquí tienes el patrón “contratable”: 
# Path + manejo de errores específicos. 
# Es el caso más usado hoy para leer JSON en scripts/servicios backend serios. 
# Cubre ~80% de situaciones reales.

# Qué hace y por qué:
# Path: rutas portables y API cómoda (mkdir, read_text, etc.).

# Errores específicos:
# FileNotFoundError → el archivo no existe y corta.
# json.JSONDecodeError → el JSON está corrupto y también se corta.
# Fail fast: si los datos base están mal, no seguimos “como si nada”.

# Código base pro:

from __future__ import annotations
from pathlib import Path
import json
from typing import Any

BASE = Path(__file__).resolve().parent # carpeta donde está main.py
DATA = BASE / "data"                   # .../Ejerc_11/data
OUT = BASE / "salida"                  # .../Ejerc_11/salida

def cargar_json(ruta: Path) -> Any:
    """Lee JSON desde ruta y devuelve el objeto Python (list/dict). 
    Falla con mensaje claro si falta archivo o JSON está corrupto."""
    try:
        return json.loads(ruta.read_text(encoding="utf-8")) # jlrre (sigla para memorizar)
    except FileNotFoundError:
        raise SystemExit(f"[ERROR] No existe el archivo: {ruta}")
    except json.JSONDecodeError as e:
        raise SystemExit(f"[ERROR] JSON inválido en {ruta}: {e}")

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
    ruta.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

def main() -> None:
    # Crear carpeta 'salida' si no existe
    OUT.mkdir(parents=True, exist_ok=True)

    # Carga robusta (fail fast con mensajes claros)
    inv_lista = cargar_json(DATA / "inventario.json")
    upd_lista = cargar_json(DATA / "actualizacion.json")

    # Aquí iría tu pipeline (indexar → actualizar → normalizar → filtrar → ordenar)
    # ...
    catalogo_final = []  # placeholder del resultado final
    reporte = {}         # placeholder del reporte


    # Guardar salidas de forma limpia
    guardar_json(OUT / "catalogo_final.json", catalogo_final)
    # se le pasan 2 argumentos: 
    # 1) la ruta: carpeta OUT y fichero "catalogo_final.json"
    # 2) la 'data' (el catalogo_final)  

    guardar_json(OUT / "reporte.json", reporte)
    # idem al anterior


if __name__ == "__main__":
    main()

# Detalles que te colocan por encima del montón
# ruta.parent.mkdir(..., exist_ok=True) antes de escribir: 90% de juniors se olvida
# ensure_ascii=False, indent=2: salidas legibles y con tildes correctas
# Sin except Exception -> genérico

