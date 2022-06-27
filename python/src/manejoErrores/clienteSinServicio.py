from manejoErrores.errorListasVacias import ErrorListasVacias

class ClienteSinServicio(ErrorListasVacias):
    def __init__(self, message):
        super().__init__(message)