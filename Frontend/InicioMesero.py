from PyQt5 import QtCore, QtGui, QtWidgets
from Parcial.Controlador.MeseroControler import MeseroController
from Parcial.Frontend.CrearMesero import Ui_CrearMesero
from Parcial.Frontend.EliminarMesero import Ui_Form
from Parcial.Frontend.GenerarFactura import Ui_FacrturaMesero

class Ui_iniciomesero(object):
    def __init__(self):
        self.controlador = MeseroController(self, self, self, self)
        self.crear = Ui_CrearMesero
        self.eliminar = Ui_Form
        self.factura = Ui_FacrturaMesero

    def setupUi(self, iniciomesero):
        iniciomesero.setObjectName("iniciomesero")
        iniciomesero.resize(342, 392)
        self.label = QtWidgets.QLabel(iniciomesero)
        self.label.setGeometry(QtCore.QRect(130, 10, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.botonCrear = QtWidgets.QPushButton(iniciomesero)
        self.botonCrear.setGeometry(QtCore.QRect(60, 70, 221, 71))
        self.botonCrear.setObjectName("botonCrear")
        self.botonEliminar = QtWidgets.QPushButton(iniciomesero)
        self.botonEliminar.setGeometry(QtCore.QRect(60, 180, 221, 71))
        self.botonEliminar.setObjectName("botonEliminar")
        self.botonFacturar = QtWidgets.QPushButton(iniciomesero)
        self.botonFacturar.setGeometry(QtCore.QRect(60, 290, 221, 71))
        self.botonFacturar.setObjectName("botonFacturar")

        self.retranslateUi(iniciomesero)
        QtCore.QMetaObject.connectSlotsByName(iniciomesero)

        # ----------------------------------------EVENTOS-----------------------------------------
        self.botonCrear.clicked.connect(self.accionCrear)
        self.botonEliminar.clicked.connect(self.accionEliminar)
        self.botonFacturar.clicked.connect(self.accionFactura)

    def accionCrear(self):
        self.crear.Ventana = QtWidgets.QMainWindow()
        self.crear.ui = Ui_CrearMesero()
        self.crear.ui.setupUi(self.crear.Ventana)
        self.crear.Ventana.show()

    def accionEliminar(self):
        self.eliminar.Ventana = QtWidgets.QMainWindow()
        self.eliminar.ui = Ui_Form()
        self.eliminar.ui.setupUi(self.eliminar.Ventana)
        self.eliminar.Ventana.show()

    def accionFactura(self):
        self.factura.Ventana = QtWidgets.QMainWindow()
        self.factura.ui = Ui_FacrturaMesero()
        self.factura.ui.setupUi(self.factura.Ventana)
        self.factura.Ventana.show()

    def retranslateUi(self, iniciomesero):
        _translate = QtCore.QCoreApplication.translate
        iniciomesero.setWindowTitle(_translate("iniciomesero", "Mesero"))
        self.label.setText(_translate("iniciomesero", "Mesero"))
        self.botonCrear.setText(_translate("iniciomesero", "Crear Pedido"))
        self.botonEliminar.setText(_translate("iniciomesero", "Eliminar Pedido"))
        self.botonFacturar.setText(_translate("iniciomesero", "Facturar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    iniciomesero = QtWidgets.QWidget()
    ui = Ui_iniciomesero()
    ui.setupUi(iniciomesero)
    iniciomesero.show()
    sys.exit(app.exec_())
