
from __future__ import annotations
from pathlib import Path
from typing import Any
import json

# 1) dict-comprehension: pares -> {n: n**2}
def pares_cuadrados(nums: list[int]) -> dict[int, int]:
    return {n: n * n for n in nums if n % 2 == 0}

# 2) sorted estable con clave compuesta: p asc, n desc
def ordenar_registros(regs: list[dict[str, Any]]) -> list[dict[str, Any]]:
    paso1 = sorted(regs, key=lambda r: r["n"], reverse=True)   # n desc
    return sorted(paso1, key=lambda r: r["p"])                 # p asc

# 3) enumerate + slicing: paginación 1-based
def paginar(items: list[Any], tam: int, pagina: int) -> list[tuple[int, Any]]:
    ini = (pagina - 1) * tam
    fin = ini + tam
    return [(i + 1, x) for i, x in enumerate(items[ini:fin], start=ini)]

# 4) range + sum: múltiplos de 3 < N
def suma_multiplos_de_tres(n: int) -> int:
    return sum(x for x in range(n) if x % 3 == 0)

# 5) .get con default: contar ocurrencias
def contar_ocurrencias(xs: list[str]) -> dict[str, int]:
    c: dict[str, int] = {}
    for x in xs:
        c[x] = c.get(x, 0) + 1
    return c

# 6) Unión | prioriza el segundo catálogo
def merge_catalogs(a: dict[int, dict[str, Any]], b: dict[int, dict[str, Any]]) -> dict[int, dict[str, Any]]:
    return a | b

# 7) Deduplicar estable con set
def dedupe_orden(seq: list[Any]) -> list[Any]:
    vistos: set[Any] = set()
    out: list[Any] = []
    for x in seq:
        if x not in vistos:
            vistos.add(x)
            out.append(x)
    return out

# 8) try/except/else/finally: contar líneas o crear archivo
def contar_lineas_creando(ruta: Path) -> int:
    ruta.parent.mkdir(parents=True, exist_ok=True)
    f = None
    try:
        f = open(ruta, mode="r", encoding="utf-8")
        lineas = f.readlines()
    except FileNotFoundError:
        ruta.write_text("creado\n", encoding="utf-8")
        return 1
    else:
        return len(lineas)
    finally:
        if f:
            f.close()

# 9) JSON ida/vuelta con validación de tipos
def json_roundtrip(data: list[dict[str, Any]]) -> list[dict[str, Any]]:
    if not isinstance(data, list) or not all(isinstance(d, dict) for d in data):
        raise TypeError("Se espera list[dict]")
    txt = json.dumps(data, ensure_ascii=False)
    out = json.loads(txt)
    if not isinstance(out, list) or not all(isinstance(d, dict) for d in out):
        raise TypeError("JSON inválido tras roundtrip")
    return out

# 10) Strings: "apellido, nombre" -> "Nombre Apellido"
def normalizar_nombres(lineas: list[str]) -> list[str]:
    def norma(s: str) -> str:
        partes = [p.strip().title() for p in s.split(",")]
        if len(partes) != 2:
            return " ".join(p for p in partes if p)
        apellido, nombre = partes
        return " ".join([nombre, apellido]).strip()
    return [norma(s) for s in lineas]


# ===================== TESTS RÁPIDOS =====================

# 1
assert pares_cuadrados([1, 2, 3, 4, 5]) == {2: 4, 4: 16}

# 2
regs = [{"n": "a", "p": 2}, {"n": "b", "p": 2}, {"n": "c", "p": 1}]
orden = ordenar_registros(regs)
assert orden == [{"n": "c", "p": 1}, {"n": "b", "p": 2}, {"n": "a", "p": 2}]

# 3
items = list("abcdefg")
assert paginar(items, tam=3, pagina=1) == [(1, "a"), (2, "b"), (3, "c")]
assert paginar(items, tam=3, pagina=3) == [(7, "g")]

# 4
assert suma_multiplos_de_tres(10) == 18  # 0+3+6+9

# 5
assert contar_ocurrencias(["a", "b", "a", "c", "a"]) == {"a": 3, "b": 1, "c": 1}

# 6
a = {1: {"n": "teclado", "p": 20}, 2: {"n": "ratón", "p": 10}}
b = {2: {"n": "mouse", "p": 12}, 3: {"n": "monitor", "p": 100}}
m = merge_catalogs(a, b)
assert m[2]["n"] == "mouse" and set(m) == {1, 2, 3}

# 7
assert dedupe_orden([1, 2, 1, 3, 2, 4, 1]) == [1, 2, 3, 4]

# 8
tmp = Path("data_test/input.txt")
tmp.unlink(missing_ok=True)
assert contar_lineas_creando(tmp) == 1
tmp.write_text("a\nb\n", encoding="utf-8")
assert contar_lineas_creando(tmp) == 2

# 9
orig = [{"id": 1, "tags": ["a", "b"]}]
copia = json_roundtrip(orig)
assert copia == orig and isinstance(copia, list) and isinstance(copia[0], dict)

# 10
noms = ["perez, ana", "  GARCIA,  luis  ", "SoloNombre"]
assert normalizar_nombres(noms) == ["Ana Perez", "Luis Garcia", "Solonombre"]

print("OK 10/10")
