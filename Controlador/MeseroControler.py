from PyQt5 import QtWidgets
from Parcial.Backend.usuarios import Mesero
from Parcial.Backend.Negocio import Negocio
from Parcial.Backend.Pedido import Pedido
from Parcial.Backend.factura import Factura
from Parcial.Backend.conexion import Database
conexion = Database

class MeseroController:
    def __init__(self, Ui_CrearMesero, Ui_Form, Ui_FacrturaMesero, Ui_FormF):
        self.crear = Ui_CrearMesero
        self.eliminar = Ui_Form
        self.factura = Ui_FacrturaMesero
        self.crearFacturaM = Ui_FormF
        self.listPedidos = Pedido.consultarFacturar(conexion.conectar())

    def crearPedido(self, comboIdM, mesa, comboPro, cantidad):
        estado = "En espera"
        valor = 0
        x = Negocio.consultaNegocio(conexion.conectar(), comboPro)
        Mesero.crearPedido(conexion.conectar(), comboIdM, mesa, estado, valor, cantidad, x, comboPro)

    def eliminarPedido(self, combo):
        Mesero.eliminarPedido(conexion.conectar(), combo)

    def generarFactura(self):
        table = self.factura.tableWidget
        pedido = self.listPedidos
        table.setRowCount(0)
        if pedido:
            for row_number, row_data in enumerate(pedido):
                table.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    table.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

    def crearFactura(self, combo, comboP, mesa, cantidad):
        x = Negocio.consultarN(conexion.conectar(), comboP)
        y = Pedido.valorTotal(conexion.conectar(), comboP)
        z = y*cantidad
        Factura.generarFactura(conexion.conectar(), combo, x, mesa, comboP, z, cantidad)
