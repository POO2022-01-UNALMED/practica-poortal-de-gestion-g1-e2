import imp
from tkinter import Frame, Tk, Menu, Toplevel, Label, Text, INSERT, scrolledtext, BOTH
import os
import pathlib
from datetime import datetime
from gestorAplicacion.general.Inventario import Inventario

from gestorAplicacion.ventas.Servicio import Servicio
from gestorAplicacion.personas.Contrato import Contrato
from gestorAplicacion.personas.Cliente import Cliente
from gestorAplicacion.personas.TipoDocumento import TipoDocumento
from gestorAplicacion.personas.Sexo import Sexo
from gestorAplicacion.general.DiaSemana import DiaSemana
from gestorAplicacion.ventas.Categoria import Categoria
from gestorAplicacion.personas.Persona import Persona
from gestorAplicacion.personas.Empleado import Empleado
from gestorAplicacion.ventas.Producto import Producto

from baseDatos.deserializador import Deserializador
from baseDatos.serializador import Serializador
from uiMain.ventanaPrincipal.pagar import Pagar
from uiMain.ventanaPrincipal.elegirEmpleado import ElegirEmpleado
from uiMain.ventanaPrincipal.devolverProducto.devolverProducto import DevolverProducto
from uiMain.ventanaPrincipal.gestionarCarrito.verCarrito import VerCarrito
from uiMain.ventanaPrincipal.gestionarCarrito.agregarProducto import AgregarProducto
from uiMain.ventanaPrincipal.gestionarCarrito.agregarServicio import AgregarServicio
from uiMain.ventanaPrincipal.gestionarCarrito.eliminarProducto import EliminarProducto
from uiMain.ventanaPrincipal.gestionarCarrito.eliminarServicio import EliminarServicio
from uiMain.ventanaPrincipal.gestionarEmpleados.contratar import ContratarPersona
from uiMain.ventanaPrincipal.gestionarEmpleados.visualizarEmpleados import VisualizarEmpleado
from uiMain.ventanaPrincipal.gestionarEmpleados.despedir import DespedirEmpleado

class Principal(Tk):
    def __init__(self):
        super().__init__()
        #self.crearObjetos()
        Deserializador.deserializarTodo()
        self.title("POOrtal de Gestión")
        self.option_add("*tearOff", False)
        self.minsize(1024, 640)

        # Se crea la barra de menu principal
        self.barraMenu = Menu(self)
        self.config(menu = self.barraMenu)

        # Se crean los submenus
        archivo = Menu(self.barraMenu)
        procesos = Menu(self.barraMenu)
        ayuda = Menu(self.barraMenu)

        # Se añaden los tres submenus al menu principal
        self.barraMenu.add_cascade(label = "Archivo", menu = archivo )
        self.barraMenu.add_cascade(label = "Procesos y Consultas", menu = procesos)
        self.barraMenu.add_cascade(label = "Ayuda", menu = ayuda)

        # Menu Archivo        
        archivo.add_command(label = "Aplicación", command = lambda: self.menuAplicion())
        archivo.add_command(label = "Guardar y salir", command = lambda: self.menuSalir())

        # Menu Ayuda        
        ayuda.add_command(label = "Acerca de", command = lambda: self.menuAyuda())

        # Submenu Gestionar Empleados 
        subMenuEmpleados = Menu(procesos)
        subMenuEmpleados.add_command(label = "Contratar persona", command = lambda: self.cambiarFrame(1))
        subMenuEmpleados.add_command(label = "Despedir persona", command = lambda: self.cambiarFrame(2))
        subMenuEmpleados.add_command(label = "Visualizar empleados", command = lambda: self.cambiarFrame(3))
        procesos.add_cascade(label = "Gestionar empleados", menu = subMenuEmpleados)

        # Submenu Gestionar Carrito 
        subMenuCarrito = Menu(procesos)
        subMenuCarrito.add_command(label = "Ver mi Carrito", command = lambda: self.cambiarFrame(4))
        subMenuCarrito.add_command(label = "Agregar producto al carrito", command = lambda: self.cambiarFrame(5))
        subMenuCarrito.add_command(label = "Agregar servicio al carrito", command = lambda: self.cambiarFrame(6))
        subMenuCarrito.add_command(label = "Eliminar producto del carrito", command = lambda: self.cambiarFrame(7))
        subMenuCarrito.add_command(label = "Eliminar servicio del carrito", command = lambda: self.cambiarFrame(8))
        procesos.add_cascade(label = "Gestionar carrito", menu = subMenuCarrito)

        procesos.add_command(label = "Devolver producto", command = lambda: self.cambiarFrame(9))

        procesos.add_command(label = "Asignar empleado a servicio", command = lambda: self.cambiarFrame(10))
        procesos.add_command(label = "Pagar", command = lambda: self.cambiarFrame(11))


        
        self.ventanaActual = Frame(self)
        text = scrolledtext.ScrolledText(self.ventanaActual)
        path = os.path.join(pathlib.Path(__file__).parent.absolute(),"instrucciones.txt")
        with open(path, "r+") as instrucciones:
            text.insert(INSERT, instrucciones.read())
        text.tag_configure('center', justify='center')
        self.ventanaActual.pack()
        text.pack()
        

    def cambiarFrame(self, num):
        self.ventanaActual.destroy()
        # Crear los frames
        ventanas = {
            # Gestionar Empleados
            1: ContratarPersona,
            2: DespedirEmpleado,
            3: VisualizarEmpleado,

            # Gestionar Carrito
            4: VerCarrito,
            5: AgregarProducto,
            6: AgregarServicio,
            7: EliminarProducto,
            8: EliminarServicio,

            9: DevolverProducto,
            
            10: ElegirEmpleado,
            
            11: Pagar
        }

        self.ventanaActual = ventanas.get(num)(self)
        self.ventanaActual.pack()


    def menuAplicion(self):
        top = Toplevel(self)
        top.geometry("580x320")
        top.resizable(False,False)
        top.title("Aplicación")

        texto = "Se necesita un sistema de gestión de facturación y de administración de contratos de empleados para poder realizar con éxito sus actividades que involucran a sus clientes, empleados, productos y servicios prestados. Para lograr esta gestión se creó el sistema “POOrtal de Gestión”, una solución orientada a objetos que incluye a todos los involucrados en tal gestión. Con POOrtal de Gestión los empleados podrán cumplir sus labores, los clientes podrán adquirir sus productos y servicios, se generarán facturas, entre otras. A continuación se muestra el diagrama de clases de la solución planteada."

        Label(top, text = texto , font = ('Times 12'), wraplength = 500).pack(fill = BOTH, expand=True)
        
    def menuSalir(self):
        # Se hace para evitar un import circular
        from uiMain.ventanaInicio.ventanaInicio import VentanaInicio
        Serializador.serializarTodo()
        self.destroy()
        ventana = VentanaInicio()
        ventana.mainloop()

    def menuAyuda(self):
        top = Toplevel(self)
        top.geometry("580x320")
        top.resizable(False,False)
        top.title("Ayuda")

        texto = "Autores:\nAlejandra Barrientos Grisales\nAlejandro Álvarez Botero\nMateo Álvarez Lebrum\nMiguel Ángel Barrera Bustamante"

        Label(top, text = texto , font = ('Times 18 bold'), wraplength = 500).pack(fill = BOTH, expand=True)


    def crearObjetos(self):
        # Creacion de servicios
        s1 = Servicio("Chef personal", 40000)
        s2 = Servicio("Fontanero", 25000)
        s3 = Servicio("Estilista", 30000)
        s4 = Servicio("Recepcionista", 30000)
        s5 = Servicio("Tendero", 30000)
        s6 = Servicio("Profesor", 37000)
        s7 = Servicio("Entrenador personal", 40000)
        
		# Creacion de contratos
        con1 = Contrato(1200000, datetime(2022, 5, 1), datetime(2025, 4, 5))
        con2 = Contrato(1300000, datetime(2022, 4, 21), datetime(2025, 2, 13))
        con3 = Contrato(3300000, datetime(2020, 5, 23), datetime(2024, 3, 11))
        con4 = Contrato(4200000, datetime(2022, 3, 15), datetime(2023, 1, 15))
        con5 = Contrato(6000000, datetime(2021, 11, 8), datetime(2026, 11, 20))

		# Creacion de clientes
        c1 = Cliente("Mateo", "3120201010", "mateo@unal.edu.co", "1234", TipoDocumento.CC, Sexo.MASCULINO)
        c2 = Cliente("Alejandro", "3120201010", "alejandro@unal.edu.co", "5678", TipoDocumento.CC, Sexo.MASCULINO)
        c3 = Cliente("Alejandra", "3120201010", "alejandra@unal.edu.co", "91011", TipoDocumento.TI, Sexo.FEMENINO)
        c4 = Cliente("Miguel", "3120201010", "miguel@unal.edu.co", "121314", TipoDocumento.CC, Sexo.MASCULINO)

		# Creacion de dias de dias laboral
        dias1 = []
        dias1.append(DiaSemana.LUNES);
        dias1.append(DiaSemana.MIERCOLES);
        dias1.append(DiaSemana.VIERNES);
        dias2 = [];
        dias2.append(DiaSemana.LUNES);
        dias2.append(DiaSemana.MARTES);
        dias2.append(DiaSemana.MIERCOLES);
        dias2.append(DiaSemana.JUEVES);
        dias2.append(DiaSemana.VIERNES);
        dias3 = [];
        dias3.append(DiaSemana.SABADO);
        dias3.append(DiaSemana.DOMINGO);

        p1 = Persona("Carlos", "32195959", "carlos@email.com", "AY14321541", TipoDocumento.PAP, Sexo.MASCULINO);
        p2 = Persona("Carolina", "314125125", "caro@email.com", "7854125", TipoDocumento.CC, Sexo.FEMENINO);
        p3 = Persona("Jose", "3141235112", "jose@email.com", "132541231", TipoDocumento.NIP, Sexo.MASCULINO);
        p4 = Persona("Valentina", "3124125412", "valen@email.com", "3542351232", TipoDocumento.CC, Sexo.FEMENINO);
        p5 = Persona("Natalia", "31241235124", "natalia@email.com", "56346326", TipoDocumento.TI, Sexo.FEMENINO);

        e1 = Empleado("Juan", "3121212111", "juan@email.com", "41412562", TipoDocumento.CC, Sexo.MASCULINO, con1, "Supervisor", s1, dias1);
        e2 = Empleado("Pepita", "3121937467", "pepita@email.com", "71384549", TipoDocumento.NIP, Sexo.FEMENINO, con2, "Supervisor", s3, dias2);
        e3 = Empleado("Nicolas", "312851745", "nico@email.com", "248520840", TipoDocumento.CC, Sexo.MASCULINO, con3, "Administrador", s2, dias2);
        e4 = Empleado("Daniela", "301651852", "daniela@email.com", "152487215", TipoDocumento.CE, Sexo.FEMENINO, con4, "Atencion al cliente", s5, dias2);
        e5 = Empleado("Samuel", "310165152", "samuel@email.com", "2148965213", TipoDocumento.CE, Sexo.MASCULINO, con5, "Atencion al cliente", s6, dias2);

        prod1 = Producto("PC", 10, Categoria.TECNOLOGIA, 3000000, 24);
        prod2 = Producto("Audifonos", 30, Categoria.TECNOLOGIA, 100000, 12);
        prod3 = Producto("Teclado", 16, Categoria.TECNOLOGIA, 140000, 9);
        prod4 = Producto("Collar", 70, Categoria.MASCOTA, 20000, 6);
        prod5 = Producto("Pelota", 60, Categoria.MASCOTA, 10000, 3);
        prod6 = Producto("Vitamina B6", 110, Categoria.SALUD, 12000, 2);
        prod7 = Producto("Aspirina", 320, Categoria.SALUD, 1500, 1);

        c1.agregarProductoALaCanasta(prod1, 7)
        c1.pagar()
        c3.solicitarServicio(s1)
