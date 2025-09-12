# main.py
from fastapi import FastAPI
from routes import archivo_de_routes
app = FastAPI()
app.include_router(archivo_de_routes.router)

# Carpeta: routes / archivo_de_routes.py
from fastapi import APIRouter
from services.archivo_de_services import funcion_logica_pura
router = APIRouter()
@router.get("/endpoint")
def controlador(param1: str, param2: int, param3:float, param4:bool):
    calculo = funcion_logica_pura(param1, param2, param3, param4)
    return {"resultado": calculo}

# Carpeta: services / archivo_de_services.py
def funcion_logica_pura(param1: str, param2: int, param3: float, param4: bool) -> dict:
    resultado = (param2 * param3)
    return {"nombre": param1, "resultado": resultado, "logueado": param4}


##################################################################################################
def convertir_a_entero(texto: str) -> int:
    try:
        return int(texto)
    except ValueError:
        raise ValueError("El valor debe ser un número entero válido.")

##################################################################################################

# main.py
from fastapi import FastAPI
from routes import archivo_de_routes
app = FastAPI
app.include_router(archivo_de_routes.router)

# routes/archivo_de_routes.py
from fastapi import APIRouter
from services.archivo_de_services import funcion_logica_pura
router = APIRouter
@router.get("/registrar")
def registrar_usuario (nombre: str, edad: int):
    validar_edad(edad)
    return {"mensaje": f'Usuario {nombre} registrado correctamente'}

# services/archivo_de_services.py
def validar_edad (edad: int) -> None:
    if edad <= 18:
        raise ValueError("Debes ser mayor de edad")

def calcular_pago (hora:float, tarifa: float) -> float:
    if horas <= 0 or tarifa <= 0:
        raise ValueError("Las horas y la tarifa deben ser valores positivos.")
    try:
        return horas * tarifa
    
##########################################################
def ver_analisis (nombre: str = "guille", activo: bool = True, edad: int = 51):
    


################################################
def tiene_acceso(rol: str) -> bool:
    return rol in ["admin", "editor"]




