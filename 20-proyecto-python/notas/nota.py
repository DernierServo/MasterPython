import usuarios.conexion as conexion

conex = conexion.conectar()
database = conex[0]
cursor = conex[1]

class Nota:

    def __init__(self, usuario_id, titulo='', descripcion=''):
        self.usuario_id = usuario_id
        self.titulo = titulo
        self.descripcion = descripcion


    def guardar(self):
        sql = "INSERT INTO notas VALUES(null, %s, %s, %s, NOW())"
        nota = (self.usuario_id, self.titulo, self.descripcion)

        cursor.execute(sql, nota)
        database.commit()

        return [cursor.rowcount, self]


    def listar(self):
        sql = f'SELECT * FROM notas WHERE usuario_id = {self.usuario_id}'

        cursor.execute(sql)
        response = cursor.fetchall()

        return response