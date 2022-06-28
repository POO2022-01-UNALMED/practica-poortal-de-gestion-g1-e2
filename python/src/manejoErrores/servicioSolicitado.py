from manejoErrores.errorIngresoDatos import ErrorIngresoDatos

class ServicioSolicitado(ErrorIngresoDatos):
    def __init__(self, message):
        super().__init__(message)