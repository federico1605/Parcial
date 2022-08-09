from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets
from Parcial.Backend.usuarios import AdminGlobal
from Parcial.Backend.Producto import Producto
from Parcial.Controlador.MeseroControler import MeseroController
from Parcial.Backend.conexion import Database
conexion = Database

class Ui_Form(object):
    def __init__(self):
        self.controlador = MeseroController(self, self, self, self)

        # LISTADO DE ROLES
        self.listadoRol = AdminGlobal.consultarMeseros(conexion.conectar())
        # LISTADO DE PRODUCTOS
        self.listadoProducto = Producto.comboBox(conexion.conectar())

    def setupUi(self, Form):
        self.main = Form
        Form.setObjectName("Form")
        Form.resize(397, 319)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(130, 20, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.botonVolver = QtWidgets.QPushButton(Form)
        self.botonVolver.setGeometry(QtCore.QRect(300, 280, 75, 23))
        self.botonVolver.setObjectName("botonVolver")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(80, 51, 256, 204))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 1, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 2, 0, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.widget)
        self.comboBox.setObjectName("comboBox")

        # GENERAR LISTADO DE ROLES
        for mesero in self.listadoRol:
            self.comboBox.addItem(str(mesero[0]))

        self.gridLayout.addWidget(self.comboBox, 2, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 3, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 3, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 4, 0, 1, 1)
        self.comboBoxProducto = QtWidgets.QComboBox(self.widget)
        self.comboBoxProducto.setObjectName("comboBoxProducto")

        # GENERAR LISTADO DE PRODUCTO
        for producto in self.listadoProducto:
            self.comboBoxProducto.addItem(str(producto[0]))

        self.gridLayout.addWidget(self.comboBoxProducto, 4, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 5, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 5, 1, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 6, 0, 1, 1)
        self.lineCantidad = QtWidgets.QLineEdit(self.widget)
        self.lineCantidad.setObjectName("lineCantidad")
        self.gridLayout.addWidget(self.lineCantidad, 6, 1, 1, 1)
        self.botonCrear = QtWidgets.QPushButton(self.widget)
        self.botonCrear.setObjectName("botonCrear")
        self.gridLayout.addWidget(self.botonCrear, 7, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        # --------------------------------------------Eventos-----------------------------------------
        self.botonVolver.clicked.connect(self.accionVolver)
        self.botonCrear.clicked.connect(self.accionCrear)

    def accionCrear(self):
        combo = (self.comboBox.currentText())
        comboP = (self.comboBoxProducto.currentText())
        mesa = (self.lineEdit.text())
        cantidad = int(self.lineCantidad.text())
        self.controlador.crearFactura(combo, comboP, mesa, cantidad)

    def accionVolver(self):
        self.main.close()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Crear Factura"))
        self.botonVolver.setText(_translate("Form", "Volver"))
        self.label_2.setText(_translate("Form", "Id factura: "))
        self.label_3.setText(_translate("Form", "Ingresa el sistema."))
        self.label_4.setText(_translate("Form", "Fecha:"))
        self.label_5.setText(_translate("Form", "Ingresa el sistema."))
        self.label_6.setText(_translate("Form", "Id Mesero:"))
        self.label_7.setText(_translate("Form", "Mesa:"))
        self.label_10.setText(_translate("Form", "Producto:"))
        self.label_8.setText(_translate("Form", "Valor total:"))
        self.label_9.setText(_translate("Form", "Ingresa el sistema."))
        self.label_11.setText(_translate("Form", "Cantidad"))
        self.botonCrear.setText(_translate("Form", "Crear"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
