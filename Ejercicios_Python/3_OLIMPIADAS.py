'''
En la competición de skeleton de las olimpiadas de invierno 
hay tres finalistas. 
El cronómetro mide los siguientes tiempos:

    Hannah Neise: 8 minutos 3 segundos y 10 centésimas
    Jackie Narracott: 12 minutos 7 segundos y 8 centésimas
    Kimberley Bos: 9 minutos 14 segundos y 3 centésimas

1. Crea un script que pida los tiempos por pantalla
para cada uno de los finalistas.-
2. Convierte los tiempos de minutos-segundos-centésimas a segundos.-
3. Sabiendo que la pista es de 100 metros calcula la velocidad media
de cada uno de ellos en metros por segundo.-
4. Imprime los resultados por pantalla.-
'''
###########################################################################
# se piden los 3 datos de Hannah Neise (en cadena de texto):
print('\n\nSeparados por espacio, ingresa: minutos, segundos y centésimas de')
Hannah_datos = input('\tHannah Neise: ').replace('.', ' ').replace(',', '').replace(';', ' ')

# se piden los 3 datos de Jackie Narracott (en cadena de texto):
print('\n\nSeparados por espacio, ingresa: minutos, segundos y centésimas de')
Jackie_datos = input('\tJackie Narracott: ').replace('.', ' ').replace(',', '').replace(';', ' ')

# se piden los 3 datos de Kimberley Bos (en cadena de texto):
print('\n\nSeparados por espacio, ingresa: minutos, segundos y centésimas de')
Kimberley_datos = input('\tKimberley Bos: ').replace('.', ' ').replace(',', '').replace(';', ' ')

##########################################################################
# se pasan a enteros los 3 datos de la cadena de texto de c/u de las atletas:
Hannah_min, Hannah_sec, Hannah_cent = map(int, Hannah_datos.split())
Jackie_min, Jackie_sec, Jackie_cent = map(int, Jackie_datos.split())
Kimberley_min, Kimberley_sec, Kimberley_cent = map(int, Kimberley_datos.split())

####################  se convierte todo a segundos  ######################
Hannah_segundos_totales = ((Hannah_min*60) + Hannah_sec + (Hannah_cent/100))
Jackie_segundos_totales = ((Jackie_min*60) + Jackie_sec + (Jackie_cent/100))
Kimberley_segundos_totales = ((Kimberley_min*60) + Kimberley_sec + (Kimberley_cent/100))

####################  calculo de la velocidad media  #####################
Hannah_veloc_media = (100/Hannah_segundos_totales)
Jackie_veloc_media = (100/Jackie_segundos_totales)
Kimberley_veloc_media = (100/Kimberley_segundos_totales)

###################  impresion de resultados  ############################
print('\n\n--- Segundos totales de las atletas ---\n')
print(f'Hannah Neise: {Hannah_segundos_totales:.3f} segundos.-')
print(f'Jackie Narracott: {Jackie_segundos_totales:.3f} segundos.-')
print(f'Kimberley Bos: {Kimberley_segundos_totales:.3f} segundos.-')

print('\n\n--- Velocidad Media de las atletas ---\n')
print(f'Hannah Neise: {Hannah_veloc_media:.3f} metros por segundo.-')
print(f'Jackie Narracott: {Jackie_veloc_media:.3f} metros por segundo.-')
print(f'Kimberley Bos: {Kimberley_veloc_media:.3f} metros por segundo.-')

