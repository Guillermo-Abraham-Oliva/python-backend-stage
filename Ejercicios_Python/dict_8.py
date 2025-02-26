import os  # (0%)
os.system('clear')  # (0%)

import sys  # (30%) 
# Para interrumpir eventualmente el flujo con ---> sys.exit()

##################################
###### REGISTRO DE PUNTAJES ######
##################################

'''Implementa un programa en Python que permita registrar y mantener un
seguimiento de los puntajes de un juego. El programa debe permitir a los
jugadores ingresar sus nombres y puntajes, almacenarlos en un
diccionario y proporcionar funcionalidades para mostrar el puntaje más
alto, el promedio de puntajes y la cantidad total de jugadores.'''

# Base de datos con puntajes
registros = {}    # (80%)
continuar = True  # (40%)

# Seguimiento de los puntajes --> actualizados
while continuar:  # (40%)
    # Pedir al usuario su nombre
    nombre = input("Ingrese nombre del jugador (o 'salir' para terminar): ")  # (0%)
    if nombre.lower() == 'salir':  
        continuar = False  
    else:
        puntaje = int(input("Ingrese el puntaje del jugador: "))  # (0%)
        registros[nombre] = puntaje  # (80%)

    # Obtener la CLAVE con que tiene el valor mas alto (en este caso: EL JUGADOR con puntaje más alto)
    # da solo el jugador con el ountaje mas alto (no el puntaje)
    # para esto, el unico camino es ---> max(diccio, key=diccio.get)
    jugador_mas_alto = max(registros, key=registros.get)#  ➝ Bob (por ej.)  (50%)
    # para recuperar el puntaje (valor):
    puntaje_mas_alto = registros[jugador_mas_alto]  #      ➝ 99  (por ej.)  (50%)
    print(f"Jugador: {jugador_mas_alto}, Puntaje: {puntaje_mas_alto}")

    # En cambio si usamos:
    puntaje_mas_alto = max(registros.values())
    print(puntaje_mas_alto)  # ➝ 200     (Pero... ¿de quién?)
    # da solo el puntaje (no el nombre del jugador)

    # ES DIFICIL Y CONTROVERSIAL PORQUE DICE key=diccio.get... y da el VALOR!
    # TAMPOCO MATARSE PORQUE NO ES TAN CRUCIAL A FUTURO (50%)
    
    # Obtener el promedio de puntajes
    total_puntajes = sum(registros.values())  # (50%)
    cantidad_jugadores = len(registros)  # (50%)
    promedio = total_puntajes / cantidad_jugadores  # (20%)
    print("Promedio de puntajes:", promedio)  # (0%)

    # Cantidad total de jugadores
    print("La cantidad de jugadores es:", cantidad_jugadores)  # (0%)

'''📌 Conclusión rápida:
✅ Este código no sirve en backend profesional.
✅ Debes aprender FastAPI + PostgreSQL en su lugar.'''