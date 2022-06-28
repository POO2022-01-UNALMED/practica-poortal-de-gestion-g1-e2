from manejoErrores.errorIngresoDatos import ErrorIngresoDatos

class DatoFueraDelRango(ErrorIngresoDatos):
    def __init__(self, message):
        super().__init__(message)