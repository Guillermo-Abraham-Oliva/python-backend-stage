import json
import logging
from pathlib import Path

# Configuración típica de logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

BASE = Path("/home/guille/Mi_Repositorio_Git/python_2025/x__data_work_para_ejercicios")
nombre_archivo = "archivo_entrada.json"

def cargar_json(nombre_archivo: str) -> dict:
    ruta = BASE / nombre_archivo
    logging.info("Cargando archivo JSON desde: %s", ruta)

    try:
        with open(ruta, "r", encoding="utf-8") as f:
            data = json.load(f)
        logging.info("Archivo cargado correctamente")
        return data
    except FileNotFoundError:
        logging.error("Archivo no encontrado en: %s", ruta)
        return {}
    except json.JSONDecodeError:
        logging.error("JSON inválido en: %s", ruta)
        return {}

def guardar_json(nombre_archivo: str, data: dict) -> None:
    ruta = BASE / nombre_archivo
    logging.info("Guardando archivo JSON en: %s", ruta)

    try:
        with open(ruta, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        logging.info("Archivo guardado correctamente")
    except Exception as e:
        logging.error("Error al guardar JSON: %s", e)

# PRUEBA
x = cargar_json(nombre_archivo)
guardar_json("archivo_salida.json", x)
