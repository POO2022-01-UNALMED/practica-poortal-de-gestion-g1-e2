from tkinter import DISABLED, END, Button, Frame, BOTH, messagebox, Label, ttk, Text


from gestorAplicacion.general.Inventario import Inventario
from manejoErrores.textoVacio import TextVacio
from uiMain.ventanaPrincipal.fieldFrame import FieldFrame

from manejoErrores.errorAplicacion import ErrorAplicacion

# Esta clase extiende de Frame y se encarga de mostrar la interfaz
# correspondiente a la funcionalidad agregar producto
# 
# @author Mateo Alvarez Lebrum
# @author Alejandro Alvarez Botero
# @author Miguel Angel Barrera Bustamante
# @author Alejandra Barrientos Grisales

class AgregarProducto(Frame):
    def __init__(self, window):
        super().__init__(window)
        self.grid_propagate(False)
        self.pack_propagate(False)
        self.pack(fill = BOTH, expand = True)

        #Se crea un frame donde van a aparecer todos los campos necesarios que el usuario debe seleccionar y completar
        self.interfazDatos = Frame(self)
        self.interfazDatos.pack(fill = BOTH)

        # Se crea un frame que va a almacenenar los resultados de la ejecución
        self.interfazResultados = Frame(self)
        self.interfazResultados.pack(fill = BOTH)
        Label(self.interfazResultados, text = "Resultados", font = ('Times 12')).pack(anchor = "w")

        # Resultados de la Ejecucion
        self.textResultados = Text(self.interfazResultados, padx = 10, pady = 10)
        self.textResultados.pack(fill = BOTH)

        self.proceso()

    # Metodo que se va a encargar de poner la informacion respecto a los clientes y los productos disponibles
    def proceso(self):
        try:
            # Se crea un frame en el que el usuario puede seleccionar un cliente
            self.interfazCliente = Frame(self.interfazDatos)
            self.interfazCliente.grid(column = 0, row = 0)

            Label(self.interfazCliente, text = "Agregar Producto al Carrito", font = ('Times 18 bold')).pack(pady = 5, anchor = 'c')
            Label(self.interfazCliente, text = "Por favor seleccione el cliente con el que quiere agregar un producto", font = ('Times 12')).pack(pady = 20, anchor = "w")

            # Se crea un frame en el que el usuario puede ingresar la informacion para agregar el prodcuto
            self.interfazProducto = Frame(self.interfazDatos)
            self.interfazProducto.grid(column = 1, row = 0)

            # Se obtiene la informacion de los clientes disponibles y se proyecta en un combobox
            self.clientes = Inventario.getClientes()
            values = [i.getNombre() for i in self.clientes]
            self.clienteCombo = ttk.Combobox(self.interfazCliente, values = values, state = "readOnly")
            self.clienteCombo.pack(pady = 20, anchor = 'c')

            # Se obtiene la informacion de los productos disponibles y se proyecta en un combobox
            self.productos = Inventario.getProductosDisponibles()
            values = [i.getNombre() for i in self.productos]
            self.productoCombo = ttk.Combobox(self.interfazCliente, values = values, state = "readOnly")
            self.productoCombo.pack(pady = 20,anchor = 'c' )

            # Se crea un boton con el que usuario puede continuar, cuando presiona este boton 
            # se ejecuta el metodo informacion()
            self.boton1 = Button(self.interfazCliente, text = "Continuar")
            self.boton1.pack(anchor = 'c')
            self.boton1.bind("<Button-1>", self.informacion)

        except ErrorAplicacion as e:
            messagebox.showinfo(title = "Error Aplicacion", message = str(e))
        
        except Exception as e:
            pass
    

    # Metodo que se va a ejecutar cuando presionen el boton continuar
    # y se va a encargar de mostrar la informacion para que el usuario debe completar
    # para poder agregar el producto al carrito
    def informacion(self, evento):
        try:
            # Si no selecciono uno de los dos campos se genera un error
            if self.clienteCombo.get() == "" or self.productoCombo.get() == "":
                raise TextVacio("Por favor seleccione un cliente y un producto")

            # De acuerdo al nombre del cliente se busca el cliente en el inventraio
            for i in self.clientes:
                if i.getNombre() == self.clienteCombo.get():
                    self.cliente = i
            
            # De acuerdo al nobre del producto se busca el producto en el inventario
            self.producto = Inventario.buscarProducto(self.productoCombo.get())

            # Se desactivan los dos combobox y el boton para evitar errores en la posterioridad
            self.clienteCombo.config(state = DISABLED)
            self.productoCombo.config(state = DISABLED)
            self.boton1.destroy()

            # Se crea un fielframe con la informacion del producto, su nombre, la cantidad disponible y un campo el cual el usuario debe completar
            self.datos = FieldFrame(self.interfazProducto, self.producto.getNombre(), ["Cantidad Disponible", "Cantidad a elegir"], "", [self.producto.getCantidadDisponible(), None], ["Cantidad Disponible"], [0, self.producto.getCantidadDisponible()])

            # Se crea un boton con el que se puede agregar el producto. Al ser presionado
            # se ejecuta el metodo agregarProducto()
            boton = Button(self.interfazProducto, text = "Agregar")
            boton.pack(anchor = 'c')
            boton.bind("<Button-1>", self.agregarProducto)

        except ErrorAplicacion as e:
            messagebox.showinfo(title = "Error Aplicacion", message = str(e))

        except Exception as e:
            pass
    

    # Metodo que se encargar de ejecutar la funcionalidad de agregar producto
    def agregarProducto(self, evento):
        try:
            # Se obtienen los datos del fieldFrame
            elementos = self.datos.obtenerDatos()
            cantidadAgregar = elementos[1]
            
            # Se agrega el producto y la cantidad al carrito del cliente
            self.cliente.agregarProductoALaCanasta(self.producto, int(cantidadAgregar))
            
            # Se vacia el texto de los resultados y se agrega uno nuevo
            self.textResultados.delete("1.0", END)
            self.textResultados.insert("1.0", "El producto fue agregado con exito")

            # Se destruye el frame donde está toda la informacion y se vuelve a crear, de esta manera se actulizan todos los campos que han de actualizarse despues de cada proceso
            self.interfazCliente.destroy()
            self.interfazProducto.destroy()
            self.proceso()
            
        except ErrorAplicacion as e:
            messagebox.showinfo(title = "Error Aplicacion", message = str(e))

        except Exception as e:
            pass