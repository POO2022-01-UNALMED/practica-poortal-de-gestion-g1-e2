from manejoErrores.errorListasVacias import ErrorListasVacias

class ClientesSinProductosEnCarrito(ErrorListasVacias):
    def __init__(self, message):
        super().__init__(message)