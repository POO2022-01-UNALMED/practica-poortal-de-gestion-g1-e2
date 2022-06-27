from tkinter import DISABLED, END, Button, Frame, BOTH, messagebox, Label, ttk, Text, LabelFrame


from gestorAplicacion.general.Inventario import Inventario
from uiMain.ventanaPrincipal.fieldFrame import FieldFrame

from manejoErrores.errorAplicacion import ErrorAplicacion

class AgregarProducto(Frame):
    def __init__(self, window):
        super().__init__(window)
        self.grid_propagate(False)
        self.pack_propagate(False)
        self.pack(fill = BOTH, expand = True)

        self.interfazDatos = Frame(self)
        self.interfazDatos.pack(fill = BOTH)

        self.interfazResultados = Frame(self)
        self.interfazResultados.pack(fill = BOTH)
        Label(self.interfazResultados, text = "Resultados", font = ('Times 12')).pack(anchor = "w")

        # Resultados de la Ejecucion
        self.textResultados = Text(self.interfazResultados, padx = 10, pady = 10)
        self.textResultados.pack(fill = BOTH)

        self.proceso()

    def proceso(self):
        try:
            self.interfazCliente = Frame(self.interfazDatos)
            self.interfazCliente.grid(column = 0, row = 0)

            Label(self.interfazCliente, text = "Agregar Producto al Carrito", font = ('Times 18 bold')).pack(pady = 5, anchor = 'c')
            Label(self.interfazCliente, text = "Por favor seleccione el cliente con el que quiere agregar un producto", font = ('Times 12')).pack(pady = 20, anchor = "w")

            self.interfazProducto = Frame(self.interfazDatos)
            self.interfazProducto.grid(column = 1, row = 0)

            self.clientes = Inventario.getClientes()
            values = [i.getNombre() for i in self.clientes]
            self.clienteCombo = ttk.Combobox(self.interfazCliente, values = values, state = "readOnly")
            self.clienteCombo.pack(pady = 20, anchor = 'c')

            self.productos = Inventario.getProductosDisponibles()
            values = [i.getNombre() for i in self.productos]
            self.productoCombo = ttk.Combobox(self.interfazCliente, values = values, state = "readOnly")
            self.productoCombo.pack(pady = 20,anchor = 'c' )

            self.boton1 = Button(self.interfazCliente, text = "Continuar")
            self.boton1.pack(anchor = 'c')
            self.boton1.bind("<Button-1>", self.informacion)

        except Exception as e:
            print(str(e))
    


    def informacion(self, evento):
        if self.clienteCombo.get() == "" or self.productoCombo.get() == "":
            raise Exception("Por favor seleccione un cliente y un producto")

        for i in self.clientes:
            if i.getNombre() == self.clienteCombo.get():
                self.cliente = i
        
        self.producto = Inventario.buscarProducto(self.productoCombo.get())

        self.clienteCombo.config(state = DISABLED)
        self.productoCombo.config(state = DISABLED)
        self.boton1.destroy()

        self.datos = FieldFrame(self.interfazProducto, self.producto.getNombre(), ["Cantidad Disponible", "Cantidad a elegir"], "", [self.producto.getCantidadDisponible(), None], ["Cantidad Disponible"], [0, self.producto.getCantidadDisponible()])

        boton = Button(self.interfazProducto, text = "Agregar")
        boton.pack(anchor = 'c')
        boton.bind("<Button-1>", self.agregarProducto)

    def agregarProducto(self, evento):
        try:

            elementos = self.datos.obtenerDatos()
            cantidadAgregar = elementos[1]
            
            self.cliente.agregarProductoALaCanasta(self.producto, int(cantidadAgregar))
            
            self.textResultados.delete("1.0", END)
            self.textResultados.insert("1.0", "El producto fue agregado con exito")

            self.interfazCliente.destroy()
            self.interfazProducto.destroy()
            self.proceso()
            
        except ErrorAplicacion as e:
            messagebox.showinfo(title = "Error Aplicacion", message = str(e))