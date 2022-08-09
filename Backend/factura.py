import psycopg2
from Parcial.Backend.conexion import Database
from datetime import datetime
fecha = datetime.today().strftime('%Y/%m/%d')

class Factura:
    
    def listaFactura(conexion):
        try:
            with conexion.cursor() as cursor:
                cursor.execute("SELECT factura.idfactura, factura.fecha, usuario.nombre, negocio.nombnegocio, factura.mesa, factura.producto, factura.valortotal FROM factura INNER JOIN usuario ON factura.idmesero = usuario.idusuario INNER JOIN negocio ON factura.idnegocio = negocio.idnegocio;")
                listaFactura = cursor.fetchall()
                if listaFactura:
                    return listaFactura
        except psycopg2.Error as e:
            print("Error",e)
        finally:
            Database.desconectar(conexion)

    def generarFactura(conexion, idmesero, idnegocio, mesa, producto, valortotal, cantidad):
        try:
            with conexion.cursor() as cursor:
                factura =("INSERT INTO factura (fecha, idmesero, idnegocio, mesa, producto, valortotal, cantidad) VALUES (%s, %s, %s, %s, %s, %s, %s)")
                cursor.execute(factura, (fecha, idmesero, idnegocio, mesa, producto, valortotal, cantidad))
                conexion.commit()
        except psycopg2.Error as e:
            print("Ocurrió un error al crear la factura: ", e)
        finally:
            Database.desconectar(conexion)