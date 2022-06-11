from random import randint
from random import choice

from gestorAplicacion.general import Documento
from gestorAplicacion.general import Inventario
from gestorAplicacion.personas import Empleado
from gestorAplicacion.ventas import Producto
from gestorAplicacion.ventas import Servicio

class Factura(Documento):
    _numConsecutivos = 0

    def __init__(self, productos, servicios, identificacion):
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

    def calcularCosto(self):
        total = 0

        for producto, cantidad in self._productos.items():
            total += producto.getPrecio() * cantidad

        for servicio in self._servicios:
            total += servicio.getPrecio()

        return total

    
    def reajustarTotal(self, total):
        self._total = total

    def retirarProducto(self, productoARetirar, cantidadARetirar):
        if (productoARetirar in self._productos):
            self._productos.pop(productoARetirar)

    def informacionProductos(self):
        if self._productos:
            text = ""

            for producto, cantidad in self._productos.items():
                text += "Se compró " + str(cantidad) + " unidad(es) de " + producto.getNombre() + "\n"

            return text[:-1]
        
        return "No se compraron productos"

    def informacionServicios(self):
        if self._servicios:
            text = ""

            for servicio, empleado in self._servicios.items():
                text += "Se compró el servicio " + servicio.getNombre() + " que va a ser ejecutado por " + empleado.getNombre() + " que lleva " + str(empleado.getContrato().cantidadDiasEmpresa()) + " dias en esta empresa\n"
            
            return text[:-1]

        return "No se compraron servicios"

    @staticmethod
    def generarIdentificador():
        text = ""

        for i in range(5):
            text += str(randint(0,9))

        return text

    @staticmethod
    def empleadoAleatorio():
        listaEmpleadosActivos = []

        for empleado in Inventario.getListadoEmpleados():
            if empleado.isActivo():
                listaEmpleadosActivos.append(empleado)

        return choice(listaEmpleadosActivos)

    def mostrarInformacion(self):
        text = ""

        text += "Factura: " + self._identificador + "\n"
        text += "La factura ha sido generada por " + self._expedidoPor.getNombre() + "\n\nDESCRIPCION\n\n"

        text += self.informacionProductos() + "\n"
        text += self.informacionServicios() + "\n"

        text += "\nTOTAL: " + str(self._total) + "\n"

        text += "Gracias por la compra. Esperamos disfrute de sus productos y servicios adquiridos."

        return text