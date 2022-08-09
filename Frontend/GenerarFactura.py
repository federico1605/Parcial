from PyQt5 import QtCore, QtGui, QtWidgets
from Parcial.Controlador.MeseroControler import MeseroController
from Parcial.Frontend.CrearFacturaM import Ui_Form

class Ui_FacrturaMesero(object):
    def __init__(self):
        self.controler = MeseroController(self, self, self, self)
        self.crear = Ui_Form

    def setupUi(self, FacrturaMesero):
        self.main = FacrturaMesero
        FacrturaMesero.setObjectName("FacrturaMesero")
        FacrturaMesero.resize(742, 348)
        self.label = QtWidgets.QLabel(FacrturaMesero)
        self.label.setGeometry(QtCore.QRect(330, 10, 89, 25))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.tableWidget = QtWidgets.QTableWidget(FacrturaMesero)
        self.tableWidget.setGeometry(QtCore.QRect(10, 80, 721, 191))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)

        self.generarFactura()

        self.label_2 = QtWidgets.QLabel(FacrturaMesero)
        self.label_2.setGeometry(QtCore.QRect(270, 50, 224, 19))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.botonFacturar = QtWidgets.QPushButton(FacrturaMesero)
        self.botonFacturar.setGeometry(QtCore.QRect(10, 270, 721, 23))
        self.botonFacturar.setObjectName("botonFacturar")
        self.butonVolver = QtWidgets.QPushButton(FacrturaMesero)
        self.butonVolver.setGeometry(QtCore.QRect(624, 310, 111, 23))
        self.butonVolver.setObjectName("butonVolver")

        self.retranslateUi(FacrturaMesero)
        QtCore.QMetaObject.connectSlotsByName(FacrturaMesero)

        # --------------------------------------------------------EVENTOS---------------------------------------------
        self.butonVolver.clicked.connect(self.accionVolver)
        self.botonFacturar.clicked.connect(self.accionFacturar)

    def generarFactura(self):
        self.controler.generarFactura()

    def accionVolver(self):
        self.main.close()

    def accionFacturar(self):
        self.crear.Ventana = QtWidgets.QMainWindow()
        self.crear.ui = Ui_Form()
        self.crear.ui.setupUi(self.crear.Ventana)
        self.crear.Ventana.show()

    def retranslateUi(self, FacrturaMesero):
        _translate = QtCore.QCoreApplication.translate
        FacrturaMesero.setWindowTitle(_translate("FacrturaMesero", "Mesero"))
        self.label.setText(_translate("FacrturaMesero", "Facturar"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("FacrturaMesero", "Id Pedido"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("FacrturaMesero", "Mesero"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("FacrturaMesero", "Mesa"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("FacrturaMesero", "Estado Pedido"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("FacrturaMesero", "Producto"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("FacrturaMesero", "Negocio"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("FacrturaMesero", "Cantidad"))
        self.label_2.setText(_translate("FacrturaMesero", "Que Pedido desea Facturar."))
        self.botonFacturar.setText(_translate("FacrturaMesero", "Facturar"))
        self.butonVolver.setText(_translate("FacrturaMesero", "Volver"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FacrturaMesero = QtWidgets.QWidget()
    ui = Ui_FacrturaMesero()
    ui.setupUi(FacrturaMesero)
    FacrturaMesero.show()
    sys.exit(app.exec_())
