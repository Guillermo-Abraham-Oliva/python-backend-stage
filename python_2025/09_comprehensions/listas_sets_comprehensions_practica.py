###########################################
########## CONSIGNAS DIVERSAS #############
###########################################


prod = [
    {"nombre": "Teclado", "precio": 25, "disponible": True},
    {"nombre": "Ratón", "precio": 15, "disponible": True},
    {"nombre": "Pantalla", "precio": 200, "disponible": False},
    {"nombre": "Cables", "precio": 5, "disponible": True},
    {"nombre": "Auriculares", "precio": 18, "disponible": False},
]

baratos_disponibles = []

# ordena diccios completos que valen < 20:
orden = sorted([p for p in prod if p["disponible"] and p["precio"] < 20], key=lambda o: o["precio"])
# [{'nombre': 'Cables', 'precio': 5, 'disponible': True},
# {'nombre': 'Ratón', 'precio': 15, 'disponible': True}]

# Da el nombre de 'todos' los productos ordenados por barato
orden = [p["nombre"] for p in sorted(prod, key=lambda o: o["precio"])]
# ['Cables', 'Ratón', 'Auriculares', 'Teclado', 'Pantalla']

# Esto arroja SOLO los nombres de los productos < 20
nomb_prod_ord_barato = [p["nombre"] for p in sorted(prod, key=lambda o: o["precio"]) if p["disponible"] and p["precio"] < 20]
# ['Cables', 'Ratón']


#########################################################################
# Crea un programa que gestione una lista de precios de productos, actualizando automáticamente los valores con un 21 % de IVA, eliminando los precios duplicados y mostrando la lista final ordenada de menor a mayor. Este ejercicio entrena **los métodos más usados y útiles con listas en el trabajo real (España, 2025): `append()`, `set()`, `sorted()`, `list comprehension`, y operaciones con expresiones lambda.


precios = [12.5, 7.99, 7.99, 22.3, 10.0]

# Con IVA, sin duplicados y ordenada

# Esta resolucion NO es buena porque hace un uso de set en sintaxis poco elegante y no redondea decimales
nueva = sorted(set(p*1.21 for p in precios))
# [9.6679, 12.1, 15.125, 26.983]

# Pero a Set hay que ABREVIARLO SIEMPRE CON { }
# y ademas, apliquemos round para mostrar mas elegante:
nueva = sorted({round(p * 1.21, 2) for p in precios})
# [9.67, 12.1, 15.12, 26.98]


#########################################################################

# Crea un programa que tome una lista de nombres, elimine los que estén vacíos o duplicados, los ordene alfabéticamente, y los convierta todos a mayúsculas. Este ejercicio entrena los métodos y operaciones más usados con listas en entornos reales (≈90 % de los casos): strip(), upper(), list comprehension, set(), sorted() y limpieza de datos.

nombres = [" Ana ", "ana", " jUaN ", "Juan  ", "", "  ", "123", "!!!", "!a"]

# Usa el operador MORSA := que asigna varios metodos a algo y luego se puede reutilizar la variable asignada sin necesidad de volver a repetir todo su contenido
nuevo = sorted({x.upper() for n in nombres if (x := n.strip().lower()).isalpha()})
# ['ANA', 'JUAN']

#########################################################################

# Crea un programa que tome una lista de números (positivos, negativos y cero) y filtre solo los positivos, los ordene de menor a mayor y elimine duplicados.
# Ejercicio útil y frecuente en procesamiento de datos, cálculos financieros y limpieza de listas numéricas.

nums = [5, -3, 0, 12, 5, 9, -1, 12, 8, 0]

orden = sorted({n for n in nums if n >= 0}, reverse=True)
# [12, 9, 8, 5, 0]

#########################################################################

# Tienes una lista de temperaturas diarias.
# Crea un programa que **muestre los días (índices) en los que la temperatura superó los 30 °C**, ordenados de menor a mayor temperatura y los almacene en un dict.

# *(día, temperatura)*, sin loops explícitos, solo comprensión y `enumerate`.

#   e = indice de enumerate
#   t = temperatura del dia

temps = [22, 31, 29, 35, 33, 28, 40]

# dict(...) transforma tuplas en pares clave-valor
dias = dict(sorted((e, t) for e, t in enumerate(temps, 1) if t > 30))
# {2: 31, 4: 35, 5: 33, 7: 40}

# Esto ordena por 'temperatura' (tomando aquellos dias que superaron los 30 °C)
dias = dict(sorted(((e, t) for e, t in enumerate(temps, 1) if t > 30), key=lambda o: o[1]))
# [(1, 31), (4, 33), (3, 35), (6, 40)]

#########################################################################

# Consigna y Objetivo:
# Tienes una lista de números enteros.
# Crea un programa que devuelva una nueva lista con los números multiplicados por 2, pero solo si son pares.

numeros = [3, 10, 7, 8, 5, 12]
nueva = [(n * 2) for n in numeros if n % 2 == 0]
# [20, 16, 24]

#########################################################################

# Tienes una lista de cadenas de texto (palabras).
# Crea un programa que devuelva una nueva lista con la longitud de cada palabra pero solo si la palabra tiene 'más' de 3 letras.

# Resultado esperado: [5, 8, 4]

palabras = ["sol", "luz", "tierra", "universo", "lago"]

longitudes = [len(p) for p in palabras if len(p) > 3]
# [5, 8, 4]

#########################################################################

# Tienes una lista de nombres con repeticiones y espacios extra.
# Crea un programa que devuelva una lista ORDENADA con los nombres ÚNICOS, pero solo aquellos cuyo nombre tenga una longitud mayor o igual a 4 letras.

nombres = ["  marta ", " aNa", " MArta ", "  iñigo ", " !a& "]

nomb_4_letras = sorted({n2 for n in nombres if len(n2 := n.strip().upper()) >= 4 and n2.isalpha()})
# ['IÑIGO', 'MARTA']

#########################################################################

# Crea un programa que devuelva una lista ORDENADA, con palabras ÚNICAS, 
# en minúsculas y de al menos 5 letras, usando:

palabras = ["  Camino ", "sol", "Tierra", "camino", "Correr ", "Sol", " mar "]

list_ord_min_may5 = sorted({p2 for p in palabras if (p2 := p.strip().lower()).isalpha() and len(p2) >= 5})
# ['camino', 'correr', 'tierra']

#########################################################################

# Tienes una lista de temperaturas como cadenas.
# Crea un programa que convierta cada valor a int(), seleccione SOLO los días pares (usando range), y devuelva una lista ORDENADA de tuplas (día, temperatura) con las que sean >= 30 °C.
# Debes usar: enumerate (con start=1), range(2, len(temps)+1, 2), int() y sorted().

temps = ["22", "31", "29", "35", "33", "28", "40"]

dias_calor_pares = sorted((indice, int(iterador)) for indice, iterador in enumerate(temps, start=1) if indice in range(2, len(temps) + 1, 2) and int(iterador) >= 30)
# [(2, 31), (4, 35)]

# lo mismo pero mas facil de entender (sin range ni len)
dias_calor_pares = sorted((indice, int(iterador)) for indice, iterador in enumerate(temps, 1) if int(indice) % 2 == 0 and int(iterador) >= 30)

#########################################################################

# Tienes una lista de precios como cadenas de texto.
# Crea un programa que convierta cada precio a float(), 
# se quede solo con los productos en posiciones impares (usando enumerate y el índice),
# y devuelva una lista ORDENADA de tuplas (posición, precio_con_iva),
# Usa: enumerate(), float(), round(), sorted(), y el operador morsa := para no repetir código.

precios = ["15.0", "20", "25.0", "30", "35.0", "40"]

# Versión 1 — sin morsa, más clara.
# Versión preferida el 90 % de los casos
nueva = sorted(
    (i, round(float(p) * 1.21, 2)) # redondea a 2 decimales
    for i, p in enumerate(precios, 1) # enumera desde el 1
    if i % 2 == 1)

# Versión 2 — con pasos previos (más didáctica)
# Usa tres pasos, más largo pero clarísimo.
# Ideal cuando estás aprendiendo o depurando.
pares = list(enumerate(precios, 1))
filtrados = [(i, float(p)) for i, p in pares if i % 2 == 1]
nueva = [(i, round(p * 1.21, 2)) for i, p in filtrados]
nueva.sort()

# Versión 3 — para ejercitar morsa. 
# Versión compleja y no muy preferible
nueva = sorted((i, (p2 := round(float(p), 2) * 1.21)) for i, p in enumerate(precios, start=1) if i % 2 == 1)

# [(1, 18.15), (3, 30.25), (5, 42.35)]

#########################################################################

# Tienes una lista de puntuaciones (algunas en texto y otras en número).
# Crea un programa que convierta todas las puntuaciones a int(),
# calcule su promedio redondeado con round(),
# y genere una lista ORDENADA de tuplas (posición, diferencia_respecto_promedio),
# donde posición proviene de enumerate().
# Usa: enumerate(), int(), round(), sorted().
# Resultado esperado: [(1, -3), (2, 0), (3, 2), (4, 1)]

puntuaciones = ["7", 10, "12", 13, "9", 8]
promedio = round(sum(int(pu) for pu in puntuaciones) / len(puntuaciones), 2)
# print(promedio) # 10

nuevo = sorted(((i, int(pu) - promedio) for i, pu in enumerate(puntuaciones, 1)), key=lambda o: o[1])
# print(nuevo) # [(1, -3), (6, -2), (5, -1), (2, 0), (3, 2), (4, 3)]
