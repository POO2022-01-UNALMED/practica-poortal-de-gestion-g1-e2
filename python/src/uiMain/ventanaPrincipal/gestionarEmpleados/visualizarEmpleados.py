from tkinter import Frame, BOTH, DISABLED, END, Button, Label, ttk, messagebox, Text
from gestorAplicacion.general.Inventario import Inventario
from uiMain.ventanaPrincipal.fieldFrame import FieldFrame
from gestorAplicacion.personas.Empleado import Empleado

from uiMain.ventanaPrincipal.excepcion.errorAplicacion import ErrorAplicacion

class VisualizarEmpleado(Frame):
    def __init__(self, window):
        super().__init__(window)
        self.grid_propagate(False)
        self.pack_propagate(False)
        self.pack(fill = BOTH, expand = True)
        self.proceso()
      
    def proceso(self):
        try:
            interfaz = Frame(self, width=400, bg="red")
            interfaz.pack(anchor = 'c')
            Label(interfaz, text = "Visualizar Empleados", font = ('Times 18 bold')).pack(pady = 5, anchor = 'c')
            Label(interfaz, text = "Por favor seleccione un empleado para poder visualizar su información", font = ('Times 12')).pack(pady = 20, anchor = "w")

            # Crea un combobox con los clientes que tienen un carrito con algún elemento
            self.NombresEmpleados = Inventario.getListadoEmpleados()
            values = [i.getNombre() for i in self.NombresEmpleados]
            #values = ["hola", "holita", "holota"] #Solo para pruebas
            self.combo = ttk.Combobox(interfaz, values = values, state = "readonly")
            self.combo.pack(pady = 20, anchor = 'c')

            # Crea boton para poder realizar el pago
            boton = Button(interfaz, text = "Ver información")
            boton.pack(pady = 10, anchor = 'c')
            boton.bind("<Button-1>", self.verInformacionEmpleados)

            # Frame para poner resultados
            self.resultados = Frame(self)
            self.resultados.pack(fill = BOTH,anchor = "c")
            Label(self.resultados, text = "Resultados", font = ('Times 12')).pack(anchor = "w")

            # Resultados de la Ejecucion
            self.textResultados = Text(self.resultados, padx = 10, pady = 10)
            self.textResultados.pack(fill = BOTH)

        except ErrorAplicacion as e:
            print(1)

    def verInformacionEmpleados(self, evento):
        # De los clientes obtiene el cliente con el que ver el carrito
        for i in self.NombresEmpleados:
            if i.getNombre() == self.combo.get():
                empleado = i

        self.textResultados.delete('1.0', END)
        self.textResultados.insert('1.0', "La información del empleado es:\n"+empleado.mostrarInformacion())