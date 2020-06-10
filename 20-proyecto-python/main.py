"""
Proyecto Python y Mysql:
    - Abrir asistente
    - Login o registro
    - Si elegimos registro, generará un usuario en la bbdd
    - Si elegimos logi, identifica al usuario y nos preguntará
    - Generar nota, mostrar notas, borrarlas.
"""
from usuarios import acciones

print("""
Acciones disponibles:
    - [R]egistro
    - [L]ogin
""")

accion = acciones.Acciones()
tipo_accion = input('¿Qué desea hacer?: ')

if tipo_accion.upper() == 'R':
    accion.registro()
    
elif tipo_accion.upper() == 'L':
    accion.login() 
    


