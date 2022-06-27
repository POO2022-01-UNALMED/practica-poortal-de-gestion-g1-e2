from tkinter import BOTH, END, Button, Frame, Label, ttk, messagebox, Text

from gestorAplicacion.general.Inventario import Inventario
from manejoErrores.errorAplicacion import ErrorAplicacion
from gestorAplicacion.personas.Cliente import Cliente
from gestorAplicacion.ventas.Factura import Factura

class Pagar(Frame):
    def __init__(self, window):
        super().__init__(window,width = 680, height = 420)
        self.grid_propagate(False)
        self.pack_propagate(False)
        self.pack(fill = BOTH, expand = True)
        self.proceso()
        

    def proceso(self):

        # Crea un frame principal para que el usuario seleccione los datos
        self.interfaz = Frame(self, width = 400)
        self.interfaz.pack(anchor = 'c')

        Label(self.interfaz, text = "Pagar", font = ('Times 18 bold')).pack(pady = 5, anchor = 'c')
        Label(self.interfaz, text = "Por favor seleccione el empleado con el que quiere realizar el pago", font = ('Times 12')).pack(pady = 20, anchor = "w")

        self.informacion()

        # Frame para poner resultados
        self.resultados = Frame(self, width = 400)
        self.resultados.pack(fill = BOTH,anchor = "c")
        Label(self.resultados, text = "Resultados", font = ('Times 12')).pack(anchor = "w")

        # Resultados de la Ejecucion
        self.textResultados = Text(self.resultados, padx = 10, pady = 10)
        self.textResultados.pack(fill = BOTH)

    
    def pagar(self, evento):
        try:
            # De los clientes obtiene el cliente con el que pagar
            for i in self.clientes:
                if i.getNombre() == self.combo.get():
                    cliente = i


            factura: Factura = cliente.pagar()
            

            self.textResultados.delete('1.0', END)
            self.textResultados.insert('1.0', "Se ha generado una factura a nombre de "+str(cliente.getNombre())+" con identificación "+str(cliente.getIdentificacion())+"\n")
            self.textResultados.insert(END, factura.mostrarInformacion())

            self.combo.destroy()
            self.boton.destroy()
            self.informacion()

        except ErrorAplicacion as e:
            print("hola")



    def informacion(self):
        # Crea un combobox con los clientes que tienen un carrito con algún elemento
        self.clientes = Inventario.clientesConCarrito()
        values = [i.getNombre() for i in self.clientes]
        #values = ["hola", "holita", "holota"] #Solo para pruebas
        self.combo = ttk.Combobox(self.interfaz, values = values, state = "readonly")
        self.combo.pack(pady = 20, anchor = 'c')

        # Crea boton para poder realizar el pago
        self.boton = Button(self.interfaz, text = "Pagar")
        self.boton.pack(pady = 10, anchor = 'c')
        self.boton.bind("<Button-1>", self.pagar)