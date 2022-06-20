from datetime import datetime

class Documento:
    def __init__(self, fecha = datetime.today()) -> None:
        self.fechaExpedicion = fecha

    def getFechaExpedicion(self):
        return self.fechaExpedicion

    def generarIdentificador(self):
        pass