from tkinter import END, Button, Frame, BOTH, Label, Text, ttk

from gestorAplicacion.general.Inventario import Inventario

class AgregarServicio(Frame):
    def __init__(self, window):
        super().__init__(window, bg = "red")
        self.grid_propagate(False)
        self.pack_propagate(False)
        self.pack(fill = BOTH, expand = True)
        self.proceso()

    def proceso(self):
        try:
            self.interfazDatos = Frame(self, bg = "blue")
            self.interfazDatos.pack(fill = BOTH)

            self.interfazCliente = Frame(self.interfazDatos)
            self.interfazCliente.grid(column = 0, row = 0)

            Label(self.interfazCliente, text = "Agregar Servicio al carrito", font = ('Times 18 bold')).pack(pady = 5, anchor = 'c')
            Label(self.interfazCliente, text = "Por favor seleccione el cliente con el que quiere agregar un servicio", font = ('Times 12')).pack(pady = 20, anchor = "w")

            self.interfazServicio = Frame(self.interfazDatos)
            self.interfazServicio.grid(column = 1, row = 0)

            self.informacion()

            self.interfazResultados = Frame(self, bg = "yellow")
            self.interfazResultados.pack(fill = BOTH)
            Label(self.interfazResultados, text = "Resultados", font = ('Times 12')).pack(anchor = "w")

            # Resultados de la Ejecucion
            self.textResultados = Text(self.interfazResultados, padx = 10, pady = 10)
            self.textResultados.pack(fill = BOTH)

        except Exception as e:
            print(1)

    def informacion(self):
        # Crea un combobox con los clientes que tienen un carrito con algún elemento
        self.clientes = Inventario.getClientes()
        values = [i.getNombre() for i in self.clientes]
        self.clienteCombo = ttk.Combobox(self.interfazCliente, values = values, state = "readonly")
        self.clienteCombo.pack(pady = 20, anchor = 'c')

        self.servicios = Inventario.getServiciosDisponibles()
        values = [i.getNombre() for i in self.servicios]
        self.servicioCombo = ttk.Combobox(self.interfazServicio, values = values, state = "readOnly")
        self.servicioCombo.pack(pady = 20, anchor = 'c')

        botonAgregar = Button(self.interfazServicio, text = "Agregar Servicio")
        botonAgregar.pack(anchor = "c")
        botonAgregar.bind("<Button-1>", self.agregarServicio)

    def agregarServicio(self, evento):
        if self.clienteCombo.get() == "" or self.servicioCombo.get() == "":
            raise Exception("Por favor seleccione un cliente y un servicio a agregar")

        
        for i in self.clientes:
            if i.getNombre() == self.clienteCombo.get():
                cliente = i

        for i in self.servicios:
            if i.getNombre() == self.servicioCombo.get():
                servicio = i

        cliente.solicitarServicio(servicio)

        self.textResultados.delete("1.0", END)
        self.textResultados.insert("1.0", "El servicio fue solicitado con exito.\nRecuerde que debe asignar un empleado a su servicio antes de realizar el pago\n\n")