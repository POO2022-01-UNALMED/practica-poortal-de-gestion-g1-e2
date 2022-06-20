from tkinter import Button, Frame, BOTH, messagebox, Label, ttk, Text, LabelFrame

from gestorAplicacion.general.Inventario import Inventario
from uiMain.ventanaPrincipal.fieldFrame import FieldFrame

from uiMain.ventanaPrincipal.excepcion.errorAplicacion import ErrorAplicacion

class AgregarProducto(Frame):
    def __init__(self, window):
        super().__init__(window, bg = "red")
        self.grid_propagate(False)
        self.pack_propagate(False)
        self.pack(fill = BOTH, expand = True)
        self.proceso()

    def proceso(self):
        try:
            # Crea un frame principal para que el usuario seleccione los datos
            self.interfazPrincipal = Frame(self)
            self.interfazPrincipal.pack()

            self.interfaz = Frame(self.interfazPrincipal, width = 400,  bg = "red")
            self.interfaz.grid(column = 0, row = 0)
            self.datosInterfaz = Frame(self.interfazPrincipal, bg = "blue")
            self.datosInterfaz.grid(column = 1, row = 0)
            self.datos = Frame(self.datosInterfaz, bg = "blue")

            Label(self.interfaz, text = "Agregar Producto al carrito", font = ('Times 18 bold')).pack(pady = 5, anchor = 'c')
            Label(self.interfaz, text = "Por favor seleccione el cliente con el que quiere agregar un producto", font = ('Times 12')).pack(pady = 20, anchor = "w")

            self.botonDatos = None

            self.informacion()

            # Frame para poner resultados
            self.resultados = Frame(self, bg = "blue")
            self.resultados.pack(fill = BOTH, anchor = "c")
            Label(self.resultados, text = "Resultados", font = ('Times 12')).pack(anchor = "w")

            # Resultados de la Ejecucion
            self.textResultados = Text(self.resultados, padx = 10, pady = 10)
            self.textResultados.pack(fill = BOTH)

        except ErrorAplicacion as e:
            messagebox.showinfo(title = "Error de la Aplicación")

    def informacion(self):
        # Crea un combobox con los clientes que tienen un carrito con algún elemento
        self.clientes = Inventario.getClientes()
        values = [i.getNombre() for i in self.clientes]
        self.clienteCombo = ttk.Combobox(self.interfaz, values = values, state = "readonly")
        self.clienteCombo.pack(pady = 20, anchor = 'c')

        # Crea un combobox con los productos disponibles
        self.productosDisp = Inventario.getListadoProductos()
        values = [i.getNombre() for i in self.productosDisp]
        self.productoCombo = ttk.Combobox(self.interfaz, values = values, state = "readOnly")
        self.productoCombo.pack(pady = 20, anchor = "c")

        self.botonCantidad = Button(self.interfaz, text = "Continuar")
        self.botonCantidad.pack(anchor = 'c')
        self.botonCantidad.bind("<Button-1>", self.verCantidad)

    def verCantidad(self, evento):
        if self.clienteCombo.get() == "" or self.productoCombo.get() == "":
            raise Exception("Por favor seleccione un cliente y un producto")

        self.productoElegido = Inventario.buscarProducto(self.productoCombo.get())
        
        self.datos.destroy()
        self.datos = FieldFrame(self.datosInterfaz, self.productoElegido.getNombre(), ["Cantidad Disponible", "Cantidad a elegir"], "", [self.productoElegido.getCantidadDisponible(), None], ["Cantidad Disponible"], [0, self.productoElegido.getCantidadDisponible()])

        if self.botonDatos != None:
            self.botonDatos.destroy()

        self.botonDatos = Button(self.datosInterfaz, text = "Agregar producto")
        self.botonDatos.pack(anchor = 'c')
        self.botonDatos.bind("<Button-1>", self.agregarProducto)

    def agregarProducto(self, evento):
        elementos = self.datos.obtenerDatos()
        cantidadAgregar = elementos[1]
        for i in self.clientes:
            if self.clienteCombo.get() == i.getNombre():
                i.agregarProductoALaCanasta(self.productoElegido, int(cantidadAgregar))
        self.verCantidad("")