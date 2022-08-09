from PyQt5 import QtCore, QtGui, QtWidgets
from Parcial.Frontend.AdminCrear import Ui_crearAdmin
from Parcial.Frontend.AdminCrearNP import Ui_AdmiCNP


class Ui_opcioncrear(object):
    def __init__(self):
        self.crear = Ui_crearAdmin
        self.crearN = Ui_AdmiCNP

    def setupUi(self, opcioncrear):
        opcioncrear.setObjectName("opcioncrear")
        opcioncrear.setFixedSize(327, 196)
        self.labelTitulo = QtWidgets.QLabel(opcioncrear)
        self.labelTitulo.setGeometry(QtCore.QRect(60, 20, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.labelTitulo.setFont(font)
        self.labelTitulo.setObjectName("labelTitulo")

        self.botonU = QtWidgets.QPushButton(opcioncrear)
        self.botonU.setGeometry(QtCore.QRect(40, 120, 75, 23))
        self.botonU.setObjectName("botonU")

        self.botonPN = QtWidgets.QPushButton(opcioncrear)
        self.botonPN.setGeometry(QtCore.QRect(200, 120, 75, 23))
        self.botonPN.setObjectName("botonPN")

        self.labelUsuario = QtWidgets.QLabel(opcioncrear)
        self.labelUsuario.setGeometry(QtCore.QRect(50, 80, 71, 16))
        self.labelUsuario.setObjectName("labelUsuario")

        self.labelPro_Ne = QtWidgets.QLabel(opcioncrear)
        self.labelPro_Ne.setGeometry(QtCore.QRect(180, 80, 121, 21))
        self.labelPro_Ne.setObjectName("labelPro_Ne")

        self.retranslateUi(opcioncrear)
        QtCore.QMetaObject.connectSlotsByName(opcioncrear)

        # ---------------------------EVENTOS--------------------------------------------------
        self.botonU.clicked.connect(self.vistaUsuario)
        self.botonPN.clicked.connect(self.vistaPN)

    def vistaUsuario(self):
        print("Hola")
        self.crear.Ventana = QtWidgets.QWidget()
        self.crear.ui = Ui_crearAdmin()
        self.crear.ui.setupUi(self.crear.Ventana)
        self.crear.Ventana.show()

    def vistaPN(self):
        print("Bien")
        self.crearN.Ventana = QtWidgets.QWidget()
        self.crearN.ui = Ui_AdmiCNP()
        self.crearN.ui.setupUi(self.crearN.Ventana)
        self.crearN.Ventana.show()

    def retranslateUi(self, opcioncrear):
        _translate = QtCore.QCoreApplication.translate
        opcioncrear.setWindowTitle(_translate("opcioncrear", "Form"))
        self.labelTitulo.setText(_translate("opcioncrear", "Administrador Crear"))
        self.botonU.setText(_translate("opcioncrear", "Crear"))
        self.botonPN.setText(_translate("opcioncrear", "Crear"))
        self.labelUsuario.setText(_translate("opcioncrear", "Crear Usuario"))
        self.labelPro_Ne.setText(_translate("opcioncrear", "Crear Producto o negocio"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    opcioncrear = QtWidgets.QWidget()
    ui = Ui_opcioncrear()
    ui.setupUi(opcioncrear)
    opcioncrear.show()
    sys.exit(app.exec_())
