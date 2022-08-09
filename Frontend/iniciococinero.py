from PyQt5 import QtCore, QtGui, QtWidgets
from Parcial.Controlador.Cocinero import ControladorPedido
from Parcial.Frontend.mensajerechazo import Ui_mensajerechazo
from Parcial.Frontend.aceptarcocinero import Ui_windowaceptar

class Ui_cocinero(object):
    def __init__(self):
        self.controlador = ControladorPedido(self, self)
        self.rechazar = Ui_mensajerechazo
        self.aceptar = Ui_windowaceptar

    def setupUi(self, cocinero):
        self.main = cocinero
        cocinero.setObjectName("cocinero")
        cocinero.setFixedSize(555, 500)
        cocinero.setMinimumSize(QtCore.QSize(400, 500))
        cocinero.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(158, 158, 158, 255), stop:1 rgba(255, 255, 255, 255));")
        self.centralwidget = QtWidgets.QWidget(cocinero)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(230, 30, 121, 31))
        self.label.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.buttonaceptar = QtWidgets.QPushButton(self.centralwidget)
        self.buttonaceptar.setGeometry(QtCore.QRect(250, 300, 75, 23))
        self.buttonaceptar.setObjectName("buttonaceptar")
        self.buttonrechazar = QtWidgets.QPushButton(self.centralwidget)
        self.buttonrechazar.setGeometry(QtCore.QRect(160, 300, 75, 23))
        self.buttonrechazar.setObjectName("buttonrechazar")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 80, 121, 16))
        self.label_2.setObjectName("label_2")
        self.buttonvolver = QtWidgets.QPushButton(self.centralwidget)
        self.buttonvolver.setGeometry(QtCore.QRect(20, 450, 75, 23))
        self.buttonvolver.setObjectName("buttonvolver")
        self.tableWidgetPedidos = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidgetPedidos.setGeometry(QtCore.QRect(50, 100, 460, 192))
        self.tableWidgetPedidos.setObjectName("tableWidgetPedidos")
        self.tableWidgetPedidos.setColumnCount(6)
        self.tableWidgetPedidos.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetPedidos.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetPedidos.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetPedidos.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetPedidos.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetPedidos.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetPedidos.setHorizontalHeaderItem(5, item)
        self.buttonVer = QtWidgets.QPushButton(self.centralwidget)
        self.buttonVer.setGeometry(QtCore.QRect(340, 300, 75, 23))
        self.buttonVer.setObjectName("buttonVer")
        cocinero.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(cocinero)
        self.statusbar.setObjectName("statusbar")
        cocinero.setStatusBar(self.statusbar)

        self.retranslateUi(cocinero)
        QtCore.QMetaObject.connectSlotsByName(cocinero)

        # ---------------------------------------------------EVENTOS-------------------------------------------
        self.buttonVer.clicked.connect(self.accionVisualizar)
        self.buttonvolver.clicked.connect(self.accionVolver)
        self.buttonaceptar.clicked.connect(self.accionAceptar)
        self.buttonrechazar.clicked.connect(self.accionRechazar)

    def accionVisualizar(self):
        self.controlador.listadoPedido()

    def accionVolver(self):
        self.main.close()

    def accionAceptar(self):
        self.main.hide()
        self.controlador.aceptarPedido()

        self.aceptar.Ventana = QtWidgets.QMainWindow()
        self.aceptar.ui = Ui_windowaceptar()
        self.aceptar.ui.setupUi(self.aceptar.Ventana)
        self.aceptar.Ventana.show()

    def accionRechazar(self):
        self.controlador.rechazoPedido()
        self.rechazar.Ventana = QtWidgets.QMainWindow()
        self.rechazar.ui = Ui_mensajerechazo()
        self.rechazar.ui.setupUi(self.rechazar.Ventana)
        self.rechazar.Ventana.show()


    def retranslateUi(self, cocinero):
        _translate = QtCore.QCoreApplication.translate
        cocinero.setWindowTitle(_translate("cocinero", "MainWindow"))
        self.label.setText(_translate("cocinero", "<html><head/><body><p align=\"center\">COCINERO</p></body></html>"))
        self.buttonaceptar.setText(_translate("cocinero", "ACEPTAR"))
        self.buttonrechazar.setText(_translate("cocinero", "RECHAZAR"))
        self.label_2.setText(_translate("cocinero", "Informacion del pedido:"))
        self.buttonvolver.setText(_translate("cocinero", "volver"))
        item = self.tableWidgetPedidos.horizontalHeaderItem(0)
        item.setText(_translate("cocinero", "Id pedido"))
        item = self.tableWidgetPedidos.horizontalHeaderItem(1)
        item.setText(_translate("cocinero", "Mesa"))
        item = self.tableWidgetPedidos.horizontalHeaderItem(2)
        item.setText(_translate("cocinero", "Estado Pedido"))
        item = self.tableWidgetPedidos.horizontalHeaderItem(3)
        item.setText(_translate("cocinero", "Producto"))
        item = self.tableWidgetPedidos.horizontalHeaderItem(4)
        item.setText(_translate("cocinero", "Negocio"))
        item = self.tableWidgetPedidos.horizontalHeaderItem(5)
        item.setText(_translate("cocinero", "Cantidad"))
        self.buttonVer.setText(_translate("cocinero", "Ver Pedidos"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    cocinero = QtWidgets.QMainWindow()
    ui = Ui_cocinero()
    ui.setupUi(cocinero)
    cocinero.show()
    sys.exit(app.exec_())
