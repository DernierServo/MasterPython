import notas.nota as modelo

class Acciones:

    def crear(self, usuario):
        print(f'\nOK {usuario[1]}!! Vamos a generar una nueva nota...')

        titulo = input('Título: ')
        descripcion = input('Contenido: ')

        nota = modelo.Nota(usuario[0], titulo, descripcion)
        nota_guardada = nota.guardar()
    
        if nota_guardada[0] >= 1:
            print(f'\nEn hora buena! Has guardado la nota: {nota.titulo}')
        else:
            print(f'\nNo se ha guardado la nota! Lo lamentamos {usuario[1]}')

    def mostrar(self, usuario):
        print(f'\nOK {usuario[1]}! Aquí la lista de Notas:')

        nota_usuario = modelo.Nota(usuario[0])
        notas = nota_usuario.listar()

        for nota in notas:
            print(nota)
        
