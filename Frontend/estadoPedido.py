from PyQt5 import QtCore, QtGui, QtWidgets
from Parcial.Controlador.pedidosE import ControladorPedido

class Ui_estadoPedido(object):
    def __init__(self):
        self.controlador = ControladorPedido(self)

    def setupUi(self, estadoPedido):
        estadoPedido.setObjectName("estadoPedido")
        estadoPedido.setFixedSize(645, 402)
        self.tableWidgetP = QtWidgets.QTableWidget(estadoPedido)
        self.tableWidgetP.setGeometry(QtCore.QRect(20, 70, 611, 251))
        self.tableWidgetP.setObjectName("tableWidgetP")
        self.tableWidgetP.setColumnCount(6)
        self.tableWidgetP.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetP.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetP.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetP.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetP.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetP.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetP.setHorizontalHeaderItem(5, item)
        self.label = QtWidgets.QLabel(estadoPedido)
        self.label.setGeometry(QtCore.QRect(240, 10, 161, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(estadoPedido)
        self.pushButton.setGeometry(QtCore.QRect(20, 340, 611, 23))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(estadoPedido)
        QtCore.QMetaObject.connectSlotsByName(estadoPedido)

        # ---------------------------------------------------EVENTOS-------------------------------------------
        self.pushButton.clicked.connect(self.accionVisualizar)

    def accionVisualizar(self):
        self.controlador.listadoPedido()

    def retranslateUi(self, estadoPedido):
        _translate = QtCore.QCoreApplication.translate
        estadoPedido.setWindowTitle(_translate("estadoPedido", "Estado Pedidos"))
        item = self.tableWidgetP.horizontalHeaderItem(0)
        item.setText(_translate("estadoPedido", "Id Pedido"))
        item = self.tableWidgetP.horizontalHeaderItem(1)
        item.setText(_translate("estadoPedido", "Id Mesero"))
        item = self.tableWidgetP.horizontalHeaderItem(2)
        item.setText(_translate("estadoPedido", "Mesa"))
        item = self.tableWidgetP.horizontalHeaderItem(3)
        item.setText(_translate("estadoPedido", "Estado Pedido"))
        item = self.tableWidgetP.horizontalHeaderItem(4)
        item.setText(_translate("estadoPedido", "Valor"))
        item = self.tableWidgetP.horizontalHeaderItem(5)
        item.setText(_translate("estadoPedido", "Cantidad"))
        self.label.setText(_translate("estadoPedido", "Estado Pedido."))
        self.pushButton.setText(_translate("estadoPedido", "Visualizar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    estadoPedido = QtWidgets.QWidget()
    ui = Ui_estadoPedido()
    ui.setupUi(estadoPedido)
    estadoPedido.show()
    sys.exit(app.exec_())
