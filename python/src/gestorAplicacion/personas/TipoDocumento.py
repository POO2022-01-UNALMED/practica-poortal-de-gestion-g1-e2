from enum import Enum

class TipoDocumento(Enum):
    CC = "Cédula de Ciudadanía"
    CE = "Cédula de Extranjería"
    NIP = "Número de Identificación"
    TI = "Tarjeta de Identidad"
    PAP = "Pasaporte"