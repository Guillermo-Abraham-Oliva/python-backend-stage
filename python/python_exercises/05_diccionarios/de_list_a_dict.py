from typing import Dict, List, Tuple, Any

lst = [
  {"id": 101, "precio": 26, "stock": 8},
  {"id": 104, "descuento": 0.20},
  {"id": 105, "nombre": "Auriculares", "precio": "18", "stock": 12, "activo": True},
  {"id": 103, "baja": True},
  {"id": 102, "precio": 14.5}
]

# crea un diccio desde una lista
def lista_a_diccio(lista: List[Dict[str, Any]]) -> Dict[int, Dict[str, Any]]:
    return {item["id"]: item for item in lista if item != "id"}

# imprime la lista con ejecucion de funcion
def imprimir(lista: List[Dict[str, Any]]):
    diccio = lista_a_diccio(lista)
    for k, v in diccio.items():
        print(k, v)

imprimir(lst)