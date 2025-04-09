import os
os.system("clear")

lista = []

# ENUMERATE ---> ENUMERA simplemente los elementos de una listas, tuplas, strings, etc!

'''Enumerate() = devuelve pares (índice, elemento).
Siempre necesitás 2 variables para capturar sus resultados.
Sirve cuando querés numerar los valores.'''

## 🧠 1. En **abstracto** para comprender la estructura de `enumerate()`

for contador, cosa in enumerate(lista, comienza=1)

# concretamente queda asi:
for índice, elemento in enumerate(lista, start=1):

    # - `enumerate()` genera **pares**: (índice, elemento).
    # - `índice` → número de posición (por defecto empieza en 0).
    # - `elemento` → valor que hay en esa posición de la lista.


# 📘 2. Características de `enumerate()`

# 1. **Devuelve siempre 2 valores** por vuelta:  
#    → un **número** (el índice) y el **elemento real**.

# 2. Podés elegir **desde qué número empieza**:  
#    enumerate(lista, 1)  # empieza desde 1

# 3. Es ideal cuando necesitás:
#    - **mostrar el orden de los ítems**.
#    - **acceder al valor y su posición al mismo tiempo**.
#    - **evitar usar un contador manual con `i = 0`**.

# 4. Solo funciona con estructuras **iterables**: listas, tuplas, strings, etc.


# Veamos el mismo código **con** y **sin** `enumerate()`:

### ❌ Sin `enumerate()` (contador manual)
colores = ["rojo", "verde", "azul"]
i = 1
for color in colores:
    print(f"{i}. {color}")
    i += 1

### ✅ Con `enumerate()` (más limpio y profesional)
colores = ["rojo", "verde", "azul"]
for i, color in enumerate(colores, start=1):
    print(f"{i}. {color}")

    ### Resultado de ambos:
            # 1. rojo
            # 2. verde
            # 3. azul

# El resultado es el mismo, pero `enumerate()` lo hace con menos líneas, más claro y sin error posible al olvidar el `i += 1`.


