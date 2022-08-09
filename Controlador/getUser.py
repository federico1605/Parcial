from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QComboBox, QApplication, QLabel, QMainWindow, QDialog
from PyQt5 import uic, QtWidgets
from Parcial.Backend.usuarios import *
from Parcial.Frontend.iniciococinero import Ui_cocinero
from Parcial.Frontend.InicioMesero import Ui_iniciomesero
from Parcial.Frontend.FacturaVista import Ui_Form


class VentanaPrincipal():
    def __init__(self, MainWindow):
        self.principal = MainWindow
        self.concinero = Ui_cocinero
        self.mesero = Ui_iniciomesero
        self.cajero = Ui_Form


    # Enviar datos al comobox
    '''def consultarUser(conexion):
        try:
            with conexion.cursor() as cursor:
                cursor.execute("SELECT * FROM roles")
                usuarios = cursor.fetchall()
                if usuarios:
                    return usuarios
        except psycopg2.Error as e:
            print("Ocurrió un error al consultar: ", e)
        finally:
            Database.desconectar(conexion)'''

    def controladorLogin(self, usu, contra, conexion, Ui_errorUsuario, Ui_Admin):
        try:
            with conexion.cursor() as cursor:
                cursor.execute("SELECT rol from usuario  where nombre ='" + str(usu) + "' and contraseña ='" + str(contra)+"'")
                user = cursor.fetchone()
                print(user)
                if user:
                    if user[0] == 1:
                        self.principal.Ventana = QtWidgets.QMainWindow()
                        self.principal.ui = Ui_Admin()
                        self.principal.ui.setupUi(self.principal.Ventana)
                        self.principal.Ventana.show()
                    elif user[0] == 2:
                        self.principal.Ventana = QtWidgets.QMainWindow()
                        self.principal.ui = Ui_iniciomesero()
                        self.principal.ui.setupUi(self.principal.Ventana)
                        self.principal.Ventana.show()
                    elif user[0] == 3:
                        self.mesero.Ventana = QtWidgets.QMainWindow()
                        self.mesero.ui = Ui_cocinero()
                        self.mesero.ui.setupUi(self.mesero.Ventana)
                        self.mesero.Ventana.show()
                    elif user[0] == 4:
                        self.cajero.Ventana = QtWidgets.QMainWindow()
                        self.cajero.ui = Ui_Form()
                        self.cajero.ui.setupUi(self.cajero.Ventana)
                        self.cajero.Ventana.show()
                else:
                    self.principal.Ventana = QtWidgets.QMainWindow()
                    self.principal.ui = Ui_errorUsuario()
                    self.principal.ui.setupUi(self.principal.Ventana)
                    self.principal.Ventana.show()

        except psycopg2.Error as e:
            print("Ocurrió un error al consultar: ", e)
        finally:
            Database.desconectar(conexion)
