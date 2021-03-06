from gestorAplicacion.ventas.Iva import Iva

'''
# @author Alejandro Alvarez
# @author Alejandra Barrientos
# @author Mateo Alvarez
# @author Miguel Barrera'''

class Servicio(Iva):
    '''Esta clase se encarga de simular un servicio'''

    def __init__(self, nombre, precio = 0):
        from gestorAplicacion.general.Inventario import Inventario
        super().__init__()
        self._nombre = nombre
        self._precio = self.calcularPrecio(precio)    
        Inventario.agregarServicio(self)

    def getNombre(self):
        return self._nombre  
    def setNombre(self, nombre):
        self._nombre = nombre

    def getPrecio(self):
        return self._precio  
    def setPrecio(self, precio):
        self._precio = precio

    def calcularPrecio(self, precio):
        return round(precio*(1 + self.IVA))

    def consultarDisponibilidad(self, fechaSoliciud):
        '''Obtiene los servicios en los que está trabajando al menos un empleado'''
        from gestorAplicacion.general.Inventario import Inventario
        listaEmpleados = Inventario.getListadoEmpleados()
        empleadosDisponibles = []
        for empleado in listaEmpleados:
            if (empleado.consultarDisponibilidadEmpleado(self, fechaSoliciud)):
                empleadosDisponibles.append(empleado)
        return empleadosDisponibles


    def __str__(self):
        return self._nombre


   