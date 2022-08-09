from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from Parcial.Backend.factura import Factura
from Parcial.Backend.conexion import Database
conexion = Database

class FacturaController:
    def __init__(self, FacturaVentana):
        self.modelFactura = Factura.listaFactura(conexion.conectar())
        self.factura = FacturaVentana
        
    def listaFactura(self):
        table = self.factura.tableFactura
        facturas = self.modelFactura
        table.setRowCount(0)
        if facturas:
            for row_number, row_data in enumerate(facturas):
                table.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    table.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))