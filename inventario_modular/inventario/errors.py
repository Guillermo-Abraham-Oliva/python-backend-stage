# aqui pruebo las funciones

import logging, json
log = logging.getLogger(__name__) #aqui pido el logger del name de este file, entonces si da error aqui, aparece como inventario.errors... ej  | ERROR | inventario.errors | JSON inválido: etc

def run_seguro(fn, *args, **kwargs) -> int: # recibe 1 argum posicional que es "run", y una cant variable de argus posicionales (*Args) y una cant variable de argumentos con nombre (**Kwargs). En el *Args entra el "parseo"
    try:
        fn(*args, **kwargs)
        return 0
    except FileNotFoundError as e:
        log.error("Archivo no encontrado: %s", e)
        return 3
    except json.JSONDecodeError as e:
        log.error("JSON inválido: %s", e)
        return 2
    except Exception as e:
        log.exception("Fallo inesperado: %s", e)
        return 1
