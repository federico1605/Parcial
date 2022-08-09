from PyQt5 import QtCore, QtGui, QtWidgets
from Parcial.Backend.Pedido import Pedido
from Parcial.Controlador.MeseroControler import MeseroController
from Parcial.Backend.conexion import Database
conexion = Database


class Ui_Form(object):
    def __init__(self):
        # LISTADOS
        self.listadoId = Pedido.consultarPedido(conexion.conectar())

        self.controlador = MeseroController(self, self, self, self)

    def setupUi(self, Form):
        self.main = Form
        Form.setObjectName("Form")
        Form.resize(292, 222)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(49, 23, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(141, 84, 69, 20))
        self.comboBox.setObjectName("comboBox")
        # GENERAR COMBOBOX
        for pedido in self.listadoId:
            self.comboBox.addItem(str(pedido[0]))

        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(70, 84, 65, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.botoneliminar = QtWidgets.QPushButton(Form)
        self.botoneliminar.setGeometry(QtCore.QRect(70, 110, 141, 23))
        self.botoneliminar.setObjectName("botoneliminar")

        self.botonVolver = QtWidgets.QPushButton(Form)
        self.botonVolver.setGeometry(QtCore.QRect(180, 190, 75, 23))
        self.botonVolver.setObjectName("botonVolver")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        # -----------------------------------------EVENTOS----------------------------------------------------
        self.botonVolver.clicked.connect(self.accionVolver)
        self.botoneliminar.clicked.connect(self.accionEliminar)

    def accionVolver(self):
        self.main.close()

    def accionEliminar(self):
        combo = (self.comboBox.currentText())
        self.controlador.eliminarPedido(combo)


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Mesero"))
        self.label.setText(_translate("Form", "Eliminar Mesero."))
        self.label_2.setText(_translate("Form", "Id Pedido:"))
        self.botoneliminar.setText(_translate("Form", "Eliminar"))
        self.botonVolver.setText(_translate("Form", "Volver"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
