from Parcial.Backend.conexion import *

class Producto:
    nomProdcuto = ""
    idproducto = 0
    idnegocio = 0
    valor = 0

    def __init__(self, nomProdcuto, idproducto,idnegocio, valor):
        self.nomProdcuto = nomProdcuto
        self.idproducto = idproducto
        self.idnegocio = idnegocio
        self.valor = valor

    def anadirProducto(conexion, nomproducto, idnegocio, valor):
        try:
            with conexion.cursor() as cursor:
                product = "INSERT INTO producto( nomproducto, idnegocio, valor) VALUES(%s, %s, %s);"
                cursor.execute(product, (nomproducto, idnegocio, valor))
                conexion.commit()
        except psycopg2.Error as e:
            print("Ocurrió un error al crear el prducto: ", e)
        finally:
                Database.desconectar(conexion)

    def cambiarProducto(conexion, idproducto, nomproducto):
        try:
            with conexion.cursor() as cursor:
                consulta = "UPDATE producto SET nomproducto = '" + str(nomproducto) + "' WHERE idproducto = " \
                        + str(idproducto)
                cursor.execute(consulta)
                conexion.commit()
                print("El registro se actualizo con exito")
        except psycopg2.Error as e:
            print("Ocurrió un error al editar: ", e)
        finally:
            Database.desconectar(conexion)

    def cambiarProductoPre(conexion, idproducto, valor):
        try:
            with conexion.cursor() as cursor:
                consulta = "UPDATE producto SET valor = '" + str(valor) + "' WHERE idproducto = " \
                        + str(idproducto)
                cursor.execute(consulta)
                conexion.commit()
                print("El registro se actualizo con exito")
        except psycopg2.Error as e:
            print("Ocurrió un error al editar: ", e)
        finally:
            Database.desconectar(conexion)

    def eliminarProducto(conexion, idproducto):
            try:
                with conexion.cursor() as cursor:
                    consulta = "DELETE FROM producto WHERE idproducto =" + str(idproducto)
                    cursor.execute(consulta)
                    print("Producto eliminado con exito")
                conexion.commit()
            except psycopg2.Error as e:
                print("Error eliminando: ", e)
            finally:
                Database.desconectar(conexion)

    def consultarProducto(conexion, idproducto, cantidad):
        try:
            with conexion.cursor() as cursor:
                consulta = "SELECT * FROM producto WHERE idproducto =" + str(idproducto)
                cursor.execute(consulta)
                producto = cursor.fetchone()
                if producto:
                    print(producto)
                    print("El producto cuesta: ", producto[3])
                    return producto[3] * cantidad
                else:
                    return "0"
        except psycopg2.Error as e:
            print("Error al conectar con la base de datos: ", e)
            return "0"
        finally:
            Database.desconectar(conexion)

    def comboBox(conexion):
        try:
            with conexion.cursor() as cursor:
                cursor.execute("SELECT * FROM producto")
                productos = cursor.fetchall()
                return productos
        except psycopg2.Error as e:
            print("Ocurrió un error al consultar: ", e)
        finally:
            Database.desconectar(conexion)