import sys
import os
myDir = os.getcwd()
sys.path.append(myDir)

from Parcial.Backend.usuarios import AdminGlobal
from Parcial.Backend.conexion import Database
from Parcial.Backend.Negocio import Negocio
from Parcial.Backend.Producto import Producto
conexion = Database

class CrearAdmin:
    def __init__(self, Ui_crearAdmin):
        self.crear = Ui_crearAdmin

    def crearUsuario(self, nomUsuario, conUsuario, telUsuario, rolUsuario, idNegocio):
        AdminGlobal.crearUsuario(conexion.conectar(), nomUsuario, telUsuario, conUsuario, idNegocio, rolUsuario)
        print(nomUsuario, telUsuario, rolUsuario, idNegocio)

    def crearNegocio(self, nomNegocio):
        Negocio.anadirNegocio(conexion.conectar(), nomNegocio)
        print(nomNegocio)

    def crearProducto(self, nomProducto, valorP, comboP):
        Producto.anadirProducto(conexion.conectar(),nomProducto, valorP, comboP)
