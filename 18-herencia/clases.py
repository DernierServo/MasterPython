"""
HERENCIA: Es la posibilidad de compartir atributos y métodos
entre clases. Y que diferentes clases hereden de otras.
"""

class Persona:
    """
    nombre
    apellidos
    altura
    edad
    """
    def getNombre(self):
        return self.nombre
    
    def getApellidos(self):
        return self.apellidos

    def getAltura(self):
        return self.getAltura
    
    def getEdad(self):
        return self.edad

    def setNombre(self, nombre):
        self.nombre = nombre

    def setApellidos(self, apellidos):
        self.apellidos = apellidos

    def setAltura(self, altura):
        self.altura = altura

    def setEdad(self, edad):
        self.edad = edad

    def hablar(self):
        return "Estoy hablando"

    def caminar(self):
        return "Estoy caminando"

    def dormir(self):
        return "Estoy durmiendo!!!!! >:("


class Informatico(Persona):
    """
    lenguajes
    experiencia
    """
    # Constructor
    def __init__(self):
        self.lenguajes = "PYTHON, GO, C, C++, R, JavaScript"
        self.experiencia = 5

    def getLenguajes(self):
        return self.lenguajes

    def aprender(self, lenguajes):
        self.lenguajes = lenguajes
        return self.lenguajes

    def programar(self):
        return "Estoy programando, no moleté!!"

    def repararPC(self):
        return "He reparado tu ordenador! >:("


class TecnicoRedes(Informatico):

    def __init__(self):
        super().__init__()
        self.auditarRedes = 'experto'
        self.experienciaRedes = 15

    def auditoria(self):
        return "Estoy auditando una red! No Molete! D:<"