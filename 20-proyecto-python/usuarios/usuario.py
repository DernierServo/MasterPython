import mysql.connector
import datetime
import hashlib

database = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Admin.123',
    database = 'master_python',
    port = 3306
)

# Sirve para hacer las consultas (queries)
cursor = database.cursor(buffered=True)

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
        return self.nombre
