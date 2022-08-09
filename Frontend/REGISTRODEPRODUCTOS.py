from PyQt5 import QtCore, QtGui, QtWidgets
from Parcial.Controlador.ConsultarControler import Consultar

class Ui_MainWindowR(object):
    def __init__(self):
        self.controler = Consultar(self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(40, 10, 731, 581))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tableUsuario = QtWidgets.QTableWidget(self.tab)
        self.tableUsuario.setGeometry(QtCore.QRect(50, 120, 601, 301))
        self.tableUsuario.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";")
        self.tableUsuario.setObjectName("tableUsuario")
        self.tableUsuario.setColumnCount(6)
        self.tableUsuario.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableUsuario.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableUsuario.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableUsuario.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableUsuario.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableUsuario.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableUsuario.setHorizontalHeaderItem(5, item)
        self.BotonBuscarUsuario = QtWidgets.QPushButton(self.tab)
        self.BotonBuscarUsuario.setGeometry(QtCore.QRect(530, 480, 121, 23))
        self.BotonBuscarUsuario.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";")
        self.BotonBuscarUsuario.setObjectName("BotonBuscarUsuario")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tableNegocio = QtWidgets.QTableWidget(self.tab_2)
        self.tableNegocio.setGeometry(QtCore.QRect(0, 140, 681, 311))
        self.tableNegocio.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";")
        self.tableNegocio.setObjectName("tableNegocio")
        self.tableNegocio.setColumnCount(2)
        self.tableNegocio.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableNegocio.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableNegocio.setHorizontalHeaderItem(1, item)
        self.label = QtWidgets.QLabel(self.tab_2)
        self.label.setGeometry(QtCore.QRect(20, 73, 71, 31))
        self.label.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.textoCodigo = QtWidgets.QLineEdit(self.tab_2)
        self.textoCodigo.setGeometry(QtCore.QRect(100, 80, 113, 20))
        self.textoCodigo.setObjectName("textoCodigo")
        self.BotonBuscarNegocio = QtWidgets.QPushButton(self.tab_2)
        self.BotonBuscarNegocio.setGeometry(QtCore.QRect(514, 510, 121, 23))
        self.BotonBuscarNegocio.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";")
        self.BotonBuscarNegocio.setObjectName("BotonBuscarNegocio")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tableProducto = QtWidgets.QTableWidget(self.tab_3)
        self.tableProducto.setGeometry(QtCore.QRect(5, 91, 671, 331))
        self.tableProducto.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";")
        self.tableProducto.setObjectName("tableProducto")
        self.tableProducto.setColumnCount(4)
        self.tableProducto.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableProducto.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableProducto.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableProducto.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableProducto.setHorizontalHeaderItem(3, item)
        self.BotonBuscarProducto = QtWidgets.QPushButton(self.tab_3)
        self.BotonBuscarProducto.setGeometry(QtCore.QRect(520, 480, 121, 23))
        self.BotonBuscarProducto.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";")
        self.BotonBuscarProducto.setObjectName("BotonBuscarProducto")
        self.tabWidget.addTab(self.tab_3, "")
        #MainWindow.setCentralWidget(self.centralwidget)

        self.controler.buscarUsuario()
        self.controler.buscarNegocio()
        self.controler.buscarProducto()

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.tableUsuario.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "idusuario"))
        item = self.tableUsuario.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "nombre"))
        item = self.tableUsuario.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "telefono"))
        item = self.tableUsuario.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "contraseña"))
        item = self.tableUsuario.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "idnegocio"))
        item = self.tableUsuario.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "rol"))
        self.BotonBuscarUsuario.setText(_translate("MainWindow", "BUSCAR"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Buscar Usuario"))
        item = self.tableNegocio.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", " nombnegocio"))
        item = self.tableNegocio.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "idnegocio"))
        self.label.setText(_translate("MainWindow", "Codigo"))
        self.BotonBuscarNegocio.setText(_translate("MainWindow", "BUSCAR"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Buscar Negocio"))
        item = self.tableProducto.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "nomproducto"))
        item = self.tableProducto.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "idproducto"))
        item = self.tableProducto.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "idnegocio"))
        item = self.tableProducto.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "valor"))
        self.BotonBuscarProducto.setText(_translate("MainWindow", "BUSCAR"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Buscar Producto"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindowR()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
