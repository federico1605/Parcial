from PyQt5 import QtCore, QtGui, QtWidgets
from Parcial.Controlador.CreatAdmin import CrearAdmin
from Parcial.Backend.Negocio import Negocio
from Parcial.Backend.conexion import Database

conexion = Database


class Ui_AdmiCNP(object):
    def __init__(self):
        self.controlador = CrearAdmin(self)

        # LISTADO IDNEGOCIO
        self.listadoNegocio = Negocio.comboBox(conexion.conectar())

    def setupUi(self, AdmiCNP):
        self.main = AdmiCNP
        AdmiCNP.setObjectName("AdmiCNP")
        AdmiCNP.resize(442, 407)
        AdmiCNP.setFixedSize(442, 407)
        self.labelTitulo = QtWidgets.QLabel(AdmiCNP)
        self.labelTitulo.setGeometry(QtCore.QRect(90, 20, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.labelTitulo.setFont(font)
        self.labelTitulo.setObjectName("labelTitulo")
        self.labelCNegocio = QtWidgets.QLabel(AdmiCNP)
        self.labelCNegocio.setGeometry(QtCore.QRect(33, 83, 115, 19))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.labelCNegocio.setFont(font)
        self.labelCNegocio.setObjectName("labelCNegocio")
        self.labelCProducto = QtWidgets.QLabel(AdmiCNP)
        self.labelCProducto.setGeometry(QtCore.QRect(31, 211, 123, 19))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.labelCProducto.setFont(font)
        self.labelCProducto.setObjectName("labelCProducto")
        self.labelNoNegocio = QtWidgets.QLabel(AdmiCNP)
        self.labelNoNegocio.setGeometry(QtCore.QRect(33, 108, 108, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.labelNoNegocio.setFont(font)
        self.labelNoNegocio.setObjectName("labelNoNegocio")
        self.label_2 = QtWidgets.QLabel(AdmiCNP)
        self.label_2.setGeometry(QtCore.QRect(33, 134, 80, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        # NOMBRE NEGOCIO
        self.lineEditNombreN = QtWidgets.QLineEdit(AdmiCNP)
        self.lineEditNombreN.setGeometry(QtCore.QRect(154, 108, 251, 20))
        self.lineEditNombreN.setObjectName("lineEditNombreN")

        self.labelMensajeN = QtWidgets.QLabel(AdmiCNP)
        self.labelMensajeN.setGeometry(QtCore.QRect(119, 134, 289, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.labelMensajeN.setFont(font)
        self.labelMensajeN.setObjectName("labelMensajeN")
        self.labelNombreP = QtWidgets.QLabel(AdmiCNP)
        self.labelNombreP.setGeometry(QtCore.QRect(31, 258, 117, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.labelNombreP.setFont(font)
        self.labelNombreP.setObjectName("labelNombreP")
        self.labelMensajeP = QtWidgets.QLabel(AdmiCNP)
        self.labelMensajeP.setGeometry(QtCore.QRect(118, 236, 289, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.labelMensajeP.setFont(font)
        self.labelMensajeP.setObjectName("labelMensajeP")
        self.labelIP = QtWidgets.QLabel(AdmiCNP)
        self.labelIP.setGeometry(QtCore.QRect(31, 236, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.labelIP.setFont(font)
        self.labelIP.setObjectName("labelIP")
        self.labelINe = QtWidgets.QLabel(AdmiCNP)
        self.labelINe.setGeometry(QtCore.QRect(31, 284, 72, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.labelINe.setFont(font)
        self.labelINe.setObjectName("labelINe")

        # COMBOBOX
        self.comboBoxINe = QtWidgets.QComboBox(AdmiCNP)
        self.comboBoxINe.setGeometry(QtCore.QRect(160, 284, 241, 20))
        self.comboBoxINe.setObjectName("comboBoxINe")
        self.comboBoxINe.addItem("")

        # GEENRAR COMBOBOX IDNEGOCIO
        for idnegocio in self.listadoNegocio:
            self.comboBoxINe.addItem(str(idnegocio[1]))

        self.labelValor = QtWidgets.QLabel(AdmiCNP)
        self.labelValor.setGeometry(QtCore.QRect(31, 310, 39, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.labelValor.setFont(font)
        self.labelValor.setObjectName("labelValor")

        # VALOR PRODUCTO
        self.lineEditValor = QtWidgets.QLineEdit(AdmiCNP)
        self.lineEditValor.setGeometry(QtCore.QRect(160, 310, 241, 20))
        self.lineEditValor.setObjectName("lineEditValor")

        # BONTON CREAR
        self.botonCrearN = QtWidgets.QPushButton(AdmiCNP)
        self.botonCrearN.setGeometry(QtCore.QRect(30, 160, 75, 23))
        self.botonCrearN.setObjectName("botonCrearN")
        self.botonCrearP = QtWidgets.QPushButton(AdmiCNP)
        self.botonCrearP.setGeometry(QtCore.QRect(30, 340, 75, 23))
        self.botonCrearP.setObjectName("botonCrearP")
        self.botonVolver = QtWidgets.QPushButton(AdmiCNP)
        self.botonVolver.setGeometry(QtCore.QRect(330, 370, 75, 23))
        self.botonVolver.setObjectName("botonVolver")

        # NOMBRE PRODUCTO
        self.lineEditNoPr = QtWidgets.QLineEdit(AdmiCNP)
        self.lineEditNoPr.setGeometry(QtCore.QRect(160, 258, 241, 20))
        self.lineEditNoPr.setObjectName("lineEditNoPr")

        self.retranslateUi(AdmiCNP)
        QtCore.QMetaObject.connectSlotsByName(AdmiCNP)
        # ------------------------EVENTOS-------------------------------------------------------
        self.botonCrearP.clicked.connect(self.accionCrearP)
        self.botonCrearN.clicked.connect(self.accionCrearN)
        self.botonVolver.clicked.connect(self.accioncerrar)

    def accionCrearP(self):
        nomProducto = (self.lineEditNoPr.text())
        valorP = (self.lineEditValor.text())
        comboP = int(self.comboBoxINe.currentText())
        self.controlador.crearProducto(nomProducto, comboP, valorP)
        print(nomProducto)
        print(valorP)

    def accionCrearN(self):
        print("Como")
        nomNegocio = (self.lineEditNombreN.text())
        self.controlador.crearNegocio(nomNegocio)

    def accioncerrar(self):
        self.main.close()
        print("Cerrar ventana")

    def retranslateUi(self, AdmiCNP):
        _translate = QtCore.QCoreApplication.translate
        AdmiCNP.setWindowTitle(_translate("AdmiCNP", "Form"))
        self.labelTitulo.setText(_translate("AdmiCNP", "Adminitrador Crear"))
        self.labelCNegocio.setText(_translate("AdmiCNP", "Crear Negocio"))
        self.labelCProducto.setText(_translate("AdmiCNP", "Crear Producto"))
        self.labelNoNegocio.setText(_translate("AdmiCNP", "Nombre Negocio:"))
        self.label_2.setText(_translate("AdmiCNP", "Id Neogocio:"))
        self.labelMensajeN.setText(_translate("AdmiCNP", "El Id se ingresa automaticamente el sistema."))
        self.labelNombreP.setText(_translate("AdmiCNP", "Nombre Producto:"))
        self.labelMensajeP.setText(_translate("AdmiCNP", "El Id se ingresa automaticamente el sistema."))
        self.labelIP.setText(_translate("AdmiCNP", "Id Prodcuto:"))
        self.labelINe.setText(_translate("AdmiCNP", "Id Negocio:"))
        self.comboBoxINe.setItemText(0, _translate("AdmiCNP", "1"))
        self.labelValor.setText(_translate("AdmiCNP", "Valor:"))
        self.botonCrearN.setText(_translate("AdmiCNP", "Crear"))
        self.botonCrearP.setText(_translate("AdmiCNP", "Crear"))
        self.botonVolver.setText(_translate("AdmiCNP", "Volver"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    AdmiCNP = QtWidgets.QWidget()
    ui = Ui_AdmiCNP()
    ui.setupUi(AdmiCNP)
    AdmiCNP.show()
    sys.exit(app.exec_())
