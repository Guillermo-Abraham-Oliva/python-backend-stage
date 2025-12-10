# Parseo es recibir datos sueltos y convertirlos
# en una estructura entendible (int, dict, list, etc...)
# para poder operar con ellos

# Ejemplos:

# string a int
numero = int("42")   # parseo

# string JSON a dict
import json
data = json.loads('{"x": 10, "y": 20}')  # parseo


# -------- -- ANALIZAMOS ----------------------

def parse_args() -> argparse.Namespace: # módulo para leer parametros 
    p = argparse.ArgumentParser(prog="inventario", 
                                description="Pipeline simple inventario")
    p.add_argument("--inventario", type=Path, default=DATA / "inventario.json")
    p.add_argument("--update", type=Path, default=DATA / "actualizacion.json")
    p.add_argument("--out", type=Path, default=OUT)
    p.add_argument("--top", type=int, default=3)
    return p.parse_args()


# 1) ¿Por qué la función se llama `parse_args`?
`parse_args` -> Es el apocope de “parsear argumentos”, puede llamarse como uno quiera pero por convención se adoptó asi y todos lo usan.
OJO -> coincide con el return! pero éste ultimo es un metodo!
SON COSAS DISTINTAS QUE COINCIDEN EN EL MISMO NOMBRE

Significa -> **leer los flags que pasas en la terminal**


# 2) `argparse.Namespace`

`argparse` = módulo estándar de Python para leer argumentos CLI.
`Namespace` = tipo de objeto que devuelve `argparse` para guardar los valores -> un tupper donde Python mete los parámetros que pasamos


# 3) Qué hace esto:

p = argparse.ArgumentParser(
        prog="inventario",
        description="Pipeline simple de inventario con catálogo y reporte final")

Esto prepara el sistema para decirle qué argumentos acepta tu script.

Cuando en la cli, se ejecuta:
python cli.py -h     [o --help]

se mostrará :

usage: inventario [-h] [--inventario INVENTARIO] [--update UPDATE] [--out OUT] [--top TOP]

Pipeline simple de inventario con catálogo y reporte final

options:
  -h, --help            show this help message and exit
  --inventario INVENTARIO
  --update UPDATE
  --out OUT
  --top TOP


# 4) `add_argument` -> “quiero aceptar este parámetro desde la cli”

Ejemplo real:

p.add_argument("--top", type=int, default=3)

- si en la cli el usuario escribe `--top 10`, lo guardo como número `10`
- si no pone nada, va `3` por default

Eso se convierte en ---> "args.top"


# 5) `return p.parse_args()`

Ese `parse_args()` NO es la función def (aunque coincida el nombre).
Es un **método de parser** que parsea los argumentos que el usuario agrego y los deja listos para usar.


Resumen:

| Código             | Significado                                     |
| ------------------ | ------------------------------------------------|
| def parse_args()   | función mia; va ese nombre por convención       |
| argparse           | módulo para leer parametros                     |
| Namespace          | el objeto donde se guardan los parametros       |
| ArgumentParser     | crea el “lector de parámetros”                  |
| add_argument       | dice qué parámetros acepta tu script            |
| return parse_args()| se parsean los argumentos que el usuario agrego |


'''
---EN LA CLI---

REGLA EN ABSTRACTO:
    python archivo.py --flag1 valor --flag2 valor   etc...

CASO CONCRETO:
python cli.py --inventario data/inventario.json --update data/actualizacion.json --top 5
- Abre cli.py
- pasa 'inventario.json' al argumento '--inventario'
- pasa 'actualizacion.json' al argumento '--update'
- pasa '5' al argumento '--top'
'''
