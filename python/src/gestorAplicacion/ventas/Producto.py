from math import round

from gestorAplicacion.general.Inventario import Inventario
from gestorAplicacion.ventas.Iva import Iva
from gestorAplicacion.ventas.Categoria import Categoria

# Esta clase implementa Iva y se encarga de guardar las características de
# un producto

# Mateo Alvarez Lebrum
# Alejandro Alvarez Botero
# Miguel Angel Barrera Bustamante
# Alejandra Barrientos Grisales


class Producto(Iva):

    def __init__(self, nombre, categoria: Categoria, mesesGarantia: int, cantidadDisponible = 0, precio = 0):
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

    def setCategoria(self, categoria: Categoria):
        self._categoria = categoria

    def getPrecio(self):
        return self._precio
    
    def setPrecio(self, precio: int):
        self._precio = precio

    def getMesesGarantia(self):
        return self._mesesGarantia

    def setMesesGarantia(self, meses: int):
        self._mesesGarantia = meses

    def agregarCantidadCarrito(self, num: int):
        self._cantidadCarrito += num

    def disminuirCantidadCarrito(self, num: int):
        self._cantidadCarrito -= num

    def getCantidadDisponible(self):
        return self._cantidadDisponible - self._cantidadCarrito

    def verificarCantidad(self, num: int):
        return self.getCantidadDisponible() >= num

    def vender(self, num: int):
        self._cantidadDisponible -= num
        self._cantidadCarrito -= num

    def calcularPrecio(self, precio: int):
        return round(precio*(1 + self.IVA))