from tkinter import DISABLED, Entry, Frame, BOTH, Label, StringVar

class FieldFrame(Frame):
    # tituloC es el titulo del criterio
    # critero es una lista con todos los nombres de los criterios
    # tituoV es el titulo del valor
    # valores es una lista con todos los valores por defecto de los criterios 
    # noHabilitado es una lista con los nombres de los criterios que no son editables
    # tipos represente el tipo de dato, -1 si es String, 0 si es int y >0 si tiene un límite máximo
    def __init__(self, window, tituloC: str, criterio: list[str], tituloV: str, valores: list[str], noHabilitado: list[str], tipos: list[int]):
        super().__init__(window)
        self.tituloC = tituloC
        self.criterios = criterio
        self.tituloV = tituloV
        self.valores = valores
        self.noHabilitado = noHabilitado
        self.tipos = tipos
        self.entradas: list[Entry] = []
        self.valoresFinal = []
        self.pack(anchor = 'c')
        self.creacion()

    def creacion(self):
        Label(self, text = self.tituloC, font = ('Times 12 bold')).grid(padx = 80, column = 0, row = 0)
        Label(self, text = self.tituloV, font = ('Times 12 bold')).grid(padx = 80, column = 1, row = 0)

        for i in range(1, len(self.valores)+1):
            # Nombre del criterio
            Label(self, text = self.criterios[i-1], font = ('Times 12 bold')).grid(padx = 80, pady=2, column=0, row=i)
        
            texto = StringVar(value = self.valores[i-1])
            # Si no se puede modificar
            if self.criterios[i-1] in self.noHabilitado:
                entrada = Entry(self, width = 40, textvariable = texto, state = DISABLED, justify = "center")
            else:
                entrada = Entry(self, width = 40, textvariable = texto, justify = "center")
        
            entrada.grid(pady = 2, column = 1, row = i)
            self.entradas.append(entrada)
    
    def getValue(self, criterio: str):
        criteriosDict = dict(zip(self.criterios, self.valores))
        return criteriosDict[criterio].get()

    def verificarDato(self, valor, tipo, criterio):
        if len(valor) == 0:
            raise Exception("Por favor complete todos los campos")
        if tipo == -1:
            if str.isdigit(valor):
                raise Exception("El campo "+criterio+"no es string")
        if tipo >= 0:
            if not str.isdigit(valor):
                raise Exception("El campo "+criterio+"no es un digito")
            if tipo > 0 and int(valor) > tipo:
                raise Exception("Dato más alto de lo permitido")
            
        
        

    def obtenerDatos(self, evento):
        self.valoresFinal = []

        for i in range(len(self.criterios)):
            valor = self.entradas[i].get()
            self.verificarDato(valor, self.tipos[i], self.criterios[i])
            self.valoresFinal.append(i)