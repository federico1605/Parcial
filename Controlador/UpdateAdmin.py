from Parcial.Backend.usuarios import AdminGlobal
from Parcial.Backend.Producto import Producto
from Parcial.Backend.Negocio import Negocio
from Parcial.Backend.conexion import Database
conexion = Database

class ActualizarAdmin:
    def __init__(self, Ui_ActuAdminUser):
        self.update = Ui_ActuAdminUser

    def UpdateUContra(self, comboC, contrasenaU):
        AdminGlobal.actualizarUsuario(conexion.conectar(), contrasenaU, comboC)

    def UpdateTele(self, comboT, telefono):
        AdminGlobal.actualizarUsuarioTe(conexion.conectar(), telefono, comboT)

    def UpdateProP(self, nomProducto, idprodcuto):
        Producto.cambiarProducto(conexion.conectar(), idprodcuto, nomProducto)

    def updateProPre(self, precio, idproducto):
        Producto.cambiarProductoPre(conexion.conectar(), idproducto, precio)

    def updateNegocio(self, nombNegocio, iduser):
        Negocio.actulizarNegocio(conexion.conectar(), iduser, nombNegocio)
