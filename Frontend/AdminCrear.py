from PyQt5 import QtCore, QtGui, QtWidgets
from Parcial.Controlador.CreatAdmin import CrearAdmin

class Ui_crearAdmin(object):
    def __init__(self):
        self.controlador = CrearAdmin(self)

    def setupUi(self, crearAdmin):
        self.main = crearAdmin
        crearAdmin.setObjectName("crearAdmin")
        crearAdmin.setFixedSize(410, 300)

        self.labelCrear = QtWidgets.QLabel(crearAdmin)
        self.labelCrear.setGeometry(QtCore.QRect(100, 10, 171, 31))
        self.labelCrear.setObjectName("labelCrear")
        self.labelIdusuario = QtWidgets.QLabel(crearAdmin)
        self.labelIdusuario.setGeometry(QtCore.QRect(52, 62, 59, 17))
        font = QtGui.QFont()
        font.setFamily("Ebrima")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.labelIdusuario.setFont(font)
        self.labelIdusuario.setObjectName("labelIdusuario")

        self.labelNombre = QtWidgets.QLabel(crearAdmin)
        self.labelNombre.setGeometry(QtCore.QRect(52, 85, 109, 17))
        font = QtGui.QFont()
        font.setFamily("Ebrima")
        font.setBold(False)
        font.setWeight(50)
        self.labelNombre.setFont(font)
        self.labelNombre.setObjectName("labelNombre")

        self.labelTelefono = QtWidgets.QLabel(crearAdmin)
        self.labelTelefono.setGeometry(QtCore.QRect(52, 137, 59, 17))
        font = QtGui.QFont()
        font.setFamily("Ebrima")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.labelTelefono.setFont(font)
        self.labelTelefono.setObjectName("labelTelefono")

        self.label_2 = QtWidgets.QLabel(crearAdmin)
        self.label_2.setGeometry(QtCore.QRect(52, 111, 73, 17))
        font = QtGui.QFont()
        font.setFamily("Ebrima")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.labelRol = QtWidgets.QLabel(crearAdmin)
        self.labelRol.setGeometry(QtCore.QRect(52, 163, 24, 17))
        font = QtGui.QFont()
        font.setFamily("Ebrima")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.labelRol.setFont(font)
        self.labelRol.setObjectName("labelRol")

        self.labelIdN = QtWidgets.QLabel(crearAdmin)
        self.labelIdN.setGeometry(QtCore.QRect(52, 189, 71, 17))
        font = QtGui.QFont()
        font.setFamily("Ebrima")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.labelIdN.setFont(font)
        self.labelIdN.setObjectName("labelIdN")

        self.labelMensaje = QtWidgets.QLabel(crearAdmin)
        self.labelMensaje.setGeometry(QtCore.QRect(167, 62, 193, 17))
        font = QtGui.QFont()
        font.setFamily("Ebrima")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.labelMensaje.setFont(font)
        self.labelMensaje.setObjectName("labelMensaje")
        # NOMBRE USUARIO
        self.lineEditNU = QtWidgets.QLineEdit(crearAdmin)
        self.lineEditNU.setGeometry(QtCore.QRect(167, 85, 191, 20))
        self.lineEditNU.setObjectName("lineEditNU")

        self.lineEditC = QtWidgets.QLineEdit(crearAdmin)
        self.lineEditC.setGeometry(QtCore.QRect(167, 111, 191, 20))
        self.lineEditC.setObjectName("lineEditC")

        self.lineEditTe = QtWidgets.QLineEdit(crearAdmin)
        self.lineEditTe.setGeometry(QtCore.QRect(167, 137, 191, 20))
        self.lineEditTe.setObjectName("lineEditTe")

        self.lineEditRo = QtWidgets.QLineEdit(crearAdmin)
        self.lineEditRo.setGeometry(QtCore.QRect(167, 163, 191, 20))
        self.lineEditRo.setObjectName("lineEditRo")

        self.lineEditIdN = QtWidgets.QLineEdit(crearAdmin)
        self.lineEditIdN.setGeometry(QtCore.QRect(167, 189, 191, 20))
        self.lineEditIdN.setObjectName("lineEditIdN")

        self.botonVolver = QtWidgets.QPushButton(crearAdmin)
        self.botonVolver.setGeometry(QtCore.QRect(80, 230, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.botonVolver.setFont(font)
        self.botonVolver.setObjectName("botonVolver")

        self.bontonCrear = QtWidgets.QPushButton(crearAdmin)
        self.bontonCrear.setGeometry(QtCore.QRect(250, 230, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.bontonCrear.setFont(font)
        self.bontonCrear.setObjectName("bontonCrear")

        self.retranslateUi(crearAdmin)
        QtCore.QMetaObject.connectSlotsByName(crearAdmin)

        # ----------------------------------------------------Eventos---------------------------------------------------
        self.bontonCrear.clicked.connect(self.accionCrear)
        self.botonVolver.clicked.connect(self.cerrarCrear)

    def accionCrear(self):
        nomUsuario = (self.lineEditNU.text())
        conUsuario = (self.lineEditC.text())
        telUsuario = (self.lineEditTe.text())
        rolUsuario = (self.lineEditRo.text())
        idNegocio = (self.lineEditIdN.text())
        self.controlador.crearUsuario(nomUsuario, conUsuario, telUsuario, rolUsuario, idNegocio)
        #print(nomUsuario,conUsuario,telUsuario,rolUsuario,idNegocio)

    def cerrarCrear(self):
        self.main.close()
        print("Cerrar Ventana")

    def retranslateUi(self, crearAdmin):
        _translate = QtCore.QCoreApplication.translate
        crearAdmin.setWindowTitle(_translate("crearAdmin", "Form"))
        self.labelCrear.setToolTip(_translate("crearAdmin", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">Crear Usuario</span></p></body></html>"))
        self.labelCrear.setText(_translate("crearAdmin", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">Crear Usuario</span></p></body></html>"))
        self.labelIdusuario.setText(_translate("crearAdmin", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Id Usario:</span></p></body></html>"))
        self.labelNombre.setText(_translate("crearAdmin", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Nombre Usuario: </span></p></body></html>"))
        self.labelTelefono.setText(_translate("crearAdmin", "Telefono:"))
        self.label_2.setText(_translate("crearAdmin", "Contraseña:"))
        self.labelRol.setText(_translate("crearAdmin", "Rol:"))
        self.labelIdN.setText(_translate("crearAdmin", "Id Negocio:"))
        self.labelMensaje.setText(_translate("crearAdmin", "El Usuario lo ingresa el sistema"))
        self.botonVolver.setText(_translate("crearAdmin", "Volver"))
        self.bontonCrear.setText(_translate("crearAdmin", "Crear"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    crearAdmin = QtWidgets.QWidget()
    ui = Ui_crearAdmin()
    ui.setupUi(crearAdmin)
    crearAdmin.show()
    sys.exit(app.exec_())
