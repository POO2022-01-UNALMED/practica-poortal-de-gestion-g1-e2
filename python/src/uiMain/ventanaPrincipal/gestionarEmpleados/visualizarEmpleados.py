from tkinter import Frame, BOTH, DISABLED, END, Button, Label, ttk, messagebox, Text
from gestorAplicacion.general.Inventario import Inventario
from uiMain.ventanaPrincipal.fieldFrame import FieldFrame
from gestorAplicacion.personas.Empleado import Empleado
from manejoErrores.textoVacio import TextoVacio

from manejoErrores.errorAplicacion import ErrorAplicacion

# Esta clase extiende de Frame y se encarga de mostrar la interfaz
# correspondiente a la funcionalidad visualizar empleados

# @author Mateo Alvarez Lebrum
# @author Alejandro Alvarez Botero
# @author Miguel Angel Barrera Bustamante
# @author Alejandra Barrientos Grisales

class VisualizarEmpleado(Frame):
    def __init__(self, window):
        super().__init__(window)
        self.grid_propagate(False)
        self.pack_propagate(False)
        self.pack(fill = BOTH, expand = True)
        self.proceso()
      
    def proceso(self):
        try:
             # Se crea un frame superior donde se seleccionará un empleado
            interfaz = Frame(self, width=400)
            interfaz.pack(anchor = 'c')
            Label(interfaz, text = "Visualizar Empleados", font = ('Times 18 bold')).pack(pady = 5, anchor = 'c')
            Label(interfaz, text = "Por favor seleccione un empleado para poder visualizar su información", font = ('Times 12')).pack(pady = 20, anchor = "w")

            # Crea un combobox con la lista de empleados
            self.NombresEmpleados = Inventario.getListadoEmpleados()
            values = [i.getNombre() for i in self.NombresEmpleados]
            self.combo = ttk.Combobox(interfaz, values = values, state = "readonly")
            self.combo.pack(pady = 20, anchor = 'c')

            # Crea boton para poder ver la información
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

    # Metodo que se va a ejecutar cuando presionen el boton ver información
    # Este metodo se encargar de mostrar la información de los empleados
    def verInformacionEmpleados(self, evento):
        try:
            
            #Saca error si no se selecciona un empleado
            if self.combo.get() == "":
                raise TextoVacio("Por favor seleccione un empleado")

            for i in self.NombresEmpleados:
                if i.getNombre() == self.combo.get():
                    empleado = i
             
            # Elimina la informacion de los resultados y genera un nuevo comentario con la informacion del empleado
            self.textResultados.delete('1.0', END)
            self.textResultados.insert('1.0', "La información del empleado es:\n"+empleado.mostrarInformacion())

        except ErrorAplicacion as e:
            messagebox.showinfo(title = "Error Aplicacacion", message = str(e))