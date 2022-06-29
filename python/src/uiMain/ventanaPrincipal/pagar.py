from tkinter import BOTH, END, Button, Frame, Label, ttk, messagebox, Text

from gestorAplicacion.general.Inventario import Inventario
from manejoErrores.errorAplicacion import ErrorAplicacion
from gestorAplicacion.personas.Cliente import Cliente
from gestorAplicacion.ventas.Factura import Factura

from manejoErrores.textoVacio import TextoVacio

# Esta clase extiende de Frame y se encarga de mostrar la interfaz
# correspondiente a la funcionalidad eliminar servicio
# 
# @author Mateo Alvarez Lebrum
# @author Alejandro Alvarez Botero
# @author Miguel Angel Barrera Bustamante
# @author Alejandra Barrientos Grisales

class Pagar(Frame):
    def __init__(self, window):
        super().__init__(window,width = 680, height = 420)
        self.grid_propagate(False)
        self.pack_propagate(False)
        self.pack(fill = BOTH, expand = True)
        self.proceso()
        

    def proceso(self):
        try:
            # Crea un frame principal para que el usuario seleccione los datos
            self.interfaz = Frame(self, width = 400)
            self.interfaz.pack(anchor = 'c')
            Label(self.interfaz, text = "Pagar", font = ('Times 18 bold')).pack(pady = 5, anchor = 'c')
            Label(self.interfaz, text = "Por favor seleccione el empleado con el que quiere realizar el pago", font = ('Times 12')).pack(pady = 20, anchor = "w")

            self.informacion()

            # Frame para poner resultados
            self.resultados = Frame(self, width = 400)
            self.resultados.pack(fill = BOTH,anchor = "c")
            Label(self.resultados, text = "Resultados", font = ('Times 12')).pack(anchor = "w")

            # Resultados de la Ejecucion
            self.textResultados = Text(self.resultados, padx = 10, pady = 10)
            self.textResultados.pack(fill = BOTH)

        except ErrorAplicacion as e:
            messagebox.showinfo(title = "Error Aplicacion", message = str(e))
        
        except Exception as e:
            pass

    
    def pagar(self, evento):
        try:
            # Si no selecciono un cliente se genera un error
            if self.combo.get() == "":
                raise TextoVacio("Por favor seleccione un cliente con el que desea realizar el pago")

            # De los clientes obtiene el cliente con el que pagar
            for i in self.clientes:
                if i.getNombre() == self.combo.get():
                    cliente = i

            # Se ejecuta el metodo pagar en cliente que retorna un objeto tipo factura
            factura: Factura = cliente.pagar()
            
            # Se borra la informacion en los resultados y se genera un nuevo comentario con la informacion de la factura generada
            self.textResultados.delete('1.0', END)
            self.textResultados.insert('1.0', "Se ha generado una factura a nombre de "+str(cliente.getNombre())+" con identificación "+str(cliente.getIdentificacion())+"\n")
            self.textResultados.insert(END, factura.mostrarInformacion())

            # Se actualiza la informacion con los clientes con los que se puede realizar el pago
            self.combo.destroy()
            self.boton.destroy()
            self.informacion()

        except ErrorAplicacion as e:
            messagebox.showinfo(title = "Error Aplicacion", message = str(e))
        
        except Exception as e:
            pass



    def informacion(self):
        try:
            # Crea un combobox con los clientes que tienen un carrito con algún elemento y se proyectan en un combobox
            self.clientes = Inventario.clientesConCarrito()
            values = [i.getNombre() for i in self.clientes]
            self.combo = ttk.Combobox(self.interfaz, values = values, state = "readonly")
            self.combo.pack(pady = 20, anchor = 'c')

            # Crea boton para poder realizar el pago. Ejecuta el metodo pagar
            self.boton = Button(self.interfaz, text = "Pagar")
            self.boton.pack(pady = 10, anchor = 'c')
            self.boton.bind("<Button-1>", self.pagar)

        except ErrorAplicacion as e:
            messagebox.showinfo(title = "Error Aplicacion", message = str(e))
        
        except Exception as e:
            pass