
# __init__.py -> indica a python qie todo en esa carpeta es parte de un módulo.
# es solo una especie de "marcador", por eso esta vacio

# Si falta -> `ModuleNotFoundError: No module named 'inventario'`


# Cuando python arranca, busca paquetes
# Si ve `inventario/` y hay `__init__.py`, LO AÑADE AL SISTEMA DE MÓDULOS.
# Si no lo ve, ignora esa carpeta.
