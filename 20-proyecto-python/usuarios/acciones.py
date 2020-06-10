import usuarios.usuario as modelo

class Acciones:

    def registro(self):
        print('\n','- '*30, '\nREGISTRO:', '\n')

        nombre = input('\t1. Nombre: ')
        apellidos = input('\t2. Apellidos: ')
        email = input('\t3. Email: ')
        password = input('\t4. Contraseña: ')

        usuario = modelo.Usuario(nombre, apellidos, email, password)
        registro = usuario.registrar()

        if registro[0] >= 1:
            print('\n', '- '*30, f'\nEN HORA BUENA! \n\t{registro[1].nombre} te has registrado con el email {registro[1].email}')
        else:
            print('\n', '- '*30, '\nERROR! No te has registrado correctamente!')

    def login(self):
        print('Identíficate por favor', '\n','- '*30)
        email = input('Introduce tu email: ')
        password = input('Introduce tu contraseña: ')

    