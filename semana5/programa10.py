"""
    Programa10 -
    Nombre:Cesar Ivan Bustamante 
    Herrera
    Fecha:13/02/2023
    Descripcion; Programa que usa la clase persona e imprimer nombre y correo
"""
class Persona: # Define la clase persona 
  __nombre = None # Variable privada __nombre
  __email= None # Variable privada __email

def __init__(self): # Definimos contenido de la variable
  print("Persona") #se imprimira el valor que esta en las comillas 
  
  def setNombre(self,nombre): # Se esta definiendo diferentes valores en una sola variable
   self.__nombre = nombre  

  def getNombre(self): # Definir la variable que estara obteniendo el valor y los datos de nbre
   return self.__nombre

  def setEmail(self, email): # Esta contendiendo el valor del self y del email
    self.__email=email
  def getEmail (self): # Se obtendra el valor de la variable email
     return self.__email


dejah=Persona() 
dejah.setNombre("Dejah")
dejah.setEmail("bustamanteherreraivan@gmail.com")
print(dejah.getNombre())
print(dejah.getEmail())

      
  
  