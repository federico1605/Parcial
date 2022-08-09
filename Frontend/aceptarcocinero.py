from PyQt5 import QtCore, QtGui, QtWidgets
from Parcial.Controlador.Cocinero import ControladorPedido
from Parcial.Backend.Pedido import Pedido
from Parcial.Backend.conexion import Database
conexion = Database

class Ui_windowaceptar(object):
    def __init__(self):
        self.controlador = ControladorPedido(self, self)

        # Listado de pedidos
        self.pedidos = Pedido.consultarPedido(conexion.conectar())

    def setupUi(self, windowaceptar):
        self.main = windowaceptar
        windowaceptar.setObjectName("windowaceptar")
        windowaceptar.resize(333, 252)
        windowaceptar.setMaximumSize(QtCore.QSize(400, 500))
        windowaceptar.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(158, 158, 158, 255), stop:1 rgba(255, 255, 255, 255));")
        self.centralwidget = QtWidgets.QWidget(windowaceptar)
        self.centralwidget.setObjectName("centralwidget")
        self.buttonnotificar = QtWidgets.QPushButton(self.centralwidget)
        self.buttonnotificar.setGeometry(QtCore.QRect(91, 96, 171, 23))
        self.buttonnotificar.setObjectName("buttonnotificar")
        self.volver = QtWidgets.QPushButton(self.centralwidget)
        self.volver.setGeometry(QtCore.QRect(30, 190, 75, 23))
        self.volver.setObjectName("volver")

        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(91, 72, 171, 18))
        self.comboBox.setObjectName("comboBox")

        # GENERAR COMBOBOX
        for pedido in self.pedidos:
            self.comboBox.addItem(str(pedido[0]))

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(91, 41, 168, 25))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        windowaceptar.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(windowaceptar)
        self.statusbar.setObjectName("statusbar")
        windowaceptar.setStatusBar(self.statusbar)

        self.retranslateUi(windowaceptar)
        QtCore.QMetaObject.connectSlotsByName(windowaceptar)

        # --------------------------------------EVENTOS--------------------------------------
        self.volver.clicked.connect(self.accionVolver)
        self.buttonnotificar.clicked.connect(self.accionNotificar)

    def accionVolver(self):
        self.main.close()

    def accionNotificar(self):
        combo = (self.comboBox.currentText())
        self.controlador.notificarPedido(combo)

    def retranslateUi(self, windowaceptar):
        _translate = QtCore.QCoreApplication.translate
        windowaceptar.setWindowTitle(_translate("windowaceptar", "MainWindow"))
        self.buttonnotificar.setText(_translate("windowaceptar", "NOTIFICAR"))
        self.volver.setText(_translate("windowaceptar", "volver"))
        self.label.setText(_translate("windowaceptar", "Notificar Pedido"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    windowaceptar = QtWidgets.QMainWindow()
    ui = Ui_windowaceptar()
    ui.setupUi(windowaceptar)
    windowaceptar.show()
    sys.exit(app.exec_())
