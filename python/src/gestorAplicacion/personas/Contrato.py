from datetime import date, datetime
import math

from gestorAplicacion.general.Documento import Documento

# Esta clase extiende de Documento y tiene como finalidad definir todos los atributos y métodos
# que tiene el contrato de un empleado
#
# @author Mateo Alvarez Lebrum
# @author Alejandro Alvarez Botero
# @author Miguel Angel Barrera Bustamante
# @author Alejandra Barrientos Grisales



class Contrato(Documento):
	def __init__(self, salario: int, fechaInicio: datetime, fechaFin: datetime):
		super().__init__()
		self._salario = salario
		self._fechaInicio = fechaInicio
		self._fechaFin = fechaFin
		self._identificador = self.generarIdentificador()

	#
	# Verificar que el empleado este activo en la empresa, teniendo en cuenta que
	# el dia actual debe ser mayor al inicio del contrato y menor a la fecha fin
	# del contrato
	# @param fechaSolicitud
	# @return boolean
	#

	def consultarVigencia(self, fecha: datetime) -> bool:
		return (fecha < self._fechaFin and fecha > self._fechaInicio) or fecha == self._fechaInicio

	def getFechaInicio(self) -> datetime:
		return self._fechaInicio

	def setFechaInicio(self, fechaInicio: datetime) -> None:
		self._fechaInicio = fechaInicio

	def getFechaFin(self) -> datetime:
		return self._fechaFin

	def setFechaFin(self, fechaFin: datetime) -> None:
		self._fechaFin = fechaFin

	def getIdentificador(self) -> str:
		return self._identificador

	def getSalario(self) -> int:
		return self._salario

	def setSalario(self, salario: int) -> None:
		self._salario = salario

	# Generar aleatoriamente un número de identificación
	# @return text

	def generarIdentificador(self) -> str:
		text = ""
		for i in range(5):
			text += str((math.random()) * 10) + ""
		return text

	# Cacular la cantidad de dias entre el inicio del contrato y la fecha actual
	# @return text

	def cantidadDiasEmpresa(self) -> int:
		dif = datetime.today() - self._fechaInicio
		return dif.days