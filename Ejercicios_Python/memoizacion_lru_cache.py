import os
os.system('clear')

'''
📌 lru_cache es un decorador de la biblioteca estándar de Python (functools).
📌 Se usa para guardar en caché los resultados de una función y evitar recalcular valores repetidos.

@lru_cache(maxsize=None)
📌 ¿Qué hace?

Guarda los valores de las llamadas previas a la función en memoria (RAM).
Si la función se llama con un valor ya calculado, lo devuelve directamente desde la caché en lugar de recalcularlo.
maxsize=None significa que la caché no tiene límite (guarda todos los resultados posibles) esto puede ser un 🔴 Peligro en backend. Se recomienda usar un límite: @lru_cache(maxsize=1000)


'''
from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci_cache(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_cache(n-1) + fibonacci_cache(n-2)

# 📌 Si n > 1, llama recursivamente a la función para calcular fibonacci(n-1) + fibonacci(n-2).
# 📌 Gracias a @lru_cache, no vuelve a calcular los valores repetidos.

'''
⚠️ ¿Se usa en backend profesional?
🔹 En producción NO se usa lru_cache porque la caché:

- Se borra al reiniciar el servidor.
- No es compartida entre múltiples instancias en backend distribuido.

✅ Alternativa moderna en backend: Usar Redis en FastAPI o Django.

🔹   Uso en backend profesional: ---> 10%
⚠️ **Advertencia:** El decorador `@lru_cache` es útil para **memorización en cálculos repetitivos**, pero **en backend real se usan Redis o bases de datos cacheadas en lugar de esto**.  

✅ **Úsalo para:**  
✔️ Optimizar funciones de alto costo computacional en scripts pequeños.  

❌ **Evítalo cuando:**  
❌ Necesites persistencia real de caché en backend (usa Redis, Memcached o FastAPI con `Depends`).  
❌ Quieras manejar caché en múltiples instancias de un servidor.  

📌 **Conclusión:** Solo aprende lo justo sobre `@lru_cache`. **En backend real, usa Redis para almacenamiento en caché eficiente.**
'''