from datetime import datetime

'''# Clase para crear un documento
# @author Alejandro Alvarez
# @author Alejandra Barrientos
# @author Mateo Alvarez
# @author Miguel Barrera'''

class Documento:
    def __init__(self, fecha = datetime.today()) -> None:
        self.fechaExpedicion = fecha

    def getFechaExpedicion(self):
        return self.fechaExpedicion

    def generarIdentificador(self):
        pass