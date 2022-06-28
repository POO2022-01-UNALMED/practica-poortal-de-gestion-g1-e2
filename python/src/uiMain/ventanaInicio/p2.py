from tkinter import INSERT, Frame, Text, PhotoImage, Label
import os
import pathlib

class P2(Frame):
    # Posiciones de las imágenes
    posiciones = [(0, 0), (0, 1), (1, 0), (1, 1)]

    def __init__(self, window):
        super().__init__(window)
        self.p5 = Frame(self)
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

    def cargarHojaVida(self, numero: int):
        self.text = Text(self.p5, height = 10)
        self.text.grid(row = 1, column = 0)
        self.text.bind("<Button-1>", self.proximo)

        path = os.path.join(pathlib.Path(__file__).parent.absolute(),"hv\hojaVida_{}.txt".format(numero))

        with open(path, "r+") as hvText:
            self.text.insert(INSERT, hvText.read())

    def proximo(self, _):
        self.indice %= 4

        self.fotos = [None, None, None, None]
        self.cargarHojaVida(self.indice)
        for i in range(0, 4):
            self.cargarImagenes(self.indice, i)

        self.indice += 1

    def cargarImagenes(self, hv_numero, numero):
        path = os.path.join(pathlib.Path(__file__).parent.absolute(),'imagenes/hv{}/{}.png'.format(hv_numero, numero))
        photo = PhotoImage(file=path)
        self.labels[numero].configure(image=photo)
        self.labels[numero].image = photo

    