from manejoErrores.errorIngresoDatos import errorIngresoDatos

class DatoNoFecha(errorIngresoDatos):
    def __init__(self, message):
        super().__init__(message)