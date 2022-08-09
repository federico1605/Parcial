from PyQt5 import QtCore, QtGui, QtWidgets
from Parcial.Controlador.Deleteadmin import ControlerDelete
from Parcial.Backend.usuarios import AdminGlobal
from Parcial.Backend.Producto import Producto
from Parcial.Backend.Negocio import Negocio
from Parcial.Backend.conexion import Database
conexion = Database

import sys
import os
myDir = os.getcwd()
sys.path.append(myDir)


class Ui_MainWindow(object):
    def __init__(self):
        self.controlador = ControlerDelete(self)

        # LISTADO DE ROLES
        self.listadoRol = AdminGlobal.consultarRol(conexion.conectar())
        # LISTADO DE PRODUCTOS
        self.listadoProducto = Producto.comboBox(conexion.conectar())
        # LISTADO DE NEGOCIO
        self.listadoNegocio = Negocio.comboBox(conexion.conectar())

    def setupUi(self, MainWindow):
        self.main = MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(650, 550)
        MainWindow.setStyleSheet("\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(135, 135, 135, 255), stop:1 rgba(255, 255, 255, 255));")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(250, 20, 151, 31))
        self.label.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 250, 238, 131))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayoutU = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayoutU.setContentsMargins(0, 0, 0, 0)
        self.gridLayoutU.setObjectName("gridLayoutU")
        self.idusuario = QtWidgets.QLabel(self.layoutWidget)
        self.idusuario.setStyleSheet("Qwidget#label3widget{\n"
"font: 9pt \"MS Shell Dlg 2\";\n"
"font: 9pt \"MS Shell Dlg 2\";}\n"
"")
        self.idusuario.setObjectName("idusuario")
        self.gridLayoutU.addWidget(self.idusuario, 2, 0, 1, 1)

        #ACCION ELIMINAR USUARIO
        self.eliminarU = QtWidgets.QPushButton(self.layoutWidget)
        self.eliminarU.setObjectName("eliminarU")
        self.gridLayoutU.addWidget(self.eliminarU, 3, 0, 1, 2)

        # COMBOBOX USUARIO
        self.comboBoxU = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBoxU.setObjectName("comboBoxU")
        self.gridLayoutU.addWidget(self.comboBoxU, 1, 1, 1, 1)
        # GENERAR LISTADO DE ROLES
        for roles in self.listadoRol:
            self.comboBoxU.addItem(roles[1])

        self.seleccionarU = QtWidgets.QLabel(self.layoutWidget)
        self.seleccionarU.setStyleSheet("Qwidget#label3widget{\n"
"font: 9pt \"MS Shell Dlg 2\";\n"
"font: 9pt \"MS Shell Dlg 2\";}\n"
"")
        self.seleccionarU.setObjectName("seleccionarU")
        self.gridLayoutU.addWidget(self.seleccionarU, 1, 0, 1, 1)

        #ID USUARIO
        self.lineEditU = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEditU.setObjectName("lineEditU")
        self.gridLayoutU.addWidget(self.lineEditU, 2, 1, 1, 1)

        self.tituloU = QtWidgets.QLabel(self.layoutWidget)
        self.tituloU.setStyleSheet("font: 9pt \"MS Shell Dlg 2\";")
        self.tituloU.setObjectName("tituloU")
        self.gridLayoutU.addWidget(self.tituloU, 0, 0, 1, 2)
        self.layoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_2.setGeometry(QtCore.QRect(350, 160, 244, 131))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.gridLayoutP = QtWidgets.QGridLayout(self.layoutWidget_2)
        self.gridLayoutP.setContentsMargins(0, 0, 0, 0)
        self.gridLayoutP.setObjectName("gridLayoutP")
        self.seleccionarP = QtWidgets.QLabel(self.layoutWidget_2)
        self.seleccionarP.setStyleSheet("Qwidget#label3widget{\n"
"font: 9pt \"MS Shell Dlg 2\";\n"
"font: 9pt \"MS Shell Dlg 2\";}\n"
"")
        self.seleccionarP.setObjectName("seleccionarP")
        self.gridLayoutP.addWidget(self.seleccionarP, 1, 0, 1, 1)
        self.idproducto = QtWidgets.QLabel(self.layoutWidget_2)
        self.idproducto.setStyleSheet("Qwidget#label3widget{\n"
"font: 9pt \"MS Shell Dlg 2\";\n"
"font: 9pt \"MS Shell Dlg 2\";}\n"
"")
        self.idproducto.setObjectName("idproducto")
        self.gridLayoutP.addWidget(self.idproducto, 2, 0, 1, 1)

        # COMBOBOX PRODUCTO
        self.comboBoxP = QtWidgets.QComboBox(self.layoutWidget_2)
        self.comboBoxP.setObjectName("comboBoxP")
        self.gridLayoutP.addWidget(self.comboBoxP, 1, 1, 1, 1)

        # GENERAR COMBOX PRODUCTO
        for pro in self.listadoProducto:
            self.comboBoxP.addItem(pro[0])

        # BOTON Y LINEEDIT PRODUCTOS
        self.lineEditP = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.lineEditP.setObjectName("lineEditP")
        self.gridLayoutP.addWidget(self.lineEditP, 2, 1, 1, 1)
        self.eliminarP = QtWidgets.QPushButton(self.layoutWidget_2)
        self.eliminarP.setObjectName("eliminarP")

        self.gridLayoutP.addWidget(self.eliminarP, 3, 0, 1, 2)
        self.tituloP = QtWidgets.QLabel(self.layoutWidget_2)
        self.tituloP.setStyleSheet("font: 9pt \"MS Shell Dlg 2\";")
        self.tituloP.setObjectName("tituloP")
        self.gridLayoutP.addWidget(self.tituloP, 0, 0, 1, 2)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(20, 80, 238, 131))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayoutN = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayoutN.setContentsMargins(0, 0, 0, 0)
        self.gridLayoutN.setObjectName("gridLayoutN")
        self.tituloN = QtWidgets.QLabel(self.layoutWidget1)
        self.tituloN.setStyleSheet("font: 9pt \"MS Shell Dlg 2\";")
        self.tituloN.setObjectName("tituloN")
        self.gridLayoutN.addWidget(self.tituloN, 0, 0, 1, 2)
        self.seleccionarN = QtWidgets.QLabel(self.layoutWidget1)
        self.seleccionarN.setStyleSheet("Qwidget#label3widget{\n"
"font: 9pt \"MS Shell Dlg 2\";\n"
"font: 9pt \"MS Shell Dlg 2\";}\n"
"")
        self.seleccionarN.setObjectName("seleccionarN")
        self.gridLayoutN.addWidget(self.seleccionarN, 1, 0, 1, 1)

        # COMBOBOX NEGOCIO
        self.comboBoxN = QtWidgets.QComboBox(self.layoutWidget1)
        self.comboBoxN.setObjectName("comboBoxN")
        self.gridLayoutN.addWidget(self.comboBoxN, 1, 1, 1, 1)
        # GENERAR COMBOBOX NEGOCIO
        for negocio in self.listadoNegocio:
            self.comboBoxN.addItem(negocio[0])

        self.idnegocio = QtWidgets.QLabel(self.layoutWidget1)
        self.idnegocio.setStyleSheet("Qwidget#label3widget{\n"
"font: 9pt \"MS Shell Dlg 2\";\n"
"font: 9pt \"MS Shell Dlg 2\";}\n"
"")
        self.idnegocio.setObjectName("idnegocio")
        self.gridLayoutN.addWidget(self.idnegocio, 2, 0, 1, 1)
        self.lineEditN = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEditN.setObjectName("lineEditN")


        self.gridLayoutN.addWidget(self.lineEditN, 2, 1, 1, 1)
        self.eliminarN = QtWidgets.QPushButton(self.layoutWidget1)
        self.eliminarN.setObjectName("eliminarN")
        self.gridLayoutN.addWidget(self.eliminarN, 3, 0, 1, 2)

        self.volver = QtWidgets.QPushButton(self.centralwidget)
        self.volver.setGeometry(QtCore.QRect(20, 440, 75, 23))
        self.volver.setObjectName("volver")

        self.alertaN = QtWidgets.QLabel(self.centralwidget)
        self.alertaN.setGeometry(QtCore.QRect(20, 220, 47, 13))
        self.alertaN.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";\n"
"color:red;")
        self.alertaN.setText("")
        self.alertaN.setObjectName("alertaN")
        self.alertaP = QtWidgets.QLabel(self.centralwidget)
        self.alertaP.setGeometry(QtCore.QRect(350, 300, 47, 13))
        self.alertaP.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";\n"
"color:red;")
        self.alertaP.setText("")
        self.alertaP.setObjectName("alertaP")
        self.alertaU = QtWidgets.QLabel(self.centralwidget)
        self.alertaU.setGeometry(QtCore.QRect(20, 390, 47, 13))
        self.alertaU.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";\n"
"color:red;")
        self.alertaU.setText("")
        self.alertaU.setObjectName("alertaU")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # -----------------------------EVENTOS-------------------------------------
        self.eliminarU.clicked.connect(self.deleteU)
        self.eliminarP.clicked.connect(self.deleteP)
        self.eliminarN.clicked.connect(self.deleteN)
        self.volver.clicked.connect(self.cerrarVolver)

    # ELIMINAR USUARIO
    def deleteU(self):
        deleU = (self.lineEditU.text())
        combo = (self.comboBoxU.currentText())
        self.controlador.deleteUsuario(deleU)

    # ELIMINAR PRODUCTO
    def deleteP(self):
        deleP = (self.lineEditP.text())
        comboP = (self.comboBoxP.currentText())
        self.controlador.deleteProducto(deleP)

    # ELIMINAR NEGOCIO
    def deleteN(self):
        deleN = (self.lineEditN.text())
        comboN =(self.comboBoxN.currentText())
        self.controlador.deleteNegocio(deleN)

    def cerrarVolver(self):
        self.main.close()
        print("Cerrar ventana")


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "ADMINISTRADOR"))
        self.idusuario.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\">ID del usuario:</p></body></html>"))
        self.eliminarU.setText(_translate("MainWindow", "eliminar"))
        self.comboBoxU.setItemText(0, _translate("MainWindow", "Admin"))
        self.seleccionarU.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\">seleccionar usuario:</p></body></html>"))
        self.tituloU.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">ELIMINAR USUARIO</p></body></html>"))
        self.seleccionarP.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\">seleccionar producto:</p></body></html>"))
        self.idproducto.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\">ID del negocio al que pertenece:</p></body></html>"))
        self.comboBoxP.setItemText(0, _translate("MainWindow", "Mexican rill"))
        self.eliminarP.setText(_translate("MainWindow", "eliminar"))
        self.tituloP.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">ELIMINAR PRODUCTO</p></body></html>"))
        self.tituloN.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">ELIMINAR NEGOCIO</p></body></html>"))
        self.seleccionarN.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\">seleccionar negocio:</p></body></html>"))
        self.comboBoxN.setItemText(0, _translate("MainWindow", "Pizzas rio"))
        self.idnegocio.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\">ID del negocio:</p></body></html>"))
        self.eliminarN.setText(_translate("MainWindow", "eliminar"))
        self.volver.setText(_translate("MainWindow", "volver"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
