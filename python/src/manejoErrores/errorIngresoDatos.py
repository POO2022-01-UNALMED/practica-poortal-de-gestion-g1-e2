from manejoErrores.errorAplicacion import ErrorAplicacion

class ErrorIngresoDatos(ErrorAplicacion):
    def __init__(self, message):
        super().__init__("Error en el ingreso de datos: " + message)