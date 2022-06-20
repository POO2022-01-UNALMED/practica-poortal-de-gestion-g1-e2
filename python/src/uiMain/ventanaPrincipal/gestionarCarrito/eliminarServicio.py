from tkinter import END, Button, Frame, BOTH, Label, Text, ttk, DISABLED

from gestorAplicacion.general.Inventario import Inventario

class EliminarServicio(Frame):
    def __init__(self, window):
        super().__init__(window, bg = "red")
        self.grid_propagate(False)
        self.pack_propagate(False)
        self.pack(fill = BOTH, expand = True)

        self.interfazDatos = Frame(self, bg = "blue")
        self.interfazDatos.pack(fill = BOTH)

        self.interfazResultados = Frame(self, bg = "yellow")
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

            Label(self.interfazCliente, text = "Eliminar Servicio del carrito", font = ('Times 18 bold')).pack(pady = 5, anchor = 'c')
            Label(self.interfazCliente, text = "Por favor seleccione el cliente con el que quiere eliminar un servicio", font = ('Times 12')).pack(pady = 20, anchor = "w")

            self.interfazServicio = Frame(self.interfazDatos)
            self.interfazServicio.grid(column = 1, row = 0)

            self.clientes = Inventario.getClientes()
            values = [i.getNombre() for i in self.clientes]
            self.clienteCombo = ttk.Combobox(self.interfazCliente, values = values, state = "readOnly")
            self.clienteCombo.pack(pady = 20, anchor = 'c')

            self.boton1 = Button(self.interfazCliente, text = "Continuar")
            self.boton1.pack(anchor = 'c')
            self.boton1.bind("<Button-1>", self.informacion)


            

        except Exception as e:
            print(str(e))

    def informacion(self, evento):
        if self.clienteCombo.get() == "":
            raise Exception("Por favor seleccione un cliente")

        for i in self.clientes:
            if i.getNombre() == self.clienteCombo.get():
                self.cliente = i

        self.servicios = self.cliente.getServicios()
        values = [i.getNombre() for i in self.servicios]  

        self.clienteCombo.config(state = DISABLED)
        self.boton1.destroy()   

        self.servicioCombo = ttk.Combobox(self.interfazServicio, values = values)
        self.servicioCombo.pack(anchor = 'c')

        boton = Button(self.interfazServicio, text = "Eliminar")
        boton.pack(anchor = 'c')
        boton.bind("<Button-1>", self.eliminar)

    def eliminar(self, evento):
        if self.servicioCombo.get() == "":
            raise Exception("Por favor seleccione un Servicio")

        for i in self.servicios:
            if i.getNombre() == self.servicioCombo.get():
                self.servicio = i

        self.cliente.eliminarServicioDeLaCanasta(self.servicio)

        self.textResultados.delete("1.0", END)
        self.textResultados.insert("1.0", "El servicio ha sido eliminado con éxito")

        self.interfazCliente.destroy()
        self.interfazServicio.destroy()
        self.proceso()