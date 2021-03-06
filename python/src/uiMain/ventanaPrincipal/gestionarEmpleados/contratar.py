from tkinter import Frame, BOTH, DISABLED, END, Button, Label, ttk, messagebox, Text
from gestorAplicacion.general.Inventario import Inventario
from gestorAplicacion.general.DiaSemana import DiaSemana
from manejoErrores.errorListasVacias import ErrorListasVacias
from uiMain.ventanaPrincipal.fieldFrame import FieldFrame
from gestorAplicacion.personas.Empleado import Empleado
from gestorAplicacion.personas.Contrato import Contrato
from gestorAplicacion.personas.Cliente import Cliente
from gestorAplicacion.personas.Persona import Persona
from manejoErrores.errorAplicacion import ErrorAplicacion
from manejoErrores.errorIngresoDatos import ErrorIngresoDatos
from manejoErrores.textoVacio import TextoVacio
from datetime import datetime

# Esta clase extiende de Frame y se encarga de mostrar la interfaz
# correspondiente a la funcionalidad contratar persona
# @author Mateo Alvarez Lebrum
# @author Alejandro Alvarez Botero
# @author Miguel Angel Barrera Bustamante
# @author Alejandra Barrientos Grisales


class ContratarPersona(Frame):
    def __init__(self, window):
        super().__init__(window)
        self.grid_propagate(False)
        self.pack_propagate(False)
        self.pack(fill = BOTH, expand = True)

        #Se crea un frame donde van a aparecer todos los campos necesarios que el usuario debe seleccionar y completar

        self.interfazDatos = Frame(self)
        self.interfazDatos.pack(fill = BOTH)

        # Se crea un frame que va a almacenenar los resultados de la ejecución

        self.interfazResultados = Frame(self)
        self.interfazResultados.pack(fill = BOTH)
        Label(self.interfazResultados, text = "Resultados", font = ('Times 12')).pack(anchor = "w")

        # Resultados de la Ejecucion

        self.textResultados = Text(self.interfazResultados, padx = 10, pady = 10)
        self.textResultados.pack(fill = BOTH)

        self.proceso()

    # Metodo que se va a encargar de poner la informacion respecto a las personas y empleados
    def proceso(self):
        try:

            # Se crea un frame en el que el usuario puede seleccionar una persona o empleado
            
            self.interfazPersona = Frame(self.interfazDatos)
            self.interfazPersona.grid(column = 0, row = 0)

            # Se crea un frame en el que el usuario puede ingresar la informacion para contratar
            self.interfazContratacion = Frame(self.interfazDatos)
            self.interfazContratacion.grid(column = 1, row = 0)

            Label(self.interfazPersona, text = "Contratar Persona", font = ('Times 18 bold')).pack(pady = 5, anchor = 'c')
            Label(self.interfazPersona, text = "Por favor seleccione la persona que desea contratar", font = ('Times 12')).pack(pady = 20, anchor =  "w")
           
            # Se obtiene la informacion de las personas y se proyecta en un combobox
            self.personasAContratar = Inventario.getListadoPersonasParaContratar()
            if len(self.personasAContratar)==0:
                raise ErrorListasVacias("En estos momentos no hay personas para ser contratadas")

            self.personasAContratar = [i for i in self.personasAContratar if not isinstance(i, Cliente)]

            values = [i.getNombre() for i in self.personasAContratar]
            self.personasAContratarCombo = ttk.Combobox(self.interfazPersona, values = values, state = "readOnly")
            self.personasAContratarCombo.pack(pady = 20, anchor = 'c')

            # Se crea un boton con el que usuario puede continuar, cuando presiona este boton 
            # se ejecuta el metodo informacion()
            self.boton1 = Button(self.interfazPersona, text = "Continuar")
            self.boton1.pack(anchor = 'c')
            self.boton1.bind("<Button-1>", self.informacion)

        except ErrorAplicacion as e:
            messagebox.showinfo(title = "Error Aplicacacion", message = str(e))


    # Metodo que se va a ejecutar cuando presionen el boton continuar
    # y se va a encargar de mostrar la informacion para que el usuario debe completar
    # para poder contratar
    def informacion(self, evento):
        try:
            
          
            if self.personasAContratarCombo.get() == "":
                raise TextoVacio("Por favor seleccione una persona")

            Label(self.interfazContratacion, text = "Información de la persona", font = ('Times 18 bold')).pack(pady = 5, anchor = 'c')

            for i in self.personasAContratar:
                if i.getNombre() == self.personasAContratarCombo.get():
                    self.personaAContratar = i
            
            self.personasAContratarCombo.config(state = DISABLED)
            self.boton1.destroy()

            servicio = Inventario.getListadoServicios()	
            # el if se ejecuta cuando la persona no es ni empleado ni cliente
            if ((isinstance(self.personaAContratar, Persona)) and (not(isinstance(self.personaAContratar, Empleado))) and(not(isinstance(self.personaAContratar, Cliente)))):

                # se le pide al usuario ingresar los datos para generar contrato
                Label(self.interfazContratacion, text = "A continuación ingrese el salario que se le asignara al nuevo empleado, su cargo, su fecha", font = ('Times 12')).pack(pady = 1, anchor = "w")
                Label(self.interfazContratacion, text = "final del contrato, el servicio que prestará y sus días laborales", font = ('Times 12')).pack(pady = 1, anchor = "w")
                self.datos = FieldFrame(self.interfazContratacion, self.personaAContratar.getNombre(), ["Salario", "Cargo", "Días laborales (Ej: lunes jueves)", "Fecha final del contrato (DD/MM/YYYY)" ], "", [None, None, None, None], [], [0, -1, -1, "date"])

                Label(self.datos, text = "Servicio", font = ('Times 12 bold')).grid(padx = 80, pady=2, column=0, row=len(self.datos.criterios)+1)
                self.comboServicio = ttk.Combobox(self.datos, values = servicio, state = "readonly")
                self.comboServicio.grid(column = 1, row = len(self.datos.criterios)+1, pady = 2)
            
            # el else se ejecuta cuando la persona es empleado sin vigencia
            else:

                  # se le pide al usuario actualizar o no los datos para la renovación de contrato
                Label(self.interfazContratacion, text = "A continuación podrá visualizar la información del empleado recién elegido al cual se le renovará contrato.", font = ('Times 12')).pack(pady = 1, anchor =  "w")
                Label(self.interfazContratacion, text = "Si desea cambiar la informacion, ingrésela", font = ('Times 12')).pack(pady = 1, anchor =  "w")
                
                self.diasLaborales = []
                for i in self.personaAContratar.getDiasLaborales():
                    self.diasLaborales.append(i.name)

                self.datos = FieldFrame(self.interfazContratacion, self.personaAContratar.getNombre(), ["Salario", "Cargo", "Días laborales (Ej: lunes jueves)", "Fecha renovación del contrato (DD/MM/YYYY)" ], "", [self.personaAContratar.getContrato().getSalario(), self.personaAContratar.getCargo(), self.diasLaborales, None], [], [0, -1, -1, "date"])

                Label(self.datos, text = "Servicio", font = ('Times 12 bold')).grid(padx = 80, pady=2, column=0, row=len(self.datos.criterios)+1)
                self.comboServicio = ttk.Combobox(self.datos, values = servicio, state = "readonly")
                self.comboServicio.grid(column = 1, row = len(self.datos.criterios)+1, pady = 2)
                self.comboServicio.set(self.personaAContratar.getServicio().getNombre())
            
            
            boton = Button(self.interfazContratacion, text = "Contratar")
            boton.pack(anchor = 'c')
            boton.bind("<Button-1>", self.crearContrato)
        except ErrorAplicacion as e:
            messagebox.showinfo(title = "Error Aplicacacion", message = str(e))


    # Metodo que se encargar de ejecutar la funcionalidad de contratar
    def crearContrato(self, evento):
    
        try:
        
            if self.comboServicio.get()=="":
                raise TextoVacio("Por favor seleccione un servicio")

            elementos = self.datos.obtenerDatos()
            
            #Se obtienen los datos ingresados por el usuario y con estos se crea un nuevo contrato
            if ((isinstance(self.personaAContratar, Persona)) and (not(isinstance(self.personaAContratar, Empleado))) and(not(isinstance(self.personaAContratar, Cliente)))):
                salario = elementos[0]
                cargo = elementos[1]
                diasLaborales = elementos[2]
                fechaContrato = elementos[3]
                
                nuevosDiasLaborales = []
                d = diasLaborales.split(" ") 
                try:
                    for i in d:
                        nuevosDiasLaborales.append(DiaSemana[i.upper()])
                except Exception as e:
                    raise ErrorIngresoDatos("Ingrese días de la semana en el formato válido")
                
                fechaFinContrato = datetime.strptime(fechaContrato, "%d/%m/%Y")

                
                servicio = Inventario.buscarServicio(self.comboServicio.get())
               
                # Se vacia el texto de los resultados y se agrega uno nuevo
                self.personaAContratar.contratar(Contrato(salario, datetime.today(), fechaFinContrato), cargo, servicio, nuevosDiasLaborales)
                self.textResultados.delete("1.0", END)
                self.textResultados.insert("1.0", "Se ha contratado correctamente a la persona " + self.personaAContratar.getNombre())

                # Se destruye el frame donde está toda la informacion y se vuelve a crear, de esta manera se actulizan todos los campos que han de actualizarse despues de cada proceso
                self.interfazPersona.destroy()
                self.interfazContratacion.destroy()
                self.proceso()
            
            #Se obtienen los datos ingresados por el usuario y con estos se hace una renovación de contrato
            else:
                salario = elementos[0]
                cargo = elementos[1]
                diasLaborales = elementos[2]
                fechaContrato = elementos[3]
                if salario != self.personaAContratar.getContrato().getSalario():
                    self.personaAContratar.getContrato().setSalario(salario)

                if cargo != self.personaAContratar.getCargo():
                    self.personaAContratar.setCargo(cargo)

                

                nuevosDiasLaborales = []
                d = diasLaborales.split(" ")
                try:
                    for i in d:
                        nuevosDiasLaborales.append(DiaSemana[i.upper()])
                except Exception as e:
                    raise ErrorIngresoDatos("Ingrese días de la semana en el formato válido")
                self.personaAContratar.setDiasLaborales(nuevosDiasLaborales)

                fechaRenovacionContrato =  datetime.strptime(fechaContrato, "%d/%m/%Y")

                self.personaAContratar.renovarContrato(fechaRenovacionContrato)

                # Se vacia el texto de los resultados y se agrega uno nuevo
                self.textResultados.delete("1.0", END)
                self.textResultados.insert("1.0", "Se ha renovado correctamente el contrato del empleado " + self.personaAContratar.getNombre())
                
                # Se destruye el frame donde está toda la informacion y se vuelve a crear, de esta manera se actulizan todos los campos que han de actualizarse despues de cada proceso
                self.interfazPersona.destroy()
                self.interfazContratacion.destroy()
                self.proceso()
            
       
        except ErrorAplicacion as e:
            messagebox.showinfo(title = "Error Aplicacacion", message = str(e))