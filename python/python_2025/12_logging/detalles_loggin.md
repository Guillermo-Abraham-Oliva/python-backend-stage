

# ¿Qué son `%s`  `%d`  `%f` ?

Son **placeholders** del *estilo de formateo clásico en Python* (heredado de C).

Logging en Python **recomienda** usar este estilo porque:

* es más eficiente (no interpola cadenas si no hace falta),
* es el estándar para logs,
* es seguro,
* mantiene el mensaje sin formatear internamente.


### **Regla básica:**

* `%s` → str →   cuando vas a imprimir **cualquier cosa como texto** (str, Path, números, objetos… lo que sea)

* `%d` → digit → cuando vas a imprimir un **entero**

* `%f` → float → cuando vas a imprimir un **float**


# ejemplos:

`log.info("Guardando JSON en %s", ruta)`  (Aquí `ruta` es un objeto `Path`)
`log.info("Guardando JSON en %d", numero_entero)`
`log.info("Guardando JSON en %f", numero_float)`
