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
        print('\n','- '*30, '\nLOGIN:', '\n')
        try:
            email = input('\t1. Email: ')
            password = input('\t2. Contraseña: ')

            usuario = modelo.Usuario('', '', email, password)
            login = usuario.identificar()

            if email == login[3]:
                print('\n', '- '*30, f'\nBienvenido {login[1]}, te has registrado el {login[5]}')
                #self.proximas_acciones(login)
        except Exception as e:
            #print(type(e))
            #print(type(e).__name__)
            print(f'ERROR: Login incorrecto, inténtalo después de la pandemia xP')

    #def proximas_acciones(self, usuario):