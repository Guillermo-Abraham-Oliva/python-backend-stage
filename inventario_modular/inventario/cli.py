import logging
import argparse            # usar el módulo es lo más común
from pathlib import Path

from .logging_config import setup_logging
from .errors import run_seguro
from .io import cargar_json, guardar_resultados
from .core import lst_a_dict, actualizar, normalizar_producto
from .report import generar_reporte

log = logging.getLogger(__name__) #aqui pido el logger del name de este file, entonces si da error aqui, aparece como 'inventario.cli'  ej  2025-12-05 10:32:17 | ERROR | inventario.cli | Archivo no encontrado: [Errno 2]

def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(
        prog="inventario",
        description="Sistema de inventario que aplica altas, bajas y actualizaciones, y genera un catálogo final de productos y un reporte resumen."
        )
    # las sig son las opciones de la consola
    p.add_argument("--inventario",
                   type=Path,
                   default=Path("data/inventario.json"),
                   help="Ruta al archivo JSON de 'inventario base'",)
    p.add_argument("--update",
                   type=Path,
                   default=Path("data/actualizacion.json"),
                   help="Ruta al archivo JSON de 'actualizaciones'",)
    p.add_argument("--out",
                   type=Path,
                   default=Path("salida"),
                   help="Carpeta donde se guardarán los resultados (catalogo_final.json y reporte.json)",)
    p.add_argument("--top",
                   type=int,
                   default=3,
                   help="Número máximo de productos con más stock en el reporte (default: 3)",
    )
    return p.parse_args()

def run(args: argparse.Namespace) -> None: # args es parametro posicional -> con los parámetros del CLI
    inv_lst = cargar_json(args.inventario)
    upd_lst = cargar_json(args.update)
    log.info("Carga de inventario con %d productos, y actualizacion con %d productos", len(inv_lst), len(upd_lst))

    inv_dict = lst_a_dict(inv_lst)
    inv_dict, ids_baja = actualizar(inv_dict, upd_lst)
    log.info("Bajas: %d", len(ids_baja))

    normalizados = [normalizar_producto(p) for p in inv_dict.values()]
    activos = [p for p in normalizados if p.get("activo") is True]
    catalogo_final = sorted(activos, key=lambda o: o["precio_final"])
    log.info("Activos finales: %d", len(catalogo_final))

    args.out.mkdir(parents=True, exist_ok=True)
    guardar_resultados(args.out / "catalogo_final.json", catalogo_final)

    reporte = generar_reporte(catalogo_final, ids_baja, args.top)
    guardar_resultados(args.out / "reporte.json", reporte)
    log.info("Proceso completado. Catálogo y reporte generados en '%s'", args.out)

def main() -> int:
    setup_logging() # (desde logging_config.py)
    return run_seguro(run, parse_args()) # se le pasa 'run' que orquesta todo y 'parse_args' (el espacio de nombres definido para la cli). En run_seguro, el espacio de nombres es *Args de run

if __name__ == "__main__":
    raise SystemExit(main())   # Cerrar programa devolviendo código de salida
