from PyQt5 import QtCore, QtGui, QtWidgets
from Parcial.Frontend.Administrador import *
from Parcial.Backend.conexion import Database
from Parcial.Controlador.getUser import VentanaPrincipal
import sys
import os
from Parcial.Frontend.ValidacionUsuario import Ui_errorUsuario
conexion = Database
myDir = os.getcwd()
sys.path.append(myDir)

class Ui_MainWindow(object):

    def __init__(self):
        self.controlador = VentanaPrincipal(self)

    def setupUi(self, MainWindow):
        self.main = MainWindow
        MainWindow.setObjectName("MainWindow")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # TAMAÑO DE LA VENTANA NO EDITABLE
        MainWindow.setFixedSize(450, 350)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(100, 40, 191, 41))
        self.label.setStyleSheet("font: 75 20pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(130, 270, 75, 23))
        self.pushButton.setStyleSheet("border-radius:10px;\n""background-color: rgb(235, 217, 255);\n""\n""")
        self.pushButton.setObjectName("pushButton")

        self.botonIngresar = QtWidgets.QPushButton(self.centralwidget)
        self.botonIngresar.setGeometry(QtCore.QRect(240, 270, 75, 23))
        self.botonIngresar.setStyleSheet("border-radius:10px;\n""background-color: rgb(235, 217, 255);\n""\n"" ")
        self.botonIngresar.setObjectName("botonIngresar")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(100, 120, 47, 13))
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(100, 160, 71, 16))
        self.label_3.setObjectName("label_3")

        self.usuario = QtWidgets.QLineEdit(self.centralwidget)
        self.usuario.setGeometry(QtCore.QRect(200, 119, 151, 21))
        self.usuario.setObjectName("usuario")

        self.contrasena = QtWidgets.QLineEdit(self.centralwidget)
        self.contrasena.setGeometry(QtCore.QRect(200, 160, 151, 20))
        self.contrasena.setText("")
        self.contrasena.setEchoMode(QtWidgets.QLineEdit.Password)
        self.contrasena.setObjectName("contrasena")

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(240, 210, 47, 21))
        self.label_4.setStyleSheet("\n""font: 75 8pt \"MS Shell Dlg 2\";")
        self.label_4.setObjectName("label_4")
        # print(self.listadouser)

        # Generador de ComboBox
        '''self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(330, 210, 151, 22))
        self.comboBox.setObjectName("comboBox")
        # Generar listado de roles
        for user in self.listadouser:
            itemUser = user[1]
            self.comboBox.addItem(itemUser)
            #print(itemUser)'''

        #---------------------------------------------Eventos-----------------------------------------------------------
        self.botonIngresar.clicked.connect(self.validarUsuario)
        self.pushButton.clicked.connect(self.cerrarVentana)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    # CERRAR VENTANA PRINCIPAL
    def cerrarVentana(self):
        self.main.close()
        print("Cerrar ventana")

    # EXTRAER USUARIO Y CONTRASEÑA
    def validarUsuario(self):
        usuario = (self.usuario.text())
        contrasena = (self.contrasena.text())
        self.controlador.controladorLogin(usuario, contrasena, conexion.conectar(), Ui_errorUsuario, Ui_Admin)
        self.main.close()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Trailers"))
        self.label.setText(_translate("MainWindow", "INICIO SESION"))
        self.pushButton.setText(_translate("MainWindow", "CANCELAR"))
        self.botonIngresar.setText(_translate("MainWindow", "INGRESAR"))
        self.label_2.setText(_translate("MainWindow", "USUARIO"))
        self.label_3.setText(_translate("MainWindow", "CONTRASEÑA"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
