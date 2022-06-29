from tkinter import Frame, BOTH, DISABLED, END, Button, Label, ttk, messagebox, Text
from gestorAplicacion.general.Inventario import Inventario
from uiMain.ventanaPrincipal.fieldFrame import FieldFrame
from gestorAplicacion.personas.Empleado import Empleado
from gestorAplicacion.personas.Contrato import Contrato
from baseDatos.serializador import Serializador


from manejoErrores.errorAplicacion import ErrorAplicacion

class DespedirEmpleado(Frame):
    def __init__(self, window):
        super().__init__(window)
        self.grid_propagate(False)
        self.pack_propagate(False)
        self.pack(fill = BOTH, expand = True)
        self.proceso()

    def proceso(self):
        try:
            interfaz = Frame(self, width=400)
            interfaz.pack(anchor = 'c')
            Label(interfaz, text = "Despedir Empleado", font = ('Times 18 bold')).pack(pady = 5, anchor = 'c')
           
            if (len(Inventario.getListadoEmpleadosActivos()) == 0):
                Label(interfaz, text = "No hay empleados activos actualmente", font = ('Times 12')).pack(pady = 20, anchor = "w")

            Label(interfaz, text = "Por favor seleccione un empleado para realizarle el proceso de despido", font = ('Times 12')).pack(pady = 20, anchor = "w")

            # Crea un combobox con los clientes que tienen un carrito con algún elemento
            self.NombresEmpleados = Inventario.getListadoEmpleadosActivos()
            values = [i.getNombre() for i in self.NombresEmpleados]
            self.combo = ttk.Combobox(interfaz, values = values, state = "readonly")
            self.combo.pack(pady = 20, anchor = 'c')

            # Crea boton para poder realizar el pago
            boton = Button(interfaz, text = "Despedir")
            boton.pack(pady = 10, anchor = 'c')
            boton.bind("<Button-1>", self.despedirEmpleado)

            # Frame para poner resultados
            self.resultados = Frame(self)
            self.resultados.pack(fill = BOTH,anchor = "c")
            Label(self.resultados, text = "Resultados", font = ('Times 12')).pack(anchor = "w")

            # Resultados de la Ejecucion
            self.textResultados = Text(self.resultados, padx = 10, pady = 10)
            self.textResultados.pack(fill = BOTH)

        except ErrorAplicacion as e:
            print(1)

    def despedirEmpleado(self, evento):
        # De los empleados, se elige a cual despedir
        for i in self.NombresEmpleados:
            if i.getNombre() == self.combo.get():
                empleado = i
                i.despedirE()
        print(empleado.getContrato().getFechaFin())
        for i in Inventario.getListadoEmpleadosActivos():
            print(i.getNombre())
        #for i in Inventario.getListadoEmpleadosActivos():
         #   if i.getNombre() == empleado:
          #      i.despedir()


        self.textResultados.delete('1.0', END)
        self.textResultados.insert('1.0', "La persona: "+ empleado.getNombre() +" ha sido despedido con éxito")