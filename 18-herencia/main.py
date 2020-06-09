import clases

persona = clases.Persona()
persona.setNombre("Carlos")
persona.setApellidos("Arrasco")
persona.setAltura("170cm")
persona.setEdad("900 años")

print(f"La persona es: {persona.getNombre()} {persona.getApellidos()} ")
print(persona.hablar())


informatico = clases.Informatico()
informatico.setNombre('Juan')
informatico.setApellidos('Perez Oso')
print("*"*50)
print(f"La informático es: {informatico.getNombre()} {informatico.getApellidos()} ")
print(informatico.repararPC())
print(informatico.getLenguajes())
print(informatico.caminar())
print("*"*50)
tecnico = clases.TecnicoRedes()
tecnico.setNombre('Mongolo')
print(tecnico.auditarRedes, tecnico.getNombre())
print(tecnico.getLenguajes()) # Para obtener esto, se debe llamar al constructor
                              # de la Clase Padre con el método super().__init__()


print("*"*50)