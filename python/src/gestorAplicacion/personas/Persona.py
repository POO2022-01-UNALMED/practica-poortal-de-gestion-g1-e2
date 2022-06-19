from gestorAplicacion.general.DiaSemana import DiaSemana
from gestorAplicacion.personas.Contrato import Contrato
from gestorAplicacion.ventas.Servicio  import Servicio

class Persona:

    def __init__(self, nombre, telefono, email, identificacion, tipoDeIdentificacion, sexo):
        from gestorAplicacion.general.Inventario import Inventario
        self._nombre = nombre
        self._telefono = telefono
        self._email = email
        self._identificacion = identificacion
        self._tipoDeIdentificacion = tipoDeIdentificacion
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

    def contratar(self, contrato: Contrato, cargo: str, servicio: Servicio, diasLaborales: list[DiaSemana]):
        from gestorAplicacion.general.Inventario import Inventario
        from gestorAplicacion.personas.Empleado import Empleado 
        Empleado(self._nombre, self._telefono, self._email, self._identificacion, self._tipoDeIdentificacion, self._sexo, contrato, cargo, servicio, diasLaborales)
        Inventario.eliminarPersona(self)
	