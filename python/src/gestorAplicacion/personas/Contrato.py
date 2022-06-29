from datetime import datetime
from random import randint

from gestorAplicacion.general.Documento import Documento

'''
# @author Alejandro Alvarez
# @author Alejandra Barrientos
# @author Mateo Alvarez
# @author Miguel Barrera'''

class Contrato(Documento):
    """Esta clase extiende de Documento y tiene como finalidad definir todos los atributos y métodos que tiene el contrato de un empleado"""
    def __init__(self, salario: int, fechaInicio: datetime, fechaFin: datetime):
        super().__init__()
        self._salario = salario
        self._fechaInicio = fechaInicio
        self._fechaFin = fechaFin
        self._identificador = self.generarIdentificador()

    def consultarVigencia(self, fecha: datetime) -> bool:
        """
        Verificar que el empleado este activo en la empresa, teniendo en cuenta que
        el dia actual debe ser mayor al inicio del contrato y menor a la fecha fin
        del contrato
        """
        return (fecha.date() < self._fechaFin.date() and fecha.date() > self._fechaInicio.date()) or fecha.date() == self._fechaInicio.date()

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
            text += str(randint(0,10))
        return text

	# Cacular la cantidad de dias entre el inicio del contrato y la fecha actual
	# @return text

    def cantidadDiasEmpresa(self) -> int:
        dif = datetime.today() - self._fechaInicio
        return dif.days