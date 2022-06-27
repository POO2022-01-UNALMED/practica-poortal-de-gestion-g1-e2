from manejoErrores.errorIngresoDatos import errorIngresoDatos

class TextVacio(errorIngresoDatos):
    def __init__(message):
        super.__init__(message)