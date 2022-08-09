from PyQt5 import QtCore, QtGui, QtWidgets
from Parcial.Frontend.AdminBorrar import Ui_MainWindow
from Parcial.Frontend.OpcionCrear import Ui_opcioncrear
from Parcial.Frontend.OpcionActualizar import Ui_OpcionActualizar
from Parcial.Frontend.estadoPedido import Ui_estadoPedido
from Parcial.Frontend.REGISTRODEPRODUCTOS import Ui_MainWindowR
from Parcial.Frontend.CierreCaja import Ui_Form

class Ui_Admin(object):
    def __init__(self):
        self.borrar = Ui_MainWindow
        self.crear = Ui_opcioncrear
        self.actualizar = Ui_OpcionActualizar
        self.estado = Ui_estadoPedido
        self.consulta = Ui_MainWindowR
        self.cierre = Ui_Form

    def setupUi(self, Admin):
        Admin.setObjectName("Admin")
        # Admin.resize(356, 620)
        Admin.setFixedSize(356, 620)
        self.centralwidget = QtWidgets.QWidget(Admin)
        self.centralwidget.setObjectName("centralwidget")
        self.botonCrear = QtWidgets.QPushButton(self.centralwidget)
        self.botonCrear.setGeometry(QtCore.QRect(90, 90, 171, 51))
        self.botonCrear.setObjectName("botonCrear")
        self.botonBorrar = QtWidgets.QPushButton(self.centralwidget)
        self.botonBorrar.setGeometry(QtCore.QRect(90, 180, 171, 51))
        self.botonBorrar.setObjectName("botonBorrar")
        self.botonConsultar = QtWidgets.QPushButton(self.centralwidget)
        self.botonConsultar.setGeometry(QtCore.QRect(90, 270, 171, 51))
        self.botonConsultar.setObjectName("botonConsultar")
        self.botonActualizar = QtWidgets.QPushButton(self.centralwidget)
        self.botonActualizar.setGeometry(QtCore.QRect(90, 360, 171, 51))
        self.botonActualizar.setObjectName("botonActualizar")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(100, 20, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.botonCierre = QtWidgets.QPushButton(self.centralwidget)
        self.botonCierre.setGeometry(QtCore.QRect(90, 460, 171, 51))
        self.botonCierre.setObjectName("botonCierre")
        self.botonCrear_3 = QtWidgets.QPushButton(self.centralwidget)
        self.botonCrear_3.setGeometry(QtCore.QRect(90, 540, 171, 51))
        self.botonCrear_3.setObjectName("botonCrear_3")
        Admin.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Admin)
        self.statusbar.setObjectName("statusbar")
        Admin.setStatusBar(self.statusbar)

        self.retranslateUi(Admin)
        QtCore.QMetaObject.connectSlotsByName(Admin)

        # ------------------------------------------Eventos-------------------------------------------------------------
        self.botonCrear.clicked.connect(self.accionCrear)
        self.botonBorrar.clicked.connect(self.accionBorrar)
        self.botonActualizar.clicked.connect(self.accionActualizar)
        self.botonConsultar.clicked.connect(self.accionConsultar)
        self.botonCierre.clicked.connect(self.accionCierre)
        self.botonCrear_3.clicked.connect(self.accionEstado)

    def accionCrear(self):
        self.crear.Ventana = QtWidgets.QWidget()
        self.crear.ui = Ui_opcioncrear()
        self.crear.ui.setupUi(self.crear.Ventana)
        self.crear.Ventana.show()

    def accionBorrar(self):
        self.borrar.Ventana = QtWidgets.QMainWindow()
        self.borrar.ui = Ui_MainWindow()
        self.borrar.ui.setupUi(self.borrar.Ventana)
        self.borrar.Ventana.show()

    def accionActualizar(self):
        self.actualizar.Ventana = QtWidgets.QWidget()
        self.actualizar.ui = Ui_OpcionActualizar()
        self.actualizar.ui.setupUi(self.actualizar.Ventana)
        self.actualizar.Ventana.show()

    def accionConsultar(self):
        self.consulta.Ventana = QtWidgets.QWidget()
        self.consulta.ui = Ui_MainWindowR()
        self.consulta.ui.setupUi(self.consulta.Ventana)
        self.consulta.Ventana.show()

    def accionCierre(self):
        self.cierre.Ventana = QtWidgets.QWidget()
        self.cierre.ui = Ui_Form()
        self.cierre.ui.setupUi(self.cierre.Ventana)
        self.cierre.Ventana.show()

    def accionEstado(self):
        self.estado.Ventana = QtWidgets.QWidget()
        self.estado.ui = Ui_estadoPedido()
        self.estado.ui.setupUi(self.estado.Ventana)
        self.estado.Ventana.show()


    def retranslateUi(self, Admin):
        _translate = QtCore.QCoreApplication.translate
        Admin.setWindowTitle(_translate("Admin", "Trailers"))
        self.botonCrear.setText(_translate("Admin", "Crear"))
        self.botonBorrar.setText(_translate("Admin", "Borrar"))
        self.botonConsultar.setText(_translate("Admin", "Consultar"))
        self.botonActualizar.setText(_translate("Admin", "Actualizar"))
        self.label.setText(_translate("Admin", "<html><head/><body><p align=\"center\">Administrador</p></body></html>"))
        self.botonCierre.setText(_translate("Admin", "Cierre Caja"))
        self.botonCrear_3.setText(_translate("Admin", "Estado Pedido"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Admin = QtWidgets.QMainWindow()
    ui = Ui_Admin()
    ui.setupUi(Admin)
    Admin.show()
    sys.exit(app.exec_())
