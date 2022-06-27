from tkinter import Frame, BOTH, DISABLED, END, Button, Label, ttk, messagebox, Text
from gestorAplicacion.general.Inventario import Inventario
from uiMain.ventanaPrincipal.fieldFrame import FieldFrame
from gestorAplicacion.personas.Empleado import Empleado
from gestorAplicacion.personas.Cliente import Cliente
from gestorAplicacion.personas.Persona import Persona

class ElegirEmpleado(Frame):
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


        self.textResultados = Text(self.interfazResultados, padx = 10, pady = 10)
        self.textResultados.pack(fill = BOTH)

        self.proceso()

    def proceso(self):
        try:
            
            self.interfazCliente = Frame(self.interfazDatos)
            self.interfazCliente.grid(column = 0, row = 0)

            self.interfazServicio = Frame(self.interfazDatos)
            self.interfazServicio.grid(column = 1, row = 0)

            #self.interfazFecha = Frame(self.interfazDatos)
            #self.interfazServicio.grid(column = 0, row = 1)
            
            Label(self.interfazCliente, text = "Asignar empleado a servicio", font = ('Times 18 bold')).pack(pady = 5, anchor = 'c')
            Label(self.interfazCliente, text = "Por favor el empleado con el que desea realizar la asignacion", font = ('Times 12')).pack(pady = 20, anchor =  "w")
           
          
            self.clientesConCarrito = Inventario.clientesConServicios()

            values = [i.getNombre() for i in self.clientesConCarrito]
            self.clientesConCarritoCombo = ttk.Combobox(self.interfazCliente, values = values, state = "readOnly")
            self.clientesConCarritoCombo.pack(pady = 20, anchor = 'c')

            self.boton1 = Button(self.interfazCliente, text = "Continuar")
            self.boton1.pack(anchor = 'c')
            self.boton1.bind("<Button-1>", self.seleccionCliente)

        except Exception as e:
            print(str(e))

    def seleccionCliente(self, evento):
      
        if self.clientesConCarritoCombo.get() == "":
            raise Exception("Por favor seleccione un cliente")

        Label(self.interfazServicio, text = "Detalles servicio", font = ('Times 18 bold')).pack(pady = 5, anchor = 'c')
        for i in self.clientesConCarrito:
            if i.getNombre() == self.clientesConCarritoCombo.get():
                self.cliente = i
        
        self.clientesConCarritoCombo.config(state = DISABLED)
        self.boton1.destroy()

        servicios = self.cliente.obtenerServiciosSinEmpleado()
        
        values = [i.getNombre() for i in servicios]
        
        

        self.datos = FieldFrame(self.interfazServicio, "", ["Fecha (DD/MM/YYYY)"], "", [""], [], ["date"])

        Label(self.datos, text = "Servicio", font = ('Times 12 bold')).grid(padx = 80, pady=2, column=0, row=len(self.datos.criterios)+1)
        self.serviciosCombo = ttk.Combobox(self.datos, values = values, state = "readonly", width = 37, justify = "center")
        self.serviciosCombo.grid(column = 1, row = len(self.datos.criterios)+1, pady = 2)

        boton = Button(self.interfazServicio, text = "Buscar empleados")
        boton.pack(anchor = 'c')
        boton.bind("<Button-1>", self.buscarEmpleados)

       
    def buscarEmpleados(self, evento):
        elementos = self.datos.obtenerDatos()
        fecha = elementos[0]
        servicio = self.serviciosCombo.get()
        servicios = self.cliente.obtenerServiciosSinEmpleado()
        servicioElegido = None
        for i in servicios:
            if i.getNombre() == servicio:
                servicioElegido = i
                break
        
        print(fecha)
        print(servicioElegido)
        empleadosDisponibles = servicioElegido.consultarDisponibilidad(fecha);

            #self.cliente.agregarProductoALaCanasta(self.producto, int(cantidadAgregar))
            
            #self.textResultados.delete("1.0", END)
            #self.textResultados.insert("1.0", "El producto fue agregado con exito")

            #self.interfazCliente.destroy()
            #self.interfazProducto.destroy()
        #self.proceso()