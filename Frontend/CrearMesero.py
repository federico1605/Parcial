from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets
from Parcial.Backend.usuarios import AdminGlobal
from Parcial.Backend.Producto import Producto
from Parcial.Controlador.MeseroControler import MeseroController
from Parcial.Backend.conexion import Database
conexion = Database


class Ui_CrearMesero(object):
    def __init__(self):
        self.controlador = MeseroController(self, self, self, self)

        # GENERAR LISTADOS
        self.listadoMesero = AdminGlobal.consultarMeseros(conexion.conectar())
        self.listadoProductos = Producto.comboBox(conexion.conectar())

    def setupUi(self, CrearMesero):
        self.main = CrearMesero
        CrearMesero.setObjectName("CrearMesero")
        CrearMesero.resize(393, 345)
        self.labelTitulo = QtWidgets.QLabel(CrearMesero)
        self.labelTitulo.setGeometry(QtCore.QRect(130, 20, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.labelTitulo.setFont(font)
        self.labelTitulo.setObjectName("labelTitulo")
        self.labelIdP = QtWidgets.QLabel(CrearMesero)
        self.labelIdP.setGeometry(QtCore.QRect(81, 85, 65, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.labelIdP.setFont(font)
        self.labelIdP.setObjectName("labelIdP")
        self.labelMensajeI = QtWidgets.QLabel(CrearMesero)
        self.labelMensajeI.setGeometry(QtCore.QRect(183, 85, 140, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.labelMensajeI.setFont(font)
        self.labelMensajeI.setObjectName("labelMensajeI")
        self.labelIdM = QtWidgets.QLabel(CrearMesero)
        self.labelIdM.setGeometry(QtCore.QRect(81, 107, 70, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.labelIdM.setFont(font)
        self.labelIdM.setObjectName("labelIdM")
        self.labelEstado = QtWidgets.QLabel(CrearMesero)
        self.labelEstado.setGeometry(QtCore.QRect(81, 133, 96, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.labelEstado.setFont(font)
        self.labelEstado.setObjectName("labelEstado")
        self.labelMesaheE = QtWidgets.QLabel(CrearMesero)
        self.labelMesaheE.setGeometry(QtCore.QRect(183, 133, 140, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.labelMesaheE.setFont(font)
        self.labelMesaheE.setObjectName("labelMesaheE")
        self.labelProducto = QtWidgets.QLabel(CrearMesero)
        self.labelProducto.setGeometry(QtCore.QRect(81, 155, 64, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.labelProducto.setFont(font)
        self.labelProducto.setObjectName("labelProducto")
        self.labelIdN = QtWidgets.QLabel(CrearMesero)
        self.labelIdN.setGeometry(QtCore.QRect(81, 181, 72, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.labelIdN.setFont(font)
        self.labelIdN.setObjectName("labelIdN")
        self.labelMeIdN = QtWidgets.QLabel(CrearMesero)
        self.labelMeIdN.setGeometry(QtCore.QRect(159, 181, 140, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.labelMeIdN.setFont(font)
        self.labelMeIdN.setObjectName("labelMeIdN")
        self.label = QtWidgets.QLabel(CrearMesero)
        self.label.setGeometry(QtCore.QRect(81, 203, 62, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.lineEditCantidad = QtWidgets.QLineEdit(CrearMesero)
        self.lineEditCantidad.setGeometry(QtCore.QRect(159, 203, 161, 20))
        self.lineEditCantidad.setObjectName("lineEditCantidad")


        self.comboBoxIdMesero = QtWidgets.QComboBox(CrearMesero)
        self.comboBoxIdMesero.setGeometry(QtCore.QRect(159, 107, 161, 20))
        self.comboBoxIdMesero.setObjectName("comboBoxIdMesero")
        # ID MESERO
        self.comboBoxIdMesero = QtWidgets.QComboBox(CrearMesero)
        self.comboBoxIdMesero.setGeometry(QtCore.QRect(169, 106, 151, 20))
        self.comboBoxIdMesero.setObjectName("comboBoxIdMesero")
        # GENERAR COMBOBOX
        for mesero in self.listadoMesero:
            self.comboBoxIdMesero.addItem(str(mesero[0]))

        self.comboBoxProductos = QtWidgets.QComboBox(CrearMesero)
        self.comboBoxProductos.setGeometry(QtCore.QRect(159, 155, 161, 20))
        self.comboBoxProductos.setObjectName("comboBoxProductos")
        # NOMBRES PRODUCTOS
        self.comboBoxProductos = QtWidgets.QComboBox(CrearMesero)
        self.comboBoxProductos.setGeometry(QtCore.QRect(169, 154, 151, 20))
        self.comboBoxProductos.setObjectName("comboBoxProductos")
        # GENERAR COMBOBOX
        for producto in self.listadoProductos:
            self.comboBoxProductos.addItem(str(producto[1]))

        self.botonCrear = QtWidgets.QPushButton(CrearMesero)
        self.botonCrear.setGeometry(QtCore.QRect(80, 260, 91, 23))
        self.botonCrear.setObjectName("botonCrear")

        self.botonVolver = QtWidgets.QPushButton(CrearMesero)
        self.botonVolver.setGeometry(QtCore.QRect(290, 300, 75, 23))
        self.botonVolver.setObjectName("botonVolver")

        self.label_2 = QtWidgets.QLabel(CrearMesero)
        self.label_2.setGeometry(QtCore.QRect(80, 230, 39, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.lineEditMesa = QtWidgets.QLineEdit(CrearMesero)
        self.lineEditMesa.setGeometry(QtCore.QRect(160, 230, 161, 20))
        self.lineEditMesa.setObjectName("lineEditMesa")

        self.retranslateUi(CrearMesero)
        QtCore.QMetaObject.connectSlotsByName(CrearMesero)

        # -----------------------------------------------EVENTOS--------------------------------------------
        self.botonVolver.clicked.connect(self.accionVolver)
        self.botonCrear.clicked.connect(self.accionCrear)

    def accionVolver(self):
        self.main.close()

    def accionCrear(self):
        comboIdM = (self.comboBoxIdMesero.currentText())
        comboPro = int(self.comboBoxProductos.currentText())
        cantidad = (self.lineEditCantidad.text())
        mesa = (self.lineEditMesa.text())
        self.controlador.crearPedido(comboIdM, mesa, comboPro, cantidad)

    def retranslateUi(self, CrearMesero):
        _translate = QtCore.QCoreApplication.translate
        CrearMesero.setWindowTitle(_translate("CrearMesero", "Mesero"))
        self.labelTitulo.setText(_translate("CrearMesero", "Crear Pedido"))
        self.labelIdP.setText(_translate("CrearMesero", "Id Pedido:"))
        self.labelMensajeI.setText(_translate("CrearMesero", "Lo ingresa el sistema."))
        self.labelIdM.setText(_translate("CrearMesero", "Id Mesero:"))
        self.labelEstado.setText(_translate("CrearMesero", "Estado Pedido:"))
        self.labelMesaheE.setText(_translate("CrearMesero", "Lo ingresa el sistema."))
        self.labelProducto.setText(_translate("CrearMesero", "Producto:"))
        self.labelIdN.setText(_translate("CrearMesero", "Id Negocio:"))
        self.labelMeIdN.setText(_translate("CrearMesero", "Lo ingresa el sistema."))
        self.label.setText(_translate("CrearMesero", "Cantidad:"))
        self.botonCrear.setText(_translate("CrearMesero", "Crear"))
        self.botonVolver.setText(_translate("CrearMesero", "Volver"))
        self.label_2.setText(_translate("CrearMesero", "Mesa:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CrearMesero = QtWidgets.QWidget()
    ui = Ui_CrearMesero()
    ui.setupUi(CrearMesero)
    CrearMesero.show()
    sys.exit(app.exec_())
