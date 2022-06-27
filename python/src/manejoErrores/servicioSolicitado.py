from manejoErrores.errorIngresoDatos import errorIngresoDatos

class ServicioSolicitado(errorIngresoDatos):
    def __init__(self, message):
        super().__init__(message)