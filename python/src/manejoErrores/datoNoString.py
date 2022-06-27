from manejoErrores.errorIngresoDatos import errorIngresoDatos

class DatoNoString(errorIngresoDatos):
    def __init__(self, message):
        super().__init__(message)