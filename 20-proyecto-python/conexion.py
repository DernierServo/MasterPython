import mysql.connector

def conectar():
    database = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        passwd = 'Admin.123',
        database = 'master_python',
        port = 3306
    )
    # Sirve para hacer las consultas (queries)
    cursor = database.cursor(buffered=True)

    return [database, cursor]