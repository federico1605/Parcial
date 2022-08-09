from Parcial.Backend.usuarios import AdminGlobal
from Parcial.Backend.Negocio import Negocio
from PyQt5 import uic, QtWidgets
from Parcial.Backend.conexion import Database
from Parcial.Backend.Producto import Producto
conexion = Database

class ControlerDelete:
    def __init__(self, Ui_MainWindow):
        self.borrar = Ui_MainWindow

    def deleteUsuario(self, deleU):
        AdminGlobal.eliminarUsuario(conexion.conectar(),deleU)

    def deleteProducto(self, deleP):
        Producto.eliminarProducto(conexion.conectar(), deleP)

    def deleteNegocio(self, deleN):
        Negocio.eliminarNegocio(conexion.conectar(), deleN)
