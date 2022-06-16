from datetime import datetime

class Documento:
    def _init_(self, fecha = datetime.today()) -> None:
        self.fechaExpedicion = fecha

    def getFechaExpedicion(self):
        return self.fechaExpedicion

    def generarIdentificador(self):
        pass