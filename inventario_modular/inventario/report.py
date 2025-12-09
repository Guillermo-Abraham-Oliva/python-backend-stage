from typing import Any
import logging

log = logging.getLogger(__name__)

def generar_reporte(catalogo_final: list[dict[str, Any]],
                    ids_baja: list[int],
                    top_n: int = 3) -> dict[str, Any]:
    total_activos = len(catalogo_final)
    valor_total_stock = round(sum(p["precio_final"] * p["stock"] for p in catalogo_final), 2)

    ordenados = sorted(catalogo_final, key=lambda o: o["stock"], reverse=True)
    top_n = max(0, int(top_n)) # Si top_n es menor que 0, lo subo a 0. Si es mayor, lo dejo como está
    top_ids = [t["id"] for t in ordenados[:top_n]]
    
    log.info("Reporte generado: %d activos, %d bajas, %d productos top stock", total_activos, len(ids_baja), top_n)

    return {
        "total_activos": total_activos,
        "valor_total_stock": valor_total_stock,
        "top_stock": top_ids,
        "ids_baja": ids_baja,
        "conteo_bajas": len(ids_baja),
    }
