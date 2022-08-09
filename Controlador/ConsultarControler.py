from PyQt5 import QtWidgets
from Parcial.Backend.usuarios import AdminGlobal
from Parcial.Backend.Negocio import Negocio
from Parcial.Backend.Producto import Producto
from Parcial.Backend.conexion import Database
conexion = Database

class Consultar:
    def __init__(self, Ui_MainWindow):
        self.consulta = Ui_MainWindow

    def buscarUsuario(self):
        table = self.consulta.tableUsuario
        consulta = AdminGlobal.consultarUsuarios(conexion.conectar())
        table.setRowCount(0)
        if consulta:
            for row_number, row_data in enumerate(consulta):
                table.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    table.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

    def buscarNegocio(self):
        table = self.consulta.tableNegocio
        consulta = Negocio.comboBox(conexion.conectar())
        table.setRowCount(0)
        if consulta:
            for row_number, row_data in enumerate(consulta):
                table.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    table.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

    def buscarProducto(self):
        table = self.consulta.tableProducto
        consulta = Producto.comboBox(conexion.conectar())
        table.setRowCount(0)
        if consulta:
            for row_number, row_data in enumerate(consulta):
                table.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    table.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
