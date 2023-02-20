"""
    Programa11 -
    Nombre:Cesar Ivan Bustamante 
    Herrera
    Fecha:13/02/2023
    Descripcion; Programa que ultiliza la clñase Alumno e imprime, nombre,matricula 
    y carrera
"""

class Alumno:
  __nombre = None # Definiendo la variable privada 
  __matricula= None # Definiendo la variable privada 
  __carrera= None # Definiendo la variable privada 

  def __init__(self): 
   print("Alumno") # Se va a imprimir el valor que estara entre comillas

  def setNombre(self,nombre):  # Esta contendiendo el valor del self y del nombre
   self.__nombre= nombre

  def getNombre(self):  # Se estara obteniendo el valor de nombre
    return self.__nombre

  def setMatricula(self,matricula):  # Esta contendiendo el valor del self y matricula
    self.__matricula = matricula

  def getMatricula(self): # se estara obteniendo o extrayendo el valor de matricula
    return self.__matricula

  def setCarrera(self,carrera): # Contiene el valor de carrera
   self.__carrera = carrera

   def getCarrera(self): # se estara obteniendo o extrayendo el valor de carrera
    return self.__carrera

ivan=Alumno()
ivan.setNombre("Ivan")
ivan.setMatricula("1722110527")
ivan.setCarrera("Tecnologias de la Informacion")    
print(ivan.getNombre())
    