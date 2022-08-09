from Parcial.Backend.conexion import *


class Login:
    def obtenerUsuario(conexion, usuario, contrasena):
        try:
            with conexion.cursor() as cursor:
                consulta = "select (nombre,contraseña) from usuario where" \
                           " nombre = '" +str(usuario) + "' and contraseña = "+str(contrasena)
                cursor.execute(consulta, (usuario, contrasena))
                user = cursor.fetchall()
                return user
        except psycopg2.Error as e:
            print("Ocurrió un error al cosultar la base de datos: ", e)
        finally:
            Database.desconectar(conexion)
