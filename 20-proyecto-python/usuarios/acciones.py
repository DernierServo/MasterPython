import usuarios.usuario as modelo
import notas.acciones 


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
            usuario_logeado = usuario.identificar()

            if email == usuario_logeado[3]:
                print('\n', '- '*30, f'\nBienvenido {usuario_logeado[1]}, te has registrado el {usuario_logeado[5]}')
                print("**************\n", usuario_logeado)
                self.proximas_acciones(usuario_logeado)
        except Exception as e:
            print(type(e))
            print(type(e).__name__)
            print(f'ERROR: Login incorrecto, inténtalo después de la pandemia xP')


    def proximas_acciones(self, usuario):
        print("""
        ACCIONES:
        - [C]rear notas
        - [M]ostrar notas
        - [E]liminar notas
        - [S]alir
        """)

        accion = input('¿Qué hacer?: ')
        nota_accion = notas.acciones.Acciones()

        if accion.upper() == 'C':
            nota_accion.crear(usuario)
            self.proximas_acciones(usuario)
        elif accion.upper() == 'M':
            print('MOSTRAR')
            nota_accion.mostrar(usuario)
            self.proximas_acciones(usuario)
        if accion.upper() == 'E':
            print('ELIMINAR')
            self.proximas_acciones(usuario)

        if accion.upper() == 'S':
            print(f'Adios {usuario[1]}, vuelve pronto!')
            exit()


        return None