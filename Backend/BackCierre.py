from datetime import datetime
from Parcial.Backend.conexion import *
conexion = Database
fecha = datetime.today().strftime('%Y/%m/%d')

class CierreTotal:

    def cierreMesas(conexion):
        try:
            with conexion.cursor() as cursor:
                cursor.execute("SELECT mesa, valortotal*cantidad FROM factura WHERE fecha = '" + str(fecha) + "';")
                Mesa = cursor.fetchall()
                if Mesa:
                    return Mesa
        except psycopg2.Error as e:
            print("ocurrio un error", e)
        finally:
            Database.desconectar(conexion)

    def cierreMeseros(conexion):
        try:
            with conexion.cursor() as cursor:
                cursor.execute("SELECT usuario.nombre, factura.valortotal*factura.cantidad FROM factura INNER JOIN usuario ON factura.idmesero = usuario.idusuario WHERE factura.estadopedido = 'Listo' AND fecha = '" + str(fecha) + "';")
                ventasNegocios = cursor.fetchall()
                if ventasNegocios:
                    return ventasNegocios
        except psycopg2.Error as e:
            print("ocurrio un error", e)
        finally:
            Database.desconectar(conexion)

    def cierreNegocios(conexion):
        try:
            with conexion.cursor() as cursor:
                cursor.execute("SELECT negocio.nombnegocio, factura.valortotal*factura.cantidad FROM factura INNER JOIN negocio ON factura.idnegocio = negocio.idnegocio WHERE factura.estadopedido = 'Listo' AND fecha = '" + str(fecha) + "';")
                ventasNegocios = cursor.fetchall()
                if ventasNegocios:
                    return ventasNegocios
        except psycopg2.Error as e:
            print("ocurrio un error", e)
        finally:
            Database.desconectar(conexion)