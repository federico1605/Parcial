from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_errorUsuario(object):
    def setupUi(self, errorUsuario):
        self.errorUsuario = errorUsuario
        errorUsuario.setObjectName("errorUsuario")
        errorUsuario.setFixedSize(373, 179)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        errorUsuario.setFont(font)
        errorUsuario.setWindowTitle("")
        self.label = QtWidgets.QLabel(errorUsuario)
        self.label.setGeometry(QtCore.QRect(70, 10, 251, 91))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(errorUsuario)
        self.label_2.setGeometry(QtCore.QRect(20, 80, 331, 91))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(errorUsuario)
        QtCore.QMetaObject.connectSlotsByName(errorUsuario)

    def retranslateUi(self, errorUsuario):
        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("errorUsuario", "Las casillas están vacias."))
        self.label_2.setText(_translate("errorUsuario", "Usuario y/o contraseña no validos"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    errorUsuario = QtWidgets.QWidget()
    ui = Ui_errorUsuario()
    ui.setupUi(errorUsuario)
    errorUsuario.show()
    sys.exit(app.exec_())
