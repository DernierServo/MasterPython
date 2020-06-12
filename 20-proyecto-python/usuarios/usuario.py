import datetime
import hashlib
#import usuarios.conexion as conexion
import conexion

conex = conexion.conectar()
database = conex[0]
cursor = conex[1]

class Usuario:

    def __init__(self, nombre, apellidos, email, password):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        self.password = password


    def registrar(self):
        fecha = datetime.datetime.now()
        # Cifrar contraseña:
        password_cifrado = hashlib.sha256()
        password_cifrado.update(self.password.encode('utf8'))   # encode para volver BytesStream
        sql = "INSERT INTO usuarios VALUES(null, %s, %s, %s, %s, %s)"
        usuario = (
            self.nombre, 
            self.apellidos, 
            self.email, 
            password_cifrado.hexdigest(), 
            fecha
        )
        try:
            cursor.execute(sql, usuario)
            database.commit()   #Guarda los datos en la BD
            response = [cursor.rowcount, self]
        except:
            response = [0, self]
        return response


    def identificar(self):
        sql = 'SELECT * FROM usuarios WHERE email = %s AND password = %s'

        # Cifrar contraseña:
        password_cifrado = hashlib.sha256()
        password_cifrado.update(self.password.encode('utf8'))   # encode para volver BytesStream

        usuario = (self.email, password_cifrado.hexdigest())

        cursor.execute(sql, usuario)    #(query, valoresTupla)
        response = cursor.fetchone()

        return response