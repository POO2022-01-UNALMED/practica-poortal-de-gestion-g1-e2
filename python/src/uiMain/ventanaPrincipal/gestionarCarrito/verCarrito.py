from tkinter import Frame

class VerCarrito(Frame):
    def __init__(self, window):
        super().__init__(window, width = 680, height = 420)
        self.config(bg = "red")