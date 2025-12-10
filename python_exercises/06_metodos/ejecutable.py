'''leer un fichero JSON externamente y a cada producto de la lista cargarlo como diccionario y asignarle un ID numérico usando el numerate de modo que cada producto tenga un campo ID, luego calcular el valor total del inventario, encontrar el producto más barato y el más caro, y finalmente guardar toda esa información generando un nuevo diccionario que hay que guardar en un fichero externo JSON con :
            - La lista completa de productos con ID
            - El valor total del inventario
            - El producto más barato
            - El producto más caro

# usar ->  sum() min(), max() enumerate()
# Lectura/Escritura de JSON y Pathlib
'''

import json
from pathlib import Path

BASE = Path("/home/guille/Mi_Repositorio_Git/python_2025/x__data_work_para_ejercicios")
DATA = BASE / "productos.json"
OUT = BASE / "resultados.json"

def main():
    with open(DATA, "r", encoding="utf-8") as f:
        productos = json.load(f)  # productos es una Lista de diccios

    # etiquetar cada producto con un ID indexado
    productos_indexados = []
    for indice, p in enumerate(productos, start=1):  # indice y valor
        nuevo = p.copy()      # copiar para desvincular
        nuevo["id"] = indice  # agrego el campo 'id' aprovechando el indice de enumerate
        productos_indexados.append(nuevo)

    # valor total de inventario (stock)
    valor_total = sum(p["precio"] * p["stock"] for p in productos)

    # encontrar el producto más barato y más caro
    mas_barato = min(productos, key=lambda p: p["precio"])
    mas_caro = max(productos, key=lambda p: p["precio"])

    # preparo resultados
    salida = {
        "productos_con_id": productos_indexados,
        "valor_total_inventario": valor_total,
        "producto_mas_barato": mas_barato,
        "producto_mas_caro": mas_caro,
    }

    # guardar en JSON
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(salida, f, indent=4, ensure_ascii=False)

    print(f"\n\tProcesamiento completado.\n \tArchivo guardado en: {OUT}\n")


if __name__ == "__main__":
    main()

# atento, esto se ejecuta desde la cli con:
# python ejecutable.py