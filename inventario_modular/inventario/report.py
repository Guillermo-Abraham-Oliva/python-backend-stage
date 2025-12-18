from typing import Any
import logging

log = logging.getLogger(__name__)

def generar_reporte(catalogo_final: list[dict[str, Any]],
                    ids_baja: list[int],
                    top_n: int = 3) -> dict[str, Any]:
    total_activos = len(catalogo_final)
    valor_total_stock = round(sum(p["precio_final"] * p["stock"] for p in catalogo_final), 2)

    ordenados = sorted(catalogo_final, key=lambda o: o["stock"], reverse=True)
    try:
        top_n = int(top_n)
    except Exception:
        top_n = 3 # asigno 3 por default
        
    if top_n < 0:
        top_n = 3 # asigno 3 por default

    top_ids = [p["id"] for p in ordenados[:top_n]]

    log.info("Reporte generado: %d activos, %d bajas, %d productos top stock", total_activos, len(ids_baja), top_n)

    return {
        "total_activos": total_activos,
        "valor_total_stock": valor_total_stock,
        "top_stock": top_ids,
        "ids_baja": ids_baja,
        "conteo_bajas": len(ids_baja),
    }

