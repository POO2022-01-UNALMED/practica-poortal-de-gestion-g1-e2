from manejoErrores.errorIngresoDatos import errorIngresoDatos

class DatoFueraDelRango(errorIngresoDatos):
    def __init__(self, message):
        super().__init__(message)