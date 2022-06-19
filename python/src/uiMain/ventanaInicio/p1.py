from tkinter import Frame, scrolledtext, INSERT, Entry, PhotoImage, Label, Button
import os
import pathlib

from uiMain.ventanaPrincipal.principal import Principal

class P1(Frame):
    def __init__(self, window):
        super().__init__(window)
        self.p3 = Frame(self)
        self.p4 = Frame(self)
        self._window = window

        # Crea saludo en p3
        saludo = Entry(self.p3, width = 100)
        saludo.insert(INSERT, "Bienvenido al software POOrtal de Gestion")
        saludo.pack()

        # Breve descripcion de lo que hace el sistema
        self.descripcion = scrolledtext.ScrolledText(self.p3, height = 5)
        self.descripcion.tag_configure("center", justify = "center")
        self.descripcion.insert(INSERT, "Se necesita un sistema de gestión de facturación y de administración de contratos de empleados para poder realizar con éxito sus actividades que involucran a sus clientes, empleados, productos y servicios prestados. Para lograr esta gestión se creó el sistema “POOrtal de Gestión”, una solución orientada a objetos que incluye a todos los involucrados en tal gestión. Con POOrtal de Gestión los empleados podrán cumplir sus labores, los clientes podrán adquirir sus productos y servicios, se generarán facturas, entre otras. A continuación se muestra el diagrama de clases de la solución planteada.")

        # Lista con todas las imágenes del programa que han de ser mostradas
        self.imagenes = []
        self.numeroImagen = 0
        for i in range(1,6):
            path = os.path.join(pathlib.Path(__file__).parent.absolute(),"imagenes\imagen_{}.png".format(i))
            self.imagenes.append(PhotoImage(file = path))

        self.label = Label(self.p4, image = self.imagenes[0], height = 500, width = 750)
        # Evento para pasar la imagen cuando el mouse ingrese a la imagen
        self.label.bind('<Enter>', self.siguienteImagen)
        self.label.pack()

        self.p3.pack()
        self.p4.pack()

        # Botón para direccionar a la página principal
        boton = Button(self, text = "Ventana Principal del Sistema", command = self.ventanaPrincipal)
        boton.pack()

    def siguienteImagen(self, _):
        self.numeroImagen %= 5
        self.label.configure(image = self.imagenes[self.numeroImagen])
        self.label.image = self.imagenes[self.numeroImagen]
        self.numeroImagen += 1

    def ventanaPrincipal(self):
        self._window.destroy()
        ventana = Principal()
        ventana.mainloop()
