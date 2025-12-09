from typing import Any

# 1) dict-comprehension: pares -> {n: n**2}
def pares_cuadrados(nums: list[int]) -> dict[int, int]:
    return {n: n * n for n in nums if n % 2 == 0}

# 2) range + sum: múltiplos de 3 dentro de rango 'n'
def suma_multiplos_de_tres(n: int) -> int:
    return sum(x for x in range(n) if x % 3 == 0)

# 3) Unión | prioriza el segundo catálogo
def merge_catalogs(a: dict[int, dict[str, Any]], b: dict[int, dict[str, Any]]) -> dict[int, dict[str, Any]]:
    return a | b
