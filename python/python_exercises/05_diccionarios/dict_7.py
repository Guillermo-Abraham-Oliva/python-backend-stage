import os

os.system("clear")

import sys  # para interrumpir eventualmente el flujo con ---> sys.exit()

###################################
##### REGISTRO DE ASISTENCIAS #####
###################################

"""Eres un profesor y deseas realizar un seguimiento de la asistencia de tus
estudiantes a lo largo del semestre. Cada estudiante tiene un nombre y
una lista de fechas en las que asistió a clases. Implementa un programa
en Python que utilice un diccionario para almacenar la información de las
asistencias. El programa debe permitir registrar la asistencia de los
estudiantes, agregar nuevas fechas de asistencia y mostrar la lista de
estudiantes y las fechas en las que asistieron.
(Pista: puedes comenzar con un diccionario vacío y construir un
diccionario de listas) """

# diccionario base de datos
asistencias = dict()  # Esto es equivalente a asistencias = {}

# Registrar asistencias de estudiantes
# se agrega una clave EstudianteX y el valor es una Lista con 3 cadenas de texto
asistencias["Guillermo"] = ["2022-01-01", "2022-01-03", "2022-01-05"]
asistencias["Antonio"] = ["2022-01-02", "2022-01-05", "2022-01-07"]
asistencias["Paola"] = ["2022-01-01", "2022-01-07", "2022-01-09"]

# Agregar nuevas fechas de asistencia para un estudiante existente
asistencias["Guillermo"].append("2022-01-07")  # append es método de Listas
asistencias["Paola"].append("2022-01-09")  # append es método de Listas

# Mostrar la lista de estudiantes y las fechas en las que asistieron
print(f"\tRegistro de Asitencias:\n")
for estudiante, fechas in asistencias.items():
    print(f"Estudiante: {estudiante}\nAsistencias: {", ".join(fechas)}\n")
