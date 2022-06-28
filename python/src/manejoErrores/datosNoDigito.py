from manejoErrores.errorIngresoDatos import ErrorIngresoDatos

class DatoNoDigito(ErrorIngresoDatos):
    def __init__(self, message):
        super().__init__(message)