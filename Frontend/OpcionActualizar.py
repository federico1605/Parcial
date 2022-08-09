from PyQt5 import QtCore, QtGui, QtWidgets
from Parcial.Frontend.AdminUpdateU import Ui_ActuAdminUser
from Parcial.Frontend.AdminUpdateP import Ui_AdminUPro
from Parcial.Frontend.AdminUpdateN import Ui_Form

class Ui_OpcionActualizar(object):
    def __init__(self):
        self.updateU = Ui_ActuAdminUser
        self.updateP = Ui_AdminUPro
        self.updateN = Ui_Form

    def setupUi(self, OpcionActualizar):
        self.main = OpcionActualizar
        OpcionActualizar.setObjectName("OpcionActualizar")
        OpcionActualizar.setFixedSize(433, 222)
        self.labelTitulo = QtWidgets.QLabel(OpcionActualizar)
        self.labelTitulo.setGeometry(QtCore.QRect(60, 20, 321, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.labelTitulo.setFont(font)
        self.labelTitulo.setObjectName("labelTitulo")
        self.labelActU = QtWidgets.QLabel(OpcionActualizar)
        self.labelActU.setGeometry(QtCore.QRect(10, 70, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.labelActU.setFont(font)
        self.labelActU.setObjectName("labelActU")
        self.labelAcN = QtWidgets.QLabel(OpcionActualizar)
        self.labelAcN.setGeometry(QtCore.QRect(160, 70, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.labelAcN.setFont(font)
        self.labelAcN.setObjectName("labelAcN")
        self.labelAcP = QtWidgets.QLabel(OpcionActualizar)
        self.labelAcP.setGeometry(QtCore.QRect(310, 70, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.labelAcP.setFont(font)
        self.labelAcP.setObjectName("labelAcP")

        self.botonAcU = QtWidgets.QPushButton(OpcionActualizar)
        self.botonAcU.setGeometry(QtCore.QRect(20, 110, 75, 23))
        self.botonAcU.setObjectName("botonAcU")

        self.botonAcN = QtWidgets.QPushButton(OpcionActualizar)
        self.botonAcN.setGeometry(QtCore.QRect(180, 110, 75, 23))
        self.botonAcN.setObjectName("botonAcN")

        self.botonAcP = QtWidgets.QPushButton(OpcionActualizar)
        self.botonAcP.setGeometry(QtCore.QRect(340, 110, 75, 23))
        self.botonAcP.setObjectName("botonAcP")

        self.botonVolver = QtWidgets.QPushButton(OpcionActualizar)
        self.botonVolver.setGeometry(QtCore.QRect(330, 180, 75, 23))
        self.botonVolver.setObjectName("botonVolver")

        self.retranslateUi(OpcionActualizar)
        QtCore.QMetaObject.connectSlotsByName(OpcionActualizar)

        # --------------------EVENTOS----------------------------------------------
        self.botonAcU.clicked.connect(self.accionUpdateU)
        self.botonVolver.clicked.connect(self.accionVolver)
        self.botonAcN.clicked.connect(self.accionUpdateN)
        self.botonAcP.clicked.connect(self.accionUpdateP)

    def accionUpdateU(self):
        self.updateU.Ventana = QtWidgets.QWidget()
        self.updateU.ui = Ui_ActuAdminUser()
        self.updateU.ui.setupUi(self.updateU.Ventana)
        self.updateU.Ventana.show()

    def accionUpdateN(self):
        self.updateN.Ventana = QtWidgets.QWidget()
        self.updateN.ui = Ui_Form()
        self.updateN.ui.setupUi(self.updateN.Ventana)
        self.updateN.Ventana.show()

    def accionUpdateP(self):
        self.updateP.Ventana = QtWidgets.QWidget()
        self.updateP.ui = Ui_AdminUPro()
        self.updateP.ui.setupUi(self.updateP.Ventana)
        self.updateP.Ventana.show()

    def accionVolver(self):
        self.main.close()
        print("Cerrar ventana")

    def retranslateUi(self, OpcionActualizar):
        _translate = QtCore.QCoreApplication.translate
        OpcionActualizar.setWindowTitle(_translate("OpcionActualizar", "Form"))
        self.labelTitulo.setText(_translate("OpcionActualizar", "OPCIONES ACTULIZAR ADMIN"))
        self.labelActU.setText(_translate("OpcionActualizar", "Actulizar Usuario"))
        self.labelAcN.setText(_translate("OpcionActualizar", "Actulizar Negocio"))
        self.labelAcP.setText(_translate("OpcionActualizar", "Actulizar Producto"))
        self.botonAcU.setText(_translate("OpcionActualizar", "Actualizar"))
        self.botonAcN.setText(_translate("OpcionActualizar", "Actualizar"))
        self.botonAcP.setText(_translate("OpcionActualizar", "Actualizar"))
        self.botonVolver.setText(_translate("OpcionActualizar", "Volver"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    OpcionActualizar = QtWidgets.QWidget()
    ui = Ui_OpcionActualizar()
    ui.setupUi(OpcionActualizar)
    OpcionActualizar.show()
    sys.exit(app.exec_())
