"""
    Programa12 -
    Nombre:Cesar Ivan Bustamante 
    Herrera
    Fecha:14/02/2023
    Descripcion; Herencia
  
"""
class Persona:
    __nombre = None
    def __init__(self):
     print("Persona")

class Alumno (Persona):
   def __init__(self):
      super().__init__()
      print("Alumno")

objeto_persona=Persona()
objeto_alumno=Alumno()

objeto_persona.nombre="Dejah"
print(objeto_persona.nombre)

objeto_alumno.nombre="John Carter"
print(objeto_alumno.nombre)

objeto_alumno.email="john@utectulancingo.edu.mx"
print(objeto_alumno.email)