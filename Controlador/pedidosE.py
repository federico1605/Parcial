import sys
import os
myDir = os.getcwd()
sys.path.append(myDir)

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from Parcial.Backend.Pedido import Pedido
from Parcial.Backend.conexion import Database
conexion = Database

class ControladorPedido:
    def __init__(self, Ui_estadoPedido):
        self.pedidos = Pedido.consultarPedido(conexion.conectar())
        self.principal = Ui_estadoPedido

    def listadoPedido(self):
        table = self.principal.tableWidgetP
        pedidos = self.pedidos
        for fila_numero, fila_data in enumerate(pedidos):
            table.insertRow(fila_numero)
            for column_number, data in enumerate(fila_data):
                table.setItem(fila_numero, column_number, QtWidgets.QTableWidgetItem(str(data)))