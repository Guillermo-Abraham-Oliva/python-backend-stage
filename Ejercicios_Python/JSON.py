### 🔹 Concepto de JSON:
# JSON (JavaScript Object Notation) es un formato de texto 
# **para almacenar y transmitir datos** en forma de **diccionarios y listas**


# Ej simple json:

import json

numeros = [2, 3, 5, 7, 11, 13]
filename = 'numeros.json'  # Aquí decides cómo se va a llamar el archivo
with open(filename, 'w') as f_obj:  # Abre (o crea) un archivo con ese nombre en modo escritura.
    json.dump(numeros, f_obj) # Convierte la lista de Python a texto JSON



#########################################################################################
#### **1️⃣ Crear un archivo JSON con `json.dump`**

import json

# Datos en forma de diccionario (un objeto JSON)
persona = {"nombre": "Guillermo",
           "edad": 51,
           "ciudad": "Alicante"}

# Guardar el diccionario en un archivo JSON
with open("datos.json", "w") as archivo:
    json.dump(persona, archivo)

# ✔ Esto crea un archivo `datos.json` con el contenido:
        # {"nombre": "Guillermo",
        #  "edad": 51,
        #  "ciudad": "Alicante"}

#########################################################################################
#### **2️⃣ Leer el archivo JSON con `json.load`**

# Leer el JSON desde el archivo
with open("datos.json", "r") as archivo:
    datos_cargados = json.load(archivo)

print(datos_cargados)  # {'nombre': 'Guillermo', 'edad': 51, 'ciudad': 'Alicante'}
print(datos_cargados["nombre"])  # Guillermo


### 🔹 Explicación:
# - **`json.dump(objeto, archivo)`** → Guarda un objeto Python en un archivo JSON.
# - **`json.load(archivo)`** → Carga datos JSON desde un archivo y lo convierte en un diccionario Python.

#########################################################################################
### 🔹 **3️⃣ `json.loads()` (💎 LA MÁS USADA: 95%)**  
# ✅ **Se usa para convertir JSON recibido en una API en un diccionario Python.**

import json

json_string = '{"usuario": "Guillermo", "edad": 51}'
data = json.loads(json_string)

print(data["usuario"])  # Guillermo

# 📌 **Caso real:** API recibe un JSON y lo convierte en un diccionario.

#########################################################################################
### 🔹 **4️⃣ `json.dumps()` (🔥 Segunda más usada: 85%)**  
# ✅ **Se usa para convertir datos Python en JSON antes de enviarlos en una API.**

import json

persona = {"nombre": "Guillermo", "edad": 51}
json_string = json.dumps(persona)

print(json_string)  # '{"nombre": "Guillermo", "edad": 51}'


#########################################################################################
# 🔴 **🚨 Advertencia:** No almacenes datos importantes en archivos JSON en backend profesional. Usa **PostgreSQL o Redis** en su lugar.
#########################################################################################