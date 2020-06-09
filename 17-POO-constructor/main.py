from coche import Coche

def es_coche(objeto):
    if isinstance(objeto, Coche):
        return 'Es un objeto correcto'
    else:
        return f'No es un objeto! Es un tipo {type(objeto)}'


carro1 = Coche('Amarillo', 'Reanult','Clio', 150, 200, 4)
carro2 = Coche('Azul', 'Volvo', 'Mazeratti', 210, 300, 2)

print(carro1.getInfo())
print(carro2.getInfo())

carro3 = 'Aleatorio'

print("Objeto: ", es_coche(carro1))
print("Objeto: ", es_coche(carro3))

# VISIBILIDAD
print(carro1.soy_publico)
print(carro2.get_privado())