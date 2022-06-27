from manejoErrores.errorListasVacias import ErrorListasVacias

class ClientesSinCarrito(ErrorListasVacias):
    def __init__(self, message):
        super().__init__(message)