import os
os.system("clear")

'''✅ Modelo 3 extendido – Ejemplo 1: Uso de .split() y .join() para limpiar y normalizar texto
Función real de backend que normaliza una cadena separada por comas y devuelve una versión limpia, capitalizada y coherente
Cuando una API recibe texto separado por comas (como etiquetas, categorías, ingredientes, etc.), es habitual:
1.	Separar ese texto  .split(",")
2.	Limpiar cada parte  .strip().title()
3.	Unirlo de nuevo  .join(...)  con formato deseado
'''

def normalizar_texto (texto: str) -> str:
    lista_de_partes = texto.split(",")
    lista_de_partes_limpia = [p.strip().lower().title() for p in lista_de_partes]
    return ", ".join(lista_de_partes_limpia)

texto = "   tomAtE,lEchugAA,   cEbollA morAdA,ACEITE DE OLIVA   , vinagrE balsámico,   sAl mArinA, pimientA negrA,    quEso parmEsano rallado ,    nuEcEAs picadAs , pAn tostAdo  "

normalizacion = normalizar_texto(texto)
print(f'{normalizacion}')

