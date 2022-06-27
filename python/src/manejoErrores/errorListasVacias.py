from manejoErrores.errorAplicacion import ErrorAplicacion

class errorListasVacias(ErrorAplicacion):
    def __init__(self, message):
        super().__init__("Error por lista vacia: " + message)