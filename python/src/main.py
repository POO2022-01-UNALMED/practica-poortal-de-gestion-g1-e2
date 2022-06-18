#from baseDatos.deserializador import Deserializador
from uiMain.ventanaInicio.ventanaInicio import VentanaInicio

# Esta clase inicializa todo el programa

if __name__ == "__main__":
    #Deserializador.deserializarTodo()
    ventana = VentanaInicio()
    ventana.mainloop()