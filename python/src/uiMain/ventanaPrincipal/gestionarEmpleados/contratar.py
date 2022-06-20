from tkinter import Frame, BOTH, DISABLED, END, Button, Label, ttk, messagebox, Text
from gestorAplicacion.general.Inventario import Inventario
from uiMain.ventanaPrincipal.fieldFrame import FieldFrame
from gestorAplicacion.personas.Empleado import Empleado
from gestorAplicacion.personas.Cliente import Cliente
from gestorAplicacion.personas.Persona import Persona
from uiMain.ventanaPrincipal.excepcion.errorAplicacion import ErrorAplicacion

class ContratarPersona(Frame):
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
            
            self.interfazPersona = Frame(self.interfazDatos)
            self.interfazPersona.grid(column = 0, row = 0)

            self.interfazContratacion = Frame(self.interfazDatos)
            self.interfazContratacion.grid(column = 1, row = 0)

            Label(self.interfazPersona, text = "Contratar Persona", font = ('Times 18 bold')).pack(pady = 5, anchor = 'c')
            Label(self.interfazPersona, text = "Por favor seleccione la persona que desea contratar", font = ('Times 12')).pack(pady = 20, anchor =  "w")
           
          
            self.personasAContratar = Inventario.getListadoPersonas()
            values = [i.getNombre() for i in self.personasAContratar]
            self.personasAContratarCombo = ttk.Combobox(self.interfazPersona, values = values, state = "readOnly")
            self.personasAContratarCombo.pack(pady = 20, anchor = 'c')

            self.boton1 = Button(self.interfazPersona, text = "Continuar")
            self.boton1.pack(anchor = 'c')
            self.boton1.bind("<Button-1>", self.informacion)

        except Exception as e:
            print(str(e))

    def informacion(self, evento):
        Label(self.interfazContratacion, text = "Información de la persona", font = ('Times 18 bold')).pack(pady = 5, anchor = 'c')
      
        if self.personasAContratarCombo.get() == "":
            raise Exception("Por favor seleccione una persona")

        for i in self.personasAContratar:
            if i.getNombre() == self.personasAContratarCombo.get():
                self.personaAContratar = i
        
        self.personasAContratarCombo.config(state = DISABLED)
        self.boton1.destroy()
			
        if ((isinstance(self.personaAContratar, Persona)) and (not(isinstance(self.personaAContratar, Empleado))) and(not(isinstance(self.personaAContratar, Cliente)))):
            Label(self.interfazContratacion, text = "A continuación ingrese el salario que se le asignara al nuevo empleado, su cargo, su fecha final del contrato, el servicio que prestará y sus días laborales", font = ('Times 12')).pack(pady = 20, anchor = "w")
            self.datos = FieldFrame(self.interfazContratacion, self.personaAContratar.getNombre(), ["Salario", "Cargo","Fecha final del contrato", "Servicio", "Días laborales" ], "", [None, None, None, None, None], [], [0, -1, -1, -1, -1])
        else:
            Label(self.interfazContratacion, text = "Actualice datos", font = ('Times 12')).pack(pady = 20, anchor =  "w")
            self.datos = FieldFrame(self.interfazContratacion, self.personaAContratar.getNombre(), ["Salario", "Cargo","Fecha final del contrato", "Servicio", "Días laborales" ], "", [None, None, None, None, None], [], [0, -1, -1, -1, -1])
       
        boton = Button(self.interfazContratacion, text = "Contratar")
        boton.pack(anchor = 'c')
       
     