from PyQt5 import QtWidgets
from Parcial.Backend.BackCierre import CierreTotal
from Parcial.Backend.conexion import Database
conexion = Database

class CierreController:
    def __init__(self, Ui_Form):
        self.cierre = Ui_Form
        self.tablas = CierreTotal

    def generarMesa(self):
        table = self.cierre.tableMesa
        mesa = self.tablas.cierreMesas(conexion.conectar())
        if mesa:
            for row_number, row_data in enumerate(mesa):
                table.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    table.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

    def generarMeseros(self):
        table = self.cierre.tableMesero
        mesero = self.tablas.cierreMeseros(conexion.conectar())
        if mesero:
            for row_number, row_data in enumerate(mesero):
                table.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    table.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

    def generarNegocios(self):
        table = self.cierre.tableNegocio
        negocio = self.tablas.cierreNegocios(conexion.conectar())
        if negocio:
            for row_number, row_data in enumerate(negocio):
                table.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    table.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

