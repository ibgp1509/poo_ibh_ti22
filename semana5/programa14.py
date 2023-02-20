"""
    Programa14 -
    Nombre:Cesar Ivan Bustamante 
    Herrera
    Fecha:15/02/2023
    Descripcion; Clase persona
"""

class Persona:  #Clase persona
  __nombre= None  #Variable privada __nombre
  __edad= None # Variable privada __edad
  def __init(self) -> None: # Constructor de la clase
      print("Persona") # Imprime el texto que esta entre comillas
  def setNombre(self,nombre:str) -> None:  # Modifica el valor de la variable
    self.__nombre=nombre # Modifica el valor y ñle asigna el valor del parametro
  def getNombre(self)->str: # Funcion que regresa el valor de la variable
   return self.__nombre # Regresa el valor de la variable