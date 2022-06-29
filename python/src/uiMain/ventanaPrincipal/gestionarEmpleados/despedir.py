from tkinter import Frame, BOTH, DISABLED, END, Button, Label, ttk, messagebox, Text
from gestorAplicacion.general.Inventario import Inventario
from uiMain.ventanaPrincipal.fieldFrame import FieldFrame
from gestorAplicacion.personas.Empleado import Empleado
from gestorAplicacion.personas.Contrato import Contrato
from baseDatos.serializador import Serializador
from manejoErrores.textoVacio import TextoVacio

# Esta clase extiende de Frame y se encarga de mostrar la interfaz
# correspondiente a la funcionalidad despedir empleado

# @author Mateo Alvarez Lebrum
# @author Alejandro Alvarez Botero
# @author Miguel Angel Barrera Bustamante
# @author Alejandra Barrientos Grisales


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
            # Se crea un frame donde van a aparecer todos los campos necesarios que el usuario debe seleccionar y completar
            interfaz = Frame(self, width=400)
            interfaz.pack(anchor = 'c')
            Label(interfaz, text = "Despedir Empleado", font = ('Times 18 bold')).pack(pady = 5, anchor = 'c')
            Label(interfaz, text = "Por favor seleccione un empleado para realizarle el proceso de despido", font = ('Times 12')).pack(pady = 20, anchor = "w")

            # Crea un combobox con los empleados activos
            self.NombresEmpleados = Inventario.getListadoEmpleadosActivos()
            values = [i.getNombre() for i in self.NombresEmpleados]
            self.combo = ttk.Combobox(interfaz, values = values, state = "readonly")
            self.combo.pack(pady = 20, anchor = 'c')

            # Crea boton para poder realizar el despido
            boton = Button(interfaz, text = "Despedir")
            boton.pack(pady = 10, anchor = 'c')
            boton.bind("<Button-1>", self.despedirEmpleado)

            # Frame para poner resultados
            self.resultados = Frame(self, bg = "blue")
            self.resultados.pack(fill = BOTH,anchor = "c")
            Label(self.resultados, text = "Resultados", font = ('Times 12')).pack(anchor = "w")

            # Resultados de la Ejecucion
            self.textResultados = Text(self.resultados, padx = 10, pady = 10)
            self.textResultados.pack(fill = BOTH)

        except ErrorAplicacion as e:
            messagebox.showinfo(title = "Error Aplicacacion", message = str(e))
    # Metodo que se va a ejecutar cuando presionen el boton despedir
    #Método que despide 
    def despedirEmpleado(self, evento):
        try: 
            
           
            if self.combo.get() == "":
                raise TextoVacio("Por favor seleccione un empleado")

            for i in self.NombresEmpleados:
                if i.getNombre() == self.combo.get():
                    empleado = i
                    i.despedirE()
            # Elimina la informacion de los resultados y genera un nuevo comentario con el mensaje de confirmación de que sí se despidió
            self.textResultados.delete('1.0', END)
            self.textResultados.insert('1.0', "La persona: "+ empleado.getNombre() +" ha sido despedido con éxito")
        except ErrorAplicacion as e:
            messagebox.showinfo(title = "Error Aplicacacion", message = str(e))
       