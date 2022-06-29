from tkinter import Frame, BOTH, DISABLED, END, Button, Label, ttk, messagebox, Text
from gestorAplicacion.general.Inventario import Inventario
from gestorAplicacion.general.DiaSemana import DiaSemana
from uiMain.ventanaPrincipal.fieldFrame import FieldFrame
from gestorAplicacion.personas.Empleado import Empleado
from gestorAplicacion.personas.Contrato import Contrato
from gestorAplicacion.personas.Cliente import Cliente
from gestorAplicacion.personas.Persona import Persona
from manejoErrores.errorAplicacion import ErrorAplicacion
from manejoErrores.textoVacio import TextVacio
from datetime import datetime

class ContratarPersona(Frame):
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
            
            self.interfazPersona = Frame(self.interfazDatos)
            self.interfazPersona.grid(column = 0, row = 0)

            self.interfazContratacion = Frame(self.interfazDatos)
            self.interfazContratacion.grid(column = 1, row = 0)

            Label(self.interfazPersona, text = "Contratar Persona", font = ('Times 18 bold')).pack(pady = 5, anchor = 'c')
            Label(self.interfazPersona, text = "Por favor seleccione la persona que desea contratar", font = ('Times 12')).pack(pady = 20, anchor =  "w")
           
          
            self.personasAContratar = Inventario.getListadoPersonas()
            self.personasAContratar = [i for i in self.personasAContratar if not isinstance(i, Cliente)]

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

        servicio = Inventario.getListadoServicios()	
        
        if ((isinstance(self.personaAContratar, Persona)) and (not(isinstance(self.personaAContratar, Empleado))) and(not(isinstance(self.personaAContratar, Cliente)))):
            Label(self.interfazContratacion, text = "A continuación ingrese el salario que se le asignara al nuevo empleado, su cargo, su fecha final del contrato, el servicio que prestará y sus días laborales", font = ('Times 12')).pack(pady = 20, anchor = "w")
            self.datos = FieldFrame(self.interfazContratacion, self.personaAContratar.getNombre(), ["Salario", "Cargo","Fecha final del contrato (DD/MM/YYYY)", "Días laborales" ], "", [None, None, None, None], [], [0, -1, "date", -1])

            Label(self.datos, text = "Servicio", font = ('Times 12 bold')).grid(padx = 80, pady=2, column=0, row=len(self.datos.criterios)+1)
            self.comboServicio = ttk.Combobox(self.datos, values = servicio, state = "readonly")
            self.comboServicio.grid(column = 1, row = len(self.datos.criterios)+1, pady = 2)
            
        else:
            Label(self.interfazContratacion, text = "A continuación podrá visualizar la información del empleado recién elegido al cual se le renovará contrato. Si desea cambiar la informacion, ingrésela", font = ('Times 12')).pack(pady = 20, anchor =  "w")
            
            diasLaborales = []
            for i in self.personaAContratar.getDiasLaborales():
                diasLaborales.append(i.name)

            self.datos = FieldFrame(self.interfazContratacion, self.personaAContratar.getNombre(), ["Salario", "Cargo", "Días laborales", "Fecha renovación del contrato (DD/MM/YYYY)" ], "", [self.personaAContratar.getContrato().getSalario(), self.personaAContratar.getCargo(), diasLaborales, None], [], [0, -1, -1, "date"])

            Label(self.datos, text = "Servicio", font = ('Times 12 bold')).grid(padx = 80, pady=2, column=0, row=len(self.datos.criterios)+1)
            self.comboServicio = ttk.Combobox(self.datos, values = servicio, state = "readonly")
            self.comboServicio.grid(column = 1, row = len(self.datos.criterios)+1, pady = 2)
            self.comboServicio.set(self.personaAContratar.getServicio().getNombre())
       
        boton = Button(self.interfazContratacion, text = "Contratar")
        boton.pack(anchor = 'c')
        boton.bind("<Button-1>", self.crearContrato)
       
    def crearContrato(self, evento):
    
        try:

            elementos = self.datos.obtenerDatos()

            if ((isinstance(self.personaAContratar, Persona)) and (not(isinstance(self.personaAContratar, Empleado))) and(not(isinstance(self.personaAContratar, Cliente)))):
                salario = elementos[0]

                cargo = elementos[1]

                diasLaborales = elementos[2]
                nuevosDiasLaborales = []
                d = diasLaborales.split(" ")
                for i in d:
                    nuevosDiasLaborales.append(DiaSemana.name(i.upper()))
                    

                fechaFinContrato = datetime.strptime(elementos[3], "%d/%m/%Y")

                if self.comboServicio.get() == "":
                    raise TextVacio("Por favor seleccione un cliente con el que desea realizar el pago")
                
                servicio = Inventario.buscarServicio(self.comboServicio.get())
               
                self.personaAContratar.contratar(Contrato(salario, datetime.today(), fechaFinContrato), cargo, servicio, nuevosDiasLaborales)

            else:
                if elementos[0] != self.personaAContratar.getContrato().getSalario():
                    salario2 = elementos[0]
                    self.personaAContratar.getContrato().setSalario(salario2)

                if elementos[1] != self.personaAContratar.getCargo():
                    cargo2 = elementos[1]
                    self.personaAContratar.setCargo(cargo2)


                if elementos[2] != diasLaborales:
                        dias = elementos[2]
                        nuevosDiasLaborales2 = []
                        d = dias.split(" ")
                        for i in d:
                            nuevosDiasLaborales2.append(DiaSemana.name(i.upper()))
                        self.personaAContratar.setDiasLaborales(nuevosDiasLaborales2)

                fechaRenovacionContrato =  datetime.strptime(elementos[3], "%d/%m/%Y")

                self.personaAContratar.renovarContrato(fechaRenovacionContrato)

        except ErrorAplicacion as e:
            messagebox.showinfo(title = "Error Aplicacacion", message = str(e))