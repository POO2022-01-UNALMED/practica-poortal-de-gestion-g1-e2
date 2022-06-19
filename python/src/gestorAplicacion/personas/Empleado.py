from datetime import datetime

from gestorAplicacion.general.DiaSemana import DiaSemana  
from gestorAplicacion.ventas.Servicio import Servicio 
from gestorAplicacion.personas.Persona import Persona
from gestorAplicacion.personas.Contrato import Contrato
from gestorAplicacion.personas.TipoDocumento import TipoDocumento 
from gestorAplicacion.personas.Sexo import Sexo 


# Esta clase extiende de persona y se encarga de manejar los empleados de la
# aplicacion los cuales se usan para atender a los servicios, la creacion de
# facturas y manejar su proceso de contratacion.

# @author Mateo Alvarez Lebrum
# @author Alejandro Alvarez Botero
# @author Miguel Angel Barrera Bustamante
# @author Alejandra Barrientos Grisales

class Empleado(Persona):

	# Este constructor se usa para la construccion generica de los empleados.
	
	# @param nombre
	# @param telefono
	# @param email
	# @param identificacion
	# @param tipoDeIdentificacion
	# @param sexo
	# @param contrato
	# @param cargo
	# @param servicio
	# @param diasLaborales
	
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

	# Verifica que el empleado que este activo, es decir, tenga un contrato
	# vigente. Adicionalmente verifica si esta disponible en el dia solicitado,
	# esto se hace segun el dia de la semana correspondiente.
	# 
	# @param servicio
	# @param fechaSolicitud
	# @return disponible
	
	def consultarDisponibilidadEmpleado(self, servicio : Servicio, fechaSolicitud : datetime) -> bool:
		disponible = False
		if (self._servicio == servicio and self.isActivo(fechaSolicitud)):
			for i in self._diasLaborales:
				if (i.ordinalDia - 1 == (fechaSolicitud.weekday())):
					disponible = True

		return disponible
	
	# Consulta si el contrato esta vigente en la fecha especificada
	# 
	# @return boolean
	
	def isActivo(self, fecha : datetime = datetime.today()) -> bool:
		return self._contrato.consultarVigencia(fecha)

	
	# Devuelve un texto con informacion del empleado dependiendo si tiene contrato
	# vigente o no.
	# 
	# @return informacion
	
	def mostrarInformacion(self) -> str:
		informacion = "";
		if (self.isActivo()):
			informacion = "Soy el empleado con contrato vigente " + self._nombre + " con numero de identificacion: " + self._identificacion
		else:
			informacion = "Soy el empleado sin contrato vigente " + self._nombre + " con numero de identificacion: " + self._identificacion;
		return informacion

	# Establece el dia actual como fecha final del contrato para realizar su
	# despido
	
	def despedir(self) -> None:
		hoy = datetime.today()
		self._contrato.setFechaFin(hoy)
	
	# Establece una nueva fecha fin del contrato para alargar su vigencia
	
	def renovarContrato(self, fechaFin : datetime) -> None:
		if (fechaFin.isAfter(self._contrato.getFechaFin())):
			self._contrato.setFechaFin(fechaFin)

	def contratar(self, contrato : Contrato, cargo : str, servicio : Servicio, diasLaborales : 'list[DiaSemana]'):
		if (not cargo == "x"):
			self.setCargo(cargo)
		
		if (servicio != None):
			self.setServicio(servicio)
		
		if (not diasLaborales.isEmpty()):
			self.setDiasLaborales(diasLaborales)
