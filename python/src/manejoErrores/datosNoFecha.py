from manejoErrores.errorIngresoDatos import ErrorIngresoDatos

class DatoNoFecha(ErrorIngresoDatos):
    def __init__(self, message):
        super().__init__(message)