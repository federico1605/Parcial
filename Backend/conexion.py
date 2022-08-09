import psycopg2

class Database:
    user = "postgres"
    password = "abcd1234"
    host = "poogrupo01.cqozrgcn8atr.us-east-1.rds.amazonaws.com"

    def conectar():
        try:
            credenciales = {
                "dbname": "grupo03",
                "user": "postgres",
                "password": "abcd1234",
                "host": "poogrupo01.cqozrgcn8atr.us-east-1.rds.amazonaws.com",
                "port": 5432
            }
            conexion = psycopg2.connect(**credenciales)
            if conexion:
                print("Conexión exitosa")
            return conexion
        except psycopg2.Error as e:
            print("Ocurrió un error al conectar a PostgreSQL: ", e)

    def desconectar(conexion):
        conexion.close()
