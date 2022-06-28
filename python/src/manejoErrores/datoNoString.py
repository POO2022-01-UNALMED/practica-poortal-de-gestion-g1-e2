from manejoErrores.errorIngresoDatos import ErrorIngresoDatos

class DatoNoString(ErrorIngresoDatos):
    def __init__(self, message):
        super().__init__(message)