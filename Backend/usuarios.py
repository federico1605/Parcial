from Parcial.Backend.Producto import *
from Parcial.Backend.Pedido import *
from Parcial.Backend.Negocio import *


class Usuario:
    idusuario = 0
    nombre = ""
    telefono = ""
    rol = ""
    contrasena = ""
    idnegocio = 0

    def __init__(self, idusuario, nombre, telefono, rol, contrasena, idnegocio):
        self.nombre = nombre
        self.telefono = telefono
        self.rol = rol
        self.contrasena = contrasena
        self.idusuario = idusuario
        self.idnegocio = idnegocio


class AdminGlobal(Usuario):
    def __init__(self, nombre, telefono, rol, contrasena, idusuario, idnegocio):
        super().__init__(idusuario, nombre, telefono, rol, contrasena, idnegocio)
        self.nombre = nombre
        self.telefono = telefono
        self.rol = rol
        self.contrasena = contrasena
        self.idusuario = idusuario
        self.idnegocio = idnegocio

    def crearUsuario(conexion, nombre, telefono, contrasena, idnegocio, rol):
        try:
            with conexion.cursor() as cursor:
                consulta = "INSERT INTO usuario(nombre, telefono, contraseña, idnegocio, rol) VALUES (%s, %s, %s, %s, %s);"
                cursor.execute(consulta, (nombre, telefono, contrasena, idnegocio, rol))
            conexion.commit()
        except psycopg2.Error as e:
            print("Ocurrió un error al crear el usuario: ", e)
        finally:
            Database.desconectar(conexion)

    def consultarUsuarios(conexion):
        try:
            with conexion.cursor() as cursor:
                cursor.execute("SELECT * FROM usuario")
                usuarios = cursor.fetchall()
                return usuarios
        except psycopg2.Error as e:
            print("Ocurrió un error al consultar: ", e)
        finally:
            Database.desconectar(conexion)

    def consultarMeseros(conexion):
        try:
            with conexion.cursor() as cursor:
                cursor.execute("SELECT * FROM usuario where rol ='2'")
                usuarios = cursor.fetchall()
                return usuarios
        except psycopg2.Error as e:
            print("Ocurrió un error al consultar: ", e)
        finally:
            Database.desconectar(conexion)

    def consultarRol(conexion):
        try:
            with conexion.cursor() as cursor:
                cursor.execute("SELECT * FROM roles")
                roles = cursor.fetchall()
                return roles
        except psycopg2.Error as e:
            print("Ocurrió un error al consultar: ", e)
        finally:
            Database.desconectar(conexion)

    def actualizarUsuario(conexion, idusuario, contrasena):
        try:
            with conexion.cursor() as cursor:
                consulta = "UPDATE usuario SET contraseña = '" + str(contrasena) + "' WHERE idusuario = " + str(
                    idusuario)
                cursor.execute(consulta)
            conexion.commit()
            print("El registro se actualizo con exito")
        except psycopg2.Error as e:
            print("Ocurrió un error al editar: ", e)

    def actualizarUsuarioTe(conexion, idusuario, telefono):
        try:
            with conexion.cursor() as cursor:
                consulta = "UPDATE usuario SET telefono = '" + str(telefono) + "' WHERE idusuario = " + str(idusuario)
                cursor.execute(consulta)
            conexion.commit()
            print("El registro se actualizo con exito")
        except psycopg2.Error as e:
            print("Ocurrió un error al editar: ", e)

    def eliminarUsuario(conexion, idusuario):
        try:
            with conexion.cursor() as cursor:
                consulta = "DELETE FROM usuario WHERE idusuario =" + str(idusuario)
                cursor.execute(consulta)
                print("Usuario eliminado con exito")
            conexion.commit()
        except psycopg2.Error as e:
            print("Error eliminando: ", e)
        finally:
            Database.desconectar(conexion)

    def cierreCaja(conexion, idfactura, fecha, mesa, idmesero, total, numnegocio):
        try:
            # fecha = datetime
            mesa = int(input("Digite la mesa que hizo el pedido: "))
            idmesero = int(input("Digite el id del mesero que atendio: "))
            total = int(input("El total es: "))
            numnegocio = int(input("Cual es el negocio: "))
        except ValueError as e:
            print("los datos no son correctos: ", e)
        else:
            try:
                with conexion.cursor() as cursor:
                    consulta = "INSERT INTO factura(fecha, mesa, idmesero, total, numnegocio) VALUES (%s, %s, %s, %s, %s)"
                    cursor.execute(consulta, (fecha, mesa, idmesero, total, numnegocio))
                conexion.commt()
            except psycopg2.Error as e:
                print("Error al conectarse a la base de datos: ", e)
            finally:
                Database.desconectar(conexion)

    def producto(conexion, idproducto, nomproducto, idnegocio, valor):
        op = int(input("Que opcion de producto quiere hacer: "))
        if op >= 1 and op <= 3:
            if op == 1:
                Producto.anadirProducto(conexion, nomproducto, valor, idnegocio)
            elif op == 2:
                Producto.cambiarProducto(conexion, idproducto, nomproducto, valor)
            elif op == 3:
                Producto.eliminarProducto(conexion, idproducto)
        else:
            print("Ingresar datos validos.")

    def negocio(conexion, nombnegocio, idnegocio):
        op = int(input("Que opcion de negocio quiere hacer: "))
        if op >= 1 and op <= 3:
            if op == 1:
                Negocio.anadirNegocio(conexion, nombnegocio)
            elif op == 2:
                Negocio.actulizarNegocio(conexion, nombnegocio, idnegocio)
            elif op == 3:
                Negocio.eliminarNegocio(conexion, idnegocio)
        else:
            print("Ingresar datos validos.")


class Mesero(Usuario):
    estadopedido = ""
    cantidad = 0
    valor = 0
    idproducto = 0
    idmesero = 0
    idpedido = 0
    valortotal = 0

    def __init__(self, estadopedido, cantidad, valor, idproducto, idmesero, idpedido, valortotal):
        self.estadopedido = estadopedido
        self.cantidad = cantidad
        self.valor = valor
        self.idnegocio = idproducto
        self.idmesero = idmesero
        self.idpedido = idpedido
        self.valortotal = valortotal

    def crearPedido(conexion, mesero, mesa, estadopedido, valortotal, cantidad, negocio, producto):
            try:
                with conexion.cursor() as cursor:
                    pen = "INSERT INTO pedidos(mesa, estadopedido, valortotal, cantidad, idproducto, idnegocio, mesero) " \
                          "VALUES(%s, %s, %s, %s, %s, %s, %s);"
                    cursor.execute(pen, (mesa, estadopedido, valortotal, cantidad,  producto, negocio,mesero))
                    conexion.commit()
            except psycopg2.Error as e:
                print("Ocurrió un error al crear el pedido: ", e)
            finally:
                Database.desconectar(conexion)

    '''def pedidos(conexion, idproducto, valor, cantidad, idpedido):
        try:
            idpedido = int(input("Escriba el id del pedido: "))
            idproducto = int(input("Dijite el id del producto: "))
            cantidad = int(input("Dijite la cantidad del producto: "))
            valor = Producto.consultarProducto(conexion, idproducto, cantidad)
        except ValueError as e:
            print("Datos invalidos: ", e)
        else:
            try:
                with conexion.cursor() as cursor:
                    pen = "INSERT INTO pedidosiguales(idpedido, idproducto, cantidad, valor) VALUES(%s, %s, %s, %s);"
                    cursor.execute(pen, (idpedido, idproducto, cantidad, valor))
                    conexion.commit()
                    print(valor)
            except psycopg2.Error as e:
                print("Ocurrió un error al crear el pedido: ", e)
            finally:
                Database.desconectar(conexion)'''

    def modificarPedido(conexion, mesa, numpedido):
        try:
            numpedido = int(input("Ingrese el numero de pedido de la mesa: "))
            mesa = int(input("Ingrese la mesa que va modificar: "))
        except ValueError as e:
            print("Ingrese datos validos: ", e)
        else:
            try:
                with conexion.cursor() as cursor:
                    mpen = "UPDATE pedido SET mesa = '" + str(mesa) + "' where idpedido = " + str(numpedido)
                    cursor.execute(mpen)
                conexion.commit()
                print("El registro se actualizo con exito")
            except psycopg2.Error as e:
                print("Ocurrió un error al editar: ", e)
            finally:
                Database.desconectar(conexion)

    def eliminarPedido(conexion, idpedido):
        try:
            with conexion.cursor() as cursor:
                mpen = "DELETE FROM pedidos WHERE idPedido = " + str(idpedido)
                cursor.execute(mpen)
                conexion.commit()
                print("Pedido eliminado")
        except psycopg2.Error as e:
            print("Ocurrio un error al eliminar el pedido: ", e)
        finally:
            Database.desconectar(conexion)


class Cocinero(Usuario):
    negocio = ""

    def __init__(self, nombre, telefono, rol, orden, negocio, pedido):
        self.nombre = nombre
        self.telefono = telefono
        self.rol = rol
        self.negocio = negocio
        self.orden = orden
        self.pedido = pedido

    def recibirPedido(conexion, recibir, idpedido):
        try:
            with conexion.cursor() as cursor:
                consulta = "UPDATE producto SET estadopedido = '" + str(recibir) + \
                           "' WHERE idpedido = " + str(idpedido)
                cursor.execute(consulta)
                conexion.commit()
        except psycopg2.Error as e:
            print("Ocurrio un error al consular el pedido: ", e)
        finally:
            Database.desconectar(conexion)

    def notificarPedido(conexion, idpedido, recibir):
        try:
            with conexion.cursor() as cursor:
                consulta = "UPDATE pedido SET estadopedido = '" + str(recibir) + \
                           "' WHERE idpedido = " + str(idpedido)
                cursor.execute(consulta)
                conexion.commit()
        except psycopg2.Error as e:
            print("Ocurrio un error al consular el pedido: ", e)
        finally:
            Database.desconectar(conexion)


class Cajero(Usuario):
    fact = ""

    def __init__(self, nombre, telefono, rol, fact):
        self.nombre = nombre
        self.telefono = telefono
        self.rol = rol
        self.fact = fact
