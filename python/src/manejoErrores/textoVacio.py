from manejoErrores.errorIngresoDatos import ErrorIngresoDatos

class TextVacio(ErrorIngresoDatos):
    def __init__(self, message):
        super().__init__(message)