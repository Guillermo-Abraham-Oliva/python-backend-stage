import os
os.system('clear')

import sys # para interrumpir eventualmente el flujo con ---> sys.exit()

###################################
### ADMINISTRACIÓN DE PROYECTOS ###
###################################

'''Eres un gerente de proyectos y necesitas un programa para administrar
las tareas y responsabilidades de tu equipo. Cada tarea tiene un nombre,
una descripción y un responsable asignado. Implementa un programa en
Python que utilice un diccionario para almacenar la información de las
tareas. El programa debe permitir agregar nuevas tareas, asignar
responsables a las tareas existentes, actualizar las descripciones de las
tareas y mostrar la lista completa de tareas y responsables.
(Pista: puedes comenzar con un diccionario vacío y construir un
diccionario de diccionarios) 
'''

# diccionario vacío 'tareas'
tareas = {}

# Agregar 3 tareas nuevas: 3 claves con sus respectivos valores (que son diccios)
tareas["Tarea1"] = {"descripcion": "Realizar analisis de requisitos", "responsable": "Juan"}
tareas["Tarea2"] = {"descripcion": "Desarrollar funcionalidad principal", "responsable": "Marta"}
tareas["Tarea3"] = {"descripcion": "Realizar validacion de proceso", "responsable": "Jacobo"}

# imprimir el diccio original
for clave, valor in tareas.items():
    print(f'{clave}: {valor['descripcion']}, Responsable: {valor['responsable']}')

print(f'\n------------------------------------\n')

# Asignar responsables a las tareas existentes
tareas["Tarea1"]["responsable"] = "Elena"
tareas["Tarea3"]["responsable"] = "Maria"

# Actualizar las descripciones de las tareas
tareas["Tarea2"]["descripcion"] = "Realizar test de hiperparametros"

# imprimir el diccio actualizado
for clave, valor in tareas.items():
    print(f'{clave}: {valor['descripcion']}, Responsable: {valor['responsable']}')


