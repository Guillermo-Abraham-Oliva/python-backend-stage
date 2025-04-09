### 🔹 Concepto de JSON:
# JSON (JavaScript Object Notation) es un formato de texto 
# **para almacenar y transmitir datos** en forma de **diccionarios y listas**

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