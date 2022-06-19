from tkinter import Frame, Tk, Menu, Toplevel, Label, Text, INSERT, scrolledtext, BOTH
import os
import pathlib


#from baseDatos.deserializador import Deserializador
#from baseDatos.serializador import Serializador
from uiMain.ventanaPrincipal.pagar import Pagar
from uiMain.ventanaPrincipal.gestionarCarrito.verCarrito import VerCarrito

class Principal(Tk):
    def __init__(self):
        super().__init__()
        #Deserializador.deserializarTodo()
        self.title("POOrtal de Gestión")
        self.option_add("*tearOff", False)
        self.minsize(680, 420)

        # Se crea la barra de menu principal
        self.barraMenu = Menu(self)
        self.config(menu = self.barraMenu)

        # Se crean los submenus
        archivo = Menu(self.barraMenu)
        procesos = Menu(self.barraMenu)
        ayuda = Menu(self.barraMenu)

        # Se añaden los tres submenus al menu principal
        self.barraMenu.add_cascade(label = "Archivo", menu = archivo )
        self.barraMenu.add_cascade(label = "Procesos y Consultas", menu = procesos)
        self.barraMenu.add_cascade(label = "Ayuda", menu = ayuda)

        # Menu Archivo        
        archivo.add_command(label = "Aplicación", command = lambda: self.menuAplicion())
        archivo.add_command(label = "Salir", command = lambda: self.menuSalir())

        # Menu Ayuda        
        ayuda.add_command(label = "Acerca de", command = lambda: self.menuAyuda())

        # Menu Procesos 
        procesos.add_command(label = "Ver mi Carrito", command = lambda: self.cambiarFrame(4))       
        procesos.add_command(label = "Pagar", command = lambda: self.cambiarFrame(11))

        self.ventanaActual = Frame(self, width = 680, height = 420, bg = "blue")
        self.ventanaActual.grid_propagate(False)
        text = scrolledtext.ScrolledText(self.ventanaActual)
        path = os.path.join(pathlib.Path(__file__).parent.absolute(),"instrucciones.txt")
        with open(path, "r+") as instrucciones:
            text.insert(INSERT, instrucciones.read())
        text.tag_configure('center', justify='center')
        self.ventanaActual.pack()
        text.pack()
        

    def cambiarFrame(self, num):
        self.ventanaActual.destroy()
        # Crear los frames
        ventanas = {11: Pagar, 4: VerCarrito}

        self.ventanaActual = ventanas.get(num)(self)
        self.ventanaActual.pack()


    def menuAplicion(self):
        top = Toplevel(self)
        top.geometry("580x320")
        top.resizable(False,False)
        top.title("Aplicación")

        texto = "Se necesita un sistema de gestión de facturación y de administración de contratos de empleados para poder realizar con éxito sus actividades que involucran a sus clientes, empleados, productos y servicios prestados. Para lograr esta gestión se creó el sistema “POOrtal de Gestión”, una solución orientada a objetos que incluye a todos los involucrados en tal gestión. Con POOrtal de Gestión los empleados podrán cumplir sus labores, los clientes podrán adquirir sus productos y servicios, se generarán facturas, entre otras. A continuación se muestra el diagrama de clases de la solución planteada."

        Label(top, text = texto , font = ('Times 12'), wraplength = 500).pack(fill = BOTH, expand=True)
        
    def menuSalir(self):
        # Se hace para evitar un import circular
        from uiMain.ventanaInicio.ventanaInicio import VentanaInicio
        #Serializador.serializarTodo()
        self.destroy()
        ventana = VentanaInicio()
        ventana.mainloop()

    def menuAyuda(self):
        top = Toplevel(self)
        top.geometry("580x320")
        top.resizable(False,False)
        top.title("Ayuda")

        texto = "Autores:\nAlejandra Barrientos Grisales\nAlejandro Álvarez Botero\nMateo Álvarez Lebrum\nMiguel Ángel Barrera Bustamante"

        Label(top, text = texto , font = ('Times 18 bold'), wraplength = 500).pack(fill = BOTH, expand=True)