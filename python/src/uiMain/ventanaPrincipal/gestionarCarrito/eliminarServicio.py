from tkinter import END, Button, Frame, BOTH, Label, Text, messagebox, ttk, DISABLED

from gestorAplicacion.general.Inventario import Inventario
from manejoErrores.errorAplicacion import ErrorAplicacion
from manejoErrores.textoVacio import TextVacio
from manejoErrores.clienteSinServicio import ClienteSinServicio

# Esta clase extiende de Frame y se encarga de mostrar la interfaz
# correspondiente a la funcionalidad eliminar servicio
# 
# @author Mateo Alvarez Lebrum
# @author Alejandro Alvarez Botero
# @author Miguel Angel Barrera Bustamante
# @author Alejandra Barrientos Grisales

class EliminarServicio(Frame):
    def __init__(self, window):
        super().__init__(window)
        self.grid_propagate(False)
        self.pack_propagate(False)
        self.pack(fill = BOTH, expand = True)

        # Se crea un frame que va a contener los datos a completar
        self.interfazDatos = Frame(self)
        self.interfazDatos.pack(fill = BOTH)

        # Se crea un frame que va a contener los resultados de la ejecucion
        self.interfazResultados = Frame(self)
        self.interfazResultados.pack(fill = BOTH)
        Label(self.interfazResultados, text = "Resultados", font = ('Times 12')).pack(anchor = "w")

        # Resultados de la Ejecucion
        self.textResultados = Text(self.interfazResultados, padx = 10, pady = 10)
        self.textResultados.pack(fill = BOTH)

        self.proceso()
        

    def proceso(self):
        try:   
            # Se crea un frame que va a contener la informacion de los clientes
            self.interfazCliente = Frame(self.interfazDatos)
            self.interfazCliente.grid(column = 0, row = 0)
            Label(self.interfazCliente, text = "Eliminar Servicio del carrito", font = ('Times 18 bold')).pack(pady = 5, anchor = 'c')
            Label(self.interfazCliente, text = "Por favor seleccione el cliente con el que quiere eliminar un servicio", font = ('Times 12')).pack(pady = 20, anchor = "w")

            # Se crea un frame que va a contener la informacion de los servicios
            self.interfazServicio = Frame(self.interfazDatos, padx = 50, pady = 10)
            self.interfazServicio.grid(column = 1, row = 0)

            # Se obtiene la informacion de los clientes y se proyecta en un combobox
            self.clientes = Inventario.getClientes()
            values = [i.getNombre() for i in self.clientes]
            self.clienteCombo = ttk.Combobox(self.interfazCliente, values = values, state = "readOnly")
            self.clienteCombo.pack(pady = 20, anchor = 'c')

            # Se crea un boton para poder continuar. Este va a ejecutar el metodo informacion()
            self.boton1 = Button(self.interfazCliente, text = "Continuar")
            self.boton1.pack(anchor = 'c')
            self.boton1.bind("<Button-1>", self.informacion)

        except ErrorAplicacion as e:
            messagebox.showinfo(title = "Error Aplicacion", message = str(e))
        
        except Exception as e:
            pass


    # Este metodo va a obtener la informacion de los servicios del cliente
    def informacion(self, evento):
        try:
            # Si no selecciono un cliente se genera un error
            if self.clienteCombo.get() == "":
                raise TextVacio("Por favor seleccione un cliente")

            # Con base en el nombre se obtiene el cliente
            for i in self.clientes:
                if i.getNombre() == self.clienteCombo.get():
                    self.cliente = i

            # Se obtienen los servicios en el carrito del cliente y se proyectan en un combobox. Adicional se desactiva la seccion para seleccionar el cliente
            self.servicios = self.cliente.getServicios()
            if not self.servicios:
                raise ClienteSinServicio("El cliente actual no tiene servicios en su carrito")
            values = [i.getNombre() for i in self.servicios]
            self.clienteCombo.config(state = DISABLED)
            self.boton1.destroy()
            self.servicioCombo = ttk.Combobox(self.interfazServicio, values = values)
            self.servicioCombo.pack(anchor = 'c')

            # Se crea un boton para poder eliminar el servicio. Ejecuya el metodo eliminar()
            boton = Button(self.interfazServicio, text = "Eliminar")
            boton.pack(anchor = 'c')
            boton.bind("<Button-1>", self.eliminar)

        except ErrorAplicacion as e:
            messagebox.showinfo(title = "Error Aplicacion", message = str(e))
        
        except Exception as e:
            pass
    
    # Este metodo se va a encargar de eliminar el servicio del carrito del cliente
    def eliminar(self, evento):
        try:
            # Si no selecciono un servicio genera un error
            if self.servicioCombo.get() == "":
                raise TextVacio("Por favor seleccione un Servicio")

            # Con base en el nombre, obtiene el servicio
            for i in self.servicios:
                if i.getNombre() == self.servicioCombo.get():
                    self.servicio = i

            # Eliminar el servicio del carrito del cliente
            self.cliente.eliminarServicioDeLaCanasta(self.servicio)

            # Elimina la informacion de los resultados y genera un nuevo comentario
            self.textResultados.delete("1.0", END)
            self.textResultados.insert("1.0", "El servicio ha sido eliminado con éxito")

            # Actualiza toda la informacion de los clientes y sus servicios
            self.interfazCliente.destroy()
            self.interfazServicio.destroy()
            self.proceso()
        
        except ErrorAplicacion as e:
            messagebox.showinfo(title = "Error Aplicacion", message = str(e))
        
        except Exception as e:
            pass