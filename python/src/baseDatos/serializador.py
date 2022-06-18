import pickle
import os
import pathlib

from gestorAplicacion.general.Inventario import Inventario

# Clase para serializar los objetos que se crean
# @author Alejandro Alvarez
# @author Alejandra Barrientos
# @author Mateo Alvarez
# @author Miguel Barrera

class Serializador:    
    def serializar(lista, className):
        def camino(className):
            string = os.path.join(pathlib.Path(__file__).parent.absolute(), "temp\\"+className+".txt")
            return string
        try:
            # Se crea el archivo pickle para guardar los objetos
            picklefile = open(camino(className), 'wb')
            # Pickle el objeto en el archivo
            pickle.dump(lista, picklefile)
            # Se cierra el archivo para guardar
            picklefile.close()
            
        except:
            print("No hay objetos en memoria")

    def serializarTodo():
        Serializador.serializar(Inventario.personas, "Personas")
        Serializador.serializar(Inventario.facturas, "Facturas")
        Serializador.serializar(Inventario.productos, "Productos")
        Serializador.serializar(Inventario.servicios, "Servicios")