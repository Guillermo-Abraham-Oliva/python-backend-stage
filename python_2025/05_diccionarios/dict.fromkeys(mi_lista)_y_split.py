import os
os.system("clear")

'''
Aprendo:
1)  dict.fromkeys() 
es un método que internamente transforma a diccionario y usando las claves elimina duplicados conservando el orden (a diferencia de set que desordena)

2)  .split() 
es un metodo que trabaja CON LISTAS !!!
osea, devuelve una lista!

puede elegirse cualquier separador, 
el más usado el es el ESPACIO,
pero los mas usados son:
.split(" ")  60%
.split(",")  20%
.split("|")  8%
.split("\n") 6%
'''

def Split(texto: str): # funcion que esplitea
    lista = texto.split(",") # esplitear por cada coma (,)
    lista = [letra.strip() for letra in lista]  # 🔥 Limpiar espacios
    return lista

texto = "A, A, A, B, B, B, C, D, E"
print(f'texto original: {texto}')

lista_split = Split(texto) # ejecuta la funcion que esplitea
print(f'Split::: {lista_split}')

lista_split_sin_rep = list(dict.fromkeys(lista_split)) # AQUI ESTA LA LECCION
print(f'Split y sin repetidos::: {lista_split_sin_rep}')

