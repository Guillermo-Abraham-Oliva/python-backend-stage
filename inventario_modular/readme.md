# Mini Sistema de Inventario (modular)
Proyecto implementado con arquitectura modular en Python, incorporando argparse para la CLI, logging para el registro estructurado y pathlib para la manipulación segura de rutas.

# Pipeline:
1) carga JSON,
2) aplica altas/bajas/actualizaciones,
3) normaliza (precio_final, stock),
4) filtra activos y ordena,
5) genera catálogo y reporte.

## Estructura
inventario/  # módulos
data/        # JSON de entrada
salida/      # resultados
logs/        # logs rotativos

## Requisitos
Python 3.10+. Sin dependencias externas.


## Uso

# 1- ir a:
cd inventario_modular

# 2- para ejecución NORMAL usando los valores por defecto: inventario.json y actualizacion.json en carpeta data/  y top=3:
python -m inventario.cli


------------------------------------------------------------------------
# 3- Si se quieren usar OTROS ficheros distintos a los dados en default:
python -m inventario.cli --inventario nueva_carpeta/nuevo_inventario.json --update nueva_carpeta/nueva_actualizacion.json --out nueva_carpeta --top 5 (u otro valor)
