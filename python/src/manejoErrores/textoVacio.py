from manejoErrores.errorIngresoDatos import ErrorIngresoDatos

class TextoVacio(ErrorIngresoDatos):
    def __init__(self, message):
        super().__init__(message)