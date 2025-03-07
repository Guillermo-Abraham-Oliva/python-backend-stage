'''En Python (y otros lenguajes dinámicos como JavaScript o Ruby)

Los objetos mutables (listas, diccionarios, conjuntos) 
se pasan por referencia y SE MODIFICAN DENTRO DE LA FUNCION sin necesidad de 'return'.
Los objetos inmutables (números, strings, tuplas) 
no se pueden modificar directamente dentro de una función, 
a menos que los reasignes con 'return'.

Recuerda esta regla de oro en Python:

🔹 Si pasas un objeto mutable (listas, diccionarios, conjuntos) a una función,
se modificará directamente sin necesidad de return.
🔹 Si pasas un objeto inmutable (números, strings, tuplas),
la función no lo podrá modificar a menos que uses return.

Esto es súper importante cuando empieces a trabajar en backend con bases de datos, APIs y estructuras en memoria. Si no tienes cuidado, puedes modificar datos sin darte cuenta'''

####### Ejemplo en Python con lista mutable: ##################################################
# 🔹 Paso por referencia en objetos mutables:
# Cuando pasas una lista, un diccionario o un conjunto a una función en Python, lo que realmente pasas es una referencia al mismo objeto en memoria.
# Esto significa que la función puede modificar ese objeto directamente, y los cambios serán visibles fuera de la función.
def modificar_lista(lista):
    lista.append(4)  # Modifica la lista original
    
mi_lista = [1, 2, 3]
modificar_lista(mi_lista) # Ejecuta la función pasandole como parámetro la lista
# Entonces lo que la función hace es MODIFICAR LA LISTA DIRECTAMENTE
# esto es porque Python modifica directamente! (no es como Pseint, Java o C)
print(mi_lista)  # Salida: [1, 2, 3, 4] (se modificó la Lista sin necesidad de 'return')
###############################################################################################


####### Ejemplo en Python con entero inmutable: ###############################################
# 🔹 Paso por valor (o referencia a objeto inmutable):
# Si pasas un número, una cadena o una tupla, la función recibe una referencia al objeto, pero como estos son inmutables, cualquier modificación crea un nuevo objeto en memoria en lugar de modificar el original.
# Para reflejar el cambio fuera de la función, tienes que hacer un return y reasignarlo.

def modificar_numero(n):
    n = n + 1  # Crea un nuevo objeto en memoria
    return n   # Devuelve el nuevo valor

num = 5
num = modificar_numero(num)  # Hay que reasignar el valor
print(num)  # Salida: 6
###############################################################################################