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
#
class ElegirEmpleado(Frame):
    """Clase usada para la interfaz de elegir empleado para los servicios en carrito de un cliente"""
    def __init__(self, window):
        super().__init__(window)
        self.grid_propagate(False)
        self.pack_propagate(False)
        self.pack(fill = BOTH, expand = True)

        # Crea el frame donde van a aparecer todos a escorger del usuario
        self.interfazDatos = Frame(self)
        self.interfazDatos.pack(fill = BOTH)

        # Crea el frame donde van a aparecer los resultados de la operacion
        self.interfazResultados = Frame(self)
        self.interfazResultados.pack(fill = BOTH)
        Label(self.interfazResultados, text = "Resultados", font = ('Times 12')).pack(anchor = "w")

        # Añade campo de texto donde se muestran los resultados
        self.textResultados = Text(self.interfazResultados, padx = 10, pady = 10)
        self.textResultados.pack(fill = BOTH)

        self.proceso()

    def proceso(self):
        """Inicia el proceso para la asignacion de empleado mostrando el cliente a elegir"""
        try:
            # Crea el frame en el cual se elige el cliente
            self.interfazCliente = Frame(self.interfazDatos)
            self.interfazCliente.grid(column = 0, row = 0)

            # Crea el frame en el cual se elige servicio, la fecha de solicitud y el empleado
            self.interfazServicio = Frame(self.interfazDatos)
            self.interfazServicio.grid(column = 1, row = 0)


            Label(self.interfazCliente, text = "Asignar empleado a servicio", font = ('Times 18 bold')).pack(pady = 5, anchor = 'c')
            Label(self.interfazCliente, text = "Por favor el cliente con el que desea realizar la asignacion", font = ('Times 12')).pack(pady = 20, anchor =  "w")
           
            # Consulta los clientes que tienen servicios para mostrarlos en la lista deplegable
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
        """Crea los campos de texto mediante un FieldFrame y un Combobox para solicitar al cliente la fecha de solicitud
        y el servicio respectivamente"""
        try:
            # Valida que se haya seleccionado un cliente para realizar la asignacion
            if self.clientesConCarritoCombo.get() == "":
                raise TextoVacio("Por favor seleccione un cliente con el que desea realizar la asignacion")

            Label(self.interfazServicio, text = "Detalles servicio", font = ('Times 18 bold')).pack(pady = 5, anchor = 'c')
            for i in self.clientesConServicios:
                if i.getNombre() == self.clientesConCarritoCombo.get():
                    self.cliente = i
            
            # Bloquea el paso anterior eliminando el boton y deshabilitando el campo
            self.clientesConCarritoCombo.config(state = DISABLED)
            self.boton1.destroy()

            servicios = self.cliente.obtenerServiciosSinEmpleado()
            
            values = [i.getNombre() for i in servicios]
            
            # Crea el field frame para la fecha de solicitud
            self.datos = FieldFrame(self.interfazServicio, "", ["Fecha (DD/MM/YYYY)"], "", [""], [], ["date"])

            # Crea el combobox para el servicio
            Label(self.datos, text = "Servicio", font = ('Times 12 bold')).grid(padx = 80, pady=2, column=0, row=len(self.datos.criterios)+1)
            self.serviciosCombo = ttk.Combobox(self.datos, values = values, state = "readonly", width = 37, justify = "center")
            self.serviciosCombo.grid(column = 1, row = len(self.datos.criterios)+1, pady = 2)

            self.boton2 = Button(self.interfazServicio, text = "Buscar empleados")
            self.boton2.pack(anchor = 'c')
            self.boton2.bind("<Button-1>", self.buscarEmpleados)
        except ErrorAplicacion as e:
            messagebox.showinfo(title = "Error Aplicacion", message = str(e))
       
    def buscarEmpleados(self, evento):
        """Busca los empleados que estan disponibles segun el servicio y la fecha solicitados en el paso anterior 
        y muestra el campo para la seleccion de este"""
        try:
            if self.serviciosCombo.get() == "":
                raise TextoVacio("Por favor seleccione un servicio antes de continuar")
            elementos = self.datos.obtenerDatos()
            fecha = elementos[0]
            servicio = self.serviciosCombo.get()
            servicios = self.cliente.obtenerServiciosSinEmpleado()
            self.servicioElegido = None
            # Obtiene el servicio seleccionado segun el nombre del combobox y la lista de servicios sin empleado asignado del cliente
            for i in servicios:
                if i.getNombre() == servicio:
                    self.servicioElegido = i
                    break
            
            fechaDate = datetime.strptime(fecha, '%d/%m/%Y')
            self.empleadosDisponibles = self.servicioElegido.consultarDisponibilidad(fechaDate)
            if len(self.empleadosDisponibles) == 0:
                raise ErrorListasVacias("No hay empleados disponibles para esta fecha") 
            else:
                # Si hay empleados disponibles, sigue al siguente paso, borra el boton previo y añade el campo de empleado
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
        """Asigna el empleado al servicio solicitado y muestra el resultado en el campo de resultado si todo fue exitoso"""
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
            self.serviciosCombo.config(state = DISABLED)
            self.cliente.seleccionarEmpleado(self.servicioElegido, self.empleadoElegido)
            self.textResultados.delete("1.0", END)
            self.textResultados.insert("1.0", "Se ha asignado el empleado " + self.empleadoElegido.getNombre() + " al servicio " + self.servicioElegido.getNombre())
        except ErrorAplicacion as e:
            messagebox.showinfo(title = "Error Aplicacion", message = str(e))