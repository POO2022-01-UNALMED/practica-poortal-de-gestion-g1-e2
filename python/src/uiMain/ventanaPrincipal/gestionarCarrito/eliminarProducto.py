from tkinter import DISABLED, END, Button, Frame, BOTH, Label, Text, messagebox, ttk

from gestorAplicacion.general.Inventario import Inventario
from manejoErrores.errorAplicacion import ErrorAplicacion
from manejoErrores.textoVacio import TextVacio

# Esta clase extiende de Frame y se encarga de mostrar la interfaz
# correspondiente a la funcionalidad eliminar prodcuto
# 
# @author Mateo Alvarez Lebrum
# @author Alejandro Alvarez Botero
# @author Miguel Angel Barrera Bustamante
# @author Alejandra Barrientos Grisales

class EliminarProducto(Frame):
    def __init__(self, window):
        super().__init__(window)
        self.grid_propagate(False)
        self.pack_propagate(False)
        self.pack(fill = BOTH, expand = True)

        # Se crea un frame superior con los datos a completar por el usuario
        self.interfazDatos = Frame(self)
        self.interfazDatos.pack(fill = BOTH)

        # Se crea un frame inferior que va a contener los resultados de la ejecucion
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
            Label(self.interfazCliente, text = "Eliminar Producto del carrito", font = ('Times 18 bold')).pack(pady = 5, anchor = 'c')
            Label(self.interfazCliente, text = "Por favor seleccione el cliente con el que quiere eliminar un producto", font = ('Times 12')).pack(pady = 20, anchor = "w")

            # Se crea un frame que va a contener la informacion del producto a eliminar
            self.interfazProducto = Frame(self.interfazDatos, padx = 50, pady = 10)
            self.interfazProducto.grid(column = 1, row = 0)

            # Se obtienen los clientes y se proyectan en un combobox
            self.clientes = Inventario.getClientes()
            values = [i.getNombre() for i in self.clientes]
            self.clienteCombo = ttk.Combobox(self.interfazCliente, values = values, state = "readOnly")
            self.clienteCombo.pack(pady = 20, anchor = 'c')

            # Se crea un botón de continuar que ejectua el metodo informacion()
            self.boton1 = Button(self.interfazCliente, text = "Continuar")
            self.boton1.pack(anchor = 'c')
            self.boton1.bind("<Button-1>", self.informacion)

        except ErrorAplicacion as e:
            messagebox.showinfo(title = "Error Aplicacion", message = str(e))
        
        except Exception as e:
            pass
    

    # Este metodo se encarga de mostrar los productos asociados al cliente
    def informacion(self, evento):
        try:
            # En caso de no seleccionar cliente se genera un error
            if self.clienteCombo.get() == "":
                raise TextVacio("Por favor seleccione un cliente")

            # Con base en el nombre se obtiene el cliente
            for i in self.clientes:
                if i.getNombre() == self.clienteCombo.get():
                    self.cliente = i

            # Se obtienen los productos en el carrito del cliente, se proyectan en un combobox y se deshabilita la seleccion del cliente
            self.productos = self.cliente.getProductos()
            values = [i.getNombre() for i in self.productos]
            self.clienteCombo.config(state = DISABLED)
            self.boton1.destroy()
            self.productoCombo = ttk.Combobox(self.interfazProducto, values = values)
            self.productoCombo.pack(anchor = 'c')
            
            # Se crea un boton para eliminar el producto, que va a ejecutar el metodo eliminar()
            boton = Button(self.interfazProducto, text = "Eliminar")
            boton.pack(anchor = 'c')
            boton.bind("<Button-1>", self.eliminar)

        except ErrorAplicacion as e:
            messagebox.showinfo(title = "Error Aplicacion", message = str(e))
        
        except Exception as e:
            pass
    

    # Este metodo se encarga de eliminar el producto del carrito del cliente
    def eliminar(self, evento):
        try:
            # Si no selecciono un producto se genera un error
            if self.productoCombo.get() == "":
                raise TextVacio("Por favor seleccione un Producto")

            # Con base en el nombre se obtiene el producto
            for i in self.productos:
                if i.getNombre() == self.productoCombo.get():
                    self.producto = i

            # Se elimina el producto del carrito del cliente
            self.cliente.eliminarProductoDeLaCanasta(self.producto)

            # Se limpia el texto del resultado y se genera un nuevo comentario
            self.textResultados.delete("1.0", END)
            self.textResultados.insert("1.0", "El producto ha sido eliminado con éxito")

            # Se actualiza toda la informacion del cliente y, por tanto, sus podructos para que el usuario lo pueda seleccionar
            self.interfazCliente.destroy()
            self.interfazProducto.destroy()
            self.proceso()

        except ErrorAplicacion as e:
            messagebox.showinfo(title = "Error Aplicacion", message = str(e))
        
        except Exception as e:
            pass