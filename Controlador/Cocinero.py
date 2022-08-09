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
    def __init__(self, Ui_cocinero, Ui_windowaceptar):
        self.pedidos = Pedido
        self.principal = Ui_cocinero
        self.principalN = Ui_windowaceptar

    def listadoPedido(self):
        table = self.principal.tableWidgetPedidos
        pedidos = self.pedidos.consultarPedidoCo(conexion.conectar())
        for fila_numero, fila_data in enumerate(pedidos):
            table.insertRow(fila_numero)
            for column_number, data in enumerate(fila_data):
                table.setItem(fila_numero, column_number, QtWidgets.QTableWidgetItem(str(data)))

    def showId(self):
        table = self.principal.tableWidgetPedidos
        idP = table.currentItem().text()
        return idP

    def rechazoPedido(self):
        idP = ControladorPedido.showId(self)
        estado = "Rechazado"
        Pedido.actualizarPedido(conexion.conectar(), idP, estado)

    def aceptarPedido(self):
        idP = ControladorPedido.showId(self)
        estado = "Aceptado"
        Pedido.actualizarPedido(conexion.conectar(), idP, estado)

        # GENERAR Mensaje PEDIDO COCINERO
        if idP is not None:
            pedido = self.pedidos.consultarPedidoN(conexion.conectar(), idP)
            if pedido:
                msg = QMessageBox()
                msg.setWindowTitle(pedido[2])
                msg.setText(pedido[2])

                msg.setStandardButtons(QMessageBox.Ok)
                msg.setDefaultButton(QMessageBox.Ok)
                msg.setInformativeText('Id Pedido: '+str(pedido[0])+ '\nMesa: '+str(pedido[1])+ '\nEstado del pedido: '+str(pedido[2])+ '\nCantidad: '+str(pedido[3])+ '\nNombre Producto: '+str(pedido[4]))
                x = msg.exec_()

    def notificarPedido(self, combo):
        estado = "Listo"
        Pedido.actualizarPedido(conexion.conectar(), combo, estado)
