from manejoErrores.errorIngresoDatos import errorIngresoDatos

class TextVacio(errorIngresoDatos):
    def __init__(self, message):
        super().__init__(message)