from tkinter import Button, Frame, BOTH, Label, ttk, Text, END

from uiMain.ventanaPrincipal.excepcion.errorAplicacion import ErrorAplicacion
from gestorAplicacion.general.Inventario import Inventario

class VerCarrito(Frame):
    def __init__(self, window):
        super().__init__(window, bg = "red")
        self.grid_propagate(False)
        self.pack_propagate(False)
        self.pack(fill = BOTH, expand = True)
        self.proceso()

    def proceso(self):
        try:
            interfaz = Frame(self, width=400, bg="red")
            interfaz.pack(anchor = 'c')
            Label(interfaz, text = "Ver mi Carrito", font = ('Times 18 bold')).pack(pady = 5, anchor = 'c')
            Label(interfaz, text = "Por favor seleccione un cliente para poder visualizar el carrito", font = ('Times 12')).pack(pady = 20, anchor = "w")

            # Crea un combobox con los clientes que tienen un carrito con algún elemento
            self.clientes = Inventario.getClientes()
            values = [i.getNombre() for i in self.clientes]
            #values = ["hola", "holita", "holota"] #Solo para pruebas
            self.combo = ttk.Combobox(interfaz, values = values, state = "readonly")
            self.combo.pack(pady = 20, anchor = 'c')

            # Crea boton para poder realizar el pago
            boton = Button(interfaz, text = "Ver Carrito")
            boton.pack(pady = 10, anchor = 'c')
            boton.bind("<Button-1>", self.verCarrito)

            # Frame para poner resultados
            self.resultados = Frame(self, bg = "blue")
            self.resultados.pack(fill = BOTH,anchor = "c")
            Label(self.resultados, text = "Resultados", font = ('Times 12')).pack(anchor = "w")

            # Resultados de la Ejecucion
            self.textResultados = Text(self.resultados, padx = 10, pady = 10)
            self.textResultados.pack(fill = BOTH)

        except ErrorAplicacion as e:
            print(1)

    def verCarrito(self, evento):
        # De los clientes obtiene el cliente con el que ver el carrito
        for i in self.clientes:
            if i.getNombre() == self.combo.get():
                cliente = i

        self.textResultados.delete('1.0', END)
        self.textResultados.insert('1.0', "Su carrito está compuesto por:\n"+cliente.verCarrito())