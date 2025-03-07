import os
os.system('clear' if os.name == 'posix' else 'cls')

"""
Este script simula un sistema de impresión de modelos 3D.

Funciona de la siguiente manera:
1. Toma una lista de modelos pendientes de impresión.
2. Simula la impresión de cada modelo, moviéndolo a una lista de modelos completados.
3. Muestra los modelos que han sido impresos.
4. Hace que la lista original de encargos no se modifique porque usa una copia.

Este código es útil para entender la manipulación de listas y el paso de parámetros por referencia o copia en Python.
"""
# ✅ Porcentaje de uso futuro en backend profesional: 20%
def imprimir_modelos(encargos, finalizados):
    """Simula la impresión de cada diseño hasta que todos han sido completados.
    Mueve cada diseño a la lista de finalizados tras imprimirlo."""
    while encargos:
        diseño_actual = encargos.pop() # Extrae el último modelo de la lista de encargos
        print("Imprimiendo modelo: " + diseño_actual) # Simula la impresión del modelo
        finalizados.append(diseño_actual) # Agrega el modelo impreso a la lista de finalizados

def muestra_modelos_completados(finalizados):
    """ Muestra los modelos impresos. """
    print("\nLos siguientes modelos han sido impresos:")
    
    # Recorre la lista de modelos finalizados y los muestra
    for modelo_finalizado in finalizados:
        print(modelo_finalizado)

# Lista de modelos pendientes de impresión
modelos_encargados = ['iphone case', 'robot pendant', 'dodecahedron']
modelos_completados = [] # Lista vacía para almacenar los modelos completados

# Llama a la función de impresión, pasando una copia de la lista de encargos
imprimir_modelos(modelos_encargados[:], modelos_completados)

muestra_modelos_completados(modelos_completados) # Muestra los modelos que han sido impresos
# Cuando 'modelos_completados' se pasa como argumento a la función imprimir_modelos(), 
# dentro de la función es referenciado como 'finalizados'. 
# Como finalizados es solo un ALIAS dentro de la función, cualquier cambio hecho dentro de la función
# afecta DIRECTAMENTE a la lista original 'modelos_completados' 
# porque es un objeto mutable pasado por referencia.

print(modelos_encargados) # Muestra la lista original de modelos encargados

'''### **Explicación del código paso a paso**

Este script simula el proceso de impresión de modelos en 3D, moviendo elementos de una lista de "encargos" a otra lista de "modelos completados". Al final, muestra los modelos que fueron impresos y verifica si la lista original de encargos se mantiene intacta.

---

## **1️⃣ Función `imprimir_modelos(encargos, finalizados)`**
Esta función simula la impresión de modelos 3D.

🔹 **Parámetros:**
- `encargos`: Lista de modelos pendientes de impresión.
- `finalizados`: Lista vacía que almacenará los modelos ya impresos.

🔹 **Proceso:**
- **Mientras la lista `encargos` no esté vacía**, se extrae el último elemento con `.pop()`.
- Se imprime un mensaje simulando la impresión del modelo.
- Se añade el modelo impreso a la lista `finalizados`.

## **2️⃣ Función `muestra_modelos_completados(finalizados)`**
Esta función muestra qué modelos han sido impresos.

🔹 **Parámetro:**
- `finalizados`: Lista de modelos que fueron impresos.

🔹 **Proceso:**
- Se imprime un mensaje indicando que los modelos han sido completados.
- Se recorre la lista `finalizados` y se imprimen los modelos.

```python
def muestra_modelos_completados(finalizados):
    print("\nLos siguientes modelos han sido impresos:")
    for modelo_finalizado in finalizados:
        print(modelo_finalizado)
```

**Ejemplo de salida:**  
```
Los siguientes modelos han sido impresos:
dodecahedron
robot pendant
iphone case
```

---

## **3️⃣ Definición de listas y ejecución del código principal**
Se definen las listas con modelos pendientes y una vacía para los modelos completados:

```python
modelos_encargados = ['iphone case', 'robot pendant', 'dodecahedron']
modelos_completados = []
```

Luego, se llama a `imprimir_modelos()` pasando **una copia de la lista** con `[:]` para evitar modificar la lista original:

```python
imprimir_modelos(modelos_encargados[:], modelos_completados)
```

Después, se llama a `muestra_modelos_completados()` para mostrar los modelos que fueron procesados:

```python
muestra_modelos_completados(modelos_completados)
```

Finalmente, se imprime la lista original `modelos_encargados` para verificar que sigue intacta:

```python
print("----")
print(modelos_encargados)
```

**Ejemplo de salida final:**  
```
Los siguientes modelos han sido impresos:
dodecahedron
robot pendant
iphone case
----
['iphone case', 'robot pendant', 'dodecahedron']
```

---

### **📌 Resumen de lo que hace este script**
1. **Toma una lista de modelos pendientes.**
2. **Imprime cada modelo en orden (simulación de impresión).**
3. **Mueve cada modelo a una lista de modelos completados.**
4. **Muestra qué modelos han sido impresos.**
5. **Verifica que la lista original de encargos no fue modificada.**

---

### **🛠️ Importancia en Backend**
✅ **Relevancia en backend: 75%**  
- **Manipulación de listas y estructuras de datos** es fundamental en cualquier backend.
- **Paso de parámetros por referencia o copia** es clave en programación segura.
- **Procesamiento de datos en lotes** es común en backend para manejar colas de trabajo (como en sistemas de impresión real o generación de reportes).

⚠️ **Advertencia:** En backend moderno, **el procesamiento de datos no se hace con listas en memoria** sino con bases de datos, colas de mensajes (RabbitMQ, Kafka) y almacenamiento persistente.  

🔹 **¿Cómo se aplicaría esto en backend real?**
- En lugar de listas, se usaría una **base de datos** (por ejemplo, PostgreSQL o MongoDB).
- Se manejaría una **cola de tareas** en lugar de un `while` (por ejemplo, con Celery en Python).
- Se haría una **API REST** para que un usuario pueda solicitar impresiones y ver su estado.

Si quieres que te muestre cómo hacerlo con bases de datos o colas de tareas reales, dime. 🚀'''