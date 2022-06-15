from general import DiaSemana 
from general import Inventario 
from ventas import Servicio

class Persona:

    def __init__(self, nombre, telefono, email, identificacion, tipoDeIdentificacion, sexo):
        self._nombre = nombre
        self._telefono = telefono
        self._email = email
        self._identificacion = identificacion
        self._mesesGarantia = tipoDeIdentificacion
        self._sexo = sexo
        Inventario.agregarPersona(self)

    def getNombre(self):
        return self._nombre  
    def setNombre(self, nombre):
        self._nombre = nombre

    def getTelefono(self):
        return self._telefono  
    def setTelefono(self, telefono):
        self._telefono = telefono

    def getEmail(self):
        return self._email  
    def setEmail(self, email):
        self._email = email

    def getIdentificacion(self):
        return self._identificacion  
    def setIdentificacion(self, identificacion):
        self._identificacion = identificacion

    def getTipoDeIdentificacion(self):
        return self._tipoDeIdentificacion  
    def setTipoDeIdentificacion(self, tipoDeIdentificacion):
        self._nombre = tipoDeIdentificacion
    
    def getSexo(self):
        return self._sexo  
    def setSexo(self, sexo):
        self._sexo = sexo

    def mostrarInformacion(self):
        return "Soy " + self._nombre + "con número de identificación: " + self._identificacion

    
	