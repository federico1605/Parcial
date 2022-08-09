from PyQt5 import QtCore, QtGui, QtWidgets
from Parcial.Controlador.UpdateAdmin import ActualizarAdmin
from Parcial.Backend.Producto import Producto
from Parcial.Backend.conexion import Database
conexion = Database

class Ui_AdminUPro(object):
    def __init__(self):
        self.controlador = ActualizarAdmin(self)

        # GENERAR COMBOBOX
        self.listadoId = Producto.comboBox(conexion.conectar())

    def setupUi(self, AdminUPro):
        self.main = AdminUPro
        AdminUPro.setObjectName("AdminUPro")
        AdminUPro.setFixedSize(536, 255)
        self.labelTitulo = QtWidgets.QLabel(AdminUPro)
        self.labelTitulo.setGeometry(QtCore.QRect(120, 20, 291, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.labelTitulo.setFont(font)
        self.labelTitulo.setObjectName("labelTitulo")
        self.labelAcNombre = QtWidgets.QLabel(AdminUPro)
        self.labelAcNombre.setGeometry(QtCore.QRect(12, 72, 152, 19))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.labelAcNombre.setFont(font)
        self.labelAcNombre.setObjectName("labelAcNombre")
        self.labelAcPrecio = QtWidgets.QLabel(AdminUPro)
        self.labelAcPrecio.setGeometry(QtCore.QRect(302, 63, 139, 19))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.labelAcPrecio.setFont(font)
        self.labelAcPrecio.setObjectName("labelAcPrecio")
        self.labelNombre = QtWidgets.QLabel(AdminUPro)
        self.labelNombre.setGeometry(QtCore.QRect(12, 97, 54, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.labelNombre.setFont(font)
        self.labelNombre.setObjectName("labelNombre")
        self.labelIProducto = QtWidgets.QLabel(AdminUPro)
        self.labelIProducto.setGeometry(QtCore.QRect(12, 123, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.labelIProducto.setFont(font)
        self.labelIProducto.setObjectName("labelIProducto")

        # NOMBRE PRODUCTO
        self.lineEditNombreP = QtWidgets.QLineEdit(AdminUPro)
        self.lineEditNombreP.setGeometry(QtCore.QRect(99, 97, 131, 20))
        self.lineEditNombreP.setObjectName("lineEditNombreP")

        # COMBOBOX ID USUARIO NOMBRE
        self.comboBoxIdP = QtWidgets.QComboBox(AdminUPro)
        self.comboBoxIdP.setGeometry(QtCore.QRect(99, 123, 131, 20))
        self.comboBoxIdP.setObjectName("comboBoxIdP")

        # GENERAR LISTA
        for idU in self.listadoId:
            self.comboBoxIdP.addItem(str(idU[1]))

        self.botonNombre = QtWidgets.QPushButton(AdminUPro)
        self.botonNombre.setGeometry(QtCore.QRect(12, 149, 221, 23))
        self.botonNombre.setObjectName("botonNombre")
        self.labelValor = QtWidgets.QLabel(AdminUPro)
        self.labelValor.setGeometry(QtCore.QRect(302, 88, 39, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.labelValor.setFont(font)
        self.labelValor.setObjectName("labelValor")

        # VALOR PRODUCTO
        self.lineEditValorP = QtWidgets.QLineEdit(AdminUPro)
        self.lineEditValorP.setGeometry(QtCore.QRect(389, 88, 131, 20))
        self.lineEditValorP.setObjectName("lineEditValorP")

        self.labelIdProducto2 = QtWidgets.QLabel(AdminUPro)
        self.labelIdProducto2.setGeometry(QtCore.QRect(302, 114, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.labelIdProducto2.setFont(font)
        self.labelIdProducto2.setObjectName("labelIdProducto2")

        # COMBOBOX ID USUARIO PRECIO
        self.comboBoxPrecio = QtWidgets.QComboBox(AdminUPro)
        self.comboBoxPrecio.setGeometry(QtCore.QRect(389, 114, 131, 20))
        self.comboBoxPrecio.setObjectName("comboBoxPrecio")

        # GENERAR LISTA
        for idU in self.listadoId:
            self.comboBoxPrecio.addItem(str(idU[1]))


        self.botonValorP = QtWidgets.QPushButton(AdminUPro)
        self.botonValorP.setGeometry(QtCore.QRect(302, 140, 221, 23))
        self.botonValorP.setObjectName("botonValorP")
        self.botonVolver = QtWidgets.QPushButton(AdminUPro)
        self.botonVolver.setGeometry(QtCore.QRect(450, 210, 75, 23))
        self.botonVolver.setObjectName("botonVolver")

        self.retranslateUi(AdminUPro)
        QtCore.QMetaObject.connectSlotsByName(AdminUPro)

        # ------------------------------------------EVENTOS-------------------------------------------------------------
        self.botonNombre.clicked.connect(self.accionUpdateN)
        self.botonValorP.clicked.connect(self.accionUpdateP)
        self.botonVolver.clicked.connect(self.accionVolver)

    def accionUpdateN(self):
        nomProducto = (self.lineEditNombreP.text())
        idproducto =(self.comboBoxIdP.currentText())
        self.controlador.UpdateProP(nomProducto, idproducto)

    def accionUpdateP(self):
        precio = (self.lineEditValorP.text())
        idproducto = 10
        self.controlador.updateProPre(precio, idproducto)

    def accionVolver(self):
        print("Cerrar Ventana")
        self.main.close()

    def retranslateUi(self, AdminUPro):
        _translate = QtCore.QCoreApplication.translate
        AdminUPro.setWindowTitle(_translate("AdminUPro", "Form"))
        self.labelTitulo.setText(_translate("AdminUPro", "ADMIN UPDATE PRODUCTO"))
        self.labelAcNombre.setText(_translate("AdminUPro", "Actualizar Nombre"))
        self.labelAcPrecio.setText(_translate("AdminUPro", "Actualizar Precio"))
        self.labelNombre.setText(_translate("AdminUPro", "Nombre:"))
        self.labelIProducto.setText(_translate("AdminUPro", "Id Producto:"))
        self.botonNombre.setText(_translate("AdminUPro", "Actualizar"))
        self.labelValor.setText(_translate("AdminUPro", "Valor:"))
        self.labelIdProducto2.setText(_translate("AdminUPro", "Id Producto:"))
        self.botonValorP.setText(_translate("AdminUPro", "Actualizar"))
        self.botonVolver.setText(_translate("AdminUPro", "Volver"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AdminUPro = QtWidgets.QWidget()
    ui = Ui_AdminUPro()
    ui.setupUi(AdminUPro)
    AdminUPro.show()
    sys.exit(app.exec_())
