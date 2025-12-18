from pathlib import Path
from typing import Any
import json
import logging

log = logging.getLogger(__name__)

def cargar_json(ruta: Path) -> list[dict[str, Any]]:
    try:
        with open(ruta, "r", encoding="utf-8") as f:
            log.info("Carga de JSON desde: %s", ruta)
            return json.load(f)
    except FileNotFoundError:
        raise SystemExit(f"Archivo no encontrado en ruta {ruta}")
    except json.JSONDecodeError as e:
        raise SystemExit(f"Json inválido en {ruta}: {e!r}")
    except PermissionError:
        raise SystemExit(f"Sin permisos para leer en ruta: {ruta}")
    except Exception as e:
        raise SystemExit(f"Error desconocido en ruta {ruta}: {e!r}")

def guardar_resultados(ruta: Path, data: Any) -> None:
    ruta.parent.mkdir(parents=True, exist_ok=True)
    try:
        with open(ruta, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
            log.info("Guardado de JSON en: %s", ruta)
    except PermissionError:
        raise SystemExit(f"Sin permisos para escribir en {ruta}")
    except FileNotFoundError:
        raise SystemExit(f"Ruta inválida: {ruta}")
    except OSError as e:
        raise SystemExit(f"Error del sistema al escribir {ruta}: {e!r}")
    except Exception as e:
        raise SystemExit(f"Fallo inesperado al guardar {ruta}: {e!r}")
