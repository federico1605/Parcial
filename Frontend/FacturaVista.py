import sys
import os
myDir = os.getcwd()
sys.path.append(myDir)

from PyQt5 import QtCore, QtGui, QtWidgets
from Parcial.Controlador.FacturaController import FacturaController

class Ui_Form(object):
    
    def __init__(self):
        self.facturaController = FacturaController(self)
    
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setFixedSize(754, 283)
        self.tableFactura = QtWidgets.QTableWidget(Form)
        self.tableFactura.setGeometry(QtCore.QRect(21, 21, 720, 192))
        self.tableFactura.setObjectName("tableFactura")
        self.tableFactura.setColumnCount(7)
        self.tableFactura.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableFactura.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableFactura.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableFactura.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableFactura.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableFactura.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableFactura.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableFactura.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableFactura.setHorizontalHeaderItem(6, item)
        
        self.actualizar()
        
        self.pushButtonActualizar = QtWidgets.QPushButton(Form)
        self.pushButtonActualizar.setGeometry(QtCore.QRect(330, 230, 75, 23))
        self.pushButtonActualizar.setObjectName("pushButtonActualizar")
        self.pushButtonActualizar.clicked.connect(self.actualizar)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def actualizar(self):
        self.facturaController.listaFactura()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Factura"))
        item = self.tableFactura.horizontalHeaderItem(0)
        item.setText(_translate("Form", "ID Factura"))
        item = self.tableFactura.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Fecha"))
        item = self.tableFactura.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Mesero"))
        item = self.tableFactura.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Negocio"))
        item = self.tableFactura.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Mesa"))
        item = self.tableFactura.horizontalHeaderItem(5)
        item.setText(_translate("Form", "Producto"))
        item = self.tableFactura.horizontalHeaderItem(6)
        item.setText(_translate("Form", "Total"))
        self.pushButtonActualizar.setText(_translate("Form", "Actualizar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
