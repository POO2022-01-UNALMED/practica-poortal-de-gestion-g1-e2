from manejoErrores.errorAplicacion import ErrorAplicacion

class errorIngresoDatos(ErrorAplicacion):
    def __init__(self, message):
        super().__init__("Error en el ingreso de datos: " + message)