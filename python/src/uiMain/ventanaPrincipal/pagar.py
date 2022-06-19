from tkinter import BOTH, DISABLED, END, Button, Frame, Label, ttk, messagebox, Text

#from gestorAplicacion.general.inventario import Inventario
from uiMain.ventanaPrincipal.excepcion.errorAplicacion import ErrorAplicacion
#from gestorAplicacion.personas.cliente import Cliente
#from gestorAplicacion.ventas.Factura import Factura

class Pagar(Frame):
    def __init__(self, window):
        super().__init__(window,width = 680, height = 420, bg = "yellow")
        self.grid_propagate(False)
        self.pack_propagate(False)
        self.pack(fill = BOTH, expand = True)
        self.proceso()
        

    def proceso(self):
        try:
            # Crea un frame principal para que el usuario seleccione los datos
            self.interfaz = Frame(self, width = 400,  bg = "red")
            self.interfaz.pack(anchor = 'c')

            Label(self.interfaz, text = "Pagar", font = ('Times 18 bold')).pack(pady = 5, anchor = 'c')
            Label(self.interfaz, text = "Por favor seleccione el empleado con el que quiere realizar el pago", font = ('Times 12')).pack(pady = 20, anchor = "w")

            # Crea un combobox con los clientes que tienen un carrito con algún elemento
            #self.clientes = Inventario.clientesConCarrito()
            #values = [i.getNombre() for i in clientes]
            values = ["hola", "holita", "holota"] #Solo para pruebas
            self.combo = ttk.Combobox(self.interfaz, values = values, state = "readonly")
            self.combo.pack(pady = 20, anchor = 'c')

            # Crea boton para poder realizar el pago
            boton = Button(self.interfaz, text = "Pagar")
            boton.pack(pady = 10, anchor = 'c')
            boton.bind("<Button-1>", self.pagar)

            # Frame para poner resultados
            self.resultados = Frame(self, width = 400, bg = "blue")
            self.resultados.pack(fill = BOTH,anchor = "c")
            Label(self.resultados, text = "Resultados", font = ('Times 12')).pack(anchor = "w")

            # Resultados de la Ejecucion
            self.textResultados = Text(self.resultados, padx = 10, pady = 10)
            self.textResultados.pack(fill = BOTH)


        except ErrorAplicacion as e:
            messagebox.showinfo(title = "Error de la Aplicación", message = str(e))
    
    def pagar(self, evento):
        '''# De los clientes obtiene el cliente con el que pagar
        for i in self.clientes:
            if i.getNombre() == self.combo.get():
                cliente = i

        factura: Factura = cliente.pagar()

        self.textResultados.delete('1.0', END)
        self.textResultados.insert('1.0', "Se ha generado una factura a nombre de "+str(cliente.getNombre())+" con identificación "+str(cliente.getIdentificacion()))
        self.textResultados.insert(END, factura.mostrarInformacion())'''


        # Muestra Resultados
        self.textResultados.delete('1.0', END)
        self.textResultados.insert('1.0', "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent imperdiet eleifend convallis. In felis urna, pharetra sed massa at, dapibus aliquam metus. Mauris in congue mi. Suspendisse auctor diam sit amet tortor malesuada elementum sed ac felis. Proin dictum libero non ipsum egestas tincidunt. Mauris vitae nulla vitae orci lacinia molestie non vitae augue. Donec vel lacus ante. Ut tincidunt tellus nec ante volutpat, et convallis mauris tempus. Proin augue nunc, placerat et finibus et, gravida vitae tortor. Fusce tincidunt lacus ipsum. Quisque suscipit urna sed enim convallis aliquam at at velit. Etiam ac gravida lacus, vel blandit urna. Nulla facilisi. Nulla eget ullamcorper eros. Vestibulum sed nisl quis leo malesuada bibendum.") #Solo para prueba
