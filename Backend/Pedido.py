from Parcial.Backend.conexion import *
from datetime import datetime
fecha = datetime.today().strftime('%Y/%m/%d')

class Pedido():
    producto = ""
    negocio = ""
    mesero = 0
    mesa = 0

    def __init__(self, producto, negocio, mesa):
        self.negocio = negocio
        self.producto = producto
        self.mesa = mesa

    def consultarPedido(conexion):
        try:
            with conexion.cursor() as cursor:
                cursor.execute("SELECT * FROM pedidos")
                pedido = cursor.fetchall()
                return pedido
        except psycopg2.Error as e:
            print("Ocurrió un error al consultar: ", e)
        finally:
            Database.desconectar(conexion)

    def consultarPedidoCo(conexion):
        try:
            with conexion.cursor() as cursor:
                cursor.execute("SELECT (pedidos.Idpedido), (pedidos.mesa), (pedidos.estadopedido), (producto.nomproducto), (negocio.nombnegocio), (pedidos.cantidad) from pedidos inner join producto on pedidos.idproducto = producto.idproducto inner join negocio on pedidos.idnegocio = negocio.idnegocio;")
                pedido = cursor.fetchall()
                return pedido
        except psycopg2.Error as e:
            print("Ocurrió un error al consultar: ", e)
        finally:
            Database.desconectar(conexion)

    def consultarPedidoN(conexion, idpedido):
        try:
            with conexion.cursor() as cursor:
                cursor.execute("SELECT (Idpedido), (mesa), (estadopedido), (cantidad), (producto.nomproducto) FROM pedidos inner join producto on pedidos.idproducto = producto.idproducto where idpedido ='" + str(idpedido) + "';")
                pedido = cursor.fetchone()
                return pedido
        except psycopg2.Error as e:
            print("Ocurrió un error al consultar: ", e)
        finally:
            Database.desconectar(conexion)

    def actualizarPedido(conexion, idpedido, estadopedido):
        try:
            with conexion.cursor() as cursor:
                consulta = "UPDATE pedidos SET estadopedido = '" + str(estadopedido) + "' WHERE idpedido = " + str(idpedido)
                cursor.execute(consulta)
            conexion.commit()
            print("El registro se actualizo con exito")
        except psycopg2.Error as e:
            print("Ocurrió un error al editar: ", e)

    def consultarFacturar(conexion):
        try:
            with conexion.cursor() as cursor:
                cursor.execute("SELECT (pedidos.Idpedido), (usuario.nombre),(pedidos.mesa), (pedidos.estadopedido), (producto.nomproducto), (negocio.nombnegocio), (pedidos.cantidad) from pedidos inner join producto on pedidos.idproducto = producto.idproducto inner join negocio on pedidos.idnegocio = negocio.idnegocio inner join usuario on pedidos.mesero = usuario. idusuario;")
                pedido = cursor.fetchall()
                return pedido
        except psycopg2.Error as e:
            print("Ocurrió un error al consultar: ", e)
        finally:
            Database.desconectar(conexion)

    def anadirFactura(conexion, idpedido):
        try:
            with conexion.cursor() as cursor:
                cursor.execute("SELECT (pedidos.Idpedido), (usuario.nombre),(pedidos.mesa), (pedidos.estadopedido), (producto.nomproducto), (negocio.nombnegocio), (pedidos.cantidad) from pedidos inner join producto on pedidos.idproducto = producto.idproducto inner join negocio on pedidos.idnegocio = negocio.idnegocio inner join usuario on pedidos.mesero = usuario. idusuario where idpedido = "+str(idpedido)+";")
                pedido = cursor.fetchall()
                return pedido
        except psycopg2.Error as e:
            print("Ocurrió un error al consultar: ", e)
        finally:
            Database.desconectar(conexion)

    def valorTotal(conexion, producto):
        try:
            with conexion.cursor() as cursor:
                cursor.execute("SELECT valor from producto where nomproducto ='"+str(producto)+"'")
                pedido = cursor.fetchone()
                res = int(''.join(map(str, pedido)))
                return res
        except psycopg2.Error as e:
            print("Ocurrió un error al consultar: ", e)
        finally:
            Database.desconectar(conexion)
