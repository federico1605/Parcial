from Parcial.Backend.conexion import *


class Negocio():
    nombnegocio = ""
    idnegocio = 0

    def __init__(self, nombnegocio, idnegocio):
        self.idnegocio = idnegocio
        self.nombnegocio = nombnegocio

    def anadirNegocio(conexion, nombnegocio):
        try:
            with conexion.cursor() as cursor:
                negon = "INSERT INTO negocio(nombnegocio) VALUES(%s);"
                cursor.execute(negon, (nombnegocio,))
                conexion.commit()
        except psycopg2.Error as e:
                print("Ocurrió un error al crear el negocio: ", e)
        finally:
            Database.desconectar(conexion)

    def actulizarNegocio(conexion, idnegocio, nombnnegocio):
        try:
            with conexion.cursor() as cursor:
                consulta = "UPDATE negocio SET nombnegocio = '" + str(nombnnegocio) + "' WHERE idnegocio = " + str(
                    idnegocio)
                cursor.execute(consulta)
                conexion.commit()
        except psycopg2.Error as e:
            print("Ocurrio un problema al actulizar la tabla: ", e)
        finally:
            Database.desconectar(conexion)

    def eliminarNegocio(conexion, idnegocio):
        try:
            with conexion.cursor() as cursor:
                consulta = "DELETE FROM negocio WHERE idnegocio =" + str(idnegocio)
                cursor.execute(consulta)
                conexion.commit()
        except psycopg2.Error as e:
            print("Ocurrio un error al eliminar la fila: ", e)
        finally:
            Database.desconectar(conexion)

    def comboBox(conexion):
        try:
            with conexion.cursor() as cursor:
                cursor.execute("SELECT * FROM negocio")
                negocio = cursor.fetchall()
                return negocio
        except psycopg2.Error as e:
            print("Ocurrió un error al consultar: ", e)
        finally:
            Database.desconectar(conexion)

    def consultaNegocio(conexion, idprodcuto):
        try:
            with conexion.cursor() as cursor:
                cursor.execute("SELECT producto.idnegocio from producto where idproducto ='" + str(idprodcuto) +"';")
                negocio = cursor.fetchone()
                return negocio
        except psycopg2.Error as e:
            print("Ocurrió un error al consultar: ", e)
        finally:
            Database.desconectar(conexion)

    def consultarN(conexion, nomproducto):
        try:
            with conexion.cursor() as cursor:
                cursor.execute("SELECT idnegocio from producto where nomproducto ='"+str(nomproducto)+"'")
                negocio = cursor.fetchone()
                res = int(''.join(map(str, negocio)))
                return res
        except psycopg2.Error as e:
            print("Ocurrió un error al consultar: ", e)
        finally:
            Database.desconectar(conexion)
