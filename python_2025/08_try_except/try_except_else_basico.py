import os
os.system("clear")

### EXPLICACION MAS PRACTICA ###
# 1) antes de la accion riesgosa ponemos TRY ---> TRATAMOS DE HACER ALGO RIEGOSO
# 2) luego escribimos lo que sucede si hay dramas ---> metemos tantos EXCEPT como necesitemos para contemplar errores. Los EXCEPT son "barreras/breaks" para que no siga el flujo hacia abajo si no se cumplen condiciones
# 3) escribimos el codigo a ejecutar en caso de estar todo ok con el ELSE

try:
    # intentamos algo 'riesgoso'como leer, ingresar, calcular, acceder, etc...
except ZeroDivisionError:
    print("Error: No se puede dividir por cero.")
except ValueError:
    print("Error: Solo se permiten números enteros.")
except FileNotFoundError:
    print("Fichero no encontrado.")
else:
    # procedemos con el script porque ya nos hemos asegurado qeu está todo ok...


# ## ¿Para qué sirven `try`, `except` y `else` en Python?

# Cuando ejecutás código que **podría fallar**, como leer un archivo o dividir entre números, usás `try` para **intentar** que funcione sin errores.  
# Si **ocurre un error**, Python salta al bloque `except` para **manejarlo sin que el programa se rompa**.  
# Y si **todo va bien**, se ejecuta el bloque `else`.

### Ejemplo práctico: división entre dos números

try:
    num1 = int(input("Ingrese el primer número: "))
    num2 = int(input("Ingrese el segundo número: "))
    resultado = num1 / num2  # Esto puede fallar si num2 es 0
except ZeroDivisionError:
    print("Error: No se puede dividir por cero.")
except ValueError:
    print("Error: Solo se permiten números enteros.")
else:
    print(f"Resultado: {resultado}")
