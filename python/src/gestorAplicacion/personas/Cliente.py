from gestorAplicacion.ventas.Factura import Factura

from gestorAplicacion.personas.Persona import Persona
from dateutil.relativedelta import relativedelta
from manejoErrores.clienteSinProductos import ClienteSinProducto
from manejoErrores.clienteSinServicio import ClienteSinServicio
from manejoErrores.errorListasVacias import ErrorListasVacias
from manejoErrores.servicioSolicitado import ServicioSolicitado

# Esta clase extiende de persona y se encarga de definir
# todos los atributos y metodos necesarios para gestionar su carrito 
# y realizar compras y devoluciones
# 
# @author Mateo Alvarez Lebrum
# @author Alejandro Alvarez Botero
# @author Miguel Angel Barrera Bustamante
# @author Alejandra Barrientos Grisales

#TODO actualizar error segun las condiciones del trabajo
#TODO ajustar documentacion de metodos
class Cliente(Persona):
    #private static final long serialVersionUID = 1L

    def __init__(self, nombre, telefono, email, identificacion, tipoDeIdentificacion, sexo):
        super().__init__(nombre, telefono, email, identificacion, tipoDeIdentificacion, sexo)
        self._productos = {}
        self._servicios = {}
     

    # Este metodo genera una factura con los productos que hay en el carrito
    # @return Factura de compra
    def pagar(self):
        # Verifica que todos los servicios del carrito tengan empleado asignado
        if None in self._servicios.values():
            raise ErrorListasVacias("\nActualmente tiene servicios sin empleado asignado, por favor seleccione empleados primero.\n\n")
        

        # Se genera una factura asociada a la compra
        factura = Factura(self._productos, self._servicios, self._identificacion)

        # Por cada producto del carrito se ejecuta su metodo "vender" que disminuye su cantidad disponible en la tienda
        for producto in self._productos:
            producto.vender(self._productos[producto])
        

        # Se limpia el carrito de compras
        self._productos = {}
        self._servicios = {}

        return factura
    

    #  Este metodo busca dentro de los servicios del carrito cuales no tienen un empleado asignado
    #  @return lista de servicios sin empleados
    def obtenerServiciosSinEmpleado(self):
        serviciosSinEmpleado = []
        
        # Recorre el hashmap correspondiente a servicio y ve cuales no tienen un objeto empleado como value
        for servicio in self._servicios:
            if self._servicios[servicio] == None:
                serviciosSinEmpleado.append(servicio)

        if len(serviciosSinEmpleado) == 0:
            raise ValueError("\nEl cliente no tiene servicios a los cuales les deba asignar un empelado\n\n")
        
        return serviciosSinEmpleado
    

    # @param producto
    # @param cantidad
    def agregarProductoALaCanasta(self, producto, cantidad):
        # Si el producto ya esta en el carrito de compras le suma la nueva cantidad
        # ingresada a la cantidad que ya tenia
        for i in self._productos:
            if i == producto:
                # Actualiza la cantidad del producto en los diferentes carritos
                producto.agregarCantidadCarrito(cantidad)

                self._productos[i] = self._productos[i] + cantidad
                return

        # Si el producto no esta en el carrito lo agrega junto a su cantidad
        producto.agregarCantidadCarrito(cantidad)
        self._productos[producto] = cantidad 


     # @param producto
    def eliminarProductoDeLaCanasta(self, producto):
        # Actualiza la suma de las cantidades del productos en los diferentes carritos
        producto.disminuirCantidadCarrito(self._productos[producto])
        self._productos.pop(producto)
    

    # @param servicio
    def solicitarServicio(self, servicio):
        # Verifica que el servicio no se encuentre en el carrito
        if (servicio in self._servicios.keys()):
            raise ServicioSolicitado("El servicio ya fue solicitado.")
        
        self._servicios[servicio] = None
    

    # Este metodo asigna un empleado a un servicio en el carrito
    # @param servicio
    # @param empleado
    def seleccionarEmpleado(self, servicio, empleado):
        for  i in self._servicios:
            if i == servicio:
                self._servicios[i] = empleado

    # @param servicio
    def eliminarServicioDeLaCanasta(self, servicio):
        self._servicios.pop(servicio)
    

    # @param nombreProducto
    # @param identificacion
    # @param cantidadADevolver
    # @param fecha
    # @return Mensaje con la informacion del dinero retornado al cliente
    @staticmethod
    def devolverProducto(nombreProducto, identificacion, cantidadADevolver, fecha):
        from gestorAplicacion.general.Inventario import Inventario
        
        # Verificar que existe un producto con ese nombre en el inventario
        productoEncontrado = False
        productoComprado = None
        for producto in Inventario.getListadoProductos():
            if producto.getNombre() == nombreProducto:
                productoEncontrado = True
                productoComprado = producto


        if not productoEncontrado:
            raise ValueError("El producto no existe en nuestro inventario")

        # Verificar que existe una factura en ese dia con ese producto

        facturaEncontrada = False
        facturaCompra = None
        fechaProporcionada = fecha
        
        # Encuentra factura que contiene ese producto y fue comprado por la persona que
        # lo esta devolviendo y coincide en la fecha proporcionada
        for factura in Inventario.getListadoFacturas():
            if factura.getNumeroIdentificacionPersona() == identificacion and Inventario.buscarFactura(date = fechaProporcionada, num = 0) != None:
                for producto in factura.getProductos():
                    if productoComprado == producto:
                        facturaEncontrada = True
                        facturaCompra = factura


        if not facturaEncontrada:
            raise ValueError("No existen facturas con dicha informacion de compra asociada(producto/identificacion/fecha)")

        # Verificar que los productos a devolver sean menores a los comprados

        cantidadValida = False
        for compra in facturaCompra.getProductos():
            if compra == productoComprado:
                if facturaCompra.getProductos()[compra] >= cantidadADevolver:
                    cantidadValida = True


        if not cantidadValida:
            raise ValueError("Intenta devolver mas productos de los que fueron comprados")

        # Verificar que el tiempo de garantia aun se cumpla
        tiempoMaximo = facturaCompra.getFechaExpedicion() + relativedelta(months=productoComprado.getMesesGarantia())
        if tiempoMaximo < fechaProporcionada:
            raise ValueError("Ya paso el tiempo de garantia")

        # Modificar el total de la factura y la cantidad de productos

        reembolso = productoComprado.getPrecio() * cantidadADevolver
        facturaCompra.reajustarTotal(facturaCompra.getTotal() - reembolso)
        facturaCompra.retirarProducto(productoComprado, cantidadADevolver)

        # Retorna dinero de reembolso
        texto = "\nLa devolucion se realizo exitosamente\n" + "\nSe han devuelto " + str(cantidadADevolver) + " " + nombreProducto + "(s) del cliente con identificacion: " + str(facturaCompra.getNumeroIdentificacionPersona()) + "\n" + "\nEl dinero retornado es " + str(reembolso) + "\n"

        return texto
    

    def carritoVacio(self):
        if len(self._productos) or len(self._servicios):
            return False
        return True

    # Muestra la informacion del cliente
    def mostrarInformacion(self):
        return "Soy el cliente " + self._nombre + " con numero de identificacion: " + self._identificacion
    
    
    # @return String con la informacion de los productos y servicios en el carrito
    def verCarrito(self):
        text = ""

        # Si el hashmap de productos tiene algun elemento, se agrega la informacion de
        # la cantidad disponible y el nombre, en caso contrario no se hace nada
        if len(self._productos):
            for i in self._productos:
                text += str(self._productos[i]) + " unidad(es) del producto " + i.getNombre() + "\n"


        # Si el hashmap de servicios tiene algun elemento, se agrega l
        if len(self._servicios):
            for i in self._servicios:
                if self._servicios[i] == None:
                    text += "Servicio " + i.getNombre() + " que no tiene un empleado asignado aun\n"
                else:
                    text += "Servicio " + i.getNombre() + " que sera ejecutado por el empleado "
                    + self._servicios[i].getNombre() + "\n"
                    

        # Si no tiene ningun producto o servicio se retorna el siguiente mensaje
        if text == "":
            return "No tiene productos ni servicios en su carrito"
        
        return text
    

    def getServicios(self):
        return self._servicios.keys()
    

    def getProductos(self):
        if not self._productos.keys():
            raise ClienteSinProducto("Este cliente no tiene productos en su carrito")
        return self._productos.keys()
    
    

