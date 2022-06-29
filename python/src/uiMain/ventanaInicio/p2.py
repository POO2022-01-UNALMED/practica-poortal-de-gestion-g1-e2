from tkinter import INSERT, Frame, Text, PhotoImage, Label
import os
import pathlib

'''# Esta clase extiende de Frame y se encarga de mostrar 
# las hoja de vida de los integrantes
# 
# @author Mateo Alvarez Lebrum
# @author Alejandro Alvarez Botero
# @author Miguel Angel Barrera Bustamante
# @author Alejandra Barrientos Grisales'''

class P2(Frame):
    """Corresponde al frame de la derecha"""
    # Posiciones de las imágenes
    posiciones = [(0, 0), (0, 1), (1, 0), (1, 1)]

    def __init__(self, window):
        super().__init__(window)
        # Crea el frame de arriba y contiene la hoja de vida de cada desarrollador
        self.p5 = Frame(self)
        # Crea el frame de abajo y contiene las 4 imagenes elegidas por los desarrolladores
        self.p6 = Frame(self)
        
        self.indice = 0
        self.text = None
        self.fotos = []
        # Se crean los espacios para las 4 imagenes
        self.labels = []
        self.cargarHojaVida(0)
        for i in range(0, 4):
            label = Label(self.p6, width = 300, height = 200)
            (r, c) = P2.posiciones[i]
            label.grid(row = r, column = c)
            self.labels.append(label)
            # Se cargan las primeras imagenes
            self.cargarImagenes(0, i)
        self.p5.grid()
        self.p6.grid()

    '''Este metodo se encarga de cargar el texto de la hoja de vida del autor
    @param indice de la hoja de vida'''
    def cargarHojaVida(self, numero: int):
        """Carga hoja de vida de cada desarrollador dependiendo del indice recibido"""
        self.text = Text(self.p5, height = 10)
        self.text.grid(row = 1, column = 0)
        self.text.bind("<Button-1>", self.proximo)

        path = os.path.join(pathlib.Path(__file__).parent.absolute(),"hv\hojaVida_{}.txt".format(numero))

        with open(path, "r+") as hvText:
            self.text.insert(INSERT, hvText.read())

    '''Este metodo se encarga de cargar las imagenes del autor y la hoja de vida'''
    def proximo(self, _):
        """Itera sobre las hojas de vida y las imagenes escogidas por cada desarrollador"""
        self.indice %= 4

        self.fotos = [None, None, None, None]
        self.cargarHojaVida(self.indice)
        for i in range(0, 4):
            self.cargarImagenes(self.indice, i)

        self.indice += 1

    '''Este metodo se encargar de cargar una imagen de la hoja de vida
    @param indice de la hoja de vida'''
    def cargarImagenes(self, hv_numero, numero):
        """Carga las imagenes en las localizaciones requeridas"""
        path = os.path.join(pathlib.Path(__file__).parent.absolute(),'imagenes/hv{}/{}.png'.format(hv_numero, numero))
        photo = PhotoImage(file=path)
        self.labels[numero].configure(image=photo)
        self.labels[numero].image = photo

    