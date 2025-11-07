# Mini Sistema de Inventario

from __future__ import annotations
from pathlib import Path
from typing import Dict, List, Tuple, Any
import json

BASE = Path(__file__).resolve().parent # carpeta donde está main.py
DATA = BASE / "data"                   # .../Ejerc_11/data  <- carpeta donde estan los inventarios
OUT = BASE / "salida"                  # .../Ejerc_11/salida <- carpeta donde saldrán los resultados

def cargar_json(ruta: Path) -> List[Dict[str, Any]]:
    try:
        return json.loads(ruta.read_text(encoding="utf-8"))
        # alternativa pelin mas antigua pero decente:
        #   with open(ruta, "r", encoding="utf-8") as f:
        #       return json.load(f)
    except FileNotFoundError:
        raise SystemExit(f"Archivo no encontrado en {ruta}")
    except json.JSONDecodeError as e:
        raise SystemExit(f"Json inválido en {ruta}: {e!r}")
    except PermissionError:
        raise SystemExit(f"Sin permisos para leer ruta {ruta}")
    except Exception as e:
        raise SystemExit(f"Error desconocido: {e!r}")

def lst_a_dict(lst: List[Dict[str, Any]]) -> Dict[int, Dict[str, Any]]:
    return {item["id"]: item for item in lst}

def actualizar(inv: dict[int, Dict[str, Any]], 
               update: List[Dict[str, Any]]) -> Tuple[Dict[int, Dict[str, Any]], List[int]]:
               # SIEMPRE TUPLA CUANDO HAY MAS DE 1 RETORNO
    ids_baja: List[int] = []
    for upd in update:
        pid = upd.get("id")
        if pid is None: #   sin id -> continue
            continue
        if upd.get("baja") and pid in inv: # si es una BAJA y el id esta en esa upd
            inv.pop(pid, None)
            ids_baja.append(pid)
            continue
        if pid in inv:  # ACTUALIZACION: agrega solo los campos que NO son id (no tocar el id)
            parche = {k: v for k, v in upd.items() if k != "id"}
            inv[pid] = inv[pid] | parche  # o inv[pid].update(parche)
        else:   # si no esta el pid en inv -> es un ALTA (crear solo si trae mínimos)
            if all(k in upd for k in ("nombre", "precio", "stock")):
                inv[pid] = upd.copy() # para que quede independiente de upd (por si upd cambia). Entonces con la copia superficial ya queda chafado fijo sin posibilidad de error.
    return inv, ids_baja

def a_float(precio: Any) -> float:
    if isinstance(precio, (int, float)):
        return float(precio)
    if isinstance(precio, str):
        precio = precio.replace(",", ".")
        precio = float("".join(precio.split())) # se separa en cada espacio, se une, y se pasa a decimal
        return precio
    raise ValueError(f"precio inválido {precio!r}") # !r para que se reproduzca tal cual es, con espacios etc.

def a_int(x: Any) -> int: # Convwersion a entero
    if isinstance(x, int):
        return x
    if isinstance(x, float):
        if x.is_integer():  # asegurar valor entero (no acepta decimales)
            return int(x)
        raise ValueError(f"stock no entero: {x!r}")
    if isinstance(x, str):
        s = x.strip()
        s = s.replace(",", "").replace(" ", "")
        if s.isdigit():
            return int(s)
    raise ValueError(f"stock inválido: {x!r}")

# Normalización: solo normaliza 1 diccio no un diccio anidado! (hay que enviarle de a 1)
# convertir precio→float, stock→int, sacar descuento, calcular precio_final
def normalizar_producto(p: Dict[str, Any]) -> Dict[str, Any]:
    precio = a_float(p.get("precio", 0)) # guardo en la variable precio para procesar el precio
    stock = a_int(p.get("stock", 0)) # guardo en la variable stock para procesar el stock
    descuento = p.get("descuento", 0) or 0 # guardo en 'descuento' previniendo bug con 'or 0' puesto que el 'or 0' agrega tolerancia para valores “falsy” basura tipo "", None, False.... lo convierte en 0 en vez de reventar.
    try:
        descuento = float(descuento) # actualizamos desceunto con descuento en float
    except Exception:    # cualquier incongruencia -> asigno 0.0
        descuento = 0.0
    precio_final = round(precio * (1 - descuento), 2)
    p = p.copy() # generalmente se quiere una 'versión' (no cambiar el original)!!!
    p["precio"] = precio # actualizo el precio correcto y en float
    p["stock"] = stock # actualizo el stock correcto y en int
    p.pop("descuento", None)
    p["precio_final"] = precio_final # agregamos la clave "precio_final"
    return p

# generar_reporte: Contar activos, sumar su valor total, identificar los tres con más stock, anotar las bajas y su cantidad, y guardar todo eso como un dict en JSON.

# Recibe:
# lista_final: lista de productos activos y normalizados (cada uno ya con precio_final y stock).
# ids_baja: lista con los IDs que fueron dados de baja.

# Campos que debe tener el reporte:
# total_activos	cantidad de productos activos finales
# valor_total_stock	valor total de todo el stock activo (precio final × unidades disponibles)
# top3_stock: los 3 productos con mayor cantidad en stock, ordenados de mayor a menor
# ids_baja: lista de los IDs eliminados (bajas)	se pasa directo com argumento ids_baja
# conteo_bajas: cant de ids_baja
                                           
# Una vez calculados, formar diccio con esos campos y volcar en el archivo salida/reporte.json

# El archivo final debe contener algo así:
# {"total_activos": 4,
#  "valor_total_stock": 896.5,
#  "top3_stock": [104, 105, 101],
#  "ids_baja": [103],
#  "conteo_bajas": 1}

def generar_reporte(catalogo_final: List[Dict[str, Any]], ids_baja: List[int]) -> Dict[str, Any]:
    total_activos = len(catalogo_final)
    valor_total_stock = round(sum(p["precio_final"] * p["stock"] for p in catalogo_final), 2)

    top3_dicts = sorted(catalogo_final, key=lambda o: o["stock"]) # creo una lista ordenada por stock
    top3_lst = top3_dicts[-3:] # creo otra lista con los últimos 3 (los 3 con mas stock)
    top3_stock = [t["id"] for t in top3_lst]
    return {
        "total_activos": total_activos,
        "valor_total_stock": valor_total_stock,
        "top3_stock": top3_stock,
        "ids_baja": ids_baja,
        "conteo_bajas": len(ids_baja),}

def main() -> None:
    # crear directorio de salida y sus 'padres' si no existen. 
    # Si ya existe la carpeta, continuar ejecucion sin error ni detencion
    OUT.mkdir(parents=True, exist_ok=True)

    # CARGAMOS el inventario (list) y la actualizacion (list)
    inv_lst = cargar_json(DATA / "inventario.json")
    upd_lst = cargar_json(DATA / "actualizacion.json")

    # transformamos inv_lst a inv_dict 
    # upd_lista NO! -> las actualizaciones SIEMPRE DEBEN SER LISTA para conservar duplicados, orden de entrada, etc!!!
    inv_dict = lst_a_dict(inv_lst)

    # ACTUALIZAR: la def tiene 2 retornos -> se desempaqueta en: inv_dict (actualizado) e ids_baja
    inv_dict, ids_baja = actualizar(inv_dict, upd_lst)
    # se actualiza antes de normalizar, porque al reves, se 'des-normalizaria' al actualizarce desde la actualizacion que no esta normalizada. 
    # Orden: actualizar todo -> normalizar el resulado final

    # NORMALIZAR: guardar en un listado de normalizados
    normalizados = [normalizar_producto(p) for p in inv_dict.values()]

    # ACTIVOS: filtrar los normalizados activos y ordenar por precio_final asc en catalogo_final
    activos = [p for p in normalizados if p.get("activo") is True]
    catalogo_final = sorted(activos, key=lambda o: o["precio_final"])

    # guardar catálogos: "catalogo_final.json" -> OUT
    # como OUT guarda la carpeta "salida", ese catalogo va a esa carpeta
    (OUT / "catalogo_final.json").write_text(json.dumps(catalogo_final, ensure_ascii=False, indent=2), encoding="utf-8")

    # Reporte (pasar como argus 'catalogo_final' e 'ids_baja')
    reporte = generar_reporte(catalogo_final, ids_baja) # como OUT guarda la carpeta "salida", ese reporte va ahi
    (OUT / "reporte.json").write_text(json.dumps(reporte, ensure_ascii=False, indent=2), encoding="utf-8")

if __name__ == "__main__":
    main()