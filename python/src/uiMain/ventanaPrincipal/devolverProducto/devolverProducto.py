from tkinter import BOTH, DISABLED, END, Button, Frame, Label, ttk, messagebox, Text
from gestorAplicacion.personas.Cliente import Cliente
from uiMain.ventanaPrincipal.fieldFrame import FieldFrame
from datetime import datetime

#from gestorAplicacion.general.inventario import Inventario
#from gestorAplicacion.personas.cliente import Cliente
#from gestorAplicacion.ventas.Factura import Factura

from manejoErrores.errorAplicacion import ErrorAplicacion
from manejoErrores.datosNoFecha import DatoNoFecha
import re

class DevolverProducto(Frame):
    def __init__(self, window):
        super().__init__(window,width = 680, height = 420)
        self.grid_propagate(False)
        self.pack_propagate(False)
        self.pack(fill = BOTH, expand = True)
        self.proceso()
        

    def proceso(self):
        try:
            # Crea un frame principal para que el usuario seleccione los datos
            self.interfaz = Frame(self, width = 400)
            self.interfaz.pack(anchor = 'c')

            Label(self.interfaz, text = "Devolver Producto", font = ('Times 18 bold')).pack(pady = 5, anchor = 'c')
            Label(self.interfaz, text = "Por favor diligencie los campos para devolver un producto", font = ('Times 12')).pack(pady = 20, anchor = "c")

            self.formulario = FieldFrame(self.interfaz, "Datos de compra", ["Nombre del producto", "Identificacion del comprador", "Numero de productos a devolver", "Fecha de compra (DD/MM/YYYY)"], "Valor", [None, None, None, None], [],[-1, 0, 0, "date"])

            # Crea boton para poder realizar la devolucion
            boton = Button(self.interfaz, text = "Devolver")
            boton.pack(pady = 10, anchor = 'c')
            boton.bind("<Button-1>", self.devolver)

            # Frame para poner resultados
            self.resultados = Frame(self, width = 400)
            self.resultados.pack(fill = BOTH,anchor = "c")
            Label(self.resultados, text = "Resultados", font = ('Times 12')).pack(anchor = "w")

            # Resultados de la Ejecucion
            self.textResultados = Text(self.resultados, padx = 10, pady = 10)
            self.textResultados.pack(fill = BOTH)


        except ErrorAplicacion as e:
            messagebox.showinfo(title = "Error de la Aplicaci??n", message = str(e))
    
    def devolver(self, evento):
        
        try:
            elementos = self.formulario.obtenerDatos()
            # conversion de datos de entrada
            elementos[3] = datetime.strptime(elementos[3], "%d/%m/%Y")
            elementos[2] = int(elementos[2])
            # llamada al metodo de la funcionalidad
            self.textResultados.delete("1.0", END)
            self.textResultados.insert("1.0", Cliente.devolverProducto(*elementos))

        except ErrorAplicacion as e:
            messagebox.showinfo(title = "Error de la Aplicaci??n", message = str(e))
        
        except Exception as e:
            pass
        