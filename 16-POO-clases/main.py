class Coche:
    
    # ATRIBUTOS o propiedades (variables)
    color = 'Rojo'
    marca = 'Ferrari'
    modelo = 'Aventador'
    velocidad = 300
    caballaje = 500
    plazas = 2

    # MÉTODOS, son acciones que hace el objeto (coche) (funciones)
    def setColor(self, color):
        self.color = color

    def getColor(self):
        return self.color

    def setModelo(self, modelo):
        self.modelo = modelo

    def getModelo(self):
        return self.modelo

    def acelerar(self):
        self.velocidad += 1
    
    def frenar(self):
        self.velocidad -= 1

    def getVelocidad(self):
        return self.velocidad
     

# fin definición clase

# crear objetos | instanciar la clase
coche = Coche()


print('INICIALMENTE:\n', f'Marca: {coche.marca}, Color: {coche.color}')
coche.setColor('amarillo')
coche.setModelo('Murciélago')
print('LUEGO:\n', f'Marca: {coche.marca}, Color: {coche.color}')


print(f'Velocidad actual INI: {coche.velocidad}')

coche.acelerar()
coche.acelerar()
print(f'Velocidad actual FIN: {coche.getVelocidad()}')

coche.frenar()
print(f'Velocidad actual FIN: {coche.velocidad}') 

# Tipo de Objeto:
comp = isinstance(coche, Coche)
print(f'TIPO OBJETO: {type(coche)}')
print(f'COMPARACIÓN: {comp}')
