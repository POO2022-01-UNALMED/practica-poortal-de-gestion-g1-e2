from tkinter import Frame, Tk, Menu
from uiMain.ventanaInicio.p1 import P1
from uiMain.ventanaInicio.p2 import P2

# Esta clase crea la interfaz principal del programa en la cual
# se mostrará la hoja de vida de cada usuario, una descripción del
# programa e imágenes asociadas a este
# @author Alejandro Alvarez
# @author Alejandra Barrientos
# @author Mateo Alvarez
# @author Miguel Barrera

class VentanaInicio(Tk):
    def __init__(self):
        super().__init__()
        self.title("POOrtal de Gestion")
        self.option_add("*tearOff", False)

        # Se crea el menú principal
        self.barraMenu = Menu(self)

        # Se crea el submenú
        inicio = Menu(self.barraMenu)
        # Se añaden las dos opciones del submenú
        # Si da click en descripcion, muestra la descripcion del sistema
        inicio.add_command(label = "Descripcion", command = lambda: self.p1.descripcion.pack())
        # Si da click en salir, cierra el programa
        inicio.add_command(label = "Salir", command = lambda: self.destroy())

        self.barraMenu.add_cascade(label = "Inicio", menu = inicio)
        self.config(menu = self.barraMenu)

        self.p1 = P1(self)
        self.p2 = P2(self)

        self.p1.grid(row = 0, column = 0)
        self.p2.grid(row = 0, column = 1)
        
        