from gestorAplicacion.personas.Empleado import Empleado
from manejoErrores.clientesSinCarrito import ClientesSinCarrito
from manejoErrores.clientesSinProductosEnCarrito import ClientesSinProductosEnCarrito
from manejoErrores.errorIngresoDatos import ErrorIngresoDatos
from manejoErrores.errorListasVacias import ErrorListasVacias



class Inventario:

    listadoProductos = []
    listadoServicios = []
    listadoFacturas = []
    listadoPersonas = []

    @classmethod
    def getListadoProductos(cls):
        return cls.listadoProductos
    

    @classmethod
    def getListadoServicios(cls):
        return cls.listadoServicios
    

    @classmethod
    def getServiciosDisponibles(cls):
        """Los servicios disponibles son aquellos en los que se hay al menos un empleado
        trabajando en el"""
        serviciosDisp = []

        # De cada empleado se extrae su servicio y se agrega a la lista
        for i in cls.getListadoEmpleados():
            if i.getServicio() != None:
                serviciosDisp.append(i.getServicio())
            
        # Se eliminan los servicios repetidos
        return list(set(serviciosDisp))
    

    @classmethod
    def getListadoFacturas(cls):
        return cls.listadoFacturas
    

    @classmethod
    def getListadoEmpleados(cls):
        empleados = []

        for i in cls.listadoPersonas:
            if isinstance(i, Empleado):
                empleados.append(i)
            
        return empleados
    
    @classmethod
    def getListadoEmpleadosNoActivos(cls):
        empleadosNoActivos = []
        for i in cls.getListadoEmpleados():
            if not i.isActivo():
                empleadosNoActivos.append(i)
            
        return empleadosNoActivos

    @classmethod
    def getListadoEmpleadosActivos(cls):
        empleadosActivos = []
        for i in cls.getListadoEmpleados():
            if i.isActivo():
                empleadosActivos.append(i)
            
        return empleadosActivos

    @classmethod
    def getListadoPersonasParaContratar(cls):
        from gestorAplicacion.personas.Cliente import Cliente 
        from gestorAplicacion.personas.Persona import Persona
        personasAContratar = []
        for i in cls.getListadoEmpleadosNoActivos():
               personasAContratar.append(i)
        for j in cls.getListadoPersonas():
            if (isinstance(j, Persona)) and (not(isinstance(j, Empleado))) and (not(isinstance(j, Cliente))):
                personasAContratar.append(j)       
        return personasAContratar
    

    @classmethod
    def agregarProducto(cls, producto):
        cls.listadoProductos.append(producto)
    

    @classmethod
    def agregarServicio(cls, servicio):
        cls.listadoServicios.append(servicio)
    

    @classmethod
    def agregarFactura(cls, factura):
        cls.listadoFacturas.append(factura)
    

    @classmethod
    def agregarPersona(cls, persona):
        cls.listadoPersonas.append(persona)

    
    @classmethod
    def eliminarPersona(cls, persona):
        cls.listadoPersonas.remove(persona)
    

    @classmethod
    def getListadoPersonas(cls):
        return cls.listadoPersonas
    

    @classmethod
    def buscarProducto(cls, nombre):
        for i in cls.listadoProductos:
            if i.getNombre() == nombre:
                return i
            
        raise ValueError("No hay Productos que coincidan con el nombre especificado")
    

    @classmethod
    def buscarServicio(cls, nombre):
        for i in cls.listadoServicios:
            if i.getNombre() == nombre:
                return i
            
        raise ErrorListasVacias("No hay Servicios que coincidan con el nombre especificado")
    

    @classmethod
    def buscarEmpleado(cls, nombre):
        for i in cls.getListadoEmpleados():
            if i.getNombre() == nombre:
                return i
            
        raise ErrorListasVacias("No hay Empleados que coincidan con el nombre especificado")
    

    @classmethod
    def buscarFactura(cls, **kwargs):
        if kwargs["num"]:
            for i in cls.listadoFacturas:
                if i.getConsecutivo() == kwargs.num:
                    return i
                
            raise ErrorListasVacias("\nNo hay Facturas que coincidan con el consecutivo especificado\n\n")
        elif kwargs["date"]:
            for  i in cls.listadoFacturas:
                if i.getFechaExpedicion().date() == kwargs["date"].date():
                    return i
                
            raise ErrorListasVacias("No hay Facturas que coincidan con la fecha especificada")
        else:
            raise ErrorIngresoDatos("Se requiere una fecha o consecutivo para buscar facturas")
            

    @classmethod
    def clientesConCarrito(cls):
        from gestorAplicacion.personas.Cliente import Cliente
        clientes = []

        for i in cls.listadoPersonas:
            if isinstance(i, Cliente) and not i.carritoVacio():
                clientes.append(i)
            
        
        if not len(clientes):
            raise ClientesSinCarrito("No hay clientes con servicios o productos en su carrito de compra")
        
        return clientes
    
    @classmethod
    def clientesConServicios(cls):
        from gestorAplicacion.personas.Cliente import Cliente
        clientes = []

        for i in cls.listadoPersonas:
            if isinstance(i, Cliente) and len(i.getServicios()):
                clientes.append(i)
            
        
        if not len(clientes):
            raise ClientesSinProductosEnCarrito("\nNo hay clientes con servicios en su carrito de compra\n\n")
        
        return clientes
    

    @classmethod
    def getClientes(cls):
        from gestorAplicacion.personas.Cliente import Cliente
        clientes = []
        for i in cls.listadoPersonas:
            if isinstance(i, Cliente):
                clientes.append(i)
            
        if not len(clientes):
            raise ValueError("\nNo hay clientes disponibles en este momento\n\n")
        
        return clientes
    

    @classmethod
    def getProductosDisponibles(cls):
        productosDisp = []

        # Solo se van a retornar los productos que tienen una cantidad disponible
        # superior a 0
        for i in cls.listadoProductos:
            if i.getCantidadDisponible() > 0:
                productosDisp.append(i)
            
        if not len(productosDisp):
            raise ValueError("\nNo tenemos productos disponibles en este momento\n\n")
        
        return productosDisp
    

