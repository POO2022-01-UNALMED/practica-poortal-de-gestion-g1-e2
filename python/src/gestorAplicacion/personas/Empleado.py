from datetime import datetime

from gestorAplicacion.general.DiaSemana import DiaSemana  
from gestorAplicacion.ventas.Servicio import Servicio 
from gestorAplicacion.personas.Persona import Persona
from gestorAplicacion.personas.Contrato import Contrato
from gestorAplicacion.personas.TipoDocumento import TipoDocumento 
from gestorAplicacion.personas.Sexo import Sexo 

'''
# @author Alejandro Alvarez
# @author Alejandra Barrientos
# @author Mateo Alvarez
# @author Miguel Barrera'''

class Empleado(Persona):
    """
    Esta clase extiende de persona y se encarga de manejar los empleados de la
    aplicacion los cuales se usan para atender a los servicios, la creacion de
    facturas y manejar su proceso de contratacion.
    """

    def __init__(self, nombre : str, telefono : int, email : str, identificacion : int, tipoDeIdentificacion : TipoDocumento, sexo : Sexo, contrato : Contrato, cargo : str, servicio : Servicio, diasLaborales : 'list[DiaSemana]'):
        super().__init__(nombre, telefono, email, identificacion, tipoDeIdentificacion, sexo)
        self._contrato = contrato
        self._cargo = cargo
        self._servicio = servicio
        self._diasLaborales = diasLaborales


    def getContrato(self) -> Contrato:
        return self._contrato

    def setContrato(self, contrato) -> None:
        self._contrato = contrato

    def getCargo(self) -> str:
        return self._cargo

    def setCargo(self, cargo : str) -> None:
        self._cargo = cargo

    def getServicio(self) -> Servicio:
        return self._servicio

    def setServicio(self, servicio : Servicio) -> None:
        self._servicio = servicio

    def getDiasLaborales(self) -> 'list[DiaSemana]':
        return self._diasLaborales

    def setDiasLaborales(self, diasLaborales : 'list[DiaSemana]'):
        self._diasLaborales = diasLaborales

    def consultarDisponibilidadEmpleado(self, servicio : Servicio, fechaSolicitud : datetime) -> bool:
        """Verifica que el empleado que este activo, es decir, tenga un contrato
        vigente. Adicionalmente verifica si esta disponible en el dia solicitado,
        esto se hace segun el dia de la semana correspondiente."""
        disponible = False
        if (self._servicio == servicio and self.isActivo(fechaSolicitud)):
            for i in self._diasLaborales:
                if (i.value - 1 == (fechaSolicitud.weekday())):
                    disponible = True

        return disponible
    

    def isActivo(self, fecha : datetime = datetime.today()) -> bool:
        """Consulta si el contrato esta vigente en la fecha especificada"""
        return self._contrato.consultarVigencia(fecha)

    
    def mostrarInformacion(self) -> str:
        """Devuelve un texto con informacion del empleado dependiendo si tiene contrato
        vigente o no."""
        informacion = ""
        if (self.isActivo()):
            informacion = "Empleado con contrato vigente " + self._nombre + " con número de identificación: " + self._identificacion + ", con cargo: "+ self._cargo
        else:
            informacion = "Empleado sin contrato vigente " + self._nombre + " con número de identificación: " + self._identificacion + ", con cargo: "+ self._cargo
        return informacion

    
    def despedirE(self) -> None:
        """Establece el dia actual como fecha final del contrato para realizar su
        despido"""
        hoy = datetime.today()
        self._contrato.setFechaFin(hoy)
    
    
    def renovarContrato(self, fechaFin : datetime) -> None:
        """Establece una nueva fecha fin del contrato para alargar su vigencia"""
        if (fechaFin > self._contrato.getFechaFin()):
            self._contrato.setFechaFin(fechaFin)

    def contratar(self, contrato : Contrato, cargo : str, servicio : Servicio, diasLaborales : 'list[DiaSemana]'):
        if (not cargo == "x"):
            self.setCargo(cargo)
        
        if (servicio != None):
            self.setServicio(servicio)
        
        if (not diasLaborales.isEmpty()):
            self.setDiasLaborales(diasLaborales)
