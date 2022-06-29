from tkinter import Frame, BOTH, DISABLED, END, Button, Label, ttk, messagebox, Text
from gestorAplicacion.general.Inventario import Inventario
from uiMain.ventanaPrincipal.fieldFrame import FieldFrame
from gestorAplicacion.personas.Empleado import Empleado
from gestorAplicacion.personas.Cliente import Cliente
from gestorAplicacion.personas.Persona import Persona
from datetime import datetime
from manejoErrores.errorAplicacion import ErrorAplicacion
from manejoErrores.textoVacio import TextoVacio
from manejoErrores.errorListasVacias import ErrorListasVacias

class ElegirEmpleado(Frame):
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


        self.textResultados = Text(self.interfazResultados, padx = 10, pady = 10)
        self.textResultados.pack(fill = BOTH)

        self.proceso()

    def proceso(self):
        try:
            
            self.interfazCliente = Frame(self.interfazDatos)
            self.interfazCliente.grid(column = 0, row = 0)

            self.interfazServicio = Frame(self.interfazDatos)
            self.interfazServicio.grid(column = 1, row = 0)


            Label(self.interfazCliente, text = "Asignar empleado a servicio", font = ('Times 18 bold')).pack(pady = 5, anchor = 'c')
            Label(self.interfazCliente, text = "Por favor el cliente con el que desea realizar la asignacion", font = ('Times 12')).pack(pady = 20, anchor =  "w")
           
          
            self.clientesConServicios = Inventario.clientesConServicios()

            values = [i.getNombre() for i in self.clientesConServicios]
            self.clientesConCarritoCombo = ttk.Combobox(self.interfazCliente, values = values, state = "readOnly")
            self.clientesConCarritoCombo.pack(pady = 20, anchor = 'c')

            self.boton1 = Button(self.interfazCliente, text = "Continuar")
            self.boton1.pack(anchor = 'c')
            self.boton1.bind("<Button-1>", self.seleccionCliente)

        except ErrorAplicacion as e:
            messagebox.showinfo(title = "Error Aplicacion", message = str(e))

    def seleccionCliente(self, evento):
        try:
            
            if self.clientesConCarritoCombo.get() == "":
                raise TextoVacio("Por favor seleccione un cliente con el que desea realizar la asignacion")

            Label(self.interfazServicio, text = "Detalles servicio", font = ('Times 18 bold')).pack(pady = 5, anchor = 'c')
            for i in self.clientesConServicios:
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

            self.boton2 = Button(self.interfazServicio, text = "Buscar empleados")
            self.boton2.pack(anchor = 'c')
            self.boton2.bind("<Button-1>", self.buscarEmpleados)
        except ErrorAplicacion as e:
            messagebox.showinfo(title = "Error Aplicacion", message = str(e))
       
    def buscarEmpleados(self, evento):
        try:
            if self.serviciosCombo.get() == "":
                raise TextoVacio("Por favor seleccione un servicio antes de continuar")
            elementos = self.datos.obtenerDatos()
            fecha = elementos[0]
            servicio = self.serviciosCombo.get()
            servicios = self.cliente.obtenerServiciosSinEmpleado()
            self.servicioElegido = None
            for i in servicios:
                if i.getNombre() == servicio:
                    self.servicioElegido = i
                    break
            
            fechaDate = datetime.strptime(fecha, '%d/%m/%Y')
            self.empleadosDisponibles = self.servicioElegido.consultarDisponibilidad(fechaDate)
            if len(self.empleadosDisponibles) == 0:
                raise ErrorListasVacias("No hay empleados disponibles para esta fecha") 
            else:
                self.boton2.destroy()
                values = [i.getNombre() for i in self.empleadosDisponibles]
                Label(self.datos, text = "Empleado", font = ('Times 12 bold')).grid(padx = 80, pady=2, column=0, row=len(self.datos.criterios)+2)
                self.empleadosCombo = ttk.Combobox(self.datos, values = values, state = "readonly", width = 37, justify = "center")
                self.empleadosCombo.grid(column = 1, row = len(self.datos.criterios)+2, pady = 2)
                
                self.boton3 = Button(self.interfazServicio, text = "Asignar")
                self.boton3.pack(anchor = 'c')
                self.boton3.bind("<Button-1>", self.asignarEmpleado)
        except ErrorAplicacion as e:
            messagebox.showinfo(title = "Error Aplicacion", message = str(e))
            
    def asignarEmpleado(self, evento):
        try:
            self.empleadoElegido = None
            for i in self.empleadosDisponibles:
                if i.getNombre() == self.empleadosCombo.get():
                    self.empleadoElegido = i
                    break
            if self.empleadoElegido == None:
                raise TextoVacio("Por favor seleccione un empleado para el servicio y fechas seleccionados")
            self.boton3.destroy()
            self.empleadosCombo.config(state = DISABLED)
            self.cliente.seleccionarEmpleado(self.servicioElegido, self.empleadoElegido)
            self.textResultados.delete("1.0", END)
            self.textResultados.insert("1.0", "Se ha asignado el empleado " + self.empleadoElegido.getNombre() + " al servicio " + self.servicioElegido.getNombre())
        except ErrorAplicacion as e:
            messagebox.showinfo(title = "Error Aplicacion", message = str(e))