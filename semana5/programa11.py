"""
    Programa11 -
    Nombre:Cesar Ivan Bustamante 
    Herrera
    Fecha:13/02/2023
    Descripcion; Programa que ultiliza la clñase Alumno e imprime, nombre,matricula 
    y carrera
"""

class Alumno:
  __nombre = None
  __matricula= None
  __carrera= None

  def __init__(self):
   print("Alumno")

  def setNombre(self,nombre):
   self.__nombre= nombre

  def getNombre(self):
    return self.__nombre

  def setMatricula(self,matricula):
    self.__matricula = matricula

  def getMatricula(self):
    return self.__matricula

  def setCarrera(self,carrera):
   self.__carrera = carrera

   def getCarrera(self):
    return self.__carrera

ivan=Alumno()
ivan.setNombre("Ivan")
ivan.setMatricula("1722110527")
ivan.setCarrera("Tecnologias de la Informacion")    
print(ivan.getNombre())
    