import os
os.system('clear')

"""Este script define una función `construir_perfil()` que crea un diccionario con la información de un usuario.

📌 Funcionamiento:
1. Recibe un nombre y un apellido como parámetros 'obligatorios'.
2. Puede recibir un número **variable** de pares 'clave-valor' adicionales
gracias a `**informacion_usuario`, los cuales se almacenan como un diccionario.
3. Crea un diccionario `perfil` donde almacena los datos.
4. Itera sobre los argumentos adicionales (`**informacion_usuario`)
y los añade al diccionario `perfil`.
5. Devuelve el diccionario con toda la información del usuario.

Este método es útil cuando se quiere almacenar información flexible sobre un usuario sin necesidad de definir un número fijo de parámetros."""

'''✅ Utilidad en backend profesional con herramientas modernas: 70%

- El uso de `**kwargs` en funciones es una técnica fundamental en Python para manejar argumentos flexibles y es común en **FastAPI**, **Flask**, y otras herramientas de backend.  
- Sin embargo, en backend real, no construirás perfiles manualmente con diccionarios; en su lugar, usarás **ORMs como SQLAlchemy o Pydantic** para manejar datos estructurados.  

⚠️ **Advertencia**: Aunque este método sigue siendo válido para pequeñas transformaciones de datos, en backend profesional **no gestionarás perfiles de usuario con diccionarios puros**.  
✅ Aprende lo justo:
- Entiende `**kwargs`, ya que lo verás en frameworks modernos.  
- Para almacenamiento de datos en backend real, usa **SQLAlchemy (para bases de datos) o Pydantic (para validación de datos en FastAPI)**.  
- En lugar de `pprint()`, en backend moderno se usan logs estructurados con **logging o herramientas como Loguru**.  

🔹 **Reemplazo en backend real**:  
- 🔹 **Pydantic (FastAPI)** para validación de datos en APIs.  
- 🔹 **SQLAlchemy** para manipular datos en bases de datos relacionales en vez de diccionarios manuales.  
- 🔹 **JSON para comunicación entre servicios (en vez de diccionarios Python en memoria).**'''


###### VERSION BASICA #########  ---> 30%

def registro(nombre, apellido, **datos_varios):
    perfil_cliente = {}
    perfil_cliente ["nombre"] = nombre
    perfil_cliente ["apellido"] = apellido
    for clave, valor in datos_varios.items():
        perfil_cliente [clave] = valor
    return perfil_cliente

# Crear un nuevo perfil de cliente
fichero_cliente = registro("guillermo", "abraham oliva", 
         habilidad="pianista", 
         curiosidad_1="espiritualista",
         curiosidad_2="tiene un grupo altruista en facebook",
         proxima_residencia="Oropesa del mar")

# Imprimir el perfil con formato
for clave, valor in fichero_cliente.items():
    print(f" {clave.title()} -> {valor.title()}")
print(f"\n------------------------------------------\n")


###### VERSION MEJORADA #########  ---> 50%

fichero_cliente = {}

def registro(nombre, apellido, **datos_varios):
    perfil_cliente = {
        "nombre": nombre,
        "apellido": apellido
    }
    perfil_cliente.update(datos_varios)  #  ¡ UPDATE !  Agrega todas las claves de golpe!
    return perfil_cliente

# Crear un nuevo perfil de cliente
fichero_cliente = registro("guillermo", "abraham oliva",
                           habilidad="pianista",
                           curiosidad_1="espiritualista",
                           curiosidad_2="tiene un grupo altruista en facebook",
                           proxima_residencia="Oropesa del mar")

# Imprimir el perfil con formato
for clave, valor in fichero_cliente.items():
    print(f" {clave.title()} -> {valor.title()}")