from ast import Import
from math import round

from gestorAplicacion.general.Inventario import Inventario
from gestorAplicacion.ventas.Iva import Iva

class Producto(Iva):

    def __init__(self, nombre, categoria, mesesGarantia, cantidadDisponible = 0, precio = 0):
        super().__init__()
        self._nombre = nombre
        self._cantidadDisponible = cantidadDisponible
        self._categoria = categoria
        self._precio = self.calcularPrecio(precio)
        self._mesesGarantia = mesesGarantia
        self._cantidadCarrito = 0
        Inventario.agregarProducto(self)

    def getNombre(self):
        return self._nombre

    def getCategoria(self):
        return self._categoria.value

    def setCategoria(self, categoria):
        self._categoria = categoria

    def getPrecio(self):
        return self._precio
    
    def setPrecio(self, precio):
        self._precio = precio

    def getMesesGarantia(self):
        return self._mesesGarantia

    def setMesesGarantia(self, meses):
        self._mesesGarantia = meses


    def agregarCantidadCarrito(self, num):
        self._cantidadCarrito += num

    def disminuirCantidadCarrito(self, num):
        self._cantidadCarrito -= num

    def getCantidadDisponible(self):
        return self._cantidadDisponible - self._cantidadCarrito

    def verificarCantidad(self, num):
        return self.getCantidadDisponible() >= num

    def vender(self, num):
        self._cantidadDisponible -= num
        self._cantidadCarrito -= num

    def calcularPrecio(self, precio):
        return round(precio*(1 + self.IVA))