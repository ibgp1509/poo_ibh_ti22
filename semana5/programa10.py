"""
    Programa10 -
    Nombre:Cesar Ivan Bustamante 
    Herrera
    Fecha:13/02/2023
    Descripcion; Programa que usa la clase persona e imprimer nombre y correo
"""
class Persona:
  __nombre = None
  __email= None

def __init__(self):
  print("Persona")
  
  def setNombre(self,nombre):
   self.__nombre = nombre

  def getNombre(self):
   return self.__nombre

  def setEmail(self, email):
    self.__email=email
  def getEmail (self):
     return self.__email


dejah=Persona()
dejah.setNombre("Dejah")
dejah.setEmail("bustamanteherreraivan@gmail.com")
print(dejah.getNombre())
print(dejah.getEmail())

      
  
  