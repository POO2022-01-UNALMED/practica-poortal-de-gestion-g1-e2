from manejoErrores.errorIngresoDatos import errorIngresoDatos

class DatoNoDigito(errorIngresoDatos):
    def __init__(self, message):
        super().__init__(message)