from enum import Enum

'''
# @author Alejandro Alvarez
# @author Alejandra Barrientos
# @author Mateo Alvarez
# @author Miguel Barrera'''

class TipoDocumento(Enum):
    CC = "Cédula de Ciudadanía"
    CE = "Cédula de Extranjería"
    NIP = "Número de Identificación"
    TI = "Tarjeta de Identidad"
    PAP = "Pasaporte"