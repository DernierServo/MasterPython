
import sqlite3

# CONEXIÓN
conexion = sqlite3.connect('prubas.db')

# GENERAR CURSOR: Ayuda a ejecutar una consulta
cursor = conexion.cursor()

# GENERAR TABLAS

cursor.execute("""
    CREATE TABLE IF NOT EXISTS productos( 
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo VARCHAR(255),
        descripcion text,
        precio int(255)
    )
""")


# Guardar cambios
conexion.commit()

# INSERTAR DATOS
'''
cursor.execute(
    """
    INSERT INTO productos VALUES ( +
        null,
        'Primer producto',
        'Descripción del primer producto',
        550
    )
    """
)
conexion.commit()
'''

# INSERSIÓN MÚLTIPLE
ls_productos = [
    ('ordenador portatil', 'MSI GF65', 800),
    ('Celular', 'Xiaomi Redmi note 8 Pro', 200),
    ('Bicicleta', 'Monark todo terreno', 300)
]
#cursor.executemany('INSERT INTO productos VALUES (null, ?, ?, ?)', ls_productos)
#conexion.commit()

#cursor.execute('UPDATE productos SET precio = 240 WHERE precio = 300')
#conexion.commit()

# LISTAR DATOS
cursor.execute('SELECT * FROM productos WHERE precio > 250;')
productos = cursor.fetchall()
for producto in productos:
    print('#'*50)
    print(f'ID: {producto[0]}')
    print(f'Título: {producto[1]}')
    print(f'Descripción: {producto[2]}')
    print(f'Precio: {producto[3]}')
    print('\n')



# BORRAR REGISTROS
#cursor.execute("DELETE FROM productos;")
#conexion.commit()

# CERRAR CONEXIÓN
conexion.close()