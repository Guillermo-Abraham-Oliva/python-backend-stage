# Parent_&_Child_Class_(Superclass_y_Subclass)
# HERENCIA: la clase hijo hereda los atributos de la clase padre

class coche:  # Clase 'PADRE'
    def __init__(self, marca: str, modelo: str, anio: int, cuentakilometros: int):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.cuentakilometros = cuentakilometros

    def actualiza_cuentakilometros(self, cuentakilometros):
        kilometros = int(input(f"Ingresa kilometros: "))
        if kilometros <= self.cuentakilometros:
            print(f"No puedes ingresar km inferiores")
        else:
            self.cuentakilometros = kilometros

class coche_electrico(coche):  # Clase 'HIJO'  // va entre parentesis la 'clase Padre' ***POR SER CLASE HIJO!!!
    def __init__(self, marca: str, modelo: str, anio: int, cuentakilometros: int, carga_wattios: int):
        super().__init__(marca, modelo, anio, cuentakilometros) # ésta es la linea que se le agrega ***POR SER CLASE HIJO!!!
        self.carga_wattios = carga_wattios #En coche_electrico solo agregas lo nuevo y específico (carga_wattios) porque no se necesita repetir código: La HERENCIA te da los atributos ya hechos (definidos en la Clase PADRE 'coche') marca, modelo, anio, cuentakilometros. 