# logica pura, solo negocio

from typing import Any
import logging

log = logging.getLogger(__name__)

def lst_a_dict(lst: list[dict[str, Any]]) -> dict[int, dict[str, Any]]:
    return {item["id"]: item for item in lst}

def actualizar(inv: dict[int, dict[str, Any]],
               update: list[dict[str, Any]]) -> tuple[dict[int, dict[str, Any]], list[int]]:
    ids_baja: list[int] = []
    for upd in update:
        pid = upd.get("id")
        if pid is None:
            continue
        if upd.get("baja") and pid in inv:
            inv.pop(pid, None)
            ids_baja.append(pid)
            continue
        if pid in inv: # actualización
            parche = {k: v for k, v in upd.items() if k != "id"}
            inv[pid].update(parche)  # patrón más usado que |
        else: # Alta
            if all(k in upd for k in ("nombre", "precio", "stock")): # para cada k en ("","","") compruebo que k esté en upd
                inv[pid] = upd.copy()
    log.info("Aplicando actualizacion...")
    return inv, ids_baja

def a_float(precio: Any) -> float:
    if isinstance(precio, (int, float)):
        return float(precio)
    if isinstance(precio, str):
        precio = precio.replace(",", ".")
        return float("".join(precio.split()))
    raise ValueError(f"precio inválido {precio!r}")

def a_int(x: Any) -> int:
    if isinstance(x, int):
        return x
    if isinstance(x, float):
        if x.is_integer():
            return int(x)
        raise ValueError(f"stock no entero: {x!r}")
    if isinstance(x, str):
        s = x.strip().replace(",", "").replace(" ", "")
        if s.isdigit():
            return int(s)
    raise ValueError(f"stock inválido: {x!r}")

def normalizar_producto(p: dict[str, Any]) -> dict[str, Any]:
    precio = a_float(p.get("precio", 0))
    stock = a_int(p.get("stock", 0))
    descuento = p.get("descuento", 0) or 0
    try:
        descuento = float(descuento)
    except Exception:
        descuento = 0.0
    precio_final = round(precio * (1 - descuento), 2)
    q = p.copy()
    q["precio"] = precio
    q["stock"] = stock
    q.pop("descuento", None)
    q["precio_final"] = precio_final
    return q
