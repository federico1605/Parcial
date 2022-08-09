from PyQt5 import QtCore, QtGui, QtWidgets
from Parcial.Controlador.UpdateAdmin import ActualizarAdmin
from Parcial.Backend.usuarios import AdminGlobal
from Parcial.Backend.conexion import Database
conexion = Database
import sys
import os
myDir = os.getcwd()
sys.path.append(myDir)

class Ui_ActuAdminUser(object):
    def __init__(self):
        self.controlador = ActualizarAdmin(self)

        # GENERAR LISTADO ID USURIO
        self.listadoId = AdminGlobal.consultarUsuarios(conexion.conectar())

    def setupUi(self, ActuAdminUser):
        self.main = ActuAdminUser
        ActuAdminUser.setObjectName("ActuAdminUser")
        ActuAdminUser.setFixedSize(541, 300)
        self.labelTitutlo = QtWidgets.QLabel(ActuAdminUser)
        self.labelTitutlo.setGeometry(QtCore.QRect(180, 20, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.labelTitutlo.setFont(font)
        self.labelTitutlo.setObjectName("labelTitutlo")
        self.labelAcC = QtWidgets.QLabel(ActuAdminUser)
        self.labelAcC.setGeometry(QtCore.QRect(21, 91, 178, 19))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.labelAcC.setFont(font)
        self.labelAcC.setObjectName("labelAcC")
        self.labelAcT = QtWidgets.QLabel(ActuAdminUser)
        self.labelAcT.setGeometry(QtCore.QRect(311, 96, 160, 19))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.labelAcT.setFont(font)
        self.labelAcT.setObjectName("labelAcT")

        # CONTRASEÑA UPDATE
        self.lineEditContraU = QtWidgets.QLineEdit(ActuAdminUser)
        self.lineEditContraU.setGeometry(QtCore.QRect(107, 116, 131, 20))
        self.lineEditContraU.setObjectName("lineEditContraU")

        self.labelContra = QtWidgets.QLabel(ActuAdminUser)
        self.labelContra.setGeometry(QtCore.QRect(21, 116, 80, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.labelContra.setFont(font)
        self.labelContra.setObjectName("labelContra")

        # COMBOBOX ID USUARIO CONTRASEÑA
        self.comboBoxIDC = QtWidgets.QComboBox(ActuAdminUser)
        self.comboBoxIDC.setGeometry(QtCore.QRect(107, 142, 131, 20))
        self.comboBoxIDC.setObjectName("comboBoxIDC")

        # GENERAR LISTADO ID USUARIO
        for idU in self.listadoId:
            self.comboBoxIDC.addItem(str(idU[0]))

        self.labelIDU = QtWidgets.QLabel(ActuAdminUser)
        self.labelIDU.setGeometry(QtCore.QRect(21, 142, 70, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.labelIDU.setFont(font)
        self.labelIDU.setObjectName("labelIDU")

        # COMBOBOX ID USUARIO TELEFONO
        self.comboBoxIDT = QtWidgets.QComboBox(ActuAdminUser)
        self.comboBoxIDT.setGeometry(QtCore.QRect(392, 147, 131, 20))
        self.comboBoxIDT.setObjectName("comboBoxIDT")
        # GENERAR LISTADO ID USUARIO
        for idU in self.listadoId:
            self.comboBoxIDT.addItem(str(idU[0]))

        self.label = QtWidgets.QLabel(ActuAdminUser)
        self.label.setGeometry(QtCore.QRect(311, 121, 64, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")

        # UPDATE TELEFONO
        self.lineEditTele = QtWidgets.QLineEdit(ActuAdminUser)
        self.lineEditTele.setGeometry(QtCore.QRect(392, 121, 131, 20))
        self.lineEditTele.setObjectName("lineEditTele")

        self.labelIDU_2 = QtWidgets.QLabel(ActuAdminUser)
        self.labelIDU_2.setGeometry(QtCore.QRect(311, 147, 70, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.labelIDU_2.setFont(font)
        self.labelIDU_2.setObjectName("labelIDU_2")
        self.botonAcC = QtWidgets.QPushButton(ActuAdminUser)
        self.botonAcC.setGeometry(QtCore.QRect(21, 168, 75, 23))
        self.botonAcC.setObjectName("botonAcC")
        self.botonACT = QtWidgets.QPushButton(ActuAdminUser)
        self.botonACT.setGeometry(QtCore.QRect(311, 173, 75, 23))
        self.botonACT.setObjectName("botonACT")
        self.botonVolver = QtWidgets.QPushButton(ActuAdminUser)
        self.botonVolver.setGeometry(QtCore.QRect(450, 220, 75, 23))
        self.botonVolver.setObjectName("botonVolver")

        self.retranslateUi(ActuAdminUser)
        QtCore.QMetaObject.connectSlotsByName(ActuAdminUser)

        # --------------------------------------------EVENTOS---------------------------------------
        self.botonAcC.clicked.connect(self.accionUdateC)
        self.botonACT.clicked.connect(self.accionUdateT)
        self.botonVolver.clicked.connect(self.accionVolver)

    def accionUdateC(self):
        contrasenaU = (self.lineEditContraU.text())
        comboC = (self.comboBoxIDC.currentText())
        print(contrasenaU)
        self.controlador.UpdateUContra(contrasenaU, comboC)

    def accionUdateT(self):
        telefono = (self.lineEditTele.text())
        comboT = (self.comboBoxIDT.currentText())
        self.controlador.UpdateTele(telefono, comboT)
        print(telefono)

    def accionVolver(self):
        self.main.close()

    def retranslateUi(self, ActuAdminUser):
        _translate = QtCore.QCoreApplication.translate
        ActuAdminUser.setWindowTitle(_translate("ActuAdminUser", "Form"))
        self.labelTitutlo.setText(_translate("ActuAdminUser", "Actulizar Admin"))
        self.labelAcC.setText(_translate("ActuAdminUser", "Actualizar contraseña"))
        self.labelAcT.setText(_translate("ActuAdminUser", "Actualizar Telefono"))
        self.labelContra.setText(_translate("ActuAdminUser", "Contraseña:"))
        self.labelIDU.setText(_translate("ActuAdminUser", "Id Usuario:"))
        self.label.setText(_translate("ActuAdminUser", "Telefono: "))
        self.labelIDU_2.setText(_translate("ActuAdminUser", "Id Usuario:"))
        self.botonAcC.setText(_translate("ActuAdminUser", "Actualizar"))
        self.botonACT.setText(_translate("ActuAdminUser", "Actualizar"))
        self.botonVolver.setText(_translate("ActuAdminUser", "Volver"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ActuAdminUser = QtWidgets.QWidget()
    ui = Ui_ActuAdminUser()
    ui.setupUi(ActuAdminUser)
    ActuAdminUser.show()
    sys.exit(app.exec_())
