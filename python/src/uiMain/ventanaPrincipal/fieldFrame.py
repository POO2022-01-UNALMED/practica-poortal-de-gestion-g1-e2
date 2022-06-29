from tkinter import DISABLED, Entry, Frame, BOTH, Label, StringVar, messagebox
import re
from manejoErrores.datoNoString import DatoNoString
from manejoErrores.datosNoFecha import DatoNoFecha

from manejoErrores.errorAplicacion import ErrorAplicacion
from manejoErrores.textoVacio import TextVacio
from manejoErrores.datosNoDigito import DatoNoDigito
from manejoErrores.datosFueraDelRango import DatoFueraDelRango
from datetime import datetime

class FieldFrame(Frame):
    # tituloC es el titulo del criterio
    # critero es una lista con todos los nombres de los criterios
    # tituoV es el titulo del valor
    # valores es una lista con todos los valores por defecto de los criterios. En caso de que no lo tenga poner None
    # noHabilitado es una lista con los nombres de los criterios que no son editables
    # tipos represente el tipo de dato, -1 si es String, 0 si es int y >0 si tiene un límite máximo
    def __init__(self, window, tituloC: str, criterio: 'list[str]', tituloV: str, valores: 'list[str]', noHabilitado: 'list[str]', tipos: 'list[int]'):
        super().__init__(window)
        self.tituloC = tituloC
        self.criterios = criterio
        self.tituloV = tituloV
        self.valores = valores
        self.noHabilitado = noHabilitado
        self.tipos = tipos
        self.entradas: list[Entry] = []
        self.valoresFinal = []
        self.pack(anchor = 'c')
        self.creacion()

    def creacion(self):
        Label(self, text = self.tituloC, font = ('Times 12 bold')).grid(padx = 80, column = 0, row = 0)
        Label(self, text = self.tituloV, font = ('Times 12 bold')).grid(padx = 80, column = 1, row = 0)

        for i in range(1, len(self.valores)+1):
            # Nombre del criterio
            Label(self, text = self.criterios[i-1], font = ('Times 12 bold')).grid(padx = 80, pady=2, column=0, row=i)
        
            texto = StringVar(value = self.valores[i-1])
            # Si no se puede modificar
            if self.criterios[i-1] in self.noHabilitado:
                entrada = Entry(self, width = 40, textvariable = texto, state = DISABLED, justify = "center")
            else:
                entrada = Entry(self, width = 40, textvariable = texto, justify = "center")
        
            entrada.grid(pady = 2, column = 1, row = i)
            self.entradas.append(entrada)
    
    def getValue(self, criterio: str):
        criteriosDict = dict(zip(self.criterios, self.valores))
        return criteriosDict[criterio]

    def verificarDato(self, valor, tipo, criterio):
        if len(valor) == 0:
            self.camposVacios.append(criterio)
        elif tipo == -1:
            if str.isdigit(valor):
                self.camposNoString.append(criterio)
        elif tipo == "date":
            if not re.fullmatch('\\d{2}/\\d{2}/\\d{4}', valor):
                self.camposNoFecha.append(criterio)
            else:
                try:
                    datetime.strptime(valor, "%d/%m/%Y")
                except ValueError as e:
                    self.camposNoFecha.append(criterio)
        elif tipo >= 0:
            if not str.isdigit(valor):
                self.camposNoDigito.append(criterio)
            if tipo > 0 and int(valor) > tipo:
                self.camposFueraRango.append(criterio)
            
        
        

    def obtenerDatos(self):
        try:
            self.valoresFinal = []
            self.camposVacios = []
            self.camposNoString = []
            self.camposNoDigito = []
            self.camposFueraRango = []
            self.camposNoFecha = []

            for i in range(len(self.entradas)):
                valor = self.entradas[i].get()
                self.verificarDato(valor, self.tipos[i], self.criterios[i])
                self.valoresFinal.append(valor)
            
            if self.camposVacios:

                text = "Por favor ingrese los datos en los campos: "
                text += ", ".join(self.camposVacios)
                raise TextVacio(text)

            if self.camposNoString:

                text = "Por favor ingrese datos tipo texto en los campos: "
                text += ", ".join(self.camposNoString)
                raise DatoNoString(text)
            
            if self.camposNoDigito:

                text = "Por favor ingrese datos tipo entero en los campos: "
                text += ", ".join(self.camposNoDigito)
                raise DatoNoDigito(text)

            if self.camposFueraRango:

                text = "Por favor ingrese datos tipo entero y en el rango permitido en los campos: "
                text += ", ".join(self.camposFueraRango)
                raise DatoFueraDelRango(text)

            if self.camposNoFecha:

                text = "Por favor ingrese una fecha valida en el formato de fecha solicitado en los campos: "
                text += ", ".join(self.camposNoFecha)
                raise DatoNoFecha(text)

            return self.valoresFinal

        except ErrorAplicacion as e:
            messagebox.showinfo(title = "Error Aplicacacion", message = str(e))
        except Exception as e:
            pass