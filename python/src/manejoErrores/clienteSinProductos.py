from manejoErrores.errorListasVacias import ErrorListasVacias

class ClienteSinProducto(ErrorListasVacias):
    def __init__(self, message):
        super().__init__(message)