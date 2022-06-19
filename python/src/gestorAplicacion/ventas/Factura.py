from ast import Str
from random import randint
from random import choice

from gestorAplicacion.general.Documento import Documento
from gestorAplicacion.general.Inventario import Inventario
from gestorAplicacion.personas.Empleado import Empleado
from gestorAplicacion.ventas.Producto import Producto
from gestorAplicacion.ventas.Servicio import Servicio


# Esta clase extiende de Documento y se encarga de manejar las facturas de la aplicacion
# los cuales se generan cada vez que hay un pago y se usan para 
# efuectuar la devolucion de un producto

# Mateo Alvarez Lebrum
# Alejandro Alvarez Botero
# Miguel Angel Barrera Bustamante
# Alejandra Barrientos Grisales


class Factura(Documento):
    _numConsecutivos = 0


    # Constructor para generar una Factura, para ello, a parte de los parámetros, se genera una identificacion
    # de la factura y se escoge un empleado aleatorio quien se encarga de expedirla
    # @param productos
    # @param servicios
    # @param identificacion    
    def __init__(self, productos: dict[Producto, int], servicios:  dict[Servicio, Empleado], identificacion: Str):
        super().__init__()

        Factura._numConsecutivos += 1
        self._consecutivo = str(Factura._numConsecutivos)
        self._productos = dict(productos)
        self._servicios = dict(servicios)
        self._total = self.calcularCosto()
        self._identificador = self.generarIdentificador()
        self._expedidoPor = self.empleadoAleatorio()
        self._numeroIdentificacionPersona = identificacion
        Inventario.agregarFactura()

    def getConsecutivo(self):
        return self._consecutivo

    def getExpedidoPor(self):
        return self._expedidoPor

    def getTotal(self):
        return self._total
    
    def getIdentificador(self):
        return self._identificador

    def getNumeroIdentificacionPersona(self):
        return self._numeroIdentificacionPersona

    def getProductos(self):
        return self._productos

    def getServicios(self):
        return self._servicios

    # Este metodo suma todos los precios de los productos y servicios que van a ser pagados
    def calcularCosto(self) -> (int):
        total = 0

        for producto, cantidad in self._productos.items():
            total += producto.getPrecio() * cantidad

        for servicio in self._servicios:
            total += servicio.getPrecio()

        return total

    # Este metodo se emplea en la devolucion de producto
    def reajustarTotal(self, total: int):
        self._total = total


    # Este metodo retira la cantidad especifica de un producto en una factura
	# se usa en la funcionalidad de devolver producto
    def retirarProducto(self, productoARetirar: Producto, cantidadARetirar: int):
        if (productoARetirar in self._productos):
            self._productos[productoARetirar] -= cantidadARetirar


    # Este metodo muestra informacion acerca de los productos y las unidades que se compraron
    def informacionProductos(self):
        if self._productos:
            text = ""

            for producto, cantidad in self._productos.items():
                text += "Se compró " + str(cantidad) + " unidad(es) de " + producto.getNombre() + "\n"

            return text[:-1]
        
        return "No se compraron productos"


    # Este metodo muestra informacion acerca del nombre de los servicios,
	# el nombre del empleado asignado y se calcula la cantidad de dias que lleva en la empresa
	# dicho empleado que va a realizar el servicio
    def informacionServicios(self):
        if self._servicios:
            text = ""

            for servicio, empleado in self._servicios.items():
                text += "Se compró el servicio " + servicio.getNombre() + " que va a ser ejecutado por " + empleado.getNombre() + " que lleva " + str(empleado.getContrato().cantidadDiasEmpresa()) + " dias en esta empresa\n"
            
            return text[:-1]

        return "No se compraron servicios"


    # Este metodo crea el identificador unico de cada factura
    @staticmethod
    def generarIdentificador():
        text = ""

        # Genera número de 5 digitos aleatorios
        for i in range(5):
            text += str(randint(0,9))

        return text


    # De los empleados activos se elige uno al azar
    @staticmethod
    def empleadoAleatorio():
        listaEmpleadosActivos = []

        # Obtiene de la los empleados en factura solo los empleados que tienen un contrato vigente
        for empleado in Inventario.getListadoEmpleados():
            if empleado.isActivo():
                listaEmpleadosActivos.append(empleado)

        # Elige un empleado al azar
        return choice(listaEmpleadosActivos)

    # Muestra la informacion de la factura, el identificador de la factura, el nombre del empleado, la informacion
    # de los productos y los servicios y el total de la compra
    def mostrarInformacion(self):
        text = ""

        text += "Factura: " + self._identificador + "\n"
        text += "La factura ha sido generada por " + self._expedidoPor.getNombre() + "\n\nDESCRIPCION\n\n"

        text += self.informacionProductos() + "\n"
        text += self.informacionServicios() + "\n"

        text += "\nTOTAL: " + str(self._total) + "\n"

        text += "Gracias por la compra. Esperamos disfrute de sus productos y servicios adquiridos."

        return text