# Mini Sistema de Inventario en Python

Proyecto backend que procesa un inventario en formato JSON, aplica actualizaciones, normaliza los datos, manejo de errores y genera un catálogo final y un reporte resumen.

Simula un flujo real básico de manejo de inventario para e-commerce o sistemas de stock.

---

## Objetivos del proyecto

- Cargar inventarios y actualizaciones desde archivos JSON
- Convertir la lista inicial en un diccionario indexado por `id` (último id gana si está duplicado)
- Aplicar operaciones:
  - Alta
  - Actualización
  - Baja
- Normalizar campos:
  - `precio` → `float`
  - `stock` → `int`
  - tomar `descuento` si existe y calcular `precio_final`
- Filtrar productos activos
- Ordenar por `precio_final` ascendente
- Generar:
  - `catalogo_final.json`
  - `reporte.json`

---

## Estructura del proyecto

Mini_Sistema_Inventario/
│── data/
│   ├── inventario.json        # entrada proporcionada
│   └── actualizacion.json     # entrada proporcionada
│── salida/
│   ├── catalogo_final.json    # salida generada
│   └── reporte.json           # salida generada
│── main.py
└── README.md

---

## Datos de entrada

### `inventario.json`

Contiene inventario original (puede tener IDs duplicados).

```json
[
  {"id": 101, "nombre": "Teclado", "precio": 25, "stock": 10, "activo": true},
  {"id": 102, "nombre": "Ratón", "precio": "15.0", "stock": 30, "activo": true, "descuento": 0.10},
  {"id": 103, "nombre": "Pantalla", "precio": 200, "stock": 5, "activo": false},
  {"id": 104, "nombre": "Cables", "precio": 5, "stock": "100", "activo": true},
  {"id": 102, "nombre": "Ratón DUP", "precio": 16, "stock": 5, "activo": true}
]
```

### `actualizacion.json`

Contiene altas, bajas y modificaciones.

```json
[
  {"id": 101, "precio": 26, "stock": 8},
  {"id": 104, "descuento": 0.20},
  {"id": 105, "nombre": "Auriculares", "precio": "18", "stock": 12, "activo": true},
  {"id": 103, "baja": true},
  {"id": 102, "precio": 14.5}
]
```

---

## Salidas generadas

### `catalogo_final.json`

Lista final de productos activos, normalizados y ordenados por `precio_final`.

Campos:

* `id`
* `nombre`
* `precio` (`float`)
* `stock` (`int`)
* `activo`
* `precio_final`

### `reporte.json`

Campos:

| Campo               | Descripción                      |
| ------------------- | -------------------------------- |
| `total_activos`     | Cantidad de productos activos    |
| `valor_total_stock` | Suma de `stock` * `precio_final` |
| `top3_stock`        | IDs con mayor stock              |
| `ids_baja`          | IDs eliminados                   |
| `conteo_bajas`      | Cantidad de bajas                |

Los archivos generados (`catalogo_final.json` y `reporte.json`) se guardan automáticamente en la carpeta `salida/`.

---

## Ejecución

En la carpeta del proyecto (donde está `main.py`):


---

## Ejemplo de ejecución

**Entrada (fragmento inventario):**

```json
[
  {"id": 101, "nombre": "Teclado", "precio": 25, "stock": 10, "activo": true},
  {"id": 102, "nombre": "Ratón", "precio": "15.0", "stock": 30, "activo": true}
]
```

**Entrada (fragmento actualizaciones):**

```json
[
  {"id": 101, "precio": 26, "stock": 8},
  {"id": 102, "precio": 14.5}
]
```

**Salida (fragmento `catalogo_final.json`):**

```json
[
  {
    "id": 102,
    "nombre": "Ratón",
    "precio": 14.5,
    "stock": 30,
    "activo": true,
    "precio_final": 13.05
  },
  {
    "id": 101,
    "nombre": "Teclado",
    "precio": 26.0,
    "stock": 8,
    "activo": true,
    "precio_final": 26.0
  }
]
```

---

## Conceptos trabajados

* Diccionarios y comprensión de diccionarios
* Manejo de JSON (`json.loads`, `json.dumps`)
* Manejo de errores (`try/except`)
* Limpieza y normalización de datos
* Conversión de tipos
* Cálculo con descuento y redondeo
* Ordenamiento (`sorted`)
* Métodos de diccionario (`pop`, merge `|`, `.copy()`)
* Organización modular con funciones
* Escritura de archivos en disco

---

## Competencias técnicas aplicadas

* Modelado de flujo de actualización de inventario
* Separación entre limpieza de datos y lógica de negocio
* Estrategias defensivas ante datos sucios
* Generación automática de reportes
* Buenas prácticas mínimas en scripts backend

---

## Posibles mejoras futuras

* Tests automáticos (`pytest`)
* Validación de esquema (`pydantic`)
* CLI (`argparse` o `typer`)
* API REST (`FastAPI` o `Flask`)
* Persistencia en SQLite o PostgreSQL

---

## Licencia

Uso educativo.