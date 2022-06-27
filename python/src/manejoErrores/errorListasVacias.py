from manejoErrores.errorAplicacion import ErrorAplicacion

class ErrorListasVacias(ErrorAplicacion):
    def __init__(self, message):
        super().__init__("Error por lista vacia: " + message)