from PyQt5 import QtCore, QtGui, QtWidgets
from Parcial.Controlador.UpdateAdmin import ActualizarAdmin
from Parcial.Backend.Negocio import Negocio
from Parcial.Backend.conexion import Database
conexion = Database

import sys
import os
myDir = os.getcwd()
sys.path.append(myDir)


class Ui_Form(object):
    def __init__(self):
        self.controlador = ActualizarAdmin(self)

        # GENERAR LISTADO
        self.listadoId = Negocio.comboBox(conexion.conectar())

    def setupUi(self, Form):
        self.main = Form
        Form.setObjectName("Form")
        Form.setFixedSize(316, 233)
        self.labelTitulo = QtWidgets.QLabel(Form)
        self.labelTitulo.setGeometry(QtCore.QRect(30, 20, 261, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.labelTitulo.setFont(font)
        self.labelTitulo.setObjectName("labelTitulo")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(51, 71, 64, 18))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(51, 97, 86, 18))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.lineEditNomN = QtWidgets.QLineEdit(Form)
        self.lineEditNomN.setGeometry(QtCore.QRect(143, 71, 141, 20))
        self.lineEditNomN.setObjectName("lineEditNomN")

        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(143, 97, 141, 20))
        self.comboBox.setObjectName("comboBox")

        # GENERAR COMBOBOX
        for user in self.listadoId:
            self.comboBox.addItem(str(user[1]))

        self.bontonVolver = QtWidgets.QPushButton(Form)
        self.bontonVolver.setGeometry(QtCore.QRect(200, 180, 75, 23))
        self.bontonVolver.setObjectName("bontonVolver")

        self.botonActualizar = QtWidgets.QPushButton(Form)
        self.botonActualizar.setGeometry(QtCore.QRect(51, 123, 231, 23))
        self.botonActualizar.setObjectName("botonActualizar")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        # ------------------------------------------EVENTOS---------------------------------------------------
        self.bontonVolver.clicked.connect(self.accionVolver)
        self.botonActualizar.clicked.connect(self.accionUpdateN)

    def accionUpdateN(self):
        nombNegocio = (self.lineEditNomN.text())
        iduser = (self.comboBox.currentText())
        self.controlador.updateNegocio(nombNegocio, iduser)

    def accionVolver(self):
        self.main.close()
        print("Cerrar ventana")

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.labelTitulo.setText(_translate("Form", "Admin Actulizar Negocio"))
        self.label.setText(_translate("Form", "Nombre:"))
        self.label_2.setText(_translate("Form", "Id Negocio:"))
        self.bontonVolver.setText(_translate("Form", "Volver"))
        self.botonActualizar.setText(_translate("Form", "Actualizar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
