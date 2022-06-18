import pickle
import os
import pathlib

from gestorAplicacion.general.Inventario import Inventario

# Clase para deserializar los objetos que se crean
# @author Alejandro Alvarez
# @author Alejandra Barrientos
# @author Mateo Alvarez
# @author Miguel Barrera

class Deserializador:
    def deserializar(lista, className):
        def camino(className):
            string = os.path.join(pathlib.Path(__file__).parent.absolute(), "temp\\"+className+".txt")
            return string
        # Se lee el archivo
        try:
            picklefile = open(camino(className), 'rb')
        except:
            picklefile = open(camino(className), 'x')
            picklefile = open(camino(className), 'rb')
        # unpickle los datos
        if os.path.getsize(camino(className)) > 0:
            lista = pickle.load(picklefile)
        
        # Se cierra el archivo
        picklefile.close()
        return lista
    
    def deserializarTodo():
        Inventario.personas = Deserializador.deserializar(Inventario.personas, "Personas")
        Inventario.facturas = Deserializador.deserializar(Inventario.facturas, "Facturas")
        Inventario.productos = Deserializador.deserializar(Inventario.productos, "Productos")
        Inventario.servicios = Deserializador.deserializar(Inventario.servicios, "Servicios")
        