# ----------Logging---------------

EN un archivo o consola -> REGISTRA EVENTOS Y MENSAJES de:
 - info
 - warning
 - errores críticos 

de mi app mientras corre, para poder ver qué pasó, depurar, investigar errores y entender el comportamiento del sistema.
Reemplaza a print saltando a pro.

logging ("Registro") es módulo... (y pathlib tb! a pesar que dice lib)

logging handlers -> manejadores de logging

RotatingFileHandler -> Manejador de archivos rotativos.

from logging.handlers import RotatingFileHandler -> desde manejadores de logging, importar manejador de archivos rotativos 

from pathlib import Path -> desde el modulo pathlib, importar Path


# ----------- Plantilla mínima --------------------

      ( copiar siempre para arrancar )

```python
import logging

logging.basicConfig(
    level=logging.INFO,  # DEBUG cuando quiera ver TODO
    format="%(asctime)s | %(levelname)s | %(message)s"
)

#   format="%(asctime)s | %(levelname)s | %(name)-17s | %(message)s"
# Si es modular -> agrega 'name' para que tome automaticamente  el nombre del modulo (requiere -> log = logging.getLogger(__name__) al inicio de cada modulo!!!):

log = logging.getLogger(__name__)

log.info("Inicio del programa")
log.warning("Atención: posible problema")
log.error("Error crítico detectado")
````

### Mis reglas para logging

* INFO = cosas importantes que pasan normalmente
* WARNING = ojo, algo raro pero no se cae
* ERROR = falló algo serio
* DEBUG = modo cirujano, solo cuando estoy desarrollando

### Para proyectos serios (archivo + consola)

Guardar logs en archivo (80% de proyectos backend):

```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    handlers=[
        logging.FileHandler("app.log", encoding="utf-8"),
        logging.StreamHandler()  # consola
    ]
)
```

Y con rotación:

```python
import logging
from logging.handlers import RotatingFileHandler

LOG_FORMAT = "%(asctime)s | %(levelname)s | %(name)s | %(message)s"

logging.basicConfig(
    level=logging.INFO,
    format=LOG_FORMAT,
    handlers=[
        logging.StreamHandler(),
        RotatingFileHandler("app.log", maxBytes=500_000, backupCount=3, encoding="utf-8")
    ]
)

log = logging.getLogger("app")
```
